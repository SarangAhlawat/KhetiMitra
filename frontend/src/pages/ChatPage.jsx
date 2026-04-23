import { useState } from "react";
import { Send } from "lucide-react";
import toast from "react-hot-toast";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";
import { askAssistant } from "../services/api";
import { useAuth } from "../context/AuthContext";

export default function ChatPage() {
  const { auth } = useAuth();
  const [messages, setMessages] = useState([
    {
      id: 1,
      role: "assistant",
      text: "Sat Sri Akal! Tell me your crop, soil issue, or water concern and I will suggest practical steps."
    }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    const text = input.trim();
    if (!text) {
      return;
    }

    const userMessage = {
      id: Date.now(),
      role: "user",
      text
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const { data } = await askAssistant({
        user_id: auth.farmerId || 1,
        message: text
      });

      setMessages((prev) => [
        ...prev,
        {
          id: Date.now() + 1,
          role: "assistant",
          text: data.response || "I could not process that query right now."
        }
      ]);
    } catch (error) {
      toast.error("Assistant unavailable");
      setMessages((prev) => [
        ...prev,
        {
          id: Date.now() + 1,
          role: "assistant",
          text: "I am having trouble connecting. Please try again in a moment."
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <KhetiShell
      title="AI Chat Advisor"
      subtitle="Human-like conversation for crop planning, sustainability, pests, and schemes."
    >
      <GlassCard className="p-0">
        <div className="max-h-[62vh] min-h-[62vh] overflow-y-auto p-5">
          <div className="space-y-3">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`max-w-[85%] rounded-xl px-4 py-3 text-sm ${message.role === "assistant"
                  ? "border border-cyan-200/25 bg-cyan-300/10 text-cyan-50"
                  : "ml-auto border border-emerald-200/30 bg-emerald-400/15 text-emerald-50"
                  }`}
              >
                {message.text}
              </div>
            ))}
            {loading ? (
              <div className="w-fit rounded-xl border border-white/10 bg-white/10 px-4 py-2 text-sm text-slate-300">
                Thinking...
              </div>
            ) : null}
          </div>
        </div>

        <div className="border-t border-white/10 p-4">
          <div className="flex gap-2">
            <input
              className="form-input w-full"
              value={input}
              placeholder="Ask in your own words..."
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  sendMessage();
                }
              }}
            />
            <button type="button" className="btn-primary" onClick={sendMessage} disabled={loading}>
              <Send size={16} />
            </button>
          </div>
        </div>
      </GlassCard>
    </KhetiShell>
  );
}