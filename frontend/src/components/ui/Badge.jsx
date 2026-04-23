const variants = {
	success: "border-emerald-300/40 bg-emerald-300/15 text-emerald-100",
	warning: "border-amber-300/40 bg-amber-300/15 text-amber-100",
	danger: "border-rose-300/40 bg-rose-300/15 text-rose-100",
	info: "border-cyan-300/40 bg-cyan-300/15 text-cyan-100"
};

export default function Badge({ children, variant = "info" }) {
	return (
		<span className={`inline-flex items-center rounded-full border px-2 py-0.5 text-xs ${variants[variant] || variants.info}`}>
			{children}
		</span>
	);
}
