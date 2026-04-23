import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import { createFarmerProfile, loginUser, registerUser } from "../services/api";
import { useAuth } from "../context/AuthContext";

const initialState = {
  username: "",
  password: "",
  name: "",
  phone: "",
  district: "",
  village: "",
  language: "Punjabi"
};

export default function RegisterPage() {
  const navigate = useNavigate();
  const { login, setFarmerId } = useAuth();

  const [form, setForm] = useState(initialState);
  const [loading, setLoading] = useState(false);

  const updateField = (field, value) => {
    setForm((prev) => ({ ...prev, [field]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      await registerUser({
        username: form.username,
        password: form.password
      });

      const { data: loginData } = await loginUser({
        username: form.username,
        password: form.password
      });

      login({ token: loginData.access_token, username: form.username });

      const { data: farmerData } = await createFarmerProfile({
        name: form.name,
        phone: form.phone,
        district: form.district,
        village: form.village,
        language: form.language
      });

      setFarmerId(farmerData.farmer_id || farmerData.id || null);
      toast.success("Registration completed");
      navigate("/onboarding");
    } catch (error) {
      toast.error(error?.response?.data?.detail || "Could not complete registration");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-bg min-h-screen px-4 py-10 text-slate-100">
      <div className="mx-auto max-w-2xl">
        <div className="auth-card rounded-3xl p-7 md:p-8">
          <p className="text-xs uppercase tracking-[0.22em] text-emerald-200">KhetiMitra</p>
          <h1 className="mt-2 text-3xl font-semibold">Farmer Registration</h1>
          <p className="mt-1 text-sm text-slate-300">Create your account and farmer profile in one step.</p>

          <form className="mt-7 grid gap-4 md:grid-cols-2" onSubmit={handleSubmit}>
            <label className="block text-sm">
              Username
              <input required value={form.username} onChange={(e) => updateField("username", e.target.value)} className="form-input" />
            </label>
            <label className="block text-sm">
              Password
              <input required type="password" value={form.password} onChange={(e) => updateField("password", e.target.value)} className="form-input" />
            </label>
            <label className="block text-sm">
              Farmer Name
              <input required value={form.name} onChange={(e) => updateField("name", e.target.value)} className="form-input" />
            </label>
            <label className="block text-sm">
              Phone
              <input required value={form.phone} onChange={(e) => updateField("phone", e.target.value)} className="form-input" />
            </label>
            <label className="block text-sm">
              District
              <input required value={form.district} onChange={(e) => updateField("district", e.target.value)} className="form-input" />
            </label>
            <label className="block text-sm">
              Village
              <input required value={form.village} onChange={(e) => updateField("village", e.target.value)} className="form-input" />
            </label>
            <label className="block text-sm md:col-span-2">
              Preferred Language
              <select value={form.language} onChange={(e) => updateField("language", e.target.value)} className="form-input">
                <option>Punjabi</option>
                <option>Hindi</option>
                <option>English</option>
              </select>
            </label>
            <button
              type="submit"
              disabled={loading}
              className="md:col-span-2 rounded-xl bg-gradient-to-r from-emerald-400 to-cyan-300 px-4 py-2.5 font-semibold text-slate-900 transition hover:brightness-110 disabled:opacity-60"
            >
              {loading ? "Creating account..." : "Create Account"}
            </button>
          </form>

          <p className="mt-5 text-sm text-slate-300">
            Already have an account?{" "}
            <Link to="/login" className="font-medium text-emerald-200 hover:text-white">
              Login
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
