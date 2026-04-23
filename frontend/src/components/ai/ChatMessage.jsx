import { motion } from "framer-motion";

export default function ChatMessage({
  message,
  sender
}) {

  const isUser =
    sender === "user";

  return (

    <motion.div

      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}

      className={`flex ${
        isUser
          ? "justify-end"
          : "justify-start"
      }`}

    >

      <div

        className={`px-4 py-2 rounded-xl max-w-xs shadow ${
          isUser
            ? "bg-green-600 text-white"
            : "bg-gray-200 text-black"
        }`}

      >

        {message}

      </div>

    </motion.div>

  );
}