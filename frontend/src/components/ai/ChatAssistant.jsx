import { useState, useRef } from "react";
// useEffect

import ChatMessage
from "./ChatMessage";

import TypingIndicator
from "./TypingIndicator";

import { chatAssistant }
from "../../services/api";

import { Send } from "lucide-react";

// useEffect(() => {

//   messagesEndRef.current?.scrollIntoView({
//     behavior: "smooth"
//   });

// }, [messages]);

export default function ChatAssistant() {

  const [messages, setMessages] =
    useState([]);

  const [input, setInput] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const messagesEndRef =
    useRef(null);

  const sendMessage =
    async () => {

      if (!input) return;

      const userMessage = {
        text: input,
        sender: "user"
      };

      setMessages(prev =>
        [...prev, userMessage]
      );

      setLoading(true);

      try {

        const res =
          await chatAssistant(input);

        const botMessage = {

          text: res.data.response,
          sender: "bot"

        };

        setMessages(prev =>
          [...prev, botMessage]
        );

      }

      catch (error) {

        setMessages(prev => [

          ...prev,

          {

            text:
              "Error fetching response.",
            sender: "bot"

          }

        ]);

      }

      setLoading(false);

      setInput("");

    };

  return (

    <div className="bg-white rounded-xl shadow flex flex-col h-[500px]">

      {/* Header */}

      <div className="bg-green-600 text-white px-4 py-2 font-bold rounded-t-xl">

        AI Assistant

      </div>

      {/* Messages */}

      <div className="flex-1 overflow-y-auto p-3 space-y-2">

        {messages.map((msg, i) => (

          <ChatMessage

            key={i}

            message={msg.text}

            sender={msg.sender}

          />

        ))}

        {loading && (

          <TypingIndicator />

        )}

        <div ref={messagesEndRef} />

      </div>

      {/* Input */}

      <div className="flex border-t">

        <input

          value={input}

          onChange={(e) =>
            setInput(e.target.value)
          }

          placeholder="Ask about farming..."

          className="flex-1 p-2 outline-none"

        />

        <button

          onClick={sendMessage}

          className="bg-green-600 text-white px-4"

        >

          <Send size={18} />

        </button>

      </div>

    </div>

  );
}