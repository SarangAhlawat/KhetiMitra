import { Link, useLocation, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { LogOut, Mic, MessageSquareText, Sparkles } from "lucide-react";

import { useAuth } from "../../context/AuthContext";
import Footer from "./Footer";

const nav = [
  { to: "/home", label: "Home" },
  { to: "/analysis", label: "Analysis", icon: Sparkles },
  { to: "/chat", label: "AI Chat", icon: MessageSquareText },
  { to: "/voice", label: "Voice Call", icon: Mic }
];

export default function KhetiShell({ title, subtitle, children }) {
  const location = useLocation();
  const navigate = useNavigate();
  const { auth, logout } = useAuth();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <div className="kheti-bg min-h-screen text-slate-100">
      <div className="ambient ambient-a" />
      <div className="ambient ambient-b" />
      <div className="relative z-10 mx-auto max-w-6xl px-4 py-6 md:px-8">
        <header className="glass-panel mb-6 flex flex-col gap-4 rounded-2xl px-5 py-4 md:flex-row md:items-center md:justify-between">
          <div>
            <p className="text-xs uppercase tracking-[0.22em] text-slate-300">KhetiMitra</p>
            <h1 className="text-xl font-semibold md:text-2xl">{title}</h1>
            {subtitle ? <p className="text-sm text-slate-300">{subtitle}</p> : null}
          </div>
          <div className="flex flex-wrap items-center gap-2">
            {nav.map((item) => {
              const active = location.pathname === item.to;
              const Icon = item.icon;
              return (
                <Link
                  key={item.to}
                  to={item.to}
                  className={`rounded-xl border px-3 py-2 text-sm transition ${active
                    ? "border-emerald-300/70 bg-emerald-300/15"
                    : "border-white/10 bg-white/5 hover:bg-white/10"
                    }`}
                >
                  <span className="inline-flex items-center gap-2">
                    {Icon ? <Icon size={14} /> : null}
                    {item.label}
                  </span>
                </Link>
              );
            })}
            <button
              type="button"
              onClick={handleLogout}
              className="rounded-xl border border-rose-300/40 bg-rose-400/10 px-3 py-2 text-sm text-rose-100 transition hover:bg-rose-400/20"
            >
              <span className="inline-flex items-center gap-2">
                <LogOut size={14} />
                Logout
              </span>
            </button>
          </div>
        </header>

        <motion.main
          initial={{ opacity: 0, y: 14 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.35, ease: "easeOut" }}
          className="space-y-6"
        >
          {children}
        </motion.main>

        <div className="mt-8 text-center text-xs text-slate-400">
          Signed in as <span className="font-medium text-slate-200">{auth.username || "farmer"}</span>
        </div>
      </div>
      <Footer />
    </div>
  );
}
