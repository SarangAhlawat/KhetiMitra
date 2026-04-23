import { useMemo, useState } from "react";
import toast from "react-hot-toast";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";
import { getHistoryByFarm } from "../services/api";

export default function DistrictAnalytics() {
	const [farmId, setFarmId] = useState("1");
	const [rows, setRows] = useState([]);
	const [loading, setLoading] = useState(false);

	const summary = useMemo(() => {
		if (!rows.length) {
			return {
				count: 0,
				avgYield: 0,
				totalProfit: 0
			};
		}

		const totalYield = rows.reduce((acc, r) => acc + Number(r.yield_value || 0), 0);
		const totalProfit = rows.reduce((acc, r) => acc + Number(r.profit || 0), 0);

		return {
			count: rows.length,
			avgYield: totalYield / rows.length,
			totalProfit
		};
	}, [rows]);

	const load = async () => {
		setLoading(true);
		try {
			const { data } = await getHistoryByFarm(Number(farmId));
			setRows(Array.isArray(data) ? data : []);
		} catch (error) {
			setRows([]);
			toast.error("Could not load backend district data.");
		} finally {
			setLoading(false);
		}
	};

	return (
		<KhetiShell
			title="District Analytics"
			subtitle="Backend-driven summary of loaded farm history records."
		>
			<GlassCard title="Load District Source Data">
				<div className="flex flex-col gap-3 sm:flex-row">
					<input className="form-input" value={farmId} onChange={(e) => setFarmId(e.target.value)} placeholder="Farm ID" />
					<button type="button" className="btn-primary" onClick={load} disabled={loading}>
						{loading ? "Loading..." : "Fetch Data"}
					</button>
				</div>
			</GlassCard>

			<GlassCard title="Aggregated Snapshot">
				<div className="grid gap-3 sm:grid-cols-3">
					<div className="rounded-xl border border-white/10 bg-white/5 p-3 text-sm">Records: {summary.count}</div>
					<div className="rounded-xl border border-white/10 bg-white/5 p-3 text-sm">Avg Yield: {summary.avgYield.toFixed(2)}</div>
					<div className="rounded-xl border border-white/10 bg-white/5 p-3 text-sm">Total Profit: Rs. {summary.totalProfit.toFixed(2)}</div>
				</div>
				{!rows.length ? <p className="mt-3 text-sm text-slate-300">No backend records loaded yet.</p> : null}
			</GlassCard>
		</KhetiShell>
	);
}
