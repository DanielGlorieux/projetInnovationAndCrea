import React, { useState, useRef, useEffect } from "react";
import "./App.css";

const API_URL = "http://localhost:5000";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState(null);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    fetch(`${API_URL}/health`)
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("offline"));
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const buildChatHistory = () =>
    messages.map((m) => ({
      role: m.role === "user" ? "human" : "ai",
      content: m.content,
    }));

  const handleSend = async () => {
    const query = input.trim();
    if (!query || loading) return;

    setInput("");
    setMessages((prev) => [...prev, { role: "user", content: query }]);
    setLoading(true);

    try {
      const res = await fetch(`${API_URL}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          query,
          chat_history: buildChatHistory(),
        }),
      });
      const data = await res.json();

      if (data.success) {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            content: data.raw_answer || data.answer,
            sources: data.sources || [],
          },
        ]);
      } else {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            content: `Erreur : ${data.error || "Réponse inattendue du serveur."}`,
          },
        ]);
      }
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Impossible de contacter le serveur. Vérifiez que le backend tourne sur le port 5000.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const clearChat = async () => {
    setMessages([]);
    try {
      await fetch(`${API_URL}/api/clear-chat`, { method: "POST" });
    } catch {
      /* ignore */
    }
  };

  return (
    <div className="app">
      {/* Sidebar */}
      <aside className="sidebar">
        <h2 className="sidebar-title">🤖 RAG Chatbot</h2>
        <p className="sidebar-subtitle">Documentation Helper</p>

        <div className="sidebar-status">
          <span
            className={`status-dot ${status === "healthy" ? "online" : "offline"}`}
          />
          <span>
            Backend : {status === "healthy" ? "Connecté" : "Déconnecté"}
          </span>
        </div>

        <div className="sidebar-info">
          <p>
            <strong>Modèle :</strong> Gemini 1.5 Flash
          </p>
          <p>
            <strong>Index :</strong> proj-rag
          </p>
          <p>
            <strong>Embeddings :</strong> text-embedding-004
          </p>
        </div>

        <button className="clear-btn" onClick={clearChat}>
          🗑️ Effacer la conversation
        </button>
      </aside>

      {/* Main chat area */}
      <main className="chat-area">
        <div className="messages">
          {messages.length === 0 && (
            <div className="welcome">
              <h1>👋 Bienvenue !</h1>
              <p>
                Posez une question sur la documentation LangChain. Le chatbot
                utilise un système RAG pour vous répondre avec des sources.
              </p>
              <div className="suggestions">
                {[
                  "Comment utiliser LangChain avec Python ?",
                  "Qu'est-ce qu'un retriever dans LangChain ?",
                  "Comment créer une chaîne RAG ?",
                ].map((q) => (
                  <button
                    key={q}
                    className="suggestion"
                    onClick={() => {
                      setInput(q);
                    }}
                  >
                    {q}
                  </button>
                ))}
              </div>
            </div>
          )}

          {messages.map((msg, i) => (
            <div key={i} className={`message ${msg.role}`}>
              <div className="message-avatar">
                {msg.role === "user" ? "👤" : "🤖"}
              </div>
              <div className="message-body">
                <div className="message-content">{msg.content}</div>
                {msg.sources && msg.sources.length > 0 && (
                  <div className="sources">
                    <strong>📚 Sources :</strong>
                    <ul>
                      {msg.sources.map((s, j) => (
                        <li key={j}>
                          <a
                            href={s.source}
                            target="_blank"
                            rel="noopener noreferrer"
                          >
                            {s.source}
                          </a>{" "}
                          <span className="score">
                            (score : {s.score?.toFixed(2)})
                          </span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          ))}

          {loading && (
            <div className="message assistant">
              <div className="message-avatar">🤖</div>
              <div className="message-body">
                <div className="typing-indicator">
                  <span />
                  <span />
                  <span />
                </div>
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Input area */}
        <div className="input-area">
          <textarea
            className="chat-input"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Posez votre question…"
            rows={1}
            disabled={loading}
          />
          <button
            className="send-btn"
            onClick={handleSend}
            disabled={loading || !input.trim()}
          >
            {loading ? "⏳" : "➤"}
          </button>
        </div>
      </main>
    </div>
  );
}

export default App;
