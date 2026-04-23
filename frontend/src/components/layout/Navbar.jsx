import { Link } from "react-router-dom";
import { Menu, Sprout, X } from "lucide-react";
import { useEffect, useState } from "react";
import { useAuth } from "../../context/AuthContext";
import { getBackendStatus } from "../../services/api";

const links = [
  { to: "#features", label: "Features" },
  { to: "#how", label: "How It Works" }
];

export default function Navbar({ ctaTo = "/login" }) {
  const [open, setOpen] = useState(false);
  const [backendOnline, setBackendOnline] = useState(false);
  const { isAuthenticated, auth } = useAuth();

  const dashboardPath = auth.hasFarmProfile ? "/home" : "/onboarding";

  useEffect(() => {
    let active = true;

    const checkBackend = async () => {
      try {
        await getBackendStatus();
        if (active) {
          setBackendOnline(true);
        }
      } catch (error) {
        if (active) {
          setBackendOnline(false);
        }
      }
    };

    checkBackend();
    const timer = setInterval(checkBackend, 15000);

    return () => {
      active = false;
      clearInterval(timer);
    };
  }, []);

  return (
    <header className="sticky top-0 z-30 border-b border-white/10 bg-[#06101a]/85 backdrop-blur-md">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3 md:px-8">
        <Link to="/" className="flex items-center gap-2">
          <span className="rounded-lg border border-emerald-300/30 bg-emerald-300/15 p-1.5">
            <Sprout size={18} className="text-emerald-200" />
          </span>
          <span className="text-base font-semibold text-slate-100 md:text-lg">KhetiMitra</span>
        </Link>

        <nav className="hidden items-center gap-6 md:flex">
          <div className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-slate-300">
            <span className={`h-2.5 w-2.5 rounded-full ${backendOnline ? "bg-emerald-400" : "bg-rose-400"}`} />
            {backendOnline ? "Backend connected" : "Backend offline"}
          </div>
          {links.map((link) => (
            <a key={link.to} href={link.to} className="text-sm text-slate-300 transition hover:text-white">
              {link.label}
            </a>
          ))}
          {isAuthenticated ? (
            <Link to={dashboardPath} className="btn-primary text-sm">Dashboard</Link>
          ) : (
            <>
              <Link to="/register" className="text-sm text-emerald-200 transition hover:text-white">Register</Link>
              <Link to={ctaTo} className="btn-primary text-sm">Farmer Login</Link>
            </>
          )}
        </nav>

        <button type="button" className="md:hidden" onClick={() => setOpen((prev) => !prev)}>
          {open ? <X size={20} /> : <Menu size={20} />}
        </button>
      </div>

      {open ? (
        <div className="border-t border-white/10 bg-[#06101a] px-4 py-3 md:hidden">
          <div className="flex flex-col gap-3">
            <div className="inline-flex w-fit items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-slate-300">
              <span className={`h-2.5 w-2.5 rounded-full ${backendOnline ? "bg-emerald-400" : "bg-rose-400"}`} />
              {backendOnline ? "Backend connected" : "Backend offline"}
            </div>
            {links.map((link) => (
              <a key={link.to} href={link.to} className="text-sm text-slate-200" onClick={() => setOpen(false)}>
                {link.label}
              </a>
            ))}
            {isAuthenticated ? (
              <Link to={dashboardPath} className="btn-primary w-fit text-sm" onClick={() => setOpen(false)}>Dashboard</Link>
            ) : (
              <>
                <Link to="/register" className="text-sm text-emerald-200" onClick={() => setOpen(false)}>Register</Link>
                <Link to={ctaTo} className="btn-primary w-fit text-sm" onClick={() => setOpen(false)}>Farmer Login</Link>
              </>
            )}
          </div>
        </div>
      ) : null}
    </header>
  );
}