/**
 * Mock data simulating AquaIA IoT sensor readings and AI predictions.
 * In production, this data would come from LoRaWAN-connected piezometric sensors
 * and an LSTM/Random Forest prediction model.
 */

export const sensors = [
  {
    id: "SEN-001",
    name: "Forage Koudougou-Centre",
    location: "Koudougou, Centre-Ouest",
    lat: 12.2533,
    lng: -2.3628,
    status: "online",
    battery: 87,
  },
  {
    id: "SEN-002",
    name: "Forage Ouagadougou-Est",
    location: "Ouagadougou, Centre",
    lat: 12.3714,
    lng: -1.5197,
    status: "online",
    battery: 92,
  },
  {
    id: "SEN-003",
    name: "Forage Bobo-Dioulasso Sud",
    location: "Bobo-Dioulasso, Hauts-Bassins",
    lat: 11.1771,
    lng: -4.2979,
    status: "warning",
    battery: 34,
  },
  {
    id: "SEN-004",
    name: "Forage Kaya-Nord",
    location: "Kaya, Centre-Nord",
    lat: 13.091,
    lng: -1.0842,
    status: "offline",
    battery: 5,
  },
  {
    id: "SEN-005",
    name: "Forage Dédougou-Ouest",
    location: "Dédougou, Boucle du Mouhoun",
    lat: 12.4633,
    lng: -3.4608,
    status: "online",
    battery: 76,
  },
  {
    id: "SEN-006",
    name: "Forage Ziniaré-Centre",
    location: "Ziniaré, Plateau-Central",
    lat: 12.5833,
    lng: -1.3,
    status: "online",
    battery: 65,
  },
];

/** Generate water level readings for the past 12 months */
function generateMonthlyReadings(seed) {
  const months = [
    "Avr 2025", "Mai 2025", "Juin 2025", "Juil 2025",
    "Août 2025", "Sep 2025", "Oct 2025", "Nov 2025",
    "Déc 2025", "Jan 2026", "Fév 2026", "Mar 2026",
  ];

  const baseLevel = 8 + (seed % 5);
  return months.map((month, i) => {
    const seasonalOffset = Math.sin((i - 3) * Math.PI / 6) * 1.5;
    const noise = Math.sin(seed * 13 + i * 7) * 0.3;
    return {
      month,
      level: +(baseLevel + seasonalOffset + noise).toFixed(2),
    };
  });
}

/** Generate AI predictions for the next 6 months */
function generatePredictions(lastLevel, seed) {
  const months = [
    "Avr 2026", "Mai 2026", "Juin 2026",
    "Juil 2026", "Août 2026", "Sep 2026",
  ];
  return months.map((month, i) => {
    const trend = -0.08 * i;
    const seasonal = Math.sin((i + 9) * Math.PI / 6) * 1.2;
    const noise = Math.sin(seed * 17 + i * 11) * 0.2;
    return {
      month,
      predicted: +(lastLevel + trend + seasonal + noise).toFixed(2),
      upper: +(lastLevel + trend + seasonal + noise + 0.8).toFixed(2),
      lower: +(lastLevel + trend + seasonal + noise - 0.8).toFixed(2),
    };
  });
}

/** Current sensor readings */
export const sensorReadings = sensors.map((sensor, idx) => {
  const readings = generateMonthlyReadings(idx + 1);
  const lastLevel = readings[readings.length - 1].level;
  return {
    sensorId: sensor.id,
    readings,
    predictions: generatePredictions(lastLevel, idx + 1),
    current: {
      waterLevel: lastLevel,
      temperature: +(27 + (idx * 1.3) % 6).toFixed(1),
      conductivity: +(250 + (idx * 47) % 250).toFixed(0),
      ph: +(6.5 + (idx * 0.3) % 1.5).toFixed(1),
    },
  };
});

/** Community alerts */
export const alerts = [
  {
    id: 1,
    type: "critical",
    message: "Niveau d'eau critique au forage Kaya-Nord — risque de pénurie dans 2 mois",
    sensor: "SEN-004",
    date: "2026-03-08T14:30:00",
    sent: true,
  },
  {
    id: 2,
    type: "warning",
    message: "Batterie faible au capteur Bobo-Dioulasso Sud — maintenance requise",
    sensor: "SEN-003",
    date: "2026-03-07T09:15:00",
    sent: true,
  },
  {
    id: 3,
    type: "warning",
    message: "Conductivité élevée détectée à Dédougou-Ouest — vérification qualité recommandée",
    sensor: "SEN-005",
    date: "2026-03-06T16:45:00",
    sent: false,
  },
  {
    id: 4,
    type: "info",
    message: "Prédiction IA : niveau d'eau stable pour les 3 prochains mois à Koudougou",
    sensor: "SEN-001",
    date: "2026-03-05T08:00:00",
    sent: true,
  },
  {
    id: 5,
    type: "info",
    message: "Nouveau capteur Ziniaré-Centre connecté avec succès au réseau LoRaWAN",
    sensor: "SEN-006",
    date: "2026-03-04T11:20:00",
    sent: true,
  },
];

/** Summary statistics */
export const dashboardStats = {
  totalSensors: sensors.length,
  onlineSensors: sensors.filter((s) => s.status === "online").length,
  alertsToday: 2,
  avgWaterLevel: +(
    sensorReadings.reduce((sum, r) => sum + r.current.waterLevel, 0) /
    sensorReadings.length
  ).toFixed(1),
  predictionAccuracy: 87,
};
