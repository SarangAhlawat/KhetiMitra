import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
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
    <div className="h-[280px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart
          data={data}
          layout="vertical"
          margin={{ top: 8, right: 12, left: 30, bottom: 0 }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
          <XAxis type="number" stroke="#cbd5e1" />
          <YAxis
            dataKey="feature"
            type="category"
            stroke="#cbd5e1"
            width={110}
          />
          <Tooltip />
          <Bar dataKey="importance" fill="#22d3ee" radius={[0, 6, 6, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}