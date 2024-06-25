import axios, { AxiosError } from "axios";
import { API_URL } from "../constants";
const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export async function getConversations(): Promise<Conversation[]> {
  try {
    const response = await apiClient.get("/api/v1/conversations");
    return response.data;
  } catch (error) {
    const axiosError = error as AxiosError;
    throw new Error(axiosError.message);
  }
}
