<script lang="ts">
  import { loadConversation } from "../../../actions/conversations";
  export let convo: Conversation;
</script>

<button
  class="border rounded py-2 px-1 cursor-pointer hover:bg-slate-100 transition-colors"
  on:click={() => loadConversation(convo.id)}
>
  {convo.id.slice(0, 25)}...
</button>
