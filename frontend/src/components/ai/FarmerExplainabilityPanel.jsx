import { motion } from "framer-motion";

import Badge from "../ui/Badge";

export default function FarmerExplainabilityPanel({ factors = [], confidence = 0 }) {
  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <p className="text-sm text-slate-300">Prediction confidence</p>
        <Badge variant={confidence >= 0.8 ? "success" : confidence >= 0.65 ? "warning" : "danger"}>
          {(confidence * 100).toFixed(0)}%
        </Badge>
      </div>

      <div className="h-2 w-full rounded-full bg-white/10">
        <div
          className="h-full rounded-full bg-gradient-to-r from-cyan-300 to-emerald-300"
          style={{ width: `${Math.max(5, confidence * 100)}%` }}
        />
      </div>

      <div className="space-y-2">
        {factors.map((factor, index) => {
          const positive = factor.contribution >= 0;
          const width = Math.min(100, Math.abs(factor.contribution) * 380);

          return (
            <motion.div
              key={factor.feature}
              initial={{ opacity: 0, x: -12 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.08 }}
              className="rounded-xl border border-white/10 bg-white/5 p-3"
            >
              <div className="mb-1 flex items-center justify-between gap-2">
                <p className="text-sm font-medium text-slate-100">{factor.feature}</p>
                <Badge variant={positive ? "success" : "danger"}>
                  {positive ? "+" : ""}{(factor.contribution * 100).toFixed(1)}
                </Badge>
              </div>

              <div className="mb-2 h-2 rounded-full bg-white/10">
                <div
                  className={`h-full rounded-full ${positive ? "bg-emerald-300" : "bg-rose-300"}`}
                  style={{ width: `${width}%` }}
                />
              </div>

              <p className="text-xs text-slate-300">{factor.note}</p>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
