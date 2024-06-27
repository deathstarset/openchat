import { getLlmResponse } from "../api/llm";
import { addMessage } from "../api/messages";
import { conversationStore } from "../store";

export async function createMessage(messageInfo: AddMessage) {
  conversationStore.update((current) => ({ ...current, loading: true }));
  try {
    const message = await addMessage(messageInfo);
    conversationStore.update((current) => ({
      ...current,
      messages: [...current.messages, message],
      loading: false,
    }));
  } catch (error) {
    conversationStore.update((current) => ({
      ...current,
      loading: false,
      error: (error as Error).message,
    }));
  }
}

export async function createBotMessage(messageInfo: AddMessage) {
  let botResponseAdded = false;
  let messageId: string = "";
  conversationStore.update((current) => ({
    ...current,
    loading: true,
  }));
  const responseStream = getLlmResponse(messageInfo.content);
  try {
    for await (const chunk of responseStream) {
      const aiResponse: AiResponse = chunk;
      if (!botResponseAdded) {
        const botMessage = await addMessage({
          conversationId: messageInfo.conversationId,
          content: aiResponse.response,
          sender: messageInfo.sender,
        });
        console.log(botMessage);
        conversationStore.update((current) => ({
          ...current,
          loading: false,
          error: null,
          messages: [
            ...current.messages,
            {
              id: botMessage.id,
              conversationId: messageInfo.conversationId,
              content: botMessage.content,
            },
          ],
        }));
        botResponseAdded = true;
        messageId = botMessage.id;
      } else {
        console.log(messageId);
        conversationStore.update((current) => ({
          ...current,
          loading: false,
          error: null,
          messages: current.messages?.map((message) => {
            if (message.id === messageId) {
              return {
                ...message,
                content: message.content + aiResponse.response,
              };
            }
            return message;
          }),
        }));
      }
    }
  } catch (error) {
    console.error("Stream error:", error);
  }
}
