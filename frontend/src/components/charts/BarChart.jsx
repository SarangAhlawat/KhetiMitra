import {
	Bar,
	BarChart,
	CartesianGrid,
	ResponsiveContainer,
	Tooltip,
	XAxis,
	YAxis
} from "recharts";

export default function CustomBarChart({ data, xKey, yKey, color = "#22d3ee" }) {
	return (
		<div className="h-[240px] w-full">
			<ResponsiveContainer width="100%" height="100%">
				<BarChart data={data} margin={{ top: 8, right: 12, left: 0, bottom: 0 }}>
					<CartesianGrid strokeDasharray="3 3" stroke="#334155" />
					<XAxis dataKey={xKey} stroke="#cbd5e1" />
					<YAxis stroke="#cbd5e1" />
					<Tooltip />
					<Bar dataKey={yKey} fill={color} radius={[6, 6, 0, 0]} />
				</BarChart>
			</ResponsiveContainer>
		</div>
	);
}
