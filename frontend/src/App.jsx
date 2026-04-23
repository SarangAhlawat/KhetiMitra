import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import FarmerDashboard
  from "./pages/FarmerDashboard";

import ResearchDashboard from "./pages/ResearchDashboard";

import OfficerDashboard from "./pages/OfficerDashboard";

import EnvironmentDashboard from "./pages/EnvironmentDashboard";

import ChatPage from "./pages/ChatPage";

import { AnimatePresence }
from "framer-motion";

function App() {

  return (

    <BrowserRouter>

        <AnimatePresence mode="wait">

      <Routes>

        <Route
          path="/"
          element={<FarmerDashboard />}
        />

        <Route
            path="/officer"
            element={<OfficerDashboard />}
        />

        <Route
            path="/research"
            element={<ResearchDashboard />}
        />

        <Route
            path="/environment"
            element={<EnvironmentDashboard />}
        />

        <Route
            path="/chat"
            element={<ChatPage />}
        />

      </Routes>

      </AnimatePresence>

    </BrowserRouter>

  );

}

export default App;