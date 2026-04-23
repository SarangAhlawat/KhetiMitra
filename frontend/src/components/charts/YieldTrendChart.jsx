import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip
} from "recharts";

export default function YieldTrendChart() {

    const data = [

        { year: 2020, yield: 3200 },
        { year: 2021, yield: 3400 },
        { year: 2022, yield: 3600 },
        { year: 2023, yield: 3900 }

    ];

    return (

        <LineChart
            width={400}
            height={250}
            data={data}
        >

            <XAxis dataKey="year" />

            <YAxis />

            <Tooltip />

            <Line
                type="monotone"
                dataKey="yield"
            />

        </LineChart>

    );
}