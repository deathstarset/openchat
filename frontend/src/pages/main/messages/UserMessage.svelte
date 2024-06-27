<script lang="ts">
  export let message: Message;
</script>

<div class="p-2 flex flex-col gap-1">
  <h3 class="font-medium">You</h3>
  <p>{message.content}</p>
</div>
