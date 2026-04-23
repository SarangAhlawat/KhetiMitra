import {
  MapContainer,
  TileLayer,
  CircleMarker,
  Popup
} from "react-leaflet";

import "leaflet/dist/leaflet.css";

export default function RiskMap() {

  const districts = [

    {
      name: "Chandigarh",
      lat: 30.7333,
      lon: 76.7794,
      risk: "high"
    },

    {
      name: "Patiala",
      lat: 30.3398,
      lon: 76.3869,
      risk: "medium"
    }

  ];

  const getColor = (risk) => {

    if (risk === "high")
      return "red";

    if (risk === "medium")
      return "yellow";

    return "green";

  };

  return (
    <div>
      <div className="mb-3 flex flex-wrap gap-2 text-xs text-slate-200">
        <span className="rounded-full border border-red-400/40 bg-red-400/15 px-2 py-1">High Risk</span>
        <span className="rounded-full border border-amber-300/40 bg-amber-300/15 px-2 py-1">Medium Risk</span>
        <span className="rounded-full border border-emerald-300/40 bg-emerald-300/15 px-2 py-1">Low Risk</span>
      </div>
      <MapContainer
        center={[30.7333, 76.7794]}
        zoom={7}
        style={{ height: "320px", width: "100%" }}
        className="rounded-xl"
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {districts.map((d, i) => (
          <CircleMarker
            key={i}
            center={[d.lat, d.lon]}
            radius={10}
            pathOptions={{
              color: getColor(d.risk),
              fillOpacity: 0.6
            }}
          >
            <Popup>
              <div>
                <p className="font-semibold">{d.name}</p>
                <p>Risk: {d.risk}</p>
              </div>
            </Popup>
          </CircleMarker>
        ))}
      </MapContainer>
    </div>
  );
}