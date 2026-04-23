import { Link } from "react-router-dom";
import { useState } from "react";
import toast from "react-hot-toast";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";
import { getHistoryByFarm } from "../services/api";

export default function OfficerDashboard() {
  const [farmId, setFarmId] = useState("1");
  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(false);

  const loadRecords = async () => {
    setLoading(true);
    try {
      const { data } = await getHistoryByFarm(Number(farmId));
      setRecords(Array.isArray(data) ? data : []);
    } catch (error) {
      setRecords([]);
      toast.error("Could not load backend records.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <KhetiShell
      title="Officer Portal"
      subtitle="Backend-backed records view for monitoring farm outcomes."
    >
      <GlassCard title="Load Farm Records" action={<Link to="/district-analytics" className="text-sm text-cyan-200">Open district view</Link>}>
        <div className="flex flex-col gap-3 sm:flex-row">
          <input
            className="form-input"
            value={farmId}
            onChange={(e) => setFarmId(e.target.value)}
            placeholder="Farm ID"
          />
          <button type="button" className="btn-primary" onClick={loadRecords} disabled={loading}>
            {loading ? "Loading..." : "Fetch Records"}
          </button>
        </div>
      </GlassCard>

      <GlassCard title="Recent Backend Records">
        {!records.length ? (
          <p className="text-sm text-slate-300">No records loaded yet.</p>
        ) : (
          <div className="space-y-2">
            {records.slice(-10).map((item) => (
              <div key={item.history_id} className="rounded-xl border border-white/10 bg-white/5 p-3 text-sm">
                <p>Farm ID: {item.farm_id}</p>
                <p>Crop: {item.crop}</p>
                <p>Yield: {item.yield_value}</p>
                <p>Profit: {item.profit}</p>
              </div>
            ))}
          </div>
        )}
      </GlassCard>

      <div className="grid gap-4 lg:grid-cols-2">
        <GlassCard title="Officer Actions">
          <p className="text-sm text-slate-300">Use history and recommendation endpoints for district decisions.</p>
          <div className="mt-3 flex flex-wrap gap-2">
            <Link to="/recommendations" className="btn-secondary">Recommendations</Link>
            <Link to="/history" className="btn-secondary">History</Link>
          </div>
        </GlassCard>
        <GlassCard title="Notes">
          <p className="text-sm text-slate-300">Risk map and trend analytics will appear here when district APIs are connected.</p>
        </GlassCard>
      </div>
    </KhetiShell>
  );
}