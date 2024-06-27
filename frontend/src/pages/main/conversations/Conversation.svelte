<script lang="ts">
  import { loadConversation } from "../../../actions/conversations";
  import { Link, Router } from "svelte-routing";
  export let convo: Conversation;
</script>

<Router>
  <Link
    to={`/conversations/${convo.id}`}
    class="border rounded py-2 px-1 cursor-pointer hover:bg-slate-100 transition-colors"
  >
    {convo.id.slice(0, 25)}...
  </Link>
</Router>
