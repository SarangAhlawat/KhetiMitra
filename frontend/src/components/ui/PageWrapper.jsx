import { motion } from "framer-motion";

import { fadeIn } 
from "../../animations/motionVariants";

export default function PageWrapper({

  children

}) {

  return (

    <motion.div

      initial={fadeIn.initial}

      animate={fadeIn.animate}

      transition={fadeIn.transition}

      className="min-h-screen"

    >

      {children}

    </motion.div>

  );

}