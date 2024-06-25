<script lang="ts">
  import Conversations from "./conversations/Conversations.svelte";
  import NewConvo from "./conversations/NewConvo.svelte";
  import SearchConvos from "./conversations/SearchConvos.svelte";
</script>

<div class="h-screen min-w-72 border-r">
  <div class="px-2 py-3 border-b">
    <img src="/logo.png" alt="" class="h-10 w-10" />
  </div>
  <div class="p-2 flex flex-col gap-3">
    <NewConvo />
    <SearchConvos />
    <Conversations />
  </div>
</div>
