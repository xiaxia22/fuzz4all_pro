<script setup>
import StatCard from '../components/StatCard.vue'
import WorkflowDiagram from '../components/WorkflowDiagram.vue'

const phase1 = [
  { icon: '📚', title: '读取 API 文档', desc: '抽取标准库 API 的文档与接口信息' },
  { icon: '🏷️', title: '离线分类', desc: '根据规则与语义为 API 分配领域标签' },
  { icon: '🗂️', title: '生成分类表', desc: '输出 JSON，记录分类结果与变异策略映射' }
]

const phase2 = [
  { icon: '🔎', title: '查询分类并加载策略', desc: '按分类表选择对应 mutation profile 与算子' },
  { icon: '✨', title: 'Auto-Prompting', desc: '文档驱动生成候选 prompt 并自动评分选择' },
  { icon: '🌱', title: '生成 Seed', desc: '代码模型批量生成初始测试样本' },
  { icon: '🧪', title: '定向变异', desc: '按类别策略对 seed 进行 mutation 扩展' },
  { icon: '⚙️', title: '编译与验证', desc: 'javac 编译 + 运行验证，区分 SAFE / FAILURE / ERROR' },
  { icon: '🔁', title: '反馈闭环', desc: '归类错误、提炼规则并回写 prompt 继续迭代' }
]
</script>

<template>
  <div class="page-inner">
    <div class="hero-band">
      <h1>基于 Fuzz4All 的 JVM 大模型测试</h1>
      <p>
        该系统面向 Java 标准库 API 的自动化测试，从 API 文档出发完成离线分类、候选 prompt 生成、
        seed 生成、分类感知 mutation、编译运行验证以及反馈闭环。当前展示结果使用每个代表 API 的历史最佳成绩，
        重点体现不同类别在分类驱动和反馈收敛后的可达上限。
      </p>
      <div class="hero-meta">
        <span>陕西科技大学</span>
        <span>夏文静</span>
        <span>2026</span>
        <span>Fuzz4All · Qwen2.5-Coder-7B · Java 21</span>
      </div>
    </div>

    <div class="g4" style="margin-bottom:20px">
      <StatCard :value="10" label="测试 API 类别" />
      <StatCard :value="1280" label="总生成测试用例" />
      <StatCard :value="'886'" label="编译通过 (SAFE)" color="var(--green)" />
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
        <div style="color:var(--muted);font-size:12px;margin-top:3px">Ollama 本地部署 · 温度 0.9~1.0 · 批量 30</div>
      </div>
      <div class="card card-sm">
        <div class="card-title">Auto-Prompting</div>
        <div style="font-weight:600;color:var(--primary)">DeepSeek / Ollama</div>
        <div style="color:var(--muted);font-size:12px;margin-top:3px">候选生成 · 评分选择 · 运行期 refresh</div>
      </div>
      <div class="card card-sm">
        <div class="card-title">验证环境</div>
        <div style="font-weight:600;color:var(--primary)">Java 21 + --enable-preview</div>
        <div style="color:var(--muted);font-size:12px;margin-top:3px">javac 编译 · java 运行 · 5 秒超时</div>
      </div>
    </div>
  </div>
</template>
