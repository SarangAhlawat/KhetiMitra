import { PhoneCall } from "lucide-react";
import { useState } from "react";
import toast from "react-hot-toast";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";
import { askAssistant } from "../services/api";
import { useAuth } from "../context/AuthContext";

const supportNumber = "+911800123456";

export default function VoicePage() {
  const { auth } = useAuth();
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  const sendVoiceIntent = async () => {
    if (!message.trim()) {
      return;
    }

    setLoading(true);
    try {
      const { data } = await askAssistant({
        user_id: auth.farmerId || 1,
        message
      });
      setReply(data.response || "No response received");
      setMessage("");
    } catch (error) {
      toast.error("Voice assistant endpoint failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <KhetiShell
      title="Voice Advisory"
      subtitle="Dial KhetiMitra and continue with AI-backed, human-like support."
    >
      <div className="grid gap-4 lg:grid-cols-2">
        <GlassCard title="Call KhetiMitra Helpline">
          <p className="text-sm text-slate-300">Use the dial button to connect your phone with the advisory agent.</p>
          <a href={`tel:${supportNumber}`} className="btn-primary mt-4 inline-flex items-center gap-2">
            <PhoneCall size={16} />
            Dial {supportNumber}
          </a>
          <p className="mt-3 text-xs text-slate-400">Telephony handoff needs provider integration (Twilio/Exotel) on backend for live IVR automation.</p>
        </GlassCard>

        <GlassCard title="Voice AI Preview">
          <p className="text-sm text-slate-300">Type what the farmer says during call and get a natural recommendation.</p>
          <textarea
            rows={4}
            className="form-input mt-3 w-full"
            placeholder="Example: Cotton crop has pest signs, what should I do this week?"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
          <button type="button" onClick={sendVoiceIntent} disabled={loading} className="btn-secondary mt-3">
            {loading ? "Processing..." : "Process Voice Query"}
          </button>
          <div className="mt-3 rounded-xl border border-white/10 bg-white/5 p-3 text-sm text-slate-200 min-h-[96px]">
            {reply || "Assistant response will appear here."}
          </div>
        </GlassCard>
      </div>
    </KhetiShell>
  );
}
