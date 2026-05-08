<script setup>
defineProps({
  value: { type: [String, Number], required: true },
  label: { type: String, required: true },
  color: { type: String, default: '' }
})
</script>

<template>
  <div class="card card-sm" style="text-align:center">
    <div class="stat-num" :style="color ? { color } : {}">{{ value }}</div>
    <div class="stat-lbl">{{ label }}</div>
  </div>
</template>
