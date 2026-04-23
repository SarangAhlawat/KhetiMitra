import { NavLink } from "react-router-dom";

export default function Sidebar({ items = [] }) {
	return (
		<aside className="glass-panel h-fit rounded-2xl p-4">
			<nav className="space-y-2">
				{items.map((item) => (
					<NavLink
						key={item.to}
						to={item.to}
						className={({ isActive }) => `block rounded-lg px-3 py-2 text-sm transition ${isActive ? "bg-emerald-300/15 text-emerald-100" : "text-slate-300 hover:bg-white/10"}`}
					>
						{item.label}
					</NavLink>
				))}
			</nav>
		</aside>
	);
}
