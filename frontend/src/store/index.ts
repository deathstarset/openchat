import { writable } from "svelte/store";

interface ConversationsState {
  data: Conversation[] | null;
  loading: boolean;
  error: null | string;
}
export const conversationsStore = writable<ConversationsState>({
  data: null,
  loading: false,
  error: null,
});

interface ConversationState {
  conversationId: string | null;
  messages: Message[] | null;
  loading: boolean;
  error: null | string;
}

export const conversationStore = writable<ConversationState>({
  conversationId: null,
  messages: null,
  loading: false,
  error: null,
});
