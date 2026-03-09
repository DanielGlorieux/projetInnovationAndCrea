import { alerts, sensors } from "../data/mockData";

const typeConfig = {
  critical: { icon: "🚨", className: "alert-critical" },
  warning: { icon: "⚠️", className: "alert-warning" },
  info: { icon: "ℹ️", className: "alert-info" },
};

function formatDate(dateStr) {
  const d = new Date(dateStr);
  return d.toLocaleDateString("fr-FR", {
    day: "numeric",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

export default function AlertsPanel() {
  return (
    <div className="panel">
      <h2>🔔 Alertes Communautaires</h2>
      <div className="alerts-list">
        {alerts.map((alert) => {
          const config = typeConfig[alert.type];
          const sensor = sensors.find((s) => s.id === alert.sensor);
          return (
            <div key={alert.id} className={`alert-item ${config.className}`}>
              <div className="alert-icon">{config.icon}</div>
              <div className="alert-content">
                <p className="alert-message">{alert.message}</p>
                <div className="alert-meta">
                  <span>{sensor ? sensor.name : alert.sensor}</span>
                  <span>•</span>
                  <span>{formatDate(alert.date)}</span>
                  <span>•</span>
                  <span className={alert.sent ? "sent" : "pending"}>
                    {alert.sent ? "✓ SMS envoyé" : "⏳ En attente"}
                  </span>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
