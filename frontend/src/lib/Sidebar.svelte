<script lang="ts"></script>

<div class="h-screen min-w-72 border-r">
  <div class="px-2 py-3 border-b">
    <img src="/logo.png" alt="" class="h-10 w-10" />
  </div>
  <div class="p-2 flex flex-col gap-3">
    <button
      class="flex items-center gap-2 bg-black p-3 text-white rounded-md w-full font-medium hover:opacity-80"
    >
      <ion-icon name="add-outline"></ion-icon> <span>New chat</span></button
    >
    <div class="relative w-full rounded-md font-medium">
      <ion-icon
        name="search-outline"
        class="absolute top-1/2 translate-y-[-50%] left-3"
      ></ion-icon>
      <input
        type="text"
        placeholder="Search"
        class="w-full p-3 px-9 rounded-md border"
      />
    </div>
  </div>
</div>
