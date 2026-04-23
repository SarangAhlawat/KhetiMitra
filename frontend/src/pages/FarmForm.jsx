import { useState } from "react";
import toast from "react-hot-toast";

import KhetiShell from "../components/layout/KhetiShell";
import GlassCard from "../components/ui/GlassCard";
import { createFarmProfile } from "../services/api";

const initialData = {
	farmer_id: 1,
	farm_name: "Main Field",
	soil_type: "Loamy",
	farm_size_acres: 3,
	irrigation_type: "Drip",
	water_source: "Canal",
	gps_lat: 30.7333,
	gps_lon: 76.7794
};

export default function FarmForm() {
	const [data, setData] = useState(initialData);
	const [saving, setSaving] = useState(false);

	const update = (field, value) => setData((prev) => ({ ...prev, [field]: value }));

	const submit = async (e) => {
		e.preventDefault();
		setSaving(true);
		try {
			await createFarmProfile({
				...data,
				farmer_id: Number(data.farmer_id),
				farm_size_acres: Number(data.farm_size_acres),
				gps_lat: Number(data.gps_lat),
				gps_lon: Number(data.gps_lon)
			});
			toast.success("Farm profile submitted");
		} catch (error) {
			toast.error(error?.response?.data?.detail || "Unable to submit farm profile");
		} finally {
			setSaving(false);
		}
	};

	return (
		<KhetiShell title="Farm Form" subtitle="Quick entry form for farm details.">
			<GlassCard title="Farm Information">
				<form className="grid gap-4 sm:grid-cols-2" onSubmit={submit}>
					{Object.entries(data).map(([key, value]) => (
						<label key={key} className="text-sm capitalize">
							{key.replaceAll("_", " ")}
							<input
								className="form-input mt-1"
								value={value}
								onChange={(e) => update(key, e.target.value)}
							/>
						</label>
					))}
					<button type="submit" disabled={saving} className="btn-primary sm:col-span-2">
						{saving ? "Saving..." : "Save Farm"}
					</button>
				</form>
			</GlassCard>
		</KhetiShell>
	);
}
