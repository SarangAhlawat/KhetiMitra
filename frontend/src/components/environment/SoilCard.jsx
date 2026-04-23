import Card from "../ui/Card";
import { Leaf } from "lucide-react";

export default function SoilCard({ data }) {

  return (

    <Card>

      <div className="flex items-center gap-2 mb-2">

        <Leaf className="text-green-600" />

        <h2 className="font-bold">
          Soil Status
        </h2>

      </div>

      <p>
        pH Level: {data.soil_ph}
      </p>

      <p>
        Organic Carbon:
        {data.organic_carbon}
      </p>

      <p>
        Nitrogen:
        {data.nitrogen}
      </p>

    </Card>

  );
}