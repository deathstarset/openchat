<script lang="ts">
  let count: number = 0;
  const increment = () => {
    count += 1;
  };
  const decrement = () => {
    count -= 1;
  };
</script>

<div>
  <button
    on:click={increment}
    class="px-3 py-2 bg-green-500 rounded-md text-white">+</button
  >
  <button
    on:click={decrement}
    class="px-3 py-2 bg-red-500 rounded-md text-white">-</button
  >
  <h1>Count {count}</h1>
</div>
