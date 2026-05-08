<script setup>
defineProps({
  steps: {
    type: Array,
    required: true
    // each: { icon, title, desc }
  }
})
</script>

<template>
  <div class="wf">
    <div v-for="(s, i) in steps" :key="i" class="wf-step">
      <div class="wf-icon">{{ s.icon }}</div>
      <div class="wf-title">{{ s.title }}</div>
      <div class="wf-desc">{{ s.desc }}</div>
    </div>
  </div>
</template>
