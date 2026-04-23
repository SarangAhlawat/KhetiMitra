import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000"
});

export const setAuthToken = (token) => {
  if (token) {
    API.defaults.headers.common.Authorization = `Bearer ${token}`;
    return;
  }

  delete API.defaults.headers.common.Authorization;
};

export const registerUser = (payload) => API.post("/register", payload);

export const loginUser = (payload) => API.post("/login", payload);

export const createFarmerProfile = (payload) => API.post("/farmer", payload);

export const createFarmProfile = (payload) => API.post("/farm", payload);

export const getEnvironment = (lat, lon) => API.get("/environment", {
  params: { lat, lon }
});

export const getRecommendation = (payload) => API.post("/recommendation", payload);

export const getRecommendationExplain = (payload) => API.post("/recommendation/explain", payload);

export const askAssistant = (payload) => API.post("/voice", payload);

export const createHistory = (payload) => API.post("/history", payload);

export const getHistoryByFarm = (farmId) => API.get(`/history/${farmId}`);

export const searchKnowledge = (domain, query) => API.get(`/knowledge/search/${domain}`, {
  params: { query }
});

export const getBackendStatus = () => API.get("/");

export default API;