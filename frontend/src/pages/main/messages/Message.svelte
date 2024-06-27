<script lang="ts">
  import BotMessage from "./BotMessage.svelte";
  import UserMessage from "./UserMessage.svelte";
  export let message: Message;
  enum Sender {
    user = "user",
    bot = "bot",
  }
</script>

{#if message.sender === Sender.user}
  <UserMessage {message} />
{/if}
{#if message.sender === Sender.bot}
  <BotMessage {message} />
{/if}
