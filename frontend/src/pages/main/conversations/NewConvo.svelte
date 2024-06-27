<script lang="ts">
  import { addConversation } from "../../../actions/conversations";
</script>

<button
  class="flex items-center gap-2 bg-black p-3 text-white rounded-md w-full font-medium hover:opacity-80 dark:bg-white dark:text-black"
  on:click={async () => {
    addConversation();
  }}
>
  <ion-icon name="add-outline"></ion-icon> <span>New chat</span></button
>
