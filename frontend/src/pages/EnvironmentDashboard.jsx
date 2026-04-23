import { useEffect, useState } from "react";

import WeatherCard
from "../components/environment/WeatherCard";

import SoilCard
from "../components/environment/SoilCard";

import LocationCard
from "../components/environment/LocationCard";

import EnvironmentSummary
from "../components/environment/EnvironmentSummary";

import { getEnvironmentData }
from "../services/api";

import PageWrapper
from "../components/ui/PageWrapper";

import Skeleton 
from "../components/ui/Skeleton";

export default function EnvironmentDashboard() {

  const [env, setEnv] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  const loadEnvironment = async () => {

    try {

      const res =
        await getEnvironmentData(30.7333, 76.7794);

      setEnv(res.data);

      setLoading(false);

    }

    catch (error) {

      console.error(error);

      setLoading(false);

    }

  };

  useEffect(() => {

    loadEnvironment();

    const interval =
      setInterval(loadEnvironment, 60000);

    return () =>
      clearInterval(interval);

  }, []);

  if (loading) {

  return (

    <div className="p-6 space-y-3">

      <Skeleton height="h-8" />

      <Skeleton height="h-32" />

      <Skeleton height="h-32" />

    </div>

  );

}

  return (
    <PageWrapper>

    <div className="p-6 bg-gray-100 min-h-screen">

      <h1 className="text-2xl font-bold mb-6">

        Real-Time Environment Dashboard

      </h1>

      <p className="text-sm text-gray-500 mt-2"> Auto-refreshing every 60 seconds </p>

      <EnvironmentSummary data={env} />

      <div className="grid md:grid-cols-3 gap-4 mt-4">

        <WeatherCard data={env} />

        <SoilCard data={env} />

        <LocationCard data={env} />

      </div>

    </div>
    </PageWrapper>

  );
}