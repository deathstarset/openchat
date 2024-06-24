<script lang="ts">
  let message = "";
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
  }
</script>

<div class="h-3/4 w-3/4 bg-slate-100 rounded-xl">
  <div class="h-[90%] p-2 overflow-y-auto rounded-xl">
    {#each messages as message}
      {#if message.type === "prompt"}
        <div class="py-2 px-4 my-2 bg-slate-200 rounded-3xl w-fit">
          {message.content}
        </div>
      {/if}
      {#if message.type === "response"}
        <div class="pl-4">{message.content}</div>
      {/if}
    {/each}
    {#if loading}
      <p>Loading....</p>
    {/if}
  </div>
  <div class="w-full bg-red-200 flex h-[10%] rounded-b-xl">
    <input
      type="text"
      placeholder="Prompt"
      bind:value={message}
      class="w-3/4 rounded-bl-xl bg-slate-100 px-2"
    />
    <button
      class="bg-black text-white font-medium rounded-br-xl hover:bg-black/85 transition-colors w-1/4"
      on:click={(e) => getResponse(e)}>Get Response</button
    >
  </div>
</div>
