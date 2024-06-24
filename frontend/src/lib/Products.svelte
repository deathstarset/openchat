<script lang="ts">
  import { onMount } from "svelte";

  let products = [];
  let error = "";
  let loading = false;

  async function getProducts() {
    loading = true;
    try {
      const response = await fetch("https://fakestoreapi.com/products");
      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }
      products = await response.json();
    } catch (err) {
      if (err instanceof Error) error = err.message;
      error = "An Error Occured";
    } finally {
      loading = false;
    }
  }
  onMount(() => {
    getProducts();
  });
</script>

<div>
  <h1 class="text-2xl font-bold my-4 text-center">Products List</h1>
  {#if error}
    <p>An error has occured : {error}</p>
  {/if}
  {#if loading}
    <p>Loading...</p>
  {/if}
  <ul class="flex flex-col gap-2">
    {#each products as product}
      <li>{product.title}</li>
    {/each}
  </ul>
</div>
