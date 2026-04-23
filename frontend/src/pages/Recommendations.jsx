import { useState } from "react";
import toast from "react-hot-toast";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";
import { getRecommendationExplain, searchKnowledge } from "../services/api";

export default function Recommendations() {
	const [crop, setCrop] = useState("");
	const [loading, setLoading] = useState(false);
	const [explain, setExplain] = useState([]);
	const [practices, setPractices] = useState([]);
	const [schemes, setSchemes] = useState([]);

	const loadRecommendations = async () => {
		if (!crop.trim()) {
			toast.error("Enter crop or issue first.");
			return;
		}

		setLoading(true);
		try {
			const payload = {
				crop,
				ph: 7,
				nitrogen_kg_per_ha: 100,
				phosphorus_kg_per_ha: 45,
				potassium_kg_per_ha: 55,
				organic_carbon_percent: 0.6,
				rainfall_mm: 650,
				temperature_c: 28,
				humidity_percent: 58,
				area_hectares: 1.5
			};

			const [explainRes, practicesRes, schemesRes] = await Promise.all([
				getRecommendationExplain(payload),
				searchKnowledge("practices", crop),
				searchKnowledge("schemes", crop)
			]);

			setExplain(explainRes.data?.explanation || []);
			setPractices(practicesRes.data?.results || []);
			setSchemes(schemesRes.data?.results || []);
		} catch (error) {
			setExplain([]);
			setPractices([]);
			setSchemes([]);
			toast.error("Could not load recommendations from backend.");
		} finally {
			setLoading(false);
		}
	};

	return (
		<KhetiShell
			title="Farmer Recommendations"
			subtitle="Get backend-generated guidance and related practices/schemes."
		>
			<GlassCard title="Find Recommendations">
				<div className="flex flex-col gap-3 sm:flex-row">
					<input
						className="form-input"
						value={crop}
						onChange={(e) => setCrop(e.target.value)}
						placeholder="Enter crop or issue (e.g., wheat, water stress)"
					/>
					<button type="button" className="btn-primary" onClick={loadRecommendations} disabled={loading}>
						{loading ? "Loading..." : "Get Recommendations"}
					</button>
				</div>
			</GlassCard>

			<div className="grid gap-4 lg:grid-cols-[1.05fr_0.95fr]">
				<GlassCard title="Model Explanation Factors">
					<div className="space-y-3">
						{explain.length ? explain.map((item, idx) => (
							<article key={`${item.feature}-${idx}`} className="rounded-xl border border-white/10 bg-white/5 p-4">
								<h3 className="text-base font-semibold">{item.feature}</h3>
								<p className="mt-1 text-sm text-slate-300">{item.note}</p>
							</article>
						)) : (
							<p className="text-sm text-slate-300">No backend recommendation loaded yet.</p>
						)}
					</div>
				</GlassCard>

				<div className="space-y-4">
					<GlassCard title="Sustainable Practices (Knowledge Base)">
						{practices.length ? (
							<ul className="space-y-2 text-sm text-slate-300">
								{practices.map((item, idx) => (
									<li key={idx} className="rounded-xl border border-white/10 bg-white/5 p-3">{item}</li>
								))}
							</ul>
						) : (
							<p className="text-sm text-slate-300">No practices loaded yet.</p>
						)}
					</GlassCard>

					<GlassCard title="Relevant Schemes (Knowledge Base)">
						{schemes.length ? (
							<ul className="space-y-2 text-sm text-slate-300">
								{schemes.map((item, idx) => (
									<li key={idx} className="rounded-xl border border-white/10 bg-white/5 p-3">{item}</li>
								))}
							</ul>
						) : (
							<p className="text-sm text-slate-300">No schemes loaded yet.</p>
						)}
					</GlassCard>
				</div>
			</div>
		</KhetiShell>
	);
}
