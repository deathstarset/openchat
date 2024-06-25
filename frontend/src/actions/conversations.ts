import { conversationsStore } from "../store";
import { getConversations } from "../api/conversations";

export async function loadConversations() {
  console.log("Hello world");
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
