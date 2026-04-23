import { useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";
import { createFarmProfile } from "../services/api";
import { useAuth } from "../context/AuthContext";

const initialFarm = {
  farmer_id: "",
  soil_type: "Loamy",
  soil_ph: 7,
  organic_carbon: 0.7,
  farm_size: 1.5,
  irrigation_type: "Drip",
  water_source: "Canal",
  gps_lat: 30.7333,
  gps_lon: 76.7794
};

export default function OnboardingPage() {
  const navigate = useNavigate();
  const { auth, setHasFarmProfile } = useAuth();

  const [farm, setFarm] = useState({
    ...initialFarm,
    farmer_id: auth.farmerId || ""
  });
  const [saving, setSaving] = useState(false);

  const updateField = (field, value) => setFarm((prev) => ({ ...prev, [field]: value }));

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!farm.farmer_id) {
      toast.error("Farmer ID is required");
      return;
    }

    setSaving(true);

    try {
      await createFarmProfile({
        ...farm,
        farmer_id: Number(farm.farmer_id),
        soil_ph: Number(farm.soil_ph),
        organic_carbon: Number(farm.organic_carbon),
        farm_size: Number(farm.farm_size),
        gps_lat: Number(farm.gps_lat),
        gps_lon: Number(farm.gps_lon)
      });

      setHasFarmProfile(true);
      toast.success("Farm profile saved");
      navigate("/home");
    } catch (error) {
      toast.error(error?.response?.data?.detail || "Could not save farm profile");
    } finally {
      setSaving(false);
    }
  };

  return (
    <KhetiShell
      title="Farm Onboarding"
      subtitle="Set your baseline farm profile once. KhetiMitra uses this for all recommendations."
    >
      <GlassCard title="Farm Details">
        <form onSubmit={handleSubmit} className="grid gap-4 md:grid-cols-2">
          <label className="text-sm">Farmer ID
            <input className="form-input mt-1" value={farm.farmer_id} onChange={(e) => updateField("farmer_id", e.target.value)} required />
          </label>
          <label className="text-sm">Soil Type
            <input className="form-input mt-1" value={farm.soil_type} onChange={(e) => updateField("soil_type", e.target.value)} required />
          </label>
          <label className="text-sm">Soil pH
            <input className="form-input mt-1" type="number" step="0.1" value={farm.soil_ph} onChange={(e) => updateField("soil_ph", e.target.value)} required />
          </label>
          <label className="text-sm">Organic Carbon
            <input className="form-input mt-1" type="number" step="0.1" value={farm.organic_carbon} onChange={(e) => updateField("organic_carbon", e.target.value)} required />
          </label>
          <label className="text-sm">Farm Size (ha)
            <input className="form-input mt-1" type="number" step="0.1" value={farm.farm_size} onChange={(e) => updateField("farm_size", e.target.value)} required />
          </label>
          <label className="text-sm">Irrigation Type
            <input className="form-input mt-1" value={farm.irrigation_type} onChange={(e) => updateField("irrigation_type", e.target.value)} required />
          </label>
          <label className="text-sm">Water Source
            <input className="form-input mt-1" value={farm.water_source} onChange={(e) => updateField("water_source", e.target.value)} required />
          </label>
          <label className="text-sm">Latitude
            <input className="form-input mt-1" type="number" step="0.0001" value={farm.gps_lat} onChange={(e) => updateField("gps_lat", e.target.value)} required />
          </label>
          <label className="text-sm">Longitude
            <input className="form-input mt-1" type="number" step="0.0001" value={farm.gps_lon} onChange={(e) => updateField("gps_lon", e.target.value)} required />
          </label>
          <button
            type="submit"
            disabled={saving}
            className="md:col-span-2 rounded-xl bg-gradient-to-r from-emerald-400 to-cyan-300 px-4 py-2.5 font-semibold text-slate-900 transition hover:brightness-110 disabled:opacity-60"
          >
            {saving ? "Saving..." : "Finish Onboarding"}
          </button>
        </form>
      </GlassCard>
    </KhetiShell>
  );
}
