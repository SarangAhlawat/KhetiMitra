import Card from "../ui/Card";
import { MapPin } from "lucide-react";

export default function LocationCard({ data }) {

  return (

    <Card>

      <div className="flex items-center gap-2 mb-2">

        <MapPin className="text-red-500" />

        <h2 className="font-bold">
          Location
        </h2>

      </div>

      <p>
        District: {data.district}
      </p>

      <p>
        State: {data.state}
      </p>

      <p>
        Country: {data.country}
      </p>

    </Card>

  );
}