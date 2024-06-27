<script lang="ts">
  export let message: Message;
</script>

<div class="p-2 bg-white border rounded flex flex-col gap-1">
  <h3 class="font-medium">Bot</h3>
  <p>{message.content}</p>
</div>
