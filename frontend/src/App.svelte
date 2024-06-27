<script lang="ts">
  import Sidebar from "./pages/main/Sidebar.svelte";
  import Nav from "./pages/main/Nav.svelte";
  import Chat from "./pages/main/conversations/Chat.svelte";
  import { Router, Route } from "svelte-routing";
</script>

<Router>
  <div class="flex h-screen">
    <Sidebar />
    <div class="w-full h-full">
      <Nav />
      <Route path="/conversations/:id" let:params>
        <Chat id={params.id} />
      </Route>
    </div>
  </div>
</Router>
