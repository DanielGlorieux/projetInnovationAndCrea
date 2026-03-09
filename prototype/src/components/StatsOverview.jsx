import { dashboardStats } from "../data/mockData";

function StatCard({ icon, label, value, unit, color }) {
  return (
    <div className="stat-card">
      <div className="stat-icon" style={{ background: color }}>
        {icon}
      </div>
      <div className="stat-info">
        <span className="stat-value">
          {value}
          {unit && <small> {unit}</small>}
        </span>
        <span className="stat-label">{label}</span>
      </div>
    </div>
  );
}

export default function StatsOverview() {
  const stats = dashboardStats;

  return (
    <div className="stats-grid">
      <StatCard
        icon="📡"
        label="Capteurs en ligne"
        value={`${stats.onlineSensors}/${stats.totalSensors}`}
        color="#1a73e8"
      />
      <StatCard
        icon="💧"
        label="Niveau moyen"
        value={stats.avgWaterLevel}
        unit="m"
        color="#0097a7"
      />
      <StatCard
        icon="🔔"
        label="Alertes aujourd'hui"
        value={stats.alertsToday}
        color="#e53935"
      />
      <StatCard
        icon="🧠"
        label="Précision IA"
        value={`${stats.predictionAccuracy}%`}
        color="#43a047"
      />
    </div>
  );
}
