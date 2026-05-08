<script setup>
import { ref, computed, watch, nextTick } from 'vue'
import { findCatData, readAny } from '../composables/useFolderLoader.js'
import { CATS } from '../data/cats.js'
import Prism from 'prismjs'
import 'prismjs/components/prism-java'

const props = defineProps({
  catId: { type: String, required: true }
})

const cat = computed(() => CATS.find(c => c.id === props.catId))
const data = computed(() => cat.value ? findCatData(cat.value) : null)

// File tree state
const promptsOpen = ref(true)
const fuzzOpen = ref(true)
const logsOpen = ref(false)

// Active file viewer
const activeFileName = ref('')
const activeFileContent = ref('')
const activeFileIsCode = ref(false)
const activeFileLoading = ref(false)
const activeFileError = ref('')

// Manifest results mapped by index
const manifestResults = computed(() => {
  if (!data.value) return {}
  const map = {}
  data.value.manifest.forEach((m, i) => {
    map[i] = m.compile_result || 'UNKNOWN'
  })
  return map
})

// Stats from manifest
const stats = computed(() => {
  if (!data.value) return null
  const c = data.value.counts
  if (!Object.values(c).some(v => v > 0)) return null
  const safe = c.SAFE || 0, fail = c.FAILURE || 0, err = c.ERROR || 0, to = c.TIMED_OUT || 0
  const total = safe + fail + err + to || data.value.fuzzFiles.length
  const r = total > 0 ? (safe / total * 100).toFixed(1) : '0.0'
  const col = parseFloat(r) >= 50 ? 'var(--green)' : parseFloat(r) >= 30 ? 'var(--orange)' : 'var(--red)'
  return { total, safe, fail, err, to, r, col }
})

function escHtml (s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}

async function loadFile (handleOrFile, name) {
  activeFileName.value = name
  activeFileContent.value = ''
  activeFileError.value = ''
  activeFileLoading.value = true
  activeFileIsCode.value = name.endsWith('.fuzz')
  try {
    const txt = await readAny(handleOrFile)
    activeFileContent.value = txt
    if (name.endsWith('.fuzz')) {
      nextTick(() => Prism.highlightAll())
    }
  } catch (e) {
    activeFileError.value = e.message
  } finally {
    activeFileLoading.value = false
  }
}
</script>

<template>
  <!-- Has data: show file browser -->
  <div v-if="data" class="fb-wrap">
    <div class="fb-tree">
      <!-- prompts -->
      <div v-if="Object.keys(data.prompts).length > 0">
        <div class="tree-folder" :class="{ open: promptsOpen }" @click="promptsOpen = !promptsOpen">
          <span style="font-size:13px">📁 prompts</span>
        </div>
        <div class="tree-children" :class="{ open: promptsOpen }">
          <div
            v-for="(handle, name) in data.prompts"
            :key="name"
            class="tree-file"
            :class="{ active: activeFileName === name }"
            @click="loadFile(handle, name)"
          >
            <span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap">📄 {{ name }}</span>
          </div>
        </div>
      </div>

      <!-- .fuzz files -->
      <div v-if="data.fuzzFiles.length > 0">
        <div class="tree-folder" :class="{ open: fuzzOpen }" @click="fuzzOpen = !fuzzOpen">
          <span style="font-size:13px">📁 .fuzz 文件 ({{ data.fuzzFiles.length }})</span>
        </div>
        <div class="tree-children" :class="{ open: fuzzOpen }">
          <div
            v-for="(ff, i) in data.fuzzFiles"
            :key="ff.name"
            class="tree-file"
            :class="{ active: activeFileName === ff.name }"
            @click="loadFile(ff.handle || ff.file, ff.name)"
          >
            <div class="result-dot" :class="'rd-' + (manifestResults[i] || 'UNKNOWN')"></div>
            <span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{{ ff.name }}</span>
          </div>
        </div>
      </div>

      <!-- log files -->
      <div v-if="Object.keys(data.logFiles).length > 0">
        <div class="tree-folder" :class="{ open: logsOpen }" @click="logsOpen = !logsOpen">
          <span style="font-size:13px">📁 日志文件</span>
        </div>
        <div class="tree-children" :class="{ open: logsOpen }">
          <div
            v-for="(handle, name) in data.logFiles"
            :key="name"
            class="tree-file"
            :class="{ active: activeFileName === name }"
            @click="loadFile(handle, name)"
          >
            <span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap">📋 {{ name }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="fb-view">
      <div class="fb-view-header">
        <span style="font-size:16px">📄</span>
        <span :style="{ color: activeFileName ? 'var(--text)' : 'var(--muted)' }">
          {{ activeFileName || '点击左侧文件查看内容' }}
        </span>
      </div>
      <div class="fb-view-content">
        <div v-if="activeFileLoading" style="padding:24px;text-align:center;color:var(--muted)">加载中…</div>
        <div v-else-if="activeFileError" style="padding:24px;color:var(--red);font-size:13px">读取失败: {{ activeFileError }}</div>
        <div v-else-if="!activeFileName" style="padding:32px;text-align:center;color:var(--muted);font-size:13px">选择左侧文件</div>
        <div v-else-if="activeFileIsCode">
          <pre style="margin:0;border:none;border-radius:0;max-height:none;height:100%;min-height:400px"><code class="language-java">{{ activeFileContent }}</code></pre>
        </div>
        <div v-else>
          <pre style="margin:0;padding:16px;font-family:monospace;font-size:12.5px;line-height:1.6;white-space:pre-wrap;word-break:break-word;color:var(--text);min-height:400px">{{ activeFileContent }}</pre>
        </div>
      </div>
    </div>
  </div>

  <!-- No data: empty state -->
  <div v-else class="empty-state">
    <div class="empty-icon">📂</div>
    <div class="empty-title">尚未加载文件夹</div>
    <div class="empty-desc">请点击左侧"选择输出文件夹"按钮，<br>加载 outputs 目录后即可浏览文件</div>
  </div>
</template>
