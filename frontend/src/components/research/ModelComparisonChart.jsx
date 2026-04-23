import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

export default function ModelComparisonChart() {

  const data = [

    {
      model: "Random Forest",
      accuracy: 88
    },

    {
      model: "XGBoost",
      accuracy: 91
    },

    {
      model: "LSTM",
      accuracy: 86
    }

  ];

  return (

    <BarChart

      width={500}
      height={300}

      data={data}

    >

      <XAxis dataKey="model" />

      <YAxis />

      <Tooltip />

      <Bar dataKey="accuracy" />

    </BarChart>

  );
}