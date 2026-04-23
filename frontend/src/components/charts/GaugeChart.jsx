import {
  RadialBarChart,
  RadialBar,
  PolarAngleAxis
} from "recharts";

export default function GaugeChart({ value }) {

  const data = [
    {
      name: "Score",
      value: value
    }
  ];

  return (

    <RadialBarChart

      width={200}
      height={200}

      innerRadius="80%"
      outerRadius="100%"

      data={data}

      startAngle={180}
      endAngle={0}

    >

      <PolarAngleAxis
        type="number"
        domain={[0, 100]}
        tick={false}
      />

      <RadialBar
        dataKey="value"
        cornerRadius={10}
      />

      <text
        x="50%"
        y="50%"
        textAnchor="middle"
        dominantBaseline="middle"
        className="text-xl font-bold"
      >
        {value}
      </text>

    </RadialBarChart>

  );
}