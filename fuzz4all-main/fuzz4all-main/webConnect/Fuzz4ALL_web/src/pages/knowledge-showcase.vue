<template>
  <div class="page">
    <section class="page-intro">
      <h1>多源知识引导机制</h1>
      <p>
        本页重点展示三种 Prompt 生成方式，以及它们如何把示例代码、标准文档、运行反馈转化为可执行的测试生成知识。
      </p>
    </section>

    <section class="mode-columns">
      <article v-for="mode in knowledgeModes" :key="mode.id" class="mode-card">
        <header>
          <h2>{{ mode.title }}</h2>
          <span>{{ mode.source }}</span>
        </header>
        <p class="mechanism">{{ mode.mechanism }}</p>
        <div class="preview-block">
          <h3>Prompt 预览</h3>
          <pre>{{ mode.promptPreview }}</pre>
        </div>
        <div class="preview-block">
          <h3>代表性生成样例</h3>
          <pre>{{ mode.outputPreview }}</pre>
        </div>
        <div class="tag-row">
          <span v-for="item in mode.highlights" :key="item" class="tag">{{ item }}</span>
        </div>
      </article>
    </section>

    <section class="timeline-panel">
      <div class="panel-header">
        <h2>Prompt 演化链路</h2>
        <span>展示你的方法细节与工作量</span>
      </div>
      <div class="timeline">
        <article class="timeline-item">
          <span class="step">01</span>
          <div>
            <h3>知识输入</h3>
            <p>输入手工 Prompt、示例代码、标准文档和近轮编译反馈，作为知识源集合。</p>
          </div>
        </article>
        <article class="timeline-item">
          <span class="step">02</span>
          <div>
            <h3>候选 Prompt 构造</h3>
            <p>对文档进行蒸馏，对手工知识进行拼接，对反馈日志进行摘要，形成可比较的候选 Prompt。</p>
          </div>
        </article>
        <article class="timeline-item">
          <span class="step">03</span>
          <div>
            <h3>生成与编译验证</h3>
            <p>使用 Qwen2.5 生成 Java 程序，并调用 javac 过滤出可编译样本。</p>
          </div>
        </article>
        <article class="timeline-item">
          <span class="step">04</span>
          <div>
            <h3>反馈回灌</h3>
            <p>将成功样本和关键编译日志继续拼回 Prompt，驱动下一轮生成策略调整。</p>
          </div>
        </article>
      </div>
    </section>

    <section class="placeholder-panel">
      <div class="panel-header">
        <h2>可替换的答辩素材</h2>
        <span>这里后续替换成真实蒸馏截图和 prompt 文件截图</span>
      </div>
      <div class="placeholder-list">
        <div v-for="item in materialPlaceholders" :key="item" class="placeholder-item">
          {{ item }}
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { knowledgeModes, materialPlaceholders } from '../services/dashboardData'
</script>

<style scoped>
.page {
  display: grid;
  gap: 24px;
}

.page-intro,
.timeline-panel,
.placeholder-panel,
.mode-card {
  border-radius: 24px;
  background: #ffffff;
  box-shadow: 0 16px 36px rgba(15, 23, 42, 0.07);
}

.page-intro,
.timeline-panel,
.placeholder-panel {
  padding: 24px;
}

.page-intro h1,
.panel-header h2,
.mode-card h2,
.preview-block h3,
.timeline-item h3 {
  margin: 0;
  color: #0f172a;
}

.page-intro p,
.mechanism,
.timeline-item p,
.panel-header span {
  color: #475569;
  line-height: 1.8;
}

.mode-columns {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}

.mode-card {
  padding: 20px;
}

.mode-card header {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 14px;
}

.mode-card header span {
  color: #2f6fed;
  font-size: 13px;
  font-weight: 600;
}

.mechanism {
  margin: 0 0 16px;
}

.preview-block {
  margin-bottom: 14px;
  padding: 14px;
  border-radius: 16px;
  background: #f8fafc;
}

.preview-block h3 {
  margin-bottom: 10px;
  font-size: 15px;
}

.preview-block pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  color: #1e293b;
  font-family: 'Consolas', 'Courier New', monospace;
  line-height: 1.7;
}

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 6px 10px;
  border-radius: 999px;
  background: #e8f0ff;
  color: #2558c7;
  font-size: 12px;
}

.panel-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 18px;
}

.timeline {
  display: grid;
  gap: 16px;
}

.timeline-item {
  display: grid;
  grid-template-columns: 56px 1fr;
  gap: 16px;
  align-items: start;
  padding: 16px;
  border-radius: 18px;
  background: #f8fafc;
}

.step {
  display: grid;
  place-items: center;
  width: 56px;
  height: 56px;
  border-radius: 18px;
  background: linear-gradient(135deg, #2f6fed, #5fa1ff);
  color: #ffffff;
  font-weight: 700;
}

.placeholder-list {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
}

.placeholder-item {
  display: grid;
  place-items: center;
  min-height: 150px;
  padding: 18px;
  border: 2px dashed #cbd5e1;
  border-radius: 18px;
  background: #f8fafc;
  color: #64748b;
  text-align: center;
}

@media (max-width: 1100px) {
  .mode-columns,
  .placeholder-list {
    grid-template-columns: 1fr;
  }
}
</style>
