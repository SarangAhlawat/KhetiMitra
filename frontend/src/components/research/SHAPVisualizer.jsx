import Card from "../ui/Card";

export default function SHAPVisualizer() {

  const shapData = [

    {
      feature: "Soil pH",
      impact: "High"
    },

    {
      feature: "Rainfall",
      impact: "Medium"
    },

    {
      feature: "Nitrogen",
      impact: "High"
    }

  ];

  return (

    <Card>

      <h2 className="font-bold mb-3">

        SHAP Explanation

      </h2>

      {shapData.map((item, i) => (

        <div

          key={i}

          className="flex justify-between mb-2 p-2 bg-green-50 rounded"

        >

          <span>

            {item.feature}

          </span>

          <span className="font-bold">

            {item.impact}

          </span>

        </div>

      ))}

    </Card>

  );
}