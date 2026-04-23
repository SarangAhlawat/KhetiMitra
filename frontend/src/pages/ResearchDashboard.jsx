import MetricsCard
from "../components/research/MetricsCard";

import ModelComparisonChart
from "../components/research/ModelComparisonChart";

import FeatureImportanceChart
from "../components/research/FeatureImportanceChart";

import SHAPVisualizer
from "../components/research/SHAPVisualizer";

import PageWrapper
from "../components/ui/PageWrapper";

export default function ResearchDashboard() {

  return (
    <PageWrapper>

    <div className="p-6 bg-gray-100 min-h-screen">

      <h1 className="text-2xl font-bold mb-6">

        Research Dashboard

      </h1>

      {/* Metrics */}

      <div className="grid md:grid-cols-4 gap-4 mb-6">

        <MetricsCard
          title="Accuracy"
          value="91%"
        />

        <MetricsCard
          title="RMSE"
          value="548.39"
        />

        <MetricsCard
          title="F1 Score"
          value="0.89"
        />

        <MetricsCard
          title="Models Trained"
          value="4"
        />

      </div>

      {/* Charts */}

      <div className="grid md:grid-cols-2 gap-6">

        <ModelComparisonChart />

        <FeatureImportanceChart />

      </div>

      {/* SHAP */}

      <div className="mt-6">

        <SHAPVisualizer />

      </div>

    </div>
    </PageWrapper>

  );
}