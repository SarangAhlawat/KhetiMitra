import { Sprout } from "lucide-react";

export default function Navbar() {
  return (
    <div className="bg-green-600 text-white px-6 py-4 flex justify-between items-center shadow">

      <div className="flex items-center gap-2">

        <Sprout size={28} />

        <h1 className="text-xl font-bold">
          KhetiMitra Farmer Dashboard
        </h1>

      </div>

    </div>
  );
}