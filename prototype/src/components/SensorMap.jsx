import { sensors } from "../data/mockData";

const statusColors = {
  online: "#43a047",
  warning: "#f9a825",
  offline: "#e53935",
};

export default function SensorMap() {
  // Simple representation of sensor locations on a Burkina Faso outline
  // Map bounds approximately: lat 9.5-15, lng -5.5 to 2.5
  const mapBounds = { latMin: 9.5, latMax: 15, lngMin: -5.5, lngMax: 2.5 };
  const mapW = 400;
  const mapH = 320;

  const toX = (lng) =>
    ((lng - mapBounds.lngMin) / (mapBounds.lngMax - mapBounds.lngMin)) * mapW;
  const toY = (lat) =>
    mapH -
    ((lat - mapBounds.latMin) / (mapBounds.latMax - mapBounds.latMin)) * mapH;

  // Simplified Burkina Faso outline (approximate polygon)
  const outlinePoints = [
    [-2.0, 14.9], [-0.7, 14.9], [0.2, 14.97], [0.6, 14.6],
    [1.3, 13.6], [1.6, 12.6], [2.1, 12.4], [2.3, 11.6],
    [1.9, 11.1], [0.9, 10.8], [0.4, 10.7], [-0.1, 11.0],
    [-0.7, 10.6], [-1.0, 10.3], [-2.0, 9.8], [-2.8, 9.6],
    [-3.2, 9.9], [-3.6, 10.6], [-4.3, 10.4], [-4.8, 10.8],
    [-5.0, 11.5], [-4.6, 12.1], [-4.3, 12.2], [-3.9, 13.0],
    [-3.5, 13.3], [-3.3, 13.1], [-2.5, 13.5], [-2.0, 14.2],
    [-2.0, 14.9],
  ].map(([lng, lat]) => `${toX(lng)},${toY(lat)}`).join(" ");

  return (
    <div className="panel">
      <h2>🗺️ Carte des Capteurs — Burkina Faso</h2>
      <div className="map-container">
        <svg viewBox={`0 0 ${mapW} ${mapH}`} className="map-svg">
          {/* Country outline */}
          <polygon
            points={outlinePoints}
            fill="rgba(0, 155, 214, 0.08)"
            stroke="#2a5a7a"
            strokeWidth="1.5"
          />

          {/* Sensor markers */}
          {sensors.map((sensor) => {
            const cx = toX(sensor.lng);
            const cy = toY(sensor.lat);
            const color = statusColors[sensor.status];
            return (
              <g key={sensor.id}>
                {/* Pulse animation circle */}
                <circle
                  cx={cx}
                  cy={cy}
                  r="12"
                  fill="none"
                  stroke={color}
                  strokeWidth="1"
                  opacity="0.3"
                  className={
                    sensor.status === "online" ? "pulse-ring" : undefined
                  }
                />
                {/* Marker */}
                <circle
                  cx={cx}
                  cy={cy}
                  r="6"
                  fill={color}
                  stroke="#0d1b2a"
                  strokeWidth="2"
                />
                {/* Label */}
                <text
                  x={cx + 10}
                  y={cy + 4}
                  fill="#c0d0e0"
                  fontSize="9"
                  fontFamily="sans-serif"
                >
                  {sensor.id}
                </text>
              </g>
            );
          })}
        </svg>

        <div className="map-legend">
          <div className="map-legend-item">
            <span
              className="map-dot"
              style={{ background: statusColors.online }}
            />
            En ligne
          </div>
          <div className="map-legend-item">
            <span
              className="map-dot"
              style={{ background: statusColors.warning }}
            />
            Attention
          </div>
          <div className="map-legend-item">
            <span
              className="map-dot"
              style={{ background: statusColors.offline }}
            />
            Hors ligne
          </div>
        </div>
      </div>
    </div>
  );
}
