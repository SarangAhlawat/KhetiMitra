import Badge from "../ui/Badge";

const factors = [
	{ feature: "Soil pH", direction: "positive", strength: "High" },
	{ feature: "Rainfall", direction: "positive", strength: "Medium" },
	{ feature: "Nitrogen", direction: "negative", strength: "Medium" }
];

export default function SHAPVisualizer() {
	return (
		<div className="space-y-2">
			{factors.map((item) => (
				<div key={item.feature} className="flex items-center justify-between rounded-xl border border-white/10 bg-white/5 px-3 py-2 text-sm">
					<span>{item.feature}</span>
					<div className="flex items-center gap-2">
						<Badge variant={item.direction === "positive" ? "success" : "warning"}>{item.direction}</Badge>
						<span className="text-slate-300">{item.strength}</span>
					</div>
				</div>
			))}
		</div>
	);
}
