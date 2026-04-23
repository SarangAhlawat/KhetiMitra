import { Navigate, useLocation } from "react-router-dom";

import { useAuth } from "../context/AuthContext";

export default function ProtectedRoute({ children, needsFarmProfile = false }) {
  const { isAuthenticated, auth } = useAuth();
  const location = useLocation();

  if (!isAuthenticated) {
    return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  }

  if (needsFarmProfile && !auth.hasFarmProfile) {
    return <Navigate to="/onboarding" replace />;
  }

  return children;
}
