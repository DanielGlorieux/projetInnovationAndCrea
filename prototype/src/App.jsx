import { useState } from "react";
import StatsOverview from "./components/StatsOverview";
import WaterLevelChart from "./components/WaterLevelChart";
import SensorTable from "./components/SensorTable";
import AlertsPanel from "./components/AlertsPanel";
import SensorMap from "./components/SensorMap";
import Quiz from "./components/Quiz";
import "./App.css";

export default function App() {
  const [page, setPage] = useState("dashboard");

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-brand">
          <span className="header-icon">💧</span>
          <div>
            <h1>AquaIA</h1>
            <p>Surveillance Intelligente des Eaux Souterraines — Sahel</p>
          </div>
        </div>
        <div className="header-info">
          <nav className="header-nav">
            <button
              className={`nav-btn ${page === "dashboard" ? "nav-active" : ""}`}
              onClick={() => setPage("dashboard")}
            >
              📊 Dashboard
            </button>
            <button
              className={`nav-btn ${page === "quiz" ? "nav-active" : ""}`}
              onClick={() => setPage("quiz")}
            >
              📝 QCM Innovation
            </button>
          </nav>
          <span className="badge badge-online">Système actif</span>
          <span className="header-date">
            {new Date().toLocaleDateString("fr-FR", {
              weekday: "long",
              year: "numeric",
              month: "long",
              day: "numeric",
            })}
          </span>
        </div>
      </header>

      <main className="app-main">
        {page === "dashboard" ? (
          <>
            <StatsOverview />

            <div className="two-columns">
              <div className="col-main">
                <WaterLevelChart />
              </div>
              <div className="col-side">
                <SensorMap />
              </div>
            </div>

            <SensorTable />

            <AlertsPanel />
          </>
        ) : (
          <Quiz />
        )}
      </main>

      <footer className="app-footer">
        <p>
          AquaIA Prototype — Projet Challenge Innovation — Institut 2iE
          2025-2026
        </p>
        <p>IA + IoT + LoRaWAN pour la gestion des eaux souterraines au Sahel</p>
      </footer>
    </div>
  );
}
