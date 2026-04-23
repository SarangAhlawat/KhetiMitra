import { Link } from "react-router-dom";
import { MessageCircle, Mic2, Sparkles, History } from "lucide-react";
import { motion } from "framer-motion";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";

const cards = [
  {
    to: "/analysis",
    title: "Farm Analysis",
    description: "Get crop prediction, sustainability score, and practical actions instantly.",
    icon: Sparkles
  },
  {
    to: "/chat",
    title: "AI Chat",
    description: "Ask in natural language and receive farmer-friendly recommendations.",
    icon: MessageCircle
  },
  {
    to: "/voice",
    title: "Voice Call Agent",
    description: "Tap to dial advisory helpline and continue with contextual AI support.",
    icon: Mic2
  },
  {
    to: "/history",
    title: "Farm History",
    description: "Review your previous records and seasonal outcomes.",
    icon: History
  }
];

export default function LandingPage() {
  return (
    <KhetiShell
      title="Decision Support Hub"
      subtitle="Choose one task and continue quickly."
    >
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-2">
        {cards.map((card, i) => {
          const Icon = card.icon;
          return (
            <motion.div
              key={card.to}
              initial={{ opacity: 0, y: 18 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.12, duration: 0.35 }}
            >
              <Link to={card.to}>
                <GlassCard className="h-full transition hover:-translate-y-1 hover:bg-white/10">
                  <div className="mb-4 inline-flex rounded-xl border border-cyan-200/30 bg-cyan-300/10 p-2">
                    <Icon size={22} />
                  </div>
                  <h3 className="text-xl font-semibold">{card.title}</h3>
                  <p className="mt-2 text-sm text-slate-300">{card.description}</p>
                </GlassCard>
              </Link>
            </motion.div>
          );
        })}
      </div>
    </KhetiShell>
  );
}
