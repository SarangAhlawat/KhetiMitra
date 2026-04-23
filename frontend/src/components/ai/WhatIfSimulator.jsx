import { useState } from "react";
import { simulateWhatIf } from "../../services/api";

export default function WhatIfSimulator() {

  const [crop, setCrop] =
    useState("Rice");

  const [result, setResult] =
    useState(null);

  const handleSimulate = async () => {

    const response =
      await simulateWhatIf({
        crop
      });

    setResult(response.data);

  };

  return (

    <div className="bg-white p-4 rounded shadow">

      <h2 className="font-bold mb-2">

        What-If Simulator

      </h2>

      <select

        value={crop}

        onChange={(e) =>
          setCrop(e.target.value)
        }

        className="border p-2 rounded"

      >

        <option>Rice</option>
        <option>Wheat</option>
        <option>Maize</option>

      </select>

      <button

        onClick={handleSimulate}

        className="ml-2 bg-green-600 text-white px-3 py-2 rounded"

      >

        Simulate

      </button>

      {result && (

        <div className="mt-2">

          <p>
            Yield: {result.yield}
          </p>

          <p>
            Sustainability: {result.qssm}
          </p>

        </div>

      )}

    </div>

  );
}