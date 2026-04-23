import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

export default function FeatureImportanceChart() {

  const data = [

    { feature: "Soil pH", importance: 0.30 },
    { feature: "Rainfall", importance: 0.25 },
    { feature: "Nitrogen", importance: 0.20 },
    { feature: "Temperature", importance: 0.15 },
    { feature: "Organic Carbon", importance: 0.10 }

  ];

  return (

    <BarChart

      width={500}
      height={300}

      data={data}

      layout="vertical"

    >

      <XAxis type="number" />

      <YAxis
        dataKey="feature"
        type="category"
      />

      <Tooltip />

      <Bar dataKey="importance" />

    </BarChart>

  );
}