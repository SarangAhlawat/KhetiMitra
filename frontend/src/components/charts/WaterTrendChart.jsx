import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

export default function WaterTrendChart() {

  const data = [

    { year: 2020, water: 80 },
    { year: 2021, water: 70 },
    { year: 2022, water: 60 },
    { year: 2023, water: 55 }

  ];

  return (

    <BarChart
      width={400}
      height={250}
      data={data}
    >

      <XAxis dataKey="year" />

      <YAxis />

      <Tooltip />

      <Bar dataKey="water" />

    </BarChart>

  );
}