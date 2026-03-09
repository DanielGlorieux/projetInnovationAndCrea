import { useState } from "react";
import { sensors, sensorReadings } from "../data/mockData";

export default function WaterLevelChart() {
  const [selectedSensor, setSelectedSensor] = useState("SEN-001");

  const sensor = sensors.find((s) => s.id === selectedSensor);
  const data = sensorReadings.find((r) => r.sensorId === selectedSensor);

  if (!data) return null;

  const allData = data.readings;
  const predictions = data.predictions;

  // SVG chart dimensions
  const width = 800;
  const height = 300;
  const padding = { top: 20, right: 30, bottom: 40, left: 50 };
  const chartW = width - padding.left - padding.right;
  const chartH = height - padding.top - padding.bottom;

  // Calculate min/max for y-axis from all values
  const allValues = [
    ...allData.map((d) => d.level),
    ...predictions.map((p) => p.upper),
    ...predictions.map((p) => p.lower),
  ];
  const yMin = Math.floor(Math.min(...allValues) - 1);
  const yMax = Math.ceil(Math.max(...allValues) + 1);

  const totalPoints = allData.length + predictions.length;
  const xStep = chartW / (totalPoints - 1);

  // Scale helpers
  const scaleY = (val) =>
    padding.top + chartH - ((val - yMin) / (yMax - yMin)) * chartH;
  const scaleX = (i) => padding.left + i * xStep;

  // Build path for actual readings
  const actualPath = allData
    .map((d, i) => `${i === 0 ? "M" : "L"} ${scaleX(i)} ${scaleY(d.level)}`)
    .join(" ");

  // Build paths for predictions
  const predStart = allData.length - 1;
  const lastActual = allData[allData.length - 1];

  const predLine =
    `M ${scaleX(predStart)} ${scaleY(lastActual.level)} ` +
    predictions
      .map((p, i) => `L ${scaleX(predStart + 1 + i)} ${scaleY(p.predicted)}`)
      .join(" ");

  // Confidence band
  const upperPoints = [
    `${scaleX(predStart)},${scaleY(lastActual.level)}`,
    ...predictions.map(
      (p, i) => `${scaleX(predStart + 1 + i)},${scaleY(p.upper)}`
    ),
  ];
  const lowerPoints = [
    ...predictions.map(
      (p, i) => `${scaleX(predStart + 1 + i)},${scaleY(p.lower)}`
    ),
    `${scaleX(predStart)},${scaleY(lastActual.level)}`,
  ].reverse();
  const bandPolygon = [...upperPoints, ...lowerPoints].join(" ");

  // Y-axis ticks
  const yTicks = [];
  for (let v = yMin; v <= yMax; v++) {
    yTicks.push(v);
  }

  // All x labels
  const allLabels = [
    ...allData.map((d) => d.month),
    ...predictions.map((p) => p.month),
  ];

  return (
    <div className="panel">
      <div className="chart-header">
        <h2>📈 Évolution du Niveau d&apos;Eau &amp; Prédictions IA</h2>
        <select
          value={selectedSensor}
          onChange={(e) => setSelectedSensor(e.target.value)}
          className="sensor-select"
        >
          {sensors.map((s) => (
            <option key={s.id} value={s.id}>
              {s.name}
            </option>
          ))}
        </select>
      </div>

      <p className="chart-subtitle">
        Capteur : <strong>{sensor.name}</strong> — {sensor.location}
      </p>

      <div className="chart-container">
        <svg viewBox={`0 0 ${width} ${height}`} className="chart-svg">
          {/* Grid lines */}
          {yTicks.map((v) => (
            <g key={v}>
              <line
                x1={padding.left}
                y1={scaleY(v)}
                x2={width - padding.right}
                y2={scaleY(v)}
                stroke="#2a3a4a"
                strokeDasharray="4,4"
              />
              <text
                x={padding.left - 8}
                y={scaleY(v) + 4}
                textAnchor="end"
                fill="#8899aa"
                fontSize="11"
              >
                {v}m
              </text>
            </g>
          ))}

          {/* X-axis labels (every other) */}
          {allLabels.map((label, i) =>
            i % 2 === 0 ? (
              <text
                key={i}
                x={scaleX(i)}
                y={height - 5}
                textAnchor="middle"
                fill="#8899aa"
                fontSize="10"
              >
                {label}
              </text>
            ) : null
          )}

          {/* Prediction separator */}
          <line
            x1={scaleX(predStart)}
            y1={padding.top}
            x2={scaleX(predStart)}
            y2={height - padding.bottom}
            stroke="#f9a825"
            strokeDasharray="6,4"
            strokeWidth="1"
          />
          <text
            x={scaleX(predStart) + 5}
            y={padding.top + 12}
            fill="#f9a825"
            fontSize="10"
          >
            Prédictions IA →
          </text>

          {/* Confidence band */}
          <polygon points={bandPolygon} fill="rgba(0, 151, 167, 0.15)" />

          {/* Actual readings line */}
          <path
            d={actualPath}
            fill="none"
            stroke="#009bd6"
            strokeWidth="2.5"
          />

          {/* Prediction line */}
          <path
            d={predLine}
            fill="none"
            stroke="#26c6da"
            strokeWidth="2"
            strokeDasharray="6,3"
          />

          {/* Data points */}
          {allData.map((d, i) => (
            <circle
              key={`a-${i}`}
              cx={scaleX(i)}
              cy={scaleY(d.level)}
              r="3.5"
              fill="#009bd6"
            />
          ))}
          {predictions.map((p, i) => (
            <circle
              key={`p-${i}`}
              cx={scaleX(predStart + 1 + i)}
              cy={scaleY(p.predicted)}
              r="3"
              fill="#26c6da"
            />
          ))}
        </svg>
      </div>

      <div className="chart-legend">
        <span className="legend-item">
          <span className="legend-line" style={{ background: "#009bd6" }} />
          Données réelles
        </span>
        <span className="legend-item">
          <span
            className="legend-line dashed"
            style={{ background: "#26c6da" }}
          />
          Prédictions LSTM
        </span>
        <span className="legend-item">
          <span
            className="legend-box"
            style={{ background: "rgba(0, 151, 167, 0.25)" }}
          />
          Intervalle de confiance
        </span>
      </div>
    </div>
  );
}
