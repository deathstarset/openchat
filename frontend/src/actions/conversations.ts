import { conversationsStore } from "../store";
import { createConversation, getConversations } from "../api/conversations";
import { getMessagesByConvo } from "../api/messages";
import { conversationStore } from "../store";
import { navigate } from "svelte-routing";

export async function loadConversations() {
  conversationsStore.set({ data: null, loading: true, error: null });
  try {
    const conversations = await getConversations();
    conversationsStore.set({
      data: conversations,
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
    const messages = await getMessagesByConvo(convo_id);
    conversationStore.set({
      conversationId: convo_id,
      messages: messages,
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

export async function addConversation() {
  conversationsStore.update((current) => ({
    ...current,
    loading: true,
  }));
  try {
    const conversation = await createConversation();
    conversationsStore.update((current) => ({
      ...current,
      data: [...current.data, conversation],
      loading: false,
    }));
    navigate(`/conversations/${conversation.id}`);
  } catch (error) {
    conversationsStore.update((current) => ({
      ...current,
      data: null,
      loading: false,
      error: (error as Error).message,
    }));
  }
}
