import { motion } from "framer-motion";

export default function MetricsCard({
  title,
  value
}) {

  return (

    <motion.div

      whileHover={{ scale: 1.05 }}

      className="bg-white shadow rounded-xl p-4"

    >

      <h3 className="text-gray-500">

        {title}

      </h3>

      <p className="text-2xl font-bold text-green-600">

        {value}

      </p>

    </motion.div>

  );
}