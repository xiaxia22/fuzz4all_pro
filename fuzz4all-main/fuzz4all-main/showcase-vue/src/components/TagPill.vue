<script setup>
import { tagColor, tagBg } from '../data/cats.js'

defineProps({
  tag: { type: String, required: true }
})
</script>

<template>
  <span class="tag-pill" :style="{ background: tagBg(tag), color: tagColor(tag) }">{{ tag }}</span>
</template>
