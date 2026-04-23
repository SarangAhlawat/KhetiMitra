export default function Button({ children, variant = "primary", className = "", ...rest }) {
	const base = "inline-flex items-center justify-center gap-2 rounded-xl px-4 py-2.5 text-sm font-semibold transition";
	const variants = {
		primary: "bg-gradient-to-r from-emerald-400 to-cyan-300 text-slate-900 hover:brightness-110",
		secondary: "border border-cyan-200/40 bg-cyan-300/10 text-cyan-100 hover:bg-cyan-300/20",
		ghost: "border border-white/15 bg-white/5 text-slate-100 hover:bg-white/10"
	};

	return (
		<button type="button" className={`${base} ${variants[variant] || variants.primary} ${className}`} {...rest}>
			{children}
		</button>
	);
}
