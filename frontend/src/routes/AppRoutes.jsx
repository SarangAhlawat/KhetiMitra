import { Navigate, Route, Routes } from "react-router-dom";
import { AnimatePresence } from "framer-motion";

import { useAuth } from "../context/AuthContext";
import ProtectedRoute from "./ProtectedRoute";
import LoginPage from "../pages/LoginPage";
import RegisterPage from "../pages/RegisterPage";
import PublicLandingPage from "../pages/PublicLandingPage";
import OnboardingPage from "../pages/OnboardingPage";
import LandingPage from "../pages/LandingPage";
import AnalysisPage from "../pages/AnalysisPage";
import ChatPage from "../pages/ChatPage";
import VoicePage from "../pages/VoicePage";
import FarmForm from "../pages/FarmForm";
import Recommendations from "../pages/Recommendations";
import History from "../pages/History";
import OfficerDashboard from "../pages/OfficerDashboard";
import DistrictAnalytics from "../pages/DistrictAnalytics";
import ResearchDashboard from "../pages/ResearchDashboard";

export default function AppRoutes() {
	const { isAuthenticated } = useAuth();

	return (
		<AnimatePresence mode="wait">
			<Routes>
				<Route path="/login" element={<LoginPage />} />
				<Route path="/register" element={<RegisterPage />} />
				<Route
					path="/onboarding"
					element={(
						<ProtectedRoute>
							<OnboardingPage />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/home"
					element={(
						<ProtectedRoute needsFarmProfile>
							<LandingPage />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/analysis"
					element={(
						<ProtectedRoute needsFarmProfile>
							<AnalysisPage />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/chat"
					element={(
						<ProtectedRoute needsFarmProfile>
							<ChatPage />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/voice"
					element={(
						<ProtectedRoute needsFarmProfile>
							<VoicePage />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/farm-form"
					element={(
						<ProtectedRoute needsFarmProfile>
							<FarmForm />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/recommendations"
					element={(
						<ProtectedRoute needsFarmProfile>
							<Recommendations />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/history"
					element={(
						<ProtectedRoute needsFarmProfile>
							<History />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/officer"
					element={(
						<ProtectedRoute>
							<OfficerDashboard />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/district-analytics"
					element={(
						<ProtectedRoute>
							<DistrictAnalytics />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/research"
					element={(
						<ProtectedRoute>
							<ResearchDashboard />
						</ProtectedRoute>
					)}
				/>
				<Route
					path="/"
					element={<PublicLandingPage />}
				/>
				<Route path="*" element={<Navigate to="/" replace />} />
			</Routes>
		</AnimatePresence>
	);
}
