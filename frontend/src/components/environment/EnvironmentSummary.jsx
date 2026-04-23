import { motion } from "framer-motion";

export default function EnvironmentSummary({ data }) {

  return (

    <motion.div

      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}

      className="bg-green-100 p-4 rounded-xl shadow"

    >

      <h2 className="font-bold mb-2">

        Environment Summary

      </h2>

      <p>

        Current temperature is
        {" "}
        <strong>
          {data.temperature}°C
        </strong>

        {" "}with humidity at{" "}

        <strong>
          {data.humidity}%
        </strong>

        {" "}in{" "}

        <strong>
          {data.district}
        </strong>.

      </p>

    </motion.div>

  );
}