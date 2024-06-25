<script lang="ts">
  export let convo: Conversation;
</script>

<div
  class="border rounded py-2 px-1 cursor-pointer hover:bg-slate-100 transition-colors"
>
  {convo.id.slice(0, 25)}...
</div>
