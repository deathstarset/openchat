<script lang="ts">
  import { onMount } from "svelte";
  import { conversationsStore } from "../../../store";
  import { loadConversations } from "../../../actions/conversations";
  import Conversation from "./Conversation.svelte";
  onMount(async () => {
    await loadConversations();
  });
</script>

<div>
  <h2 class="font-medium mb-3">Conversations</h2>
  {#if $conversationsStore.loading}
    <p>Loading....</p>
  {/if}
  {#if $conversationsStore.data}
    <div class="flex flex-col gap-2">
      {#each $conversationsStore.data as convo}
        <Conversation {convo} />
      {/each}
    </div>
  {/if}
</div>
