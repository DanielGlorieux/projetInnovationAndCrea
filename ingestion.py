import json
import logging
import os
import sys
from typing import Any, Dict, List

from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

# ---------------------------------------------------------------------------
# Logging configuration
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Pinecone configuration
# ---------------------------------------------------------------------------
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY", "")
PINECONE_INDEX_NAME = "proj-rag"
# The Pinecone index is configured with multilingual-e5-large integrated
# inference (dimension=1024, metric=cosine). Pinecone generates the
# embeddings server-side so no external embedding API is required.
EMBEDDING_MODEL = "multilingual-e5-large"

# Ingestion tuning
EMBED_BATCH_SIZE = 96  # texts per embedding request (Pinecone inference limit)
UPSERT_BATCH_SIZE = 100  # vectors per upsert request


def load_chunks(path: str) -> List[Dict[str, Any]]:
    """Load chunks from a JSONL file, skipping malformed lines."""
    chunks: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as fh:
        for lineno, raw_line in enumerate(fh, start=1):
            line = raw_line.strip()
            if not line:
                continue
            # Handle possible non-JSON prefix on a line (e.g. BOM or stray text)
            idx = line.find("{")
            if idx == -1:
                log.warning("Skipping line %d – no JSON object found", lineno)
                continue
            try:
                obj = json.loads(line[idx:])
                chunks.append(obj)
            except json.JSONDecodeError as exc:
                log.warning("Skipping line %d – %s", lineno, exc)
    return chunks


def load_manifest(path: str) -> Dict[str, Dict[str, Any]]:
    """Load the document manifest into a dict keyed by document_id."""
    manifest: Dict[str, Dict[str, Any]] = {}
    with open(path, "r", encoding="utf-8") as fh:
        for lineno, raw_line in enumerate(fh, start=1):
            line = raw_line.strip()
            if not line:
                continue
            idx = line.find("{")
            if idx == -1:
                continue
            try:
                obj = json.loads(line[idx:])
                manifest[obj["document_id"]] = obj
            except (json.JSONDecodeError, KeyError) as exc:
                log.warning("Manifest line %d skipped – %s", lineno, exc)
    return manifest


def build_metadata(chunk: Dict[str, Any]) -> Dict[str, Any]:
    """Build the metadata dict stored alongside each vector in Pinecone."""
    return {
        "document_id": chunk.get("document_id", ""),
        "source_site": chunk.get("source_site", ""),
        "source_url": chunk.get("source_url", ""),
        "filename": chunk.get("filename", ""),
        "page_number": chunk.get("page_number", 0),
        "chunk_index_in_page": chunk.get("chunk_index_in_page", 0),
        "text": chunk.get("text", ""),
    }


def ingest(chunks_path: str, manifest_path: str) -> None:
    """Main ingestion pipeline: read local JSONL data → embed → upsert to Pinecone."""

    if not PINECONE_API_KEY:
        log.error("PINECONE_API_KEY is not set. Please configure your .env file.")
        sys.exit(1)

    # ------------------------------------------------------------------
    # 1. Load local data
    # ------------------------------------------------------------------
    log.info("=" * 60)
    log.info("LOADING LOCAL DATA")
    log.info("=" * 60)

    manifest = load_manifest(manifest_path)
    log.info("📄  Manifest loaded: %d documents", len(manifest))

    chunks = load_chunks(chunks_path)
    log.info("📄  Chunks loaded: %d chunks", len(chunks))

    if not chunks:
        log.warning("No chunks to ingest – exiting.")
        return

    # ------------------------------------------------------------------
    # 2. Connect to Pinecone
    # ------------------------------------------------------------------
    log.info("=" * 60)
    log.info("CONNECTING TO PINECONE")
    log.info("=" * 60)

    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
    log.info("✅  Connected to Pinecone index '%s'", PINECONE_INDEX_NAME)

    # ------------------------------------------------------------------
    # 3. Embed & upsert in batches
    # ------------------------------------------------------------------
    log.info("=" * 60)
    log.info("EMBEDDING & UPSERTING (%d chunks)", len(chunks))
    log.info("=" * 60)

    total_upserted = 0

    for batch_start in range(0, len(chunks), EMBED_BATCH_SIZE):
        batch = chunks[batch_start : batch_start + EMBED_BATCH_SIZE]
        texts = [c.get("text", "") for c in batch]
        batch_num = batch_start // EMBED_BATCH_SIZE + 1
        total_batches = (len(chunks) + EMBED_BATCH_SIZE - 1) // EMBED_BATCH_SIZE

        # Generate embeddings via Pinecone Inference API
        try:
            embeddings = pc.inference.embed(
                model=EMBEDDING_MODEL,
                inputs=texts,
                parameters={"input_type": "passage", "truncate": "END"},
            )
        except Exception as exc:
            log.error(
                "Embedding failed for batch %d/%d – %s", batch_num, total_batches, exc
            )
            continue

        # Build vector dicts for upsert
        vectors = []
        for chunk, emb in zip(batch, embeddings):
            vectors.append(
                {
                    "id": chunk["chunk_id"],
                    "values": emb["values"],
                    "metadata": build_metadata(chunk),
                }
            )

        # Upsert in sub-batches
        for upsert_start in range(0, len(vectors), UPSERT_BATCH_SIZE):
            upsert_batch = vectors[upsert_start : upsert_start + UPSERT_BATCH_SIZE]
            try:
                index.upsert(vectors=upsert_batch)
                total_upserted += len(upsert_batch)
            except Exception as exc:
                log.error("Upsert failed – %s", exc)

        log.info(
            "📦  Batch %d/%d – embedded & upserted %d chunks (total: %d/%d)",
            batch_num,
            total_batches,
            len(batch),
            total_upserted,
            len(chunks),
        )

    # ------------------------------------------------------------------
    # 4. Summary
    # ------------------------------------------------------------------
    log.info("=" * 60)
    log.info("PIPELINE COMPLETE")
    log.info("=" * 60)
    log.info("🎉  Ingestion finished!")
    log.info("   • Documents in manifest : %d", len(manifest))
    log.info("   • Chunks processed      : %d", len(chunks))
    log.info("   • Vectors upserted      : %d", total_upserted)


if __name__ == "__main__":
    ingest(
        chunks_path="chunks.jsonl",
        manifest_path="rag_manifest.jsonl",
    )
