<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { CATS, tagColor } from '../data/cats.js'
import { folderName, openFolder, handleFileInput } from '../composables/useFolderLoader.js'

const router = useRouter()
const route = useRoute()
const catsOpen = ref(true)
const fileInput = ref(null)

function navTo (name) {
  router.push({ name })
}

function navToCat (id) {
  router.push({ name: 'category', params: { id } })
}

function isActive (name) {
  return route.name === name
}

function isCatActive (id) {
  return route.name === 'category' && route.params.id === id
}

function onFileChange (e) {
  if (e.target.files && e.target.files.length > 0) {
    handleFileInput(e.target.files)
  }
}
</script>

<template>
  <aside class="sidebar">
    <div class="sb-header">
      <div class="sb-logo">基于Fuzz4All的<br>JVM大模型测试</div>
      <div class="sb-sub">陕西科技大学 · 夏文静 · 2026</div>
    </div>
    <div v-if="folderName" class="sb-folder-info">📂 {{ folderName }}</div>
    <nav class="sb-nav">
      <div class="nav-item" :class="{ active: isActive('intro') }" @click="navTo('intro')">
        <i class="ico"></i>系统介绍
      </div>
      <div class="nav-item" :class="{ active: isActive('evidence') }" @click="navTo('evidence')">
        <i class="ico"></i>流程证据
      </div>
      <div class="nav-item" :class="{ active: isActive('results') }" @click="navTo('results')">
        <i class="ico"></i>测试结果
      </div>
      <div class="nav-section">成果浏览</div>
      <div class="nav-item" :class="{ active: isActive('classification') }" @click="navTo('classification')">
        <i class="ico">🗂️</i>离线分类对应表
      </div>
      <div class="nav-group-toggle" :class="{ open: catsOpen }" @click="catsOpen = !catsOpen">
        <i class="ico">📁</i><span>10类测试成果</span><span class="arrow">▶</span>
      </div>
      <div class="nav-sub" :class="{ open: catsOpen }">
        <div
          v-for="c in CATS"
          :key="c.id"
          class="nav-item"
          :class="{ active: isCatActive(c.id) }"
          @click="navToCat(c.id)"
        >
          <span class="tag-dot" :style="{ background: tagColor(c.tagTxt) }"></span>{{ c.display }}
        </div>
      </div>
    </nav>
    <div class="sb-actions">
      <button class="sb-btn primary" @click="openFolder()">📂 选择输出文件夹</button>
      <label class="sb-btn" style="cursor:pointer">
        📤 上传文件夹
        <input
          ref="fileInput"
          type="file"
          webkitdirectory
          multiple
          style="display:none"
          @change="onFileChange"
        />
      </label>
    </div>
  </aside>
</template>
