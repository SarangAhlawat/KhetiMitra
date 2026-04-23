import { useMemo, useState } from "react";
import toast from "react-hot-toast";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";
import { getHistoryByFarm } from "../services/api";

export default function History() {
	const [farmId, setFarmId] = useState("1");
	const [rows, setRows] = useState([]);
	const [loading, setLoading] = useState(false);

	const totalProfit = useMemo(() => rows.reduce((acc, row) => acc + Number(row.profit || 0), 0), [rows]);

	const loadHistory = async () => {
		setLoading(true);
		try {
			const { data } = await getHistoryByFarm(Number(farmId));
			setRows(Array.isArray(data) ? data : []);
		} catch (error) {
			setRows([]);
			toast.error("History API unavailable.");
		} finally {
			setLoading(false);
		}
	};

	return (
		<KhetiShell
			title="Farm History"
			subtitle="Track season-wise crop, input usage, and profit in one place."
		>
			<GlassCard title="Load Farm History">
				<div className="flex flex-col gap-3 sm:flex-row sm:items-end">
					<label className="text-sm">
						Farm ID
						<input className="form-input mt-1" value={farmId} onChange={(e) => setFarmId(e.target.value)} />
					</label>
					<button type="button" className="btn-primary" onClick={loadHistory} disabled={loading}>
						{loading ? "Loading..." : "Load History"}
					</button>
					<p className="text-sm text-slate-300 sm:ml-auto">Total Profit: <span className="font-semibold text-emerald-200">Rs. {totalProfit.toLocaleString()}</span></p>
				</div>
			</GlassCard>

			<GlassCard title="Season Records">
				<div className="overflow-x-auto">
					<table className="min-w-full text-sm">
						<thead>
							<tr className="border-b border-white/10 text-left text-slate-300">
								<th className="px-2 py-2">ID</th>
								<th className="px-2 py-2">Crop</th>
								<th className="px-2 py-2">Yield</th>
								<th className="px-2 py-2">Fertilizer</th>
								<th className="px-2 py-2">Pesticide</th>
								<th className="px-2 py-2">Profit</th>
							</tr>
						</thead>
						<tbody>
							{rows.map((row) => (
								<tr key={row.history_id} className="border-b border-white/5">
									<td className="px-2 py-2">{row.history_id}</td>
									<td className="px-2 py-2">{row.crop}</td>
									<td className="px-2 py-2">{row.yield_value}</td>
									<td className="px-2 py-2">{row.fertilizer}</td>
									<td className="px-2 py-2">{row.pesticide}</td>
									<td className="px-2 py-2">{row.profit}</td>
								</tr>
							))}
						</tbody>
					</table>
					{!rows.length ? (
						<p className="mt-3 text-sm text-slate-300">No history records found for this farm yet.</p>
					) : null}
				</div>
			</GlassCard>
		</KhetiShell>
	);
}
