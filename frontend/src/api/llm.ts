import axios, { AxiosError } from "axios";
import { API_URL } from "../constants";

export async function* getLlmResponse(userMessage: string) {
  const response = await fetch(`${API_URL}/api/v1/generate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: userMessage }),
  });
  if (!response.ok) {
    throw new Error(`HTTP error status : ${response.status}`);
  }
  const reader = response.body?.getReader();
  const decoder = new TextDecoder("utf-8");
  let buffer = "";

  try {
    while (true && reader) {
      const { done, value } = await reader.read();
      if (done) {
        break;
      }

      buffer += decoder.decode(value, { stream: true });

      let boundary = buffer.indexOf("\n");

      while (boundary !== -1) {
        const jsonChunk = buffer.slice(0, boundary).trim();
        buffer = buffer.slice(boundary + 1);

        if (jsonChunk) {
          try {
            yield JSON.parse(jsonChunk);
          } catch (err) {
            throw new Error(
              "Failed to parse JSON chunk: " + (err as Error).message
            );
          }
        }

        boundary = buffer.indexOf("\n");
      }
    }

    // Handle any remaining buffered data
    if (buffer.trim()) {
      try {
        yield JSON.parse(buffer);
      } catch (err) {
        throw new Error(
          "Failed to parse JSON chunk: " + (err as Error).message
        );
      }
    }
  } catch (error) {
    throw new Error("Stream error: " + (error as Error).message);
  } finally {
    reader?.releaseLock();
  }
}
/* async function getResponse(e: Event) {
  const user_message = message;
  message = "";
  messages.push({ type: "prompt", content: user_message });
  messages = messages;
  loading = true;
  let response_added = false;
  try {
    while (true && reader) {
      const { done, value } = await reader.read();
      if (done) break;
      const chunk: AiResponse = JSON.parse(decoder.decode(value));
      if (!response_added) {
        messages.push({ type: "response", content: chunk.response });
        messages = messages;
        loading = false;
        response_added = true;
      } else {
        messages[messages.length - 1].content += chunk.response;
        messages = messages;
      }
    }
  } catch (error) {}
  console.log(messages);
} */
