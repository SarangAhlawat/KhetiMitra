import { motion }
from "framer-motion";

export default function Card({

  children

}) {

  return (

    <motion.div

      whileHover={{
        scale: 1.03
      }}

      className="
        bg-white
        rounded-xl
        shadow
        p-4
      "

    >

      {children}

    </motion.div>

  );

}