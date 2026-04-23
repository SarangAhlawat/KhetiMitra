import { motion } from "framer-motion";

import {
  scaleHover,
  buttonTap
}
from "../../animations/motionVariants";

export default function AnimatedButton({

  children,
  onClick

}) {

  return (

    <motion.button

      whileHover={scaleHover.whileHover}

      whileTap={buttonTap.whileTap}

      onClick={onClick}

      className="
        bg-green-600
        text-white
        px-4
        py-2
        rounded-lg
        shadow
      "

    >

      {children}

    </motion.button>

  );

}