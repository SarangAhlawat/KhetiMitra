import OfficerSidebar
  from "../components/layout/OfficerSidebar";

import RiskMap
  from "../components/maps/RiskMap";

import YieldTrendChart
  from "../components/charts/YieldTrendChart";

import WaterTrendChart
  from "../components/charts/WaterTrendChart";

import AlertPanel
  from "../components/alerts/AlertPanel";

import PageWrapper
from "../components/ui/PageWrapper";

export default function OfficerDashboard() {

  return (
    <PageWrapper>

    <div className="flex">

      <OfficerSidebar />

      <div className="flex-1 p-6 bg-gray-100">

        <h1 className="text-2xl font-bold mb-4">

          District Dashboard

        </h1>

        <div className="grid gap-6">

          <RiskMap />

          <div className="grid md:grid-cols-2 gap-4">

            <YieldTrendChart />

            <WaterTrendChart />

          </div>

          <AlertPanel />

        </div>

      </div>

    </div>
    </PageWrapper>

  );
}