<script setup>
import { computed } from 'vue'
import { CATS } from '../data/cats.js'
import { findCatData } from '../composables/useFolderLoader.js'
import FileBrowser from '../components/FileBrowser.vue'

const props = defineProps({ id: String })

const cat = computed(() => CATS.find(c => c.id === props.id) || CATS[0])

// Use loaded data stats if available, otherwise fall back to static
const loadedData = computed(() => findCatData(cat.value))

const displayStats = computed(() => {
  const d = loadedData.value
  if (d && d.counts && Object.values(d.counts).some(v => v > 0)) {
    const safe = d.counts.SAFE || 0
    const fail = d.counts.FAILURE || 0
    const err = d.counts.ERROR || 0
    const to = d.counts.TIMED_OUT || 0
    const total = safe + fail + err + to || d.fuzzFiles.length
    const r = total > 0 ? (safe / total * 100).toFixed(1) : '0.0'
    const col = parseFloat(r) >= 50 ? 'var(--green)' : parseFloat(r) >= 30 ? 'var(--orange)' : 'var(--red)'
    return { total, safe, fail, err, to, r, col, fromFile: true }
  }
  const c = cat.value
  const r = (c.safe / c.total * 100).toFixed(1)
  const col = parseFloat(r) >= 50 ? 'var(--green)' : parseFloat(r) >= 30 ? 'var(--orange)' : 'var(--red)'
  return { total: c.total, safe: c.safe, fail: c.fail, err: c.err, to: c.to, r, col, fromFile: false }
})
</script>

<template>
  <div class="page-inner" v-if="cat">
    <div class="page-header">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
        <div class="page-title">{{ cat.display }}</div>
        <span class="badge" :class="cat.badge">{{ cat.tagTxt }}</span>
        <span v-if="displayStats.fromFile" style="font-size:11px;color:var(--green);background:var(--green-l);padding:2px 8px;border-radius:10px">📂 已加载文件数据</span>
      </div>
      <div class="page-subtitle" style="font-family:monospace">{{ cat.fullName }}</div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:10px;margin-bottom:16px">
      <div class="card card-sm" style="text-align:center">
        <div style="font-size:20px;font-weight:700;color:var(--primary)">{{ displayStats.total }}</div>
        <div style="font-size:11px;color:var(--muted)">总文件</div>
      </div>
      <div class="card card-sm" style="text-align:center">
        <div style="font-size:20px;font-weight:700;color:var(--green)">{{ displayStats.safe }}</div>
        <div style="font-size:11px;color:var(--muted)">SAFE</div>
      </div>
      <div class="card card-sm" style="text-align:center">
        <div style="font-size:20px;font-weight:700;color:var(--red)">{{ displayStats.fail }}</div>
        <div style="font-size:11px;color:var(--muted)">FAILURE</div>
      </div>
      <div class="card card-sm" style="text-align:center">
        <div style="font-size:20px;font-weight:700;color:var(--orange)">{{ displayStats.err }}</div>
        <div style="font-size:11px;color:var(--muted)">ERROR</div>
      </div>
      <div class="card card-sm" style="text-align:center">
        <div style="font-size:20px;font-weight:700" :style="{ color: displayStats.col }">{{ displayStats.r }}%</div>
        <div style="font-size:11px;color:var(--muted)">通过率</div>
      </div>
    </div>
    <FileBrowser :cat-id="cat.id" />
  </div>
</template>
