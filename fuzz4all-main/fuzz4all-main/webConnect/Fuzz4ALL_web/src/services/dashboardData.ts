export interface OverviewMetric {
  label: string
  value: string
  note: string
}

export interface KnowledgeMode {
  id: string
  title: string
  source: string
  mechanism: string
  promptPreview: string
  outputPreview: string
  highlights: string[]
}

export interface ExperimentResult {
  mode: string
  generated: number
  passed: number
  passRate: number
  diffFindings: number
}

export interface TestCaseShowcase {
  id: string
  testPoint: string
  mode: string
  status: 'PASS' | 'FAIL' | 'DIFF'
  promptSummary: string
  code: string
  compilerLog: string
  diffSummary: string
}

export interface DiffCase {
  id: string
  title: string
  testPoint: string
  mode: string
  javacA: string
  javacB: string
  conclusion: string
  snippet: string
}

export const overviewMetrics: OverviewMetric[] = [
  { label: '目标编译器', value: 'javac', note: '面向 JVM 编译器的定向测试' },
  { label: '知识模式', value: '3', note: '示例知识、文档蒸馏、反馈迭代' },
  { label: '测试点数量', value: '5+', note: 'finally、instanceof、synchronized 等' },
  { label: '差分阶段', value: '2', note: '有效样本整理后进入版本差分测试' },
]

export const workflowSteps = [
  '收集多源知识：示例代码、标准文档、编译反馈',
  '构造或蒸馏 Prompt，形成目标测试点的知识引导',
  '使用 Qwen2.5 生成 Java 测试程序',
  '调用 javac 编译，记录成功样本与异常日志',
  '基于成功样本和日志继续迭代 Prompt',
  '整理最终有效样本并执行差分测试',
]

export const contributionPoints = [
  '将原始 Fuzz4All 框架扩展到 javac 定向测试场景。',
  '实现三种知识引导 Prompt 生成方式，并统一到同一测试流程中。',
  '把编译日志和历史运行反馈纳入 Prompt 更新过程，形成反馈迭代链路。',
  '补充测试样例整理与差分测试分析页面，形成完整展示系统。',
]

export const knowledgeModes: KnowledgeMode[] = [
  {
    id: 'manual',
    title: '示例/手工知识引导',
    source: '手工 Prompt + 示例代码',
    mechanism: '把人工编写的提示词和代表性 Java 示例代码拼接成初始 Prompt，作为生成阶段的结构先验。',
    promptPreview:
      'Generate short but non-trivial Java programs for testing javac. Prefer records, pattern matching, lambdas, generics, switch expressions, and try/finally interactions...',
    outputPreview:
      'record Pair<T>(T left, T right) {} class SeedCase { static int f(Pair<Integer> p) { ... } }',
    highlights: ['适合快速验证环境', '便于控制测试风格', '可直接映射“源代码知识”'],
  },
  {
    id: 'distill',
    title: '标准文档蒸馏引导',
    source: 'Java 标准文档 + DeepSeek 蒸馏',
    mechanism: '把 Java 标准文档输入大模型，自动提炼语法构造、边界组合和编译敏感点，再筛选最佳 Prompt。',
    promptPreview:
      'Use modern Java features in compact but valid ways. Focus on records, sealed hierarchies, pattern matching, nested switch expressions, and interactions between control flow and type inference...',
    outputPreview:
      'sealed interface Expr permits Lit, Add {} record Lit(int v) implements Expr {} record Add(Expr l, Expr r) implements Expr {}',
    highlights: ['体现“文档指导生成”', '支持测试点定制', '适合作为主要实验对比组'],
  },
  {
    id: 'feedback',
    title: '反馈迭代引导',
    source: '成功样本 + 编译日志反馈',
    mechanism: '把成功样本作为结构种子，同时把编译失败和异常日志摘要加入下一轮 Prompt，驱动生成策略逐轮调整。',
    promptPreview:
      'Recent compiler feedback: preview feature parse conflict near nested switch label. Recent compiler feedback: type inference fails with generic record pattern...',
    outputPreview:
      'public class FeedbackCase { static <T> void run(T value) { switch (value) { ... } } }',
    highlights: ['体现“历史反馈知识”', '更贴近真实测试闭环', '适合后续差分测试样本挖掘'],
  },
]

