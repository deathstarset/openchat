<script lang="ts">
  import Conversations from "./conversations/Conversations.svelte";
  import NewConvo from "./conversations/NewConvo.svelte";
  import SearchConvos from "./conversations/SearchConvos.svelte";
</script>

<div class="h-screen min-w-72 border-r dark:bg-black">
  <div class="px-2 py-4 border-b">
    <h1 class="text-2xl font-bold">OpenChat</h1>
  </div>
  <div class="p-2 flex flex-col gap-3">
    <NewConvo />
    <SearchConvos />
    <Conversations />
  </div>
</div>
