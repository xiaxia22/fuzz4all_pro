<script setup>
defineProps({
  cls: { type: String, default: '' },
  text: { type: String, required: true }
})
</script>

<template>
  <span class="badge" :class="cls">{{ text }}</span>
</template>
