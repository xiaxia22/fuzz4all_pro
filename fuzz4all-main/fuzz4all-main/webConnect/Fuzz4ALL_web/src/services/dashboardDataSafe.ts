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
  { label: 'Compiler Target', value: 'javac', note: 'JVM compiler oriented testcase generation' },
  { label: 'Knowledge Modes', value: '3', note: 'Manual seeds, document distillation, feedback iteration' },
  { label: 'Test Points', value: '5+', note: 'finally, instanceof, synchronized, record, sealed' },
  { label: 'Diff Stage', value: '2', note: 'Compile filtering first, cross-version comparison second' },
]

export const workflowSteps = [
  'Collect prompt seeds, example programs, standard documents, and compiler feedback.',
  'Construct or distill prompts for the chosen javac test point.',
  'Use Qwen2.5 to generate Java test programs.',
  'Compile generated programs with javac and record valid samples plus logs.',
  'Feed valid samples and feedback back into the next prompt.',
  'Organize final valid samples and run differential testing.',
]

export const contributionPoints = [
  'Extend the original Fuzz4All workflow toward a javac focused testing scenario.',
  'Implement three knowledge-guided prompt generation modes in one pipeline.',
  'Bring compiler logs and historical execution feedback into prompt updates.',
  'Add testcase organization and differential-analysis oriented presentation pages.',
]

export const knowledgeModes: KnowledgeMode[] = [
  {
    id: 'manual',
    title: 'Manual Seed Guidance',
    source: 'Hand-written prompt plus example code',
    mechanism:
      'Human-written prompts and representative Java samples are merged into an initial structured prompt so the model starts from a stable syntax prior.',
    promptPreview:
      'Generate short but non-trivial Java programs for testing javac. Prefer records, pattern matching, lambdas, generics, switch expressions, and try/finally interactions.',
    outputPreview:
      'record Pair<T>(T left, T right) {} class SeedCase { static int f(Pair<Integer> p) { return p.left(); } }',
    highlights: ['Fast baseline', 'Controllable style', 'Maps to source-code knowledge'],
  },
  {
    id: 'distill',
    title: 'Document Distillation Guidance',
    source: 'Java standard documents plus DeepSeek distillation',
    mechanism:
      'Java documents are summarized into syntax patterns, boundary combinations, and compiler sensitive constructs, then candidate prompts are scored to choose the best one.',
    promptPreview:
      'Use modern Java features in compact but valid ways. Focus on records, sealed hierarchies, pattern matching, nested switch expressions, and interactions between control flow and type inference.',
    outputPreview:
      'sealed interface Expr permits Lit, Add {} record Lit(int v) implements Expr {} record Add(Expr l, Expr r) implements Expr {}',
    highlights: ['Document-guided generation', 'Test-point targeting', 'Best prompt selection'],
  },
  {
    id: 'feedback',
    title: 'Feedback Iteration Guidance',
    source: 'Valid samples plus compiler log feedback',
    mechanism:
      'Valid samples become structural seeds while failure logs and compiler anomalies are summarized into the next-round prompt, enabling iterative prompt refinement.',
    promptPreview:
      'Recent compiler feedback: preview feature parse conflict near nested switch label. Recent compiler feedback: type inference fails with generic record pattern.',
    outputPreview:
      'public class FeedbackCase { static <T> void run(T value) { switch (value) { default -> System.out.println(value); } } }',
    highlights: ['History-aware generation', 'Closed-loop workflow', 'Good for later diff testing'],
  },
]

export const experimentResults: ExperimentResult[] = [
  { mode: 'Manual Seeds', generated: 1200, passed: 428, passRate: 35.7, diffFindings: 3 },
  { mode: 'Document Distillation', generated: 1200, passed: 561, passRate: 46.8, diffFindings: 5 },
  { mode: 'Feedback Iteration', generated: 1200, passed: 638, passRate: 53.2, diffFindings: 7 },
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
    mode: 'Manual Seeds',
    status: 'PASS',
    promptSummary: 'Manual prompt emphasizes try/finally, cleanup logic, and modern syntax composition.',
    code:
      'public class Case001 {\n  static int calc(int x) {\n    try {\n      return switch (x) {\n        case 0 -> 1;\n        default -> x + 1;\n      };\n    } finally {\n      System.out.println("cleanup");\n    }\n  }\n}',
    compilerLog: '[INFO] javac exit code = 0\n[INFO] sample accepted as valid testcase',
    diffSummary: 'Moved into the diff-testing sample pool.',
  },
  {
    id: 'TC-014',
    testPoint: 'instanceof',
    mode: 'Document Distillation',
    status: 'DIFF',
    promptSummary: 'Distilled prompt emphasizes pattern matching, generics, and nested control flow.',
    code:
      'record Box<T>(T value) {}\npublic class Case014 {\n  static int run(Object obj) {\n    if (obj instanceof Box<?> box && box.value() instanceof Integer v) {\n      return v;\n    }\n    return -1;\n  }\n}',
    compilerLog: '[INFO] javac-22: success\n[WARN] javac-21: preview parsing mismatch around pattern binding',
    diffSummary: 'Observed version-dependent behavior and marked as a key diff sample.',
  },
  {
    id: 'TC-032',
    testPoint: 'synchronized',
    mode: 'Feedback Iteration',
    status: 'FAIL',
    promptSummary: 'The previous round mentioned a parsing conflict near nested switch plus synchronized blocks.',
    code:
      'public class Case032 {\n  final Object lock = new Object();\n  void run(int x) {\n    synchronized (lock) {\n      switch (x) {\n        case 0 -> System.out.println("zero");\n        default -> {\n          if (x > 2) System.out.println(x);\n        }\n      }\n    }\n  }\n}',
    compilerLog: '[ERROR] compiler feedback: preview feature parse conflict near nested block',
    diffSummary: 'Compiler feedback is fed back into the next prompt update.',
  },
]

export const diffCases: DiffCase[] = [
  {
    id: 'DF-001',
    title: 'Pattern Matching Preview Difference',
    testPoint: 'instanceof',
    mode: 'Document Distillation',
    javacA: 'javac 22: compile success',
    javacB: 'javac 21: preview feature warning or rejection',
    conclusion:
      'The same program behaves differently across compiler versions near the preview semantics boundary, so it should be classified as a version-sensitive sample.',
    snippet:
      'if (obj instanceof Box<?> box && box.value() instanceof Integer v) {\n  return v;\n}',
  },
  {
    id: 'DF-002',
    title: 'Nested Control-flow Case Triggered by Feedback Iteration',
    testPoint: 'finally',
    mode: 'Feedback Iteration',
    javacA: 'javac 22: normal exit',
    javacB: 'javac 22-debug: richer anomaly log',
    conclusion:
      'Feedback iteration is more likely to construct boundary samples with complex cleanup logic, making it useful for later root-cause inspection.',
    snippet:
      'try {\n  return switch (x) { case 0 -> 1; default -> x + 1; };\n} finally {\n  cleanup();\n}',
  },
]

export const materialPlaceholders = [
  'Replace with architecture diagram screenshot',
  'Replace with prompt evolution screenshot',
  'Replace with generated testcase screenshot',
  'Replace with differential testing comparison screenshot',
]
