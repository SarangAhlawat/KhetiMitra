import {
  MapContainer,
  TileLayer,
  CircleMarker
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

    <MapContainer

      center={[30.7333, 76.7794]}
      zoom={7}

      style={{ height: "400px" }}

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
            color: getColor(d.risk)
          }}

        />

      ))}

    </MapContainer>

  );
}