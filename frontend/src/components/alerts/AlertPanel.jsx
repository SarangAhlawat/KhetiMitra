export default function AlertPanel() {

  const alerts = [

    {
      type: "High Risk",
      message: "Soil degradation detected"
    },

    {
      type: "Warning",
      message: "Water stress increasing"
    }

  ];

  return (

    <div className="bg-white rounded shadow p-4">

      <h2 className="font-bold mb-3">

        Alerts

      </h2>

      {alerts.map((a, i) => (

        <div

          key={i}

          className="mb-2 p-2 rounded bg-red-100"

        >

          <strong>{a.type}:</strong>

          {a.message}

        </div>

      ))}

    </div>

  );
}