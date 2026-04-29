<template>
  <div class="page">
    <section class="page-intro">
      <h1>差分分析与缺陷结果</h1>
      <p>
        本页突出系统的后处理能力，包括有效样本整理、跨版本 javac 差分，以及典型异常案例分析。
      </p>
    </section>

    <section class="summary-grid">
      <article class="summary-card">
        <span>差分候选池</span>
        <strong>{{ diffCases.length }}</strong>
        <p>当前页面展示的是重点样例卡片，后续可以替换成真实统计数据。</p>
      </article>
      <article class="summary-card">
        <span>重点模式</span>
        <strong>文档蒸馏 + 反馈迭代</strong>
        <p>这两种模式更容易产出结构复杂、适合进入差分测试阶段的样本。</p>
      </article>
      <article class="summary-card">
        <span>分析输出</span>
        <strong>版本差异 / 日志差异 / 样例归类</strong>
        <p>能够在答辩时直接说明你不仅生成了样本，还做了缺陷分析与归档。</p>
      </article>
    </section>

    <section class="case-list">
      <article v-for="item in diffCases" :key="item.id" class="case-card">
        <header class="case-header">
          <div>
            <p class="case-id">{{ item.id }}</p>
            <h2>{{ item.title }}</h2>
            <p class="case-meta">{{ item.testPoint }} · {{ item.mode }}</p>
          </div>
          <span class="focus-badge">重点样例</span>
        </header>

        <div class="compare-grid">
          <div class="compare-box">
            <h3>编译器 A</h3>
            <p>{{ item.javacA }}</p>
          </div>
          <div class="compare-box">
            <h3>编译器 B</h3>
            <p>{{ item.javacB }}</p>
          </div>
        </div>

        <div class="detail-block">
          <h3>差异代码片段</h3>
          <pre>{{ item.snippet }}</pre>
        </div>

        <div class="detail-block conclusion">
          <h3>分析结论</h3>
          <p>{{ item.conclusion }}</p>
        </div>
      </article>
    </section>

    <section class="material-panel">
      <div class="panel-header">
        <h2>补充材料占位</h2>
        <span>这里后续放差分日志截图、异常详情截图和实验图表</span>
      </div>
      <div class="material-grid">
        <div v-for="item in materialPlaceholders" :key="item" class="material-box">
          {{ item }}
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { diffCases, materialPlaceholders } from '../services/dashboardData'
</script>

<style scoped>
.page {
  display: grid;
  gap: 24px;
}

.page-intro,
.summary-card,
.case-card,
.material-panel {
  padding: 24px;
  border-radius: 24px;
  background: #ffffff;
  box-shadow: 0 16px 36px rgba(15, 23, 42, 0.07);
}

.page-intro h1,
.summary-card strong,
.case-card h2,
.compare-box h3,
.detail-block h3,
.panel-header h2 {
  margin: 0;
  color: #0f172a;
}

.page-intro p,
.summary-card p,
.case-meta,
.compare-box p,
.detail-block p,
.panel-header span {
  color: #475569;
  line-height: 1.8;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}

.summary-card span,
.case-id {
  color: #64748b;
  font-size: 13px;
}

.summary-card strong {
  display: block;
  margin: 12px 0;
  font-size: 28px;
}

.case-list {
  display: grid;
  gap: 18px;
}

.case-header,
.compare-grid {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 16px;
}

.case-header {
  margin-bottom: 18px;
}

.case-meta {
  margin: 8px 0 0;
}

.focus-badge {
  align-self: start;
  padding: 8px 12px;
  border-radius: 999px;
  background: #eef4ff;
  color: #2558c7;
  font-size: 12px;
  font-weight: 700;
}

.compare-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
  margin-bottom: 16px;
}

.compare-box,
.detail-block,
.material-box {
  padding: 16px;
  border-radius: 18px;
  background: #f8fafc;
}

.detail-block {
  margin-top: 14px;
}

.detail-block pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  color: #1e293b;
  font-family: 'Consolas', 'Courier New', monospace;
  line-height: 1.7;
}

.conclusion {
  background: linear-gradient(135deg, #fff7ed, #fffbeb);
}

.panel-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 18px;
}

.material-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
}

.material-box {
  display: grid;
  place-items: center;
  min-height: 150px;
  border: 2px dashed #cbd5e1;
  color: #64748b;
  text-align: center;
}

@media (max-width: 1100px) {
  .summary-grid,
  .compare-grid,
  .material-grid,
  .case-header {
    grid-template-columns: 1fr;
  }
}
</style>
