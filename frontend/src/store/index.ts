import { writable } from "svelte/store";

interface ConversationState {
  data: Conversation[] | null;
  loading: boolean;
  error: null | string;
}
export const conversationsStore = writable<ConversationState>({
  data: null,
  loading: false,
  error: null,
});