export const experimentResults: ExperimentResult[] = [
  { mode: '示例/手工知识', generated: 1200, passed: 428, passRate: 35.7, diffFindings: 3 },
  { mode: '文档蒸馏', generated: 1200, passed: 561, passRate: 46.8, diffFindings: 5 },
  { mode: '反馈迭代', generated: 1200, passed: 638, passRate: 53.2, diffFindings: 7 },
]

export const testPointStats = [
  { label: 'finally', manual: 76, distill: 102, feedback: 118 },
  { label: 'instanceof', manual: 83, distill: 109, feedback: 125 },
  { label: 'synchronized', manual: 69, distill: 95, feedback: 112 },
  { label: 'record', manual: 88, distill: 121, feedback: 136 },
  { label: 'sealed', manual: 54, distill: 88, feedback: 101 },
]

export const testcaseShowcases: TestCaseShowcase[] = [
  {
    id: 'TC-001',
    testPoint: 'finally',
    mode: '示例/手工知识',
    status: 'PASS',
    promptSummary: '手工 Prompt 强调 try/finally、资源释放和现代语法组合。',
    code:
      'public class Case001 {\n  static int calc(int x) {\n    try {\n      return switch (x) {\n        case 0 -> 1;\n        default -> x + 1;\n      };\n    } finally {\n      System.out.println("cleanup");\n    }\n  }\n}',
    compilerLog: '[INFO] javac exit code = 0\n[INFO] sample accepted as valid testcase',
    diffSummary: '进入差分测试样本池。',
  },
  {
    id: 'TC-014',
    testPoint: 'instanceof',
    mode: '文档蒸馏',
    status: 'DIFF',
    promptSummary: '文档蒸馏 Prompt 强调模式匹配、泛型和嵌套控制流组合。',
    code:
      'record Box<T>(T value) {}\npublic class Case014 {\n  static int run(Object obj) {\n    if (obj instanceof Box<?> box && box.value() instanceof Integer v) {\n      return v;\n    }\n    return -1;\n  }\n}',
    compilerLog: '[INFO] javac-22: success\n[WARN] javac-21: preview parsing mismatch around pattern binding',
    diffSummary: '在不同 javac 版本间出现差异，已标记为重点样例。',
  },
  {
    id: 'TC-032',
    testPoint: 'synchronized',
    mode: '反馈迭代',
    status: 'FAIL',
    promptSummary: '上一轮日志提示“嵌套 switch + synchronized”附近出现解析冲突。',
    code:
      'public class Case032 {\n  final Object lock = new Object();\n  void run(int x) {\n    synchronized (lock) {\n      switch (x) {\n        case 0 -> System.out.println("zero");\n        default -> {\n          if (x > 2) System.out.println(x);\n        }\n      }\n    }\n  }\n}',
    compilerLog: '[ERROR] compiler feedback: preview feature parse conflict near nested block',
    diffSummary: '日志已回灌到下一轮 Prompt，继续迭代。',
  },
]

export const diffCases: DiffCase[] = [
  {
    id: 'DF-001',
    title: 'Pattern Matching Preview 差异',
    testPoint: 'instanceof',
    mode: '文档蒸馏',
    javacA: 'javac 22: 编译通过',
    javacB: 'javac 21: 预览特性报错',
    conclusion: '同一程序在不同版本的 preview 语义边界不同，需要进一步归类为版本敏感样例。',
    snippet:
      'if (obj instanceof Box<?> box && box.value() instanceof Integer v) {\n  return v;\n}',
  },
  {
    id: 'DF-002',
    title: '反馈迭代触发的嵌套控制流差异',
    testPoint: 'finally',
    mode: '反馈迭代',
    javacA: 'javac 22: 正常退出',
    javacB: 'javac 22-debug: 异常日志更详细',
    conclusion: '反馈迭代模式更容易构造包含复杂清理逻辑的边界样例，适合进一步做缺陷定位。',
    snippet:
      'try {\n  return switch (x) { case 0 -> 1; default -> x + 1; };\n} finally {\n  cleanup();\n}',
  },
]

export const materialPlaceholders = [
  '这里后续放系统架构图截图',
  '这里后续放 Prompt 演化截图',
  '这里后续放生成样例代码截图',
  '这里后续放差分测试对比截图',
]
