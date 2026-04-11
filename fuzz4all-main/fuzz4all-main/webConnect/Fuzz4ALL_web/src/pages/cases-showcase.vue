<template>
  <div class="page">
    <section class="page-intro">
      <h1>测试样例展示</h1>
      <p>
        这一页集中展示不同知识引导方式在 javac 场景中的生成结果，包含对比统计、测试点覆盖和代表性代码样例。
      </p>
    </section>

    <section class="result-grid">
      <article v-for="item in experimentResults" :key="item.mode" class="result-card">
        <h2>{{ item.mode }}</h2>
        <div class="result-meta">
          <span>生成样本 {{ item.generated }}</span>
          <span>编译通过 {{ item.passed }}</span>
        </div>
        <strong>{{ item.passRate }}%</strong>
        <p>差分阶段发现 {{ item.diffFindings }} 个重点样例</p>
      </article>
    </section>

    <section class="panel">
      <div class="panel-header">
        <h2>测试点覆盖统计</h2>
        <span>适合替换为后续真实图表</span>
      </div>
      <div class="bar-table">
        <div class="bar-head">
          <span>测试点</span>
          <span>示例/手工</span>
          <span>文档蒸馏</span>
          <span>反馈迭代</span>
        </div>
        <div v-for="item in testPointStats" :key="item.label" class="bar-row">
          <span class="row-label">{{ item.label }}</span>
          <div class="bar-cell">
            <i :style="{ width: `${item.manual / 1.6}%` }" class="bar manual"></i>
            <b>{{ item.manual }}</b>
          </div>
          <div class="bar-cell">
            <i :style="{ width: `${item.distill / 1.6}%` }" class="bar distill"></i>
            <b>{{ item.distill }}</b>
          </div>
          <div class="bar-cell">
            <i :style="{ width: `${item.feedback / 1.6}%` }" class="bar feedback"></i>
            <b>{{ item.feedback }}</b>
          </div>
        </div>
      </div>
    </section>

    <section class="showcase-grid">
      <article v-for="item in testcaseShowcases" :key="item.id" class="case-card">
        <header class="case-header">
          <div>
            <h2>{{ item.id }} · {{ item.testPoint }}</h2>
            <p>{{ item.mode }}</p>
          </div>
          <span :class="['status', item.status.toLowerCase()]">{{ item.status }}</span>
        </header>
        <div class="info-block">
          <h3>Prompt 摘要</h3>
          <p>{{ item.promptSummary }}</p>
        </div>
        <div class="info-block">
          <h3>代码样例</h3>
          <pre>{{ item.code }}</pre>
        </div>
        <div class="dual-info">
          <div class="info-block">
            <h3>编译日志</h3>
            <pre>{{ item.compilerLog }}</pre>
          </div>
          <div class="info-block">
            <h3>差分去向</h3>
            <p>{{ item.diffSummary }}</p>
          </div>
        </div>
      </article>
    </section>
  </div>
</template>

<script setup lang="ts">
import { experimentResults, testcaseShowcases, testPointStats } from '../services/dashboardData'
</script>

<style scoped>
.page {
  display: grid;
  gap: 24px;
}

.page-intro,
.panel,
.result-card,
.case-card {
  border-radius: 24px;
  background: #ffffff;
  box-shadow: 0 16px 36px rgba(15, 23, 42, 0.07);
}

.page-intro,
.panel,
.result-card,
.case-card {
  padding: 24px;
}

.page-intro h1,
.panel-header h2,
.result-card h2,
.case-card h2,
.info-block h3 {
  margin: 0;
  color: #0f172a;
}

.page-intro p,
.panel-header span,
.result-card p,
.case-header p,
.info-block p {
  color: #475569;
  line-height: 1.8;
}

.result-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}

.result-meta {
  display: flex;
  justify-content: space-between;
  margin: 14px 0 10px;
  color: #64748b;
  font-size: 14px;
}

.result-card strong {
  color: #2f6fed;
  font-size: 34px;
}

.panel-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 18px;
}

.bar-table {
  display: grid;
  gap: 12px;
}

.bar-head,
.bar-row {
  display: grid;
  grid-template-columns: 160px repeat(3, minmax(0, 1fr));
  gap: 12px;
  align-items: center;
}

.bar-head {
  color: #64748b;
  font-size: 13px;
}

.row-label {
  font-weight: 600;
  color: #0f172a;
}

.bar-cell {
  position: relative;
  height: 36px;
  overflow: hidden;
  border-radius: 999px;
  background: #f1f5f9;
}

.bar {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  border-radius: 999px;
}

.manual {
  background: linear-gradient(90deg, #3b82f6, #7ab4ff);
}

.distill {
  background: linear-gradient(90deg, #10b981, #4ade80);
}

.feedback {
  background: linear-gradient(90deg, #f59e0b, #facc15);
}

.bar-cell b {
  position: relative;
  z-index: 1;
  display: inline-block;
  padding: 8px 14px;
  color: #0f172a;
}

.showcase-grid {
  display: grid;
  gap: 18px;
}

.case-header,
.dual-info {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 16px;
  align-items: start;
}

.case-header {
  margin-bottom: 16px;
}

.case-header p {
  margin: 8px 0 0;
}

.status {
  padding: 8px 12px;
  border-radius: 999px;
  color: #ffffff;
  font-size: 12px;
  font-weight: 700;
}

.status.pass {
  background: #16a34a;
}

.status.fail {
  background: #ef4444;
}

.status.diff {
  background: #2563eb;
}

.info-block {
  margin-top: 14px;
  padding: 16px;
  border-radius: 18px;
  background: #f8fafc;
}

.info-block h3 {
  margin-bottom: 10px;
  font-size: 15px;
}

.info-block pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  color: #1e293b;
  font-family: 'Consolas', 'Courier New', monospace;
  line-height: 1.7;
}

.dual-info {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

@media (max-width: 1100px) {
  .result-grid,
  .dual-info,
  .bar-head,
  .bar-row {
    grid-template-columns: 1fr;
  }
}
</style>
