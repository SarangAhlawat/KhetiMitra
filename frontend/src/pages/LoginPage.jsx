import { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import { loginUser } from "../services/api";
import { useAuth } from "../context/AuthContext";

export default function LoginPage() {
  const navigate = useNavigate();
  const location = useLocation();
  const { login } = useAuth();

  const [form, setForm] = useState({ username: "", password: "" });
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const { data } = await loginUser(form);
      login({ token: data.access_token, username: form.username });
      toast.success("Welcome back to KhetiMitra");
      navigate(location.state?.from || "/onboarding");
    } catch (error) {
      toast.error(error?.response?.data?.detail || "Login failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-bg min-h-screen px-4 py-10 text-slate-100">
      <div className="mx-auto max-w-md">
        <div className="auth-card rounded-3xl p-7 md:p-8">
          <p className="text-xs uppercase tracking-[0.22em] text-emerald-200">KhetiMitra</p>
          <h1 className="mt-2 text-3xl font-semibold">Farmer Login</h1>
          <p className="mt-1 text-sm text-slate-300">Sign in to access AI-guided sustainable farming support.</p>

          <form className="mt-7 space-y-4" onSubmit={handleSubmit}>
            <label className="block text-sm">
              Username
              <input
                required
                value={form.username}
                onChange={(e) => setForm((prev) => ({ ...prev, username: e.target.value }))}
                className="mt-1 w-full rounded-xl border border-white/10 bg-white/5 px-4 py-2.5 outline-none transition focus:border-emerald-300/60"
                placeholder="farmer_raj"
              />
            </label>
            <label className="block text-sm">
              Password
              <input
                required
                type="password"
                value={form.password}
                onChange={(e) => setForm((prev) => ({ ...prev, password: e.target.value }))}
                className="mt-1 w-full rounded-xl border border-white/10 bg-white/5 px-4 py-2.5 outline-none transition focus:border-emerald-300/60"
                placeholder="••••••••"
              />
            </label>
            <button
              type="submit"
              disabled={loading}
              className="w-full rounded-xl bg-gradient-to-r from-emerald-400 to-cyan-300 px-4 py-2.5 font-semibold text-slate-900 transition hover:brightness-110 disabled:opacity-60"
            >
              {loading ? "Signing in..." : "Sign In"}
            </button>
          </form>

          <p className="mt-5 text-sm text-slate-300">
            New to KhetiMitra?{" "}
            <Link to="/register" className="font-medium text-emerald-200 hover:text-white">
              Register now
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
