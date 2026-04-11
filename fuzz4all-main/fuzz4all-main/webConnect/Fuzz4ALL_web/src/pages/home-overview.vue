<template>
  <div class="placeholder-card">
    <h1>欢迎回来，{{ username }}</h1>
    <p>请从左侧选择模块开始工作。</p>
    <div class="grid-hint">
      <div class="hint-box">系统概览</div>
      <div class="hint-box">提示词库</div>
      <div class="hint-box">测试用例</div>
      <div class="hint-box">缺陷分析</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const username = ref(localStorage.getItem('username') || 'Admin')
</script>

<style scoped>
.placeholder-card {
  background: #fff;
  padding: 40px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  max-width: 800px;
  margin: 0 auto;
}

.placeholder-card h1 {
  color: #2c3e50;
  font-size: 28px;
  margin-bottom: 10px;
}

.placeholder-card p {
  color: #7f8c8d;
  margin-bottom: 30px;
}

.grid-hint {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
  max-width: 400px;
  margin: 0 auto;
}

.hint-box {
  background: #f9f9f9;
  padding: 15px;
  border-radius: 6px;
  color: #555;
  font-size: 14px;
  border: 1px dashed #ddd;
}
</style>
