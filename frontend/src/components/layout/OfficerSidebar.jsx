import { motion } from "framer-motion";

export default function OfficerSidebar() {

  return (

    <motion.div

      initial={{ x: -200 }}
      animate={{ x: 0 }}

      className="bg-green-700 text-white w-64 min-h-screen p-4"

    >

      <h2 className="text-xl font-bold mb-6">
        Officer Panel
      </h2>

      <ul className="space-y-4">

        <li className="hover:text-yellow-300 cursor-pointer">
          Dashboard
        </li>

        <li className="hover:text-yellow-300 cursor-pointer">
          District Analytics
        </li>

        <li className="hover:text-yellow-300 cursor-pointer">
          Reports
        </li>

      </ul>

    </motion.div>

  );
}