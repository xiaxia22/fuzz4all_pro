<script setup>
import { onMounted, nextTick, ref, watch } from 'vue'
import Prism from 'prismjs'
import 'prismjs/components/prism-java'
import 'prismjs/themes/prism.min.css'

const props = defineProps({
  title: { type: String, default: '' },
  badgeCls: { type: String, default: '' },
  badgeText: { type: String, default: '' },
  code: { type: String, required: true },
  language: { type: String, default: 'java' }
})

const codeRef = ref(null)

function highlight () {
  nextTick(() => {
    if (codeRef.value) Prism.highlightElement(codeRef.value)
  })
}

onMounted(highlight)
watch(() => props.code, highlight)
</script>

<template>
  <div class="code-block">
    <div v-if="title" class="code-header">
      <span>
        <span v-if="badgeText" class="badge" :class="badgeCls">{{ badgeText }}</span>
        {{ title }}
      </span>
    </div>
    <pre><code ref="codeRef" :class="'language-' + language">{{ code }}</code></pre>
  </div>
</template>
