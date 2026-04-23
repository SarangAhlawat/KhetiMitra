import { useState } from "react";
import toast from "react-hot-toast";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";
import { getRecommendationExplain } from "../services/api";

export default function ResearchDashboard() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const loadExplainability = async () => {
    setLoading(true);
    try {
      const { data } = await getRecommendationExplain({
        ph: 7,
        nitrogen_kg_per_ha: 100,
        phosphorus_kg_per_ha: 45,
        potassium_kg_per_ha: 55,
        organic_carbon_percent: 0.6,
        rainfall_mm: 650,
        temperature_c: 28,
        humidity_percent: 58,
        area_hectares: 1.5
      });
      setResult(data);
    } catch (error) {
      setResult(null);
      toast.error("Could not load explainability output.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <KhetiShell
      title="Research Dashboard"
      subtitle="Inspect backend explainability output for current recommendation model."
    >
      <GlassCard title="Load Explainability Data">
        <button type="button" className="btn-primary" onClick={loadExplainability} disabled={loading}>
          {loading ? "Loading..." : "Fetch From Backend"}
        </button>
      </GlassCard>

      <GlassCard title="Backend Explainability Output">
        {!result ? (
          <p className="text-sm text-slate-300">No backend data loaded yet.</p>
        ) : (
          <div className="space-y-3 text-sm">
            <p>Recommended Crop: <span className="text-emerald-200">{result.recommended_crop}</span></p>
            <p>Sustainability Score: <span className="text-cyan-200">{result.sustainability_score}</span></p>
            <p>Confidence: <span className="text-cyan-200">{(result.confidence_score * 100).toFixed(0)}%</span></p>

            <div className="space-y-2">
              {(result.explanation || []).map((item, idx) => (
                <div key={`${item.feature}-${idx}`} className="rounded-xl border border-white/10 bg-white/5 p-3">
                  <p className="font-semibold">{item.feature}</p>
                  <p className="text-slate-300">{item.note}</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </GlassCard>
    </KhetiShell>
  );
}