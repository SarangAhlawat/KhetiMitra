import Card from "../ui/Card";
import { CloudRain } from "lucide-react";

export default function WeatherCard({ data }) {

  return (

    <Card>

      <div className="flex items-center gap-2 mb-2">

        <CloudRain className="text-blue-500" />

        <h2 className="font-bold">
          Weather Status
        </h2>

      </div>

      <p>
        🌡 Temperature: {data.temperature}°C
      </p>

      <p>
        🌧 Rainfall: {data.rainfall} mm
      </p>

      <p>
        💧 Humidity: {data.humidity}%
      </p>

    </Card>

  );
}









// import Card from "../ui/Card";

// export default function WeatherCard({ data }) {

//   return (

//     <Card>

//       <h2 className="font-bold mb-2">

//         Weather

//       </h2>

//       <p>
//         Temperature: {data.temperature}°C
//       </p>

//       <p>
//         Rainfall: {data.rainfall} mm
//       </p>

//       <p>
//         Humidity: {data.humidity}%
//       </p>

//     </Card>

//   );
// }