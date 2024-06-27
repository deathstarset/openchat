<script lang="ts">
  import { conversationStore } from "../../../store";
  import AddMessage from "../messages/AddMessage.svelte";
  import BotMessage from "../messages/BotMessage.svelte";
  import UserMessage from "../messages/UserMessage.svelte";
  import { loadConversation } from "../../../actions/conversations";
  import { afterUpdate } from "svelte";
  export let id: string;
  function scrollToBottom() {
    const container = document.getElementById("message-container");
    if (container) {
      container.scrollTop = container.scrollHeight;
    }
  }
  afterUpdate(scrollToBottom);
  enum Sender {
    user = "user",
    bot = "bot",
  }
  $: {
    loadConversation(id);
  }
</script>

<div class="bg-slate-100 h-[92vh] flex flex-col items-center">
  <div class="h-[85%] p-2 overflow-y-auto w-1/2" id="message-container">
    <div class="flex flex-col justify-between h-full">
      {#if $conversationStore.messages}
        <div>
          <p class="p-2">Conversation id : {id}</p>
          {#each $conversationStore.messages as message}
            {#if message.sender === Sender.user}
              <UserMessage {message} />
            {/if}
            {#if message.sender === Sender.bot}
              <BotMessage {message} />
            {/if}
          {/each}
          {#if $conversationStore.loading}
            <p>Loading....</p>
          {/if}
        </div>
      {/if}
    </div>
  </div>
  <AddMessage conversationId={id} />
</div>
