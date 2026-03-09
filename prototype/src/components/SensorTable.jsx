import { sensors, sensorReadings } from "../data/mockData";

const statusLabels = {
  online: "En ligne",
  warning: "Attention",
  offline: "Hors ligne",
};

export default function SensorTable() {
  return (
    <div className="panel">
      <h2>📡 Capteurs IoT — État du Réseau</h2>
      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Nom du forage</th>
              <th>Localisation</th>
              <th>Statut</th>
              <th>Batterie</th>
              <th>Niveau (m)</th>
              <th>Temp. (°C)</th>
              <th>Cond. (µS/cm)</th>
              <th>pH</th>
            </tr>
          </thead>
          <tbody>
            {sensors.map((sensor) => {
              const reading = sensorReadings.find(
                (r) => r.sensorId === sensor.id
              );
              return (
                <tr key={sensor.id}>
                  <td className="mono">{sensor.id}</td>
                  <td>{sensor.name}</td>
                  <td>{sensor.location}</td>
                  <td>
                    <span className={`badge badge-${sensor.status}`}>
                      {statusLabels[sensor.status]}
                    </span>
                  </td>
                  <td>
                    <div className="battery-bar">
                      <div
                        className="battery-fill"
                        style={{
                          width: `${sensor.battery}%`,
                          background:
                            sensor.battery > 50
                              ? "#43a047"
                              : sensor.battery > 20
                              ? "#f9a825"
                              : "#e53935",
                        }}
                      />
                      <span>{sensor.battery}%</span>
                    </div>
                  </td>
                  <td className="mono">
                    {reading ? reading.current.waterLevel : "—"}
                  </td>
                  <td className="mono">
                    {reading ? reading.current.temperature : "—"}
                  </td>
                  <td className="mono">
                    {reading ? reading.current.conductivity : "—"}
                  </td>
                  <td className="mono">
                    {reading ? reading.current.ph : "—"}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
