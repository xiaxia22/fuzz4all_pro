<script setup>
import AppSidebar from './components/AppSidebar.vue'
</script>

<template>
  <div class="layout">
    <AppSidebar />
    <main class="main">
      <router-view />
    </main>
  </div>
</template>
