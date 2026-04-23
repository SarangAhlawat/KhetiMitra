import { createContext, useContext, useEffect, useMemo, useState } from "react";

import { setAuthToken } from "../services/api";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [auth, setAuth] = useState(() => {
    const stored = localStorage.getItem("khetimitra_auth");
    return stored ? JSON.parse(stored) : {
      token: "",
      username: "",
      farmerId: null,
      hasFarmProfile: false
    };
  });

  useEffect(() => {
    localStorage.setItem("khetimitra_auth", JSON.stringify(auth));
    setAuthToken(auth.token);
  }, [auth]);

  const value = useMemo(() => ({
    auth,
    isAuthenticated: Boolean(auth.token),
    login: ({ token, username }) => setAuth((prev) => ({
      ...prev,
      token,
      username
    })),
    logout: () => setAuth({
      token: "",
      username: "",
      farmerId: null,
      hasFarmProfile: false
    }),
    setFarmerId: (farmerId) => setAuth((prev) => ({
      ...prev,
      farmerId
    })),
    setHasFarmProfile: (hasFarmProfile) => setAuth((prev) => ({
      ...prev,
      hasFarmProfile
    }))
  }), [auth]);

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);

  if (!ctx) {
    throw new Error("useAuth must be used inside AuthProvider");
  }

  return ctx;
}
