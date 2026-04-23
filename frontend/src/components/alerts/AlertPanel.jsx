export default function AlertPanel() {

  const alerts = [

    {
      type: "High Risk",
      message: "Soil degradation detected"
    },

    {
      type: "Warning",
      message: "Water stress increasing"
    }

  ];

  return (
    <div className="space-y-2">
      {alerts.map((a, i) => (
        <div
          key={i}
          className="rounded-xl border border-rose-300/25 bg-rose-300/10 p-3 text-sm"
        >
          <p className="font-semibold text-rose-100">{a.type}</p>
          <p className="text-slate-200">{a.message}</p>
        </div>
      ))}
    </div>
  );
}