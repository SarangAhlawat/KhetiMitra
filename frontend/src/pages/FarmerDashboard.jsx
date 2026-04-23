import { useEffect, useState } from "react";

import Navbar from "../components/layout/Navbar";

import WeatherCard from "../components/environment/WeatherCard";

import GaugeChart from "../components/charts/GaugeChart";

import DecisionTimeline from "../components/ai/DecisionTimeline";

import WhatIfSimulator from "../components/ai/WhatIfSimulator";

import { getEnvironment } from "../services/api";


import PageWrapper
from "../components/ui/PageWrapper";

export default function FarmerDashboard() {

  const [env, setEnv] =
    useState(null);

  useEffect(() => {

    async function loadData() {

      const res =
        await getEnvironment(30, 76);

      setEnv(res.data);

    }

    loadData();

  }, []);

  return (

    <PageWrapper>
    <div className="bg-gray-100 min-h-screen">

      <Navbar />

      <div className="p-6 grid gap-6">

        <div className="grid md:grid-cols-3 gap-4">

          {env && (

            <WeatherCard data={env} />

          )}

          <GaugeChart value={75} />

        </div>

        <DecisionTimeline />

        <WhatIfSimulator />

      </div>

    </div>
    </PageWrapper>

  );
}