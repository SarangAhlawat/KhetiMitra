import { createContext, useContext, useMemo, useState } from "react";

const AppContext = createContext(null);

export function AppProvider({ children }) {
	const [selectedDistrict, setSelectedDistrict] = useState("Patiala");
	const [globalLoading, setGlobalLoading] = useState(false);

	const value = useMemo(() => ({
		selectedDistrict,
		setSelectedDistrict,
		globalLoading,
		setGlobalLoading
	}), [selectedDistrict, globalLoading]);

	return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}

export function useAppContext() {
	const ctx = useContext(AppContext);
	if (!ctx) {
		throw new Error("useAppContext must be used within AppProvider");
	}
	return ctx;
}
