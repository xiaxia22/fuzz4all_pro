<script setup>
import StatCard from '../components/StatCard.vue'
import WorkflowDiagram from '../components/WorkflowDiagram.vue'

const phase1 = [
  { icon: '📖', title: '读取API文档', desc: '逐API提取标准库文档内容' },
  { icon: '🏷️', title: '规则匹配分类', desc: '关键词+评分为每个API打领域标签' },
  { icon: '🗂️', title: '生成分类表', desc: '输出JSON，记录类别与变异策略' }
]

const phase2 = [
  { icon: '🔍', title: '查询分类 加载策略', desc: '查分类表，加载领域变异策略' },
  { icon: '✍️', title: 'Auto-Prompting', desc: '大模型读文档，生成并评分候选提示词' },
  { icon: '🤖', title: '生成 Seed', desc: '代码模型基于提示词批量生成测试程序' },
  { icon: '🔀', title: '定向变异', desc: '按领域策略对seed变异生成mutation' },
  { icon: '⚙️', title: '编译与验证', desc: 'javac编译+运行，分SAFE/FAIL/ERROR' },
  { icon: '🔄', title: '反馈写回闭环', desc: '规则归类+成功样例写回提示词，迭代优化' }
]
</script>

<template>
  <div class="page-inner">
    <div class="hero-band">
      <h1>基于Fuzz4All的JVM大模型测试</h1>
      <p>
        基于文档驱动与分类策略的API自动化测试框架。
        该框架首先通过离线分析构建API分类体系，并在运行时动态加载适配的变异策略。
        在核心生成阶段，系统利用大语言模型解析文档生成初始种子代码，并结合定向变异策略扩展测试用例。
        此外，系统建立了一个自适应的反馈闭环机制：通过对编译与运行结果的智能归因分析，将失败约束与成功范例动态融入提示词工程，
        驱动模型进行多轮迭代优化，从而实现测试用例生成的持续进化与质量提升。
      </p>
      <div class="hero-meta">
        <span> 陕西科技大学</span>
        <span> 夏文静</span>
        <span> 2026</span>
        <span> Fuzz4All · Qwen2.5-Coder-7B · Java 21</span>
      </div>
    </div>

    <div class="g4" style="margin-bottom:20px">
      <StatCard :value="10" label="测试 API 类别" />
      <StatCard :value="568" label="总生成测试用例" />
      <StatCard :value="'164'" label="编译通过 (SAFE)" color="var(--green)" />
      <StatCard :value="'38+'" label="领域变异算子" />
    </div>

    <div class="card" style="margin-bottom:16px">
      <div class="card-title">系统工作流程</div>
      <div style="font-size:11px;color:var(--muted);margin-bottom:12px;padding:4px 10px;
        background:var(--surface2);border-radius:5px;border-left:3px solid var(--light);display:inline-block">
        阶段一：离线构建分类知识库
      </div>
      <WorkflowDiagram :steps="phase1" style="margin-bottom:20px" />
      <div style="font-size:11px;color:var(--primary);margin-bottom:12px;padding:4px 10px;
        background:var(--primary-xl);border-radius:5px;border-left:3px solid var(--primary);display:inline-block">
        阶段二：在线自适应闭环生成
      </div>
      <WorkflowDiagram :steps="phase2" />
    </div>

    <div class="g3">
      <div class="card card-sm">
        <div class="card-title">代码生成模型</div>
        <div style="font-weight:600;color:var(--primary)">Qwen2.5-Coder-7B</div>
        <div style="color:var(--muted);font-size:12px;margin-top:3px">Ollama本地 · 温度1.0 · 批量30</div>
      </div>
      <div class="card card-sm">
        <div class="card-title">Auto-Prompting</div>
        <div style="font-weight:600;color:var(--primary)">DeepSeek / Ollama</div>
        <div style="color:var(--muted);font-size:12px;margin-top:3px">候选生成·贪心+采样·评分筛选</div>
      </div>
      <div class="card card-sm">
        <div class="card-title">验证环境</div>
        <div style="font-weight:600;color:var(--primary)">Java 21 + --enable-preview</div>
        <div style="color:var(--muted);font-size:12px;margin-top:3px">javac编译 · java运行 · 5秒超时</div>
      </div>
    </div>
  </div>
</template>
