<script lang="ts">
  import { conversationStore } from "../../../store";
  import { addMessage } from "../../../api/messages";
  import { createMessage } from "../../../actions/messages";
  import AddMessage from "../messages/AddMessage.svelte";
  let userMessage = "";
  let conversationId: string | null = null;
  conversationStore.subscribe((value) => {
    conversationId = value.conversationId;
  });
  /* let message = "";
  let messages: ChatChunk[] = [];
  let loading = false;
  const URL = "http://127.0.0.1:8000";
  async function getResponse(e: Event) {
    const user_message = message;
    message = "";
    messages.push({ type: "prompt", content: user_message });
    messages = messages;
    loading = true;
    let response_added = false;
    try {
      const response = await fetch(`${URL}/api/v1/generate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: user_message }),
      });
      if (!response.ok) {
        throw new Error(`HTTP error status : ${response.status}`);
      }
      const reader = response.body?.getReader();
      const decoder = new TextDecoder("utf-8");
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
</script>

<div class="bg-slate-100 h-[92vh] flex flex-col items-center">
  <div class="h-[89%] p-2 overflow-y-auto w-1/2">
    <div>
      {#if $conversationStore.messages && conversationId}
        <p>{conversationId}</p>
        {#each $conversationStore.messages as message}
          <p>{message.content}</p>
        {/each}
        {#if $conversationStore.loading}
          <p>Loading....</p>
        {/if}
        <AddMessage {conversationId} />
      {/if}
    </div>
  </div>
</div>
