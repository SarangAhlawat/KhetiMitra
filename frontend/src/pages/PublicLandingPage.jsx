import { Link } from "react-router-dom";
import { ArrowRight, BrainCircuit, Leaf, Mic2, Sparkles } from "lucide-react";
import { motion } from "framer-motion";
import { useAuth } from "../context/AuthContext";

import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";

const features = [
  {
    icon: Sparkles,
    title: "Smart Crop Recommendation",
    description: "Get a crop suggestion from your farm and environment data."
  },
  {
    icon: BrainCircuit,
    title: "Explainable AI Insights",
    description: "Understand why the model suggested a crop in simple terms."
  },
  {
    icon: Mic2,
    title: "Voice & Chat Advisory",
    description: "Ask questions naturally and get practical farming guidance."
  },
  {
    icon: Leaf,
    title: "Sustainability Score",
    description: "Track sustainability health and improve soil and water practices."
  }
];

export default function PublicLandingPage() {
  const { isAuthenticated } = useAuth();

  const gatedPath = (path) => (isAuthenticated ? path : "/login");

  return (
    <div className="marketing-hero min-h-screen text-slate-100">
      <div className="relative overflow-hidden">
        <div className="absolute -left-24 top-24 h-72 w-72 rounded-full bg-emerald-300/20 blur-3xl" />
        <div className="absolute -right-20 top-10 h-72 w-72 rounded-full bg-cyan-300/20 blur-3xl" />
        <Navbar />

        <section className="mx-auto grid max-w-6xl gap-10 px-4 pb-16 pt-14 md:grid-cols-[1.1fr_0.9fr] md:px-8 md:pt-20">
          <div>
            <p className="inline-flex rounded-full border border-emerald-300/30 bg-emerald-300/10 px-3 py-1 text-xs uppercase tracking-[0.18em] text-emerald-200">
              AI-Powered Sustainable Farming
            </p>
            <h1 className="mt-4 text-3xl font-semibold leading-tight md:text-5xl">
              Farmer-first decisions with transparent AI recommendations
            </h1>
            <p className="mt-4 max-w-xl text-base text-slate-300 md:text-lg">
              KhetiMitra helps farmers quickly check crop recommendations, ask AI questions, and get voice guidance in one simple flow.
            </p>
            <div className="mt-7 flex flex-wrap gap-3">
              <Link to={gatedPath("/analysis")} className="btn-primary">
                Start Analysis
                <ArrowRight size={15} />
              </Link>
              <Link to={gatedPath("/chat")} className="btn-secondary">AI Chat</Link>
              <Link to={gatedPath("/voice")} className="btn-secondary">Voice Call</Link>
            </div>

            {!isAuthenticated ? (
              <p className="mt-3 text-sm text-slate-300">
                New farmer? <Link to="/register" className="text-emerald-200">Register first</Link> to save your farm profile.
              </p>
            ) : null}
          </div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.45 }}
            className="glass-panel rounded-3xl p-6"
          >
            <p className="text-sm text-slate-300">Farmer-first flow</p>
            <div className="mt-4 space-y-3 text-sm">
              <div className="rounded-xl border border-white/10 bg-white/5 p-3">
                1. Register and add farm details once.
              </div>
              <div className="rounded-xl border border-white/10 bg-white/5 p-3">
                2. Run Analysis to get recommendation and explanation.
              </div>
              <div className="rounded-xl border border-white/10 bg-white/5 p-3">
                3. Use Chat or Voice for clear next-step advice.
              </div>
            </div>
          </motion.div>
        </section>
      </div>

      <section id="features" className="mx-auto max-w-6xl px-4 pb-10 md:px-8">
        <h2 className="text-2xl font-semibold md:text-3xl">Everything arranged for the farmer journey</h2>
        <p className="mt-2 text-slate-300">From onboarding to recommendation to explainability, each step is mobile-friendly and practical.</p>

        <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((feature, index) => {
            const Icon = feature.icon;
            return (
              <motion.article
                key={feature.title}
                initial={{ opacity: 0, y: 16 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-80px" }}
                transition={{ delay: index * 0.08 }}
                className="glass-panel rounded-2xl p-4"
              >
                <div className="mb-3 inline-flex rounded-xl border border-cyan-200/30 bg-cyan-300/10 p-2">
                  <Icon size={18} />
                </div>
                <h3 className="text-lg font-semibold">{feature.title}</h3>
                <p className="mt-2 text-sm text-slate-300">{feature.description}</p>
              </motion.article>
            );
          })}
        </div>
      </section>

      <section id="explainability" className="mx-auto max-w-6xl px-4 pb-12 md:px-8">
        <div className="glass-panel rounded-3xl p-6 md:p-8">
          <h2 className="text-2xl font-semibold md:text-3xl">Explainability AI built for trust</h2>
          <p className="mt-2 text-slate-300">After analysis, the app shows which factors increased or reduced your recommendation confidence and what you can improve.</p>
        </div>
      </section>

      <section id="how" className="mx-auto max-w-6xl px-4 pb-14 md:px-8">
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          {["Register", "Add Farm Data", "Run AI Analysis", "Act on Recommendations"].map((step, idx) => (
            <div key={step} className="rounded-xl border border-white/10 bg-white/5 p-3 text-sm">
              <p className="text-xs text-slate-400">Step {idx + 1}</p>
              <p className="mt-1 font-semibold">{step}</p>
            </div>
          ))}
        </div>
      </section>

      <Footer />
    </div>
  );
}
