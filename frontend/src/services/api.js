import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000"
});

export const addFarm = (data) =>
  API.post("/farm", data);

export const getRecommendation = (data) =>
  API.post("/recommendation", data);

export const getEnvironment = (lat, lon) =>
  API.get(`/environment?lat=${lat}&lon=${lon}`);

export const simulateWhatIf = (data) =>
  API.post("/simulate", data);

export const getEnvironmentData = (lat, lon) =>
  API.get(`/environment?lat=${lat}&lon=${lon}`);

export const chatAssistant = (message) =>
  API.post("/chat", {
    query: message
  });