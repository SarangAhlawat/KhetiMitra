import {
	CartesianGrid,
	Line,
	LineChart,
	ResponsiveContainer,
	Tooltip,
	XAxis,
	YAxis
} from "recharts";

export default function CustomLineChart({ data, xKey, yKey, color = "#34d399" }) {
	return (
		<div className="h-[240px] w-full">
			<ResponsiveContainer width="100%" height="100%">
				<LineChart data={data} margin={{ top: 8, right: 12, left: 0, bottom: 0 }}>
					<CartesianGrid strokeDasharray="3 3" stroke="#334155" />
					<XAxis dataKey={xKey} stroke="#cbd5e1" />
					<YAxis stroke="#cbd5e1" />
					<Tooltip />
					<Line type="monotone" dataKey={yKey} stroke={color} strokeWidth={2} />
				</LineChart>
			</ResponsiveContainer>
		</div>
	);
}
