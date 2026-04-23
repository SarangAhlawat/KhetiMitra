import { motion } from "framer-motion";

const steps = [

  "Input Received",
  "Weather Loaded",
  "Soil Analyzed",
  "ML Model Prediction",
  "QSSM Computed",
  "Recommendation Generated"

];

export default function DecisionTimeline() {

  return (

    <div className="space-y-2">

      {steps.map((step, i) => (

        <motion.div

          key={i}

          initial={{ opacity: 0 }}

          animate={{ opacity: 1 }}

          transition={{ delay: i * 0.3 }}

          className="bg-green-50 p-2 rounded"

        >
          {step}

        </motion.div>

      ))}

    </div>

  );
}