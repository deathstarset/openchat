<script lang="ts">
  import { createBotMessage, createMessage } from "../../../actions/messages";
  let userMessage: string = "";
  export let conversationId: string;
  enum Sender {
    user = "user",
    bot = "bot",
  }
</script>

<div class="flex w-1/2 gap-2 mt-5">
  <input
    type="text"
    placeholder="Prompt"
    class="px-2 w-full py-3 rounded border"
    bind:value={userMessage}
  />
  <button
    class=" hover:bg-black/85 transition-colors text-white bg-black rounded p-3 grid place-items-center w-16"
    on:click={async () => {
      await createMessage({
        conversationId: conversationId,
        content: userMessage,
        sender: Sender.user,
      });
      await createBotMessage({
        conversationId: conversationId,
        content: userMessage,
        sender: Sender.bot,
      });
    }}
  >
    <ion-icon name="send-outline"></ion-icon></button
  >
</div>
