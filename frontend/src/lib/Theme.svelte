<script lang="ts">
  let dark = false;
  function setDarkTheme() {
    dark = true;
  }
  function setWhiteTheme() {
    dark = false;
  }
</script>

<div class="bg-slate-200 p-1 rounded flex items-center gap-1 h-2/3">
  <button
    class={`cursor-pointer rounded p-2 grid place-items-center ${!dark && "bg-white"}`}
    on:click={setWhiteTheme}
  >
    <ion-icon name="sunny-outline"></ion-icon>
  </button>

  <button
    on:click={setDarkTheme}
    class={`cursor-pointer rounded p-2 grid place-items-center ${dark && "bg-white"}`}
  >
    <ion-icon name="moon-outline"></ion-icon>
  </button>
</div>
