import axios, { AxiosError } from "axios";
import { API_URL } from "../constants";

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export async function getMessagesByConvo(convoId: string): Promise<Message[]> {
  try {
    const response = await apiClient.get(
      `/api/v1/messages?convo_id=${convoId}`
    );
    return response.data.messages;
  } catch (error) {
    throw new Error((error as AxiosError).message);
  }
}

export async function addMessage(messageInfo: AddMessage): Promise<Message> {
  try {
    const response = await apiClient.post("/api/v1/messages", {
      conversation_id: messageInfo.conversationId,
      sender: messageInfo.sender,
      content: messageInfo.content,
    });
    return response.data.message;
  } catch (error) {
    throw new Error((error as AxiosError).message);
  }
}

export async function editMessage(
  id: string,
  message_info: AddMessage
): Promise<Message> {
  try {
    const response = await apiClient.put(`api/v1/messages/${id}`, {
      conversation_id: message_info.conversationId,
      content: message_info.content,
      sender: message_info.sender,
    });
    return response.data.message;
  } catch (error) {
    throw new Error((error as Error).message);
  }
}
