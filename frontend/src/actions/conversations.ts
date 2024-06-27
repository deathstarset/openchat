import { conversationsStore } from "../store";
import { getConversations } from "../api/conversations";
import { getMessagesByConvo } from "../api/messages";
import { conversationStore } from "../store";

export async function loadConversations() {
  conversationsStore.set({ data: null, loading: true, error: null });
  try {
    const data = await getConversations();
    conversationsStore.set({
      data: data.conversations,
      loading: false,
      error: null,
    });
  } catch (error) {
    conversationsStore.set({
      data: null,
      loading: false,
      error: (error as Error).message,
    });
  }
}

export async function loadConversation(convo_id: string) {
  conversationStore.set({
    conversationId: convo_id,
    messages: null,
    loading: true,
    error: null,
  });
  try {
    const data = await getMessagesByConvo(convo_id);
    conversationStore.set({
      conversationId: convo_id,
      messages: data.messages,
      loading: false,
      error: null,
    });
  } catch (error) {
    conversationStore.set({
      conversationId: convo_id,
      messages: null,
      loading: false,
      error: (error as Error).message,
    });
  }
}
