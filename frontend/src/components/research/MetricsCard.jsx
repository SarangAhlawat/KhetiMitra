import { motion } from "framer-motion";

export default function MetricsCard({
  title,
  value
}) {

  return (

    <motion.div

      whileHover={{ scale: 1.05 }}

      className="rounded-xl border border-white/10 bg-white/5 p-4"

    >

      <h3 className="text-slate-300">

        {title}

      </h3>

      <p className="text-2xl font-bold text-emerald-200">

        {value}

      </p>

    </motion.div>

  );
}