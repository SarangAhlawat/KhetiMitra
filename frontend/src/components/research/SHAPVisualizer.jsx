export default function SHAPVisualizer() {

  const shapData = [

    {
      feature: "Soil pH",
      impact: "High"
    },

    {
      feature: "Rainfall",
      impact: "Medium"
    },

    {
      feature: "Nitrogen",
      impact: "High"
    }

  ];

  return (
    <div>
      <h2 className="mb-3 text-base font-semibold text-slate-100">SHAP Explanation</h2>
      <div className="grid gap-2 sm:grid-cols-2">
        {shapData.map((item, i) => (
          <div
            key={i}
            className="flex items-center justify-between rounded-xl border border-white/10 bg-white/5 p-3 text-sm"
          >
            <span>{item.feature}</span>
            <span className="font-semibold text-emerald-200">{item.impact}</span>
          </div>
        ))}
      </div>
    </div>
  );
}