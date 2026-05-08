import { reactive, ref } from 'vue'

// Shared reactive state
export const folderName = ref('')
export const catDataMap = reactive({})  // folderKey -> { fuzzFiles, prompts, logFiles, manifest, counts }

function parseManifest (txt) {
  return txt.trim().split('\n').filter(l => l).map(l => { try { return JSON.parse(l) } catch { return null } }).filter(Boolean)
}

function countManifest (m) {
  const c = { SAFE: 0, FAILURE: 0, ERROR: 0, TIMED_OUT: 0, UNKNOWN: 0 }
  ;(m || []).forEach(r => { const k = r.compile_result || 'UNKNOWN'; c[k] = (c[k] || 0) + 1 })
  return c
}

function numSort (a, b) {
  const na = parseInt(a), nb = parseInt(b)
  return (!isNaN(na) && !isNaN(nb)) ? na - nb : a.localeCompare(b)
}

async function readAny (h) {
  if (!h) return '(空)'
  if (h instanceof File) return await h.text()
  if (typeof h.getFile === 'function') return await (await h.getFile()).text()
  if (typeof h.text === 'function') return await h.text()
  return '(无法读取)'
}

// ── File System Access API ──
async function readCatFSA (dirHandle) {
  const d = { fuzzFiles: [], prompts: {}, logFiles: {}, manifest: [], counts: {} }
  for await (const [n, h] of dirHandle.entries()) {
    if (n.endsWith('.fuzz')) d.fuzzFiles.push({ name: n, handle: h })
    else if (n === 'mutation_manifest.jsonl') {
      try { d.manifest = parseManifest(await (await h.getFile()).text()) } catch {}
    } else if (['log.txt', 'log_generation.txt', 'log_validation.txt'].includes(n)) {
      d.logFiles[n] = h
    } else if (n === 'prompts' && h.kind === 'directory') {
      for await (const [pn, ph] of h.entries()) {
        if (ph.kind === 'file') d.prompts[pn] = ph
      }
    }
  }
  d.fuzzFiles.sort((a, b) => numSort(a.name, b.name))
  d.counts = countManifest(d.manifest)
  return d
}

async function loadFromFSA (rootHandle) {
  Object.keys(catDataMap).forEach(k => delete catDataMap[k])
  const name = rootHandle.name
  for await (const [n, handle] of rootHandle.entries()) {
    if (handle.kind === 'directory' && !n.startsWith('.')) {
      catDataMap[n] = await readCatFSA(handle)
    }
  }
  folderName.value = name
}

// ── <input webkitdirectory> fallback ──
function loadFromInput (files) {
  Object.keys(catDataMap).forEach(k => delete catDataMap[k])
  const map = {}
  for (const f of files) map[f.webkitRelativePath] = f
  let name = ''
  const catMap = {}
  for (const path of Object.keys(map)) {
    const parts = path.split('/')
    if (!name && parts.length > 0) name = parts[0]
    if (parts.length < 3) continue
    const catName = parts[1]
    if (!catMap[catName]) catMap[catName] = { fuzzFiles: [], prompts: {}, logFiles: {}, manifest: [], counts: {} }
    const fileName = parts[parts.length - 1]
    if (parts.length === 3 && fileName.endsWith('.fuzz')) {
      catMap[catName].fuzzFiles.push({ name: fileName, file: map[path] })
    } else if (parts.length === 3 && ['log.txt', 'log_generation.txt', 'log_validation.txt'].includes(fileName)) {
      catMap[catName].logFiles[fileName] = map[path]
    } else if (parts.length === 3 && fileName === 'mutation_manifest.jsonl') {
      map[path].text().then(txt => {
        catMap[catName].manifest = parseManifest(txt)
        catMap[catName].counts = countManifest(catMap[catName].manifest)
      }).catch(() => {})
    } else if (parts.length === 4 && parts[2] === 'prompts') {
      catMap[catName].prompts[fileName] = map[path]
    }
  }
  for (const [k, v] of Object.entries(catMap)) {
    v.fuzzFiles.sort((a, b) => numSort(a.name, b.name))
    v.counts = countManifest(v.manifest)
    catDataMap[k] = v
  }
  folderName.value = name || '已上传'
}

// ── Match loaded folder to a CATS entry ──
export function findCatData (catDef) {
  for (const [k, v] of Object.entries(catDataMap)) {
    const kl = k.toLowerCase()
    const fk = catDef.folderKey.toLowerCase()
    if (kl.includes(fk) || fk.includes(kl.replace(/[._]/g, '_'))) return v
    if (fk.split('_').every(seg => kl.includes(seg))) return v
  }
  for (const [k, v] of Object.entries(catDataMap)) {
    const kl = k.toLowerCase().replace(/[._]/g, '')
    const fk = catDef.folderKey.toLowerCase().replace(/[._]/g, '')
    if (kl.includes(fk) || fk.includes(kl)) return v
  }
  return null
}

// ── Public API ──
export async function openFolder () {
  if (!window.showDirectoryPicker) {
    alert('请使用"上传文件夹"按钮，或切换到 Chrome/Edge 浏览器。')
    return
  }
  try {
    const h = await window.showDirectoryPicker({ mode: 'read' })
    await loadFromFSA(h)
  } catch (e) {
    if (e.name !== 'AbortError') console.error(e)
  }
}

export function handleFileInput (files) {
  loadFromInput(files)
}

export { readAny }
