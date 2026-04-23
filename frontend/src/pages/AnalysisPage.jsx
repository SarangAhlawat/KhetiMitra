import { useMemo, useState } from "react";
import toast from "react-hot-toast";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";
import FarmerExplainabilityPanel from "../components/ai/FarmerExplainabilityPanel";
import { getEnvironment, getRecommendation, getRecommendationExplain } from "../services/api";

const initialInput = {
  ph: 6.9,
  nitrogen_kg_per_ha: 110,
  phosphorus_kg_per_ha: 42,
  potassium_kg_per_ha: 58,
  organic_carbon_percent: 0.72,
  rainfall_mm: 680,
  temperature_c: 28,
  humidity_percent: 58,
  area_hectares: 1.6,
  lat: 30.7333,
  lon: 76.7794
};

export default function AnalysisPage() {
  const [input, setInput] = useState(initialInput);
  const [environment, setEnvironment] = useState(null);
  const [result, setResult] = useState(null);
  const [explain, setExplain] = useState(null);
  const [loading, setLoading] = useState(false);

  const recommendationHint = useMemo(() => {
    if (!result) {
      return "Run analysis to generate crop and sustainability insights.";
    }

    if (result.sustainability_score > 75) {
      return "Strong sustainability pattern. Keep current nutrient and water discipline.";
    }

    if (result.sustainability_score > 60) {
      return "Moderate sustainability. Improve organic carbon and precision irrigation.";
    }

    return "Risky sustainability profile. Immediate soil and water interventions recommended.";
  }, [result]);

  const update = (field, value) => {
    setInput((prev) => ({ ...prev, [field]: Number(value) }));
  };

  const loadEnvironment = async () => {
    try {
      const { data } = await getEnvironment(input.lat, input.lon);
      setEnvironment(data);
      toast.success("Environment loaded");
    } catch (error) {
      toast.error("Could not load environment data");
    }
  };

  const runAnalysis = async () => {
    setLoading(true);

    const payload = {
      ph: input.ph,
      nitrogen_kg_per_ha: input.nitrogen_kg_per_ha,
      phosphorus_kg_per_ha: input.phosphorus_kg_per_ha,
      potassium_kg_per_ha: input.potassium_kg_per_ha,
      organic_carbon_percent: input.organic_carbon_percent,
      rainfall_mm: environment?.rainfall_mm || input.rainfall_mm,
      temperature_c: environment?.temperature_c || input.temperature_c,
      humidity_percent: environment?.humidity_percent || input.humidity_percent,
      area_hectares: input.area_hectares
    };

    try {
      const { data } = await getRecommendation(payload);
      setResult(data);

      try {
        const { data: explainData } = await getRecommendationExplain(payload);
        setExplain(explainData);
      } catch (error) {
        setExplain(null);
      }

      toast.success("Analysis completed");
    } catch (error) {
      setResult(null);
      setExplain(null);
      toast.error("Backend recommendation unavailable.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <KhetiShell
      title="AI Farm Analysis"
      subtitle="Get prediction and sustainability guidance directly in the UI."
    >
      <div className="grid gap-4 lg:grid-cols-[1.15fr_0.85fr]">
        <GlassCard title="Input Features">
          <div className="grid gap-3 sm:grid-cols-2">
            {Object.entries(input).map(([field, value]) => (
              <label key={field} className="text-sm capitalize text-slate-200">
                {field.replaceAll("_", " ")}
                <input
                  type="number"
                  step="0.01"
                  className="form-input mt-1"
                  value={value}
                  onChange={(e) => update(field, e.target.value)}
                />
              </label>
            ))}
          </div>
          <div className="mt-4 flex flex-wrap gap-3">
            <button type="button" onClick={loadEnvironment} className="btn-secondary">Load Live Environment</button>
            <button type="button" onClick={runAnalysis} disabled={loading} className="btn-primary">
              {loading ? "Analyzing..." : "Run Analysis"}
            </button>
          </div>
        </GlassCard>

        <div className="space-y-4">
          <GlassCard title="Prediction">
            <p className="text-sm text-slate-300">Recommended Crop</p>
            <p className="mt-1 text-2xl font-semibold text-emerald-200">{result?.recommended_crop || "-"}</p>
            <p className="mt-4 text-sm text-slate-300">Sustainability Score</p>
            <p className="mt-1 text-2xl font-semibold text-cyan-200">{result?.sustainability_score ?? "-"}</p>
            <p className="mt-4 rounded-xl border border-white/10 bg-white/5 p-3 text-sm text-slate-200">{recommendationHint}</p>
          </GlassCard>

          <GlassCard title="Explainability AI (Farmer-Friendly)">
            {explain ? (
              <FarmerExplainabilityPanel
                factors={explain.explanation || []}
                confidence={explain.confidence_score || 0}
              />
            ) : (
              <p className="text-sm text-slate-300">Run analysis to see feature-level explanation and confidence.</p>
            )}
          </GlassCard>

          <GlassCard title="Environment Snapshot">
            {environment ? (
              <div className="grid grid-cols-2 gap-2 text-sm">
                {Object.entries(environment).slice(0, 8).map(([k, v]) => (
                  <p key={k} className="rounded-lg border border-white/10 bg-white/5 px-2 py-1.5">
                    <span className="text-slate-300">{k}: </span>
                    <span className="text-slate-100">{String(v)}</span>
                  </p>
                ))}
              </div>
            ) : (
              <p className="text-sm text-slate-300">No environment data loaded yet.</p>
            )}
          </GlassCard>
        </div>
      </div>
    </KhetiShell>
  );
}
