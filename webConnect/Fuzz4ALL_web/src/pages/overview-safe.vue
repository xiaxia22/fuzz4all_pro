<template>
  <div class="page">
    <section class="hero">
      <div class="hero-copy">
        <p class="eyebrow">JVM Testing Dashboard</p>
        <h1>LLM-based JVM Testing System</h1>
        <p class="summary">
          This page is designed for thesis presentation. It emphasizes the system target,
          knowledge-guided workflow, experiment scale, and engineering extensions over the
          original Fuzz4All framework.
        </p>
      </div>
      <div class="hero-side">
        <div class="mini-card"><span class="mini-label">Generation Model</span><strong>Qwen2.5</strong></div>
        <div class="mini-card"><span class="mini-label">Distillation Model</span><strong>DeepSeek</strong></div>
        <div class="mini-card"><span class="mini-label">Target Compiler</span><strong>javac</strong></div>
      </div>
    </section>

    <section class="metric-grid">
      <article v-for="metric in overviewMetrics" :key="metric.label" class="metric-card">
        <span class="metric-label">{{ metric.label }}</span>
        <strong class="metric-value">{{ metric.value }}</strong>
        <p class="metric-note">{{ metric.note }}</p>
      </article>
    </section>

    <section class="double-grid">
      <article class="panel">
        <div class="panel-header"><h2>Workflow</h2><span>Shows system design effort</span></div>
        <ol class="workflow-list"><li v-for="step in workflowSteps" :key="step">{{ step }}</li></ol>
      </article>
      <article class="panel">
        <div class="panel-header"><h2>Extensions over Fuzz4All</h2><span>Shows method and implementation work</span></div>
        <ul class="contribution-list"><li v-for="point in contributionPoints" :key="point">{{ point }}</li></ul>
      </article>
    </section>

    <section class="panel">
      <div class="panel-header"><h2>Three Knowledge Modes</h2><span>Highlights the core innovation</span></div>
      <div class="mode-grid">
        <article v-for="mode in knowledgeModes" :key="mode.id" class="mode-card">
          <h3>{{ mode.title }}</h3>
          <p class="mode-source">{{ mode.source }}</p>
          <p class="mode-text">{{ mode.mechanism }}</p>
          <div class="tag-row"><span v-for="item in mode.highlights" :key="item" class="tag">{{ item }}</span></div>
        </article>
      </div>
    </section>

    <section class="panel">
      <div class="panel-header"><h2>Material Placeholders</h2><span>Replace these with real screenshots later</span></div>
      <div class="placeholder-grid">
        <div v-for="item in materialPlaceholders" :key="item" class="placeholder-box">{{ item }}</div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import {
  contributionPoints,
  knowledgeModes,
  materialPlaceholders,
  overviewMetrics,
  workflowSteps,
} from '../services/dashboardDataSafe'
</script>

<style scoped>
.page { display: grid; gap: 24px; }
.hero { display: grid; grid-template-columns: 2fr 1fr; gap: 20px; padding: 28px; border-radius: 24px; background: radial-gradient(circle at top left, rgba(53, 122, 255, 0.16), transparent 34%), linear-gradient(135deg, #ffffff, #eef4ff); box-shadow: 0 18px 40px rgba(31, 45, 61, 0.08); }
.eyebrow { margin: 0 0 10px; color: #2f6fed; font-size: 13px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; }
.hero h1 { margin: 0 0 12px; color: #0f172a; font-size: 34px; line-height: 1.2; }
.summary { margin: 0; color: #475569; font-size: 15px; line-height: 1.8; }
.hero-side { display: grid; gap: 14px; }
.mini-card, .metric-card, .panel, .mode-card, .placeholder-box { border: 1px solid rgba(148, 163, 184, 0.18); background: rgba(255, 255, 255, 0.92); box-shadow: 0 14px 28px rgba(15, 23, 42, 0.06); }
.mini-card { display: flex; flex-direction: column; justify-content: center; padding: 18px; border-radius: 18px; }
.mini-label { margin-bottom: 8px; color: #64748b; font-size: 12px; }
.mini-card strong { color: #0f172a; font-size: 22px; }
.metric-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; }
.metric-card { padding: 20px; border-radius: 20px; }
.metric-label { color: #64748b; font-size: 13px; }
.metric-value { display: block; margin: 10px 0 8px; color: #0f172a; font-size: 28px; }
.metric-note { margin: 0; color: #475569; font-size: 14px; line-height: 1.6; }
.double-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px; }
.panel { padding: 22px; border-radius: 24px; }
.panel-header { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; margin-bottom: 16px; }
.panel-header h2 { margin: 0; color: #0f172a; font-size: 22px; }
.panel-header span { color: #64748b; font-size: 13px; }
.workflow-list, .contribution-list { margin: 0; padding-left: 20px; color: #334155; line-height: 1.9; }
.mode-grid, .placeholder-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
.mode-card { padding: 18px; border-radius: 20px; }
.mode-card h3 { margin: 0 0 8px; color: #0f172a; }
.mode-source { margin: 0 0 10px; color: #2f6fed; font-size: 13px; font-weight: 600; }
.mode-text { margin: 0 0 14px; color: #475569; line-height: 1.8; }
.tag-row { display: flex; flex-wrap: wrap; gap: 8px; }
.tag { padding: 6px 10px; border-radius: 999px; background: #eef4ff; color: #2457c5; font-size: 12px; }
.placeholder-box { display: grid; place-items: center; min-height: 160px; padding: 16px; border-radius: 20px; border-style: dashed; color: #64748b; text-align: center; line-height: 1.8; }
@media (max-width: 1100px) { .hero, .double-grid, .mode-grid, .placeholder-grid, .metric-grid { grid-template-columns: 1fr; } }
</style>
