export type CaseStatus = 'SUCCESS' | 'COMPILE_ERROR' | 'CRASH'
export type ModuleKey = 'prompt' | 'code' | 'bugs' | 'runs' | 'upload'
export type UploadModuleKey = 'prompt' | 'code' | 'bugs'

export interface Feature {
  id: number
  name: string
  category: string
  version: string
  jvm_name: string
}

export interface PromptVersion {
  id: number
  feature_id: number
  version_no: string
  content: string
  module_scope?: ModuleKey
  metrics_snapshot: {
    coverage: number
    bugCount: number
  }
}

export interface TestCase {
  id: number
  prompt_version_id: number
  file_path: string
  status: CaseStatus
  coverage_score: number
  is_bug: boolean
  run_id: number
  artifact_root: string
  created_at: string
}

export interface BugRecord {
  id: number
  case_id: number
  feature_id: number
  description: string
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL'
}

export interface RunRecord {
  run_id: number
  feature_id: number
  jvm_name: string
  source: 'generate' | 'scan'
  created_at: string
  summary: {
    fileCount: number
    totalSizeMB: number
    errorCount: number
  }
}

export interface ArtifactFile {
  id: number
  run_id: number
  case_id?: number
  path: string
  key: string
  hash: string
  size: number
  type: 'code' | 'log' | 'coverage' | 'misc'
}

export interface NavTreeNode {
  id: string
  label: string
  nodeType: 'jvm' | 'feature' | 'module'
  jvmName?: string
  featureId?: number
  moduleKey?: ModuleKey
  coverage?: number
  bugCount?: number
  children?: NavTreeNode[]
}

export interface OverviewStats {
  totalFeatures: number
  totalCases: number
  totalBugs: number
  avgCoverage: number
}

export interface CaseDetail {
  code_content: string
  log_content: string
  coverage_html_url: string
}

export interface GenerateProgressEvent {
  percent: number
  message: string
}

export interface GenerateInput {
  feature_id: number
  prompt_version_id: number
}

export interface ScanArtifactsInput {
  feature_id: number
  server_path: string
}

export interface ScanArtifactsResult {
  run: RunRecord
  importedFiles: number
}

export interface RunFilesResult {
  total: number
  page: number
  pageSize: number
  items: ArtifactFile[]
}

export interface ModuleFileRecord {
  id: number
  feature_id: number
  module: UploadModuleKey
  file_name: string
  file_size: number
  mime_type: string
  file_content: string
  created_at: string
  run_image_name?: string
  run_image_mime_type?: string
  run_image_content?: string
}

const MODULES: Array<{ key: ModuleKey; label: string }> = [
  { key: 'prompt', label: 'Prompt' },
  { key: 'code', label: '代码' },
  { key: 'bugs', label: 'Bug' },
  { key: 'runs', label: '运行记录' },
  { key: 'upload', label: '上传' }
]

const featuresFallback: Feature[] = [
  { id: 1, name: 'Collections API', category: 'Core', version: 'Java 21', jvm_name: 'OpenJDK21' },
  { id: 2, name: 'Virtual Threads', category: 'Concurrency', version: 'Java 21', jvm_name: 'OpenJDK21' },
  { id: 3, name: 'Pattern Matching', category: 'Language', version: 'Java 22', jvm_name: 'OpenJDK22' },
  { id: 4, name: 'Foreign Memory API', category: 'Runtime', version: 'Java 22', jvm_name: 'OpenJDK22' },
  { id: 5, name: 'JIT Stability', category: 'Compiler', version: 'Java 21', jvm_name: 'GraalVM' },
  { id: 6, name: 'GC Barrier', category: 'Runtime', version: 'Java 17', jvm_name: 'OpenJ9' }
]

let featuresRemote: Feature[] = [
  { id: 1, name: 'Collections API', category: 'Core', version: 'Java 21', jvm_name: 'OpenJDK21' },
  { id: 2, name: 'Virtual Threads', category: 'Concurrency', version: 'Java 21', jvm_name: 'OpenJDK21' },
  { id: 3, name: 'Pattern Matching', category: 'Language', version: 'Java 22', jvm_name: 'OpenJDK22' },
  { id: 5, name: 'JIT Stability', category: 'Compiler', version: 'Java 21', jvm_name: 'GraalVM' }
]

let promptVersions: PromptVersion[] = [
  {
    id: 101,
    feature_id: 1,
    version_no: 'v1',
    module_scope: 'prompt',
    content: 'Generate boundary-value tests for Java Collections APIs.',
    metrics_snapshot: { coverage: 58, bugCount: 3 }
  },
  {
    id: 102,
    feature_id: 1,
    version_no: 'v2',
    module_scope: 'prompt',
    content: 'Add mutation-oriented cases and exception path validation.',
    metrics_snapshot: { coverage: 69, bugCount: 2 }
  },
  {
    id: 103,
    feature_id: 1,
    version_no: 'v3',
    module_scope: 'prompt',
    content: 'Bias generation toward hash collision and concurrent modification scenarios.',
    metrics_snapshot: { coverage: 78, bugCount: 1 }
  },
  {
    id: 201,
    feature_id: 2,
    version_no: 'v1',
    module_scope: 'prompt',
    content: 'Generate stress tests for virtual thread scheduling and cancellation.',
    metrics_snapshot: { coverage: 55, bugCount: 4 }
  }
]

let runRecords: RunRecord[] = [
  {
    run_id: 5001,
    feature_id: 1,
    jvm_name: 'OpenJDK21',
    source: 'generate',
    created_at: new Date(Date.now() - 1000 * 60 * 25).toISOString(),
    summary: { fileCount: 26, totalSizeMB: 12.4, errorCount: 1 }
  },
  {
    run_id: 5002,
    feature_id: 2,
    jvm_name: 'OpenJDK21',
    source: 'generate',
    created_at: new Date(Date.now() - 1000 * 60 * 14).toISOString(),
    summary: { fileCount: 31, totalSizeMB: 16.2, errorCount: 2 }
  }
]

let testCases: TestCase[] = [
  {
    id: 1001,
    prompt_version_id: 103,
    file_path: 'cases/collections/case_1001.java',
    status: 'SUCCESS',
    coverage_score: 91,
    is_bug: false,
    run_id: 5001,
    artifact_root: '/artifacts/runs/5001',
    created_at: new Date(Date.now() - 1000 * 60 * 24).toISOString()
  },
  {
    id: 1002,
    prompt_version_id: 103,
    file_path: 'cases/collections/case_1002.java',
    status: 'CRASH',
    coverage_score: 75,
    is_bug: true,
    run_id: 5001,
    artifact_root: '/artifacts/runs/5001',
    created_at: new Date(Date.now() - 1000 * 60 * 23).toISOString()
  },
  {
    id: 2001,
    prompt_version_id: 201,
    file_path: 'cases/threads/case_2001.java',
    status: 'CRASH',
    coverage_score: 61,
    is_bug: true,
    run_id: 5002,
    artifact_root: '/artifacts/runs/5002',
    created_at: new Date(Date.now() - 1000 * 60 * 13).toISOString()
  },
  {
    id: 2002,
    prompt_version_id: 201,
    file_path: 'cases/threads/case_2002.java',
    status: 'SUCCESS',
    coverage_score: 67,
    is_bug: false,
    run_id: 5002,
    artifact_root: '/artifacts/runs/5002',
    created_at: new Date(Date.now() - 1000 * 60 * 12).toISOString()
  }
]

let bugs: BugRecord[] = [
  {
    id: 1,
    case_id: 1002,
    feature_id: 1,
    description: 'ConcurrentModificationException not handled in iteration branch.',
    severity: 'HIGH'
  },
  {
    id: 2,
    case_id: 2001,
    feature_id: 2,
    description: 'Thread leak after interrupted shutdown path.',
    severity: 'CRITICAL'
  }
]

let artifactFiles: ArtifactFile[] = [
  {
    id: 9001,
    run_id: 5001,
    case_id: 1001,
    path: 'src/GeneratedCase1001.java',
    key: 'runs/5001/src/GeneratedCase1001.java',
    hash: 'sha1:6ac4e2',
    size: 1822,
    type: 'code'
  },
  {
    id: 9002,
    run_id: 5001,
    case_id: 1002,
    path: 'logs/case_1002.log',
    key: 'runs/5001/logs/case_1002.log',
    hash: 'sha1:99ca1d',
    size: 1024,
    type: 'log'
  },
  {
    id: 9003,
    run_id: 5002,
    case_id: 2001,
    path: 'coverage/index.html',
    key: 'runs/5002/coverage/index.html',
    hash: 'sha1:aa21bc',
    size: 23000,
    type: 'coverage'
  }
]

const fileContentMap = new Map<string, string>([
  ['runs/5001/src/GeneratedCase1001.java', 'public class GeneratedCase1001 {\n  public static void main(String[] args) {\n    System.out.println("ok");\n  }\n}'],
  ['runs/5001/logs/case_1002.log', '[INFO] compile begin\n[ERROR] ConcurrentModificationException\n[INFO] abort'],
  ['runs/5002/coverage/index.html', '<html><body><h1>Coverage 67%</h1></body></html>']
])

const MODULE_FILES_STORAGE_KEY = 'fuzz4all_module_files_v1'

let moduleFiles: ModuleFileRecord[] = []
let moduleFileSeed = 1

function loadModuleFilesFromStorage() {
  if (typeof localStorage === 'undefined') return
  try {
    const raw = localStorage.getItem(MODULE_FILES_STORAGE_KEY)
    if (!raw) return
    const parsed = JSON.parse(raw) as ModuleFileRecord[]
    if (!Array.isArray(parsed)) return
    moduleFiles = parsed
    moduleFileSeed = Math.max(1, ...parsed.map((item) => item.id + 1))
  } catch {
    moduleFiles = []
    moduleFileSeed = 1
  }
}

function persistModuleFiles() {
  if (typeof localStorage === 'undefined') return
  localStorage.setItem(MODULE_FILES_STORAGE_KEY, JSON.stringify(moduleFiles))
}

loadModuleFilesFromStorage()

function wait(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

function mergedFeatures() {
  const map = new Map<number, Feature>()
  for (const item of featuresFallback) map.set(item.id, item)
  for (const item of featuresRemote) map.set(item.id, item)
  return Array.from(map.values())
}

function getPromptVersionsByFeatureSync(featureId: number) {
  return promptVersions
    .filter((item) => item.feature_id === featureId)
    .sort((a, b) => Number(a.version_no.slice(1)) - Number(b.version_no.slice(1)))
}

function latestVersion(featureId: number) {
  return getPromptVersionsByFeatureSync(featureId).at(-1)
}

function metricByFeature(featureId: number) {
  const v = latestVersion(featureId)
  if (!v) return { coverage: 0, bugCount: 0 }
  return v.metrics_snapshot
}

function buildNavTree(features: Feature[]): NavTreeNode[] {
  const jvmMap = new Map<string, NavTreeNode>()
  for (const feature of features) {
    if (!jvmMap.has(feature.jvm_name)) {
      jvmMap.set(feature.jvm_name, {
        id: `jvm:${feature.jvm_name}`,
        label: feature.jvm_name,
        nodeType: 'jvm',
        jvmName: feature.jvm_name,
        children: []
      })
    }

    const metrics = metricByFeature(feature.id)
    const featureNode: NavTreeNode = {
      id: `feature:${feature.id}`,
      label: `${feature.name} (${feature.version})`,
      nodeType: 'feature',
      featureId: feature.id,
      jvmName: feature.jvm_name,
      coverage: metrics.coverage,
      bugCount: metrics.bugCount,
      children: MODULES.map((module) => ({
        id: `module:${feature.id}:${module.key}`,
        label: module.label,
        nodeType: 'module',
        featureId: feature.id,
        jvmName: feature.jvm_name,
        moduleKey: module.key
      }))
    }

    jvmMap.get(feature.jvm_name)?.children?.push(featureNode)
  }

  return Array.from(jvmMap.values())
}

function featureName(featureId: number) {
  const f = mergedFeatures().find((item) => item.id === featureId)
  return f ? f.name : `Feature-${featureId}`
}

export async function getNavTree() {
  await wait(200)
  return buildNavTree(mergedFeatures())
}

export async function getOverviewStats(params?: { jvm?: string; featureId?: number }): Promise<OverviewStats> {
  await wait(120)
  const features = mergedFeatures()
  let featureIds = features.map((item) => item.id)

  if (params?.jvm) {
    featureIds = features.filter((item) => item.jvm_name === params.jvm).map((item) => item.id)
  }

  if (params?.featureId) {
    featureIds = [params.featureId]
  }

  const versionIds = promptVersions.filter((item) => featureIds.includes(item.feature_id)).map((item) => item.id)
  const filteredCases = testCases.filter((item) => versionIds.includes(item.prompt_version_id))
  const filteredBugs = bugs.filter((item) => featureIds.includes(item.feature_id))

  const avgCoverage = filteredCases.length
    ? Math.round(filteredCases.reduce((acc, item) => acc + item.coverage_score, 0) / filteredCases.length)
    : 0

  return {
    totalFeatures: featureIds.length,
    totalCases: filteredCases.length,
    totalBugs: filteredBugs.length,
    avgCoverage
  }
}

export async function getPromptVersionsByFeature(featureId: number) {
  await wait(100)
  return getPromptVersionsByFeatureSync(featureId)
}

export async function updatePromptVersion(versionId: number, content: string) {
  await wait(80)
  const target = promptVersions.find((item) => item.id === versionId)
  if (!target) throw new Error('Prompt version not found')
  target.content = content
}

export async function getCasesByPromptVersion(promptVersionId: number) {
  await wait(120)
  return testCases
    .filter((item) => item.prompt_version_id === promptVersionId)
    .sort((a, b) => (a.created_at > b.created_at ? -1 : 1))
}

export async function getRecentCasesByFeature(featureId: number, limit = 20) {
  await wait(120)
  const versionIds = promptVersions.filter((item) => item.feature_id === featureId).map((item) => item.id)
  return testCases
    .filter((item) => versionIds.includes(item.prompt_version_id))
    .sort((a, b) => (a.created_at > b.created_at ? -1 : 1))
    .slice(0, limit)
}

export async function getBugsByFeature(featureId: number) {
  await wait(100)
  return bugs.filter((item) => item.feature_id === featureId)
}

export async function getCaseDetail(id: number): Promise<CaseDetail> {
  await wait(120)
  const targetCase = testCases.find((item) => item.id === id)
  if (!targetCase) throw new Error('Case not found')

  const bug = bugs.find((item) => item.case_id === id)
  return {
    code_content: `import java.util.*;\n\npublic class GeneratedCase${id} {\n  public static void main(String[] args) {\n    List<String> data = new ArrayList<>();\n    data.add("seed");\n    for (String item : data) {\n      if (item.isEmpty()) {\n        throw new IllegalStateException("unexpected empty item");\n      }\n    }\n    System.out.println("status=${targetCase.status}");\n  }\n}`,
    log_content: bug
      ? `[INFO] run ${id}\n[WARN] unstable branch\n[ERROR] ${bug.description}\n[INFO] severity=${bug.severity}`
      : `[INFO] run ${id}\n[INFO] build ok\n[INFO] execute done`,
    coverage_html_url: `https://coverage.local/cases/${id}/index.html`
  }
}

export async function getRunsByFeature(featureId: number) {
  await wait(100)
  return runRecords
    .filter((item) => item.feature_id === featureId)
    .sort((a, b) => (a.created_at > b.created_at ? -1 : 1))
}

export async function getRunFiles(params: { run_id: number; page: number; pageSize: number; keyword?: string }): Promise<RunFilesResult> {
  await wait(140)
  const keyword = params.keyword?.trim().toLowerCase() || ''
  let items = artifactFiles.filter((item) => item.run_id === params.run_id)
  if (keyword) items = items.filter((item) => item.path.toLowerCase().includes(keyword) || item.type.toLowerCase().includes(keyword))

  const total = items.length
  const start = (params.page - 1) * params.pageSize
  const end = start + params.pageSize
  return {
    total,
    page: params.page,
    pageSize: params.pageSize,
    items: items.slice(start, end)
  }
}

export async function getRunFileContent(fileKey: string) {
  await wait(80)
  return fileContentMap.get(fileKey) || `content of ${fileKey}`
}

export async function getModuleFiles(featureId: number, module: UploadModuleKey) {
  await wait(80)
  return moduleFiles
    .filter((item) => item.feature_id === featureId && item.module === module)
    .sort((a, b) => (a.created_at > b.created_at ? -1 : 1))
}

export async function uploadModuleFile(input: {
  feature_id: number
  module: UploadModuleKey
  file_name: string
  file_size: number
  mime_type: string
  file_content: string
}) {
  await wait(120)
  const record: ModuleFileRecord = {
    id: moduleFileSeed++,
    feature_id: input.feature_id,
    module: input.module,
    file_name: input.file_name,
    file_size: input.file_size,
    mime_type: input.mime_type,
    file_content: input.file_content,
    created_at: new Date().toISOString()
  }
  moduleFiles = [record, ...moduleFiles]
  persistModuleFiles()
  return record
}

export async function getModuleFileById(id: number) {
  await wait(60)
  return moduleFiles.find((item) => item.id === id) || null
}

export async function uploadModuleRunImage(input: {
  id: number
  image_name: string
  image_mime_type: string
  image_content: string
}) {
  await wait(90)
  const record = moduleFiles.find((item) => item.id === input.id)
  if (!record) throw new Error('file not found')
  record.run_image_name = input.image_name
  record.run_image_mime_type = input.image_mime_type
  record.run_image_content = input.image_content
  persistModuleFiles()
  return record
}

export async function scanArtifacts(input: ScanArtifactsInput): Promise<ScanArtifactsResult> {
  await wait(650)
  const feature = mergedFeatures().find((item) => item.id === input.feature_id)
  if (!feature) throw new Error('Feature not found')

  const nextRunId = Math.max(...runRecords.map((item) => item.run_id), 5000) + 1
  const fileCount = 120
  const run: RunRecord = {
    run_id: nextRunId,
    feature_id: input.feature_id,
    jvm_name: feature.jvm_name,
    source: 'scan',
    created_at: new Date().toISOString(),
    summary: {
      fileCount,
      totalSizeMB: 43.5,
      errorCount: 4
    }
  }

  runRecords = [run, ...runRecords]

  const newFiles: ArtifactFile[] = []
  const startId = Math.max(...artifactFiles.map((item) => item.id), 9000) + 1
  for (let idx = 0; idx < fileCount; idx += 1) {
    const id = startId + idx
    const isLog = idx % 5 === 0
    const rel = isLog ? `logs/scan_${idx}.log` : `src/generated_${idx}.java`
    const key = `runs/${nextRunId}/${rel}`
    newFiles.push({
      id,
      run_id: nextRunId,
      path: rel,
      key,
      hash: `sha1:${id.toString(16)}`,
      size: isLog ? 1800 : 2400,
      type: isLog ? 'log' : 'code'
    })

    fileContentMap.set(
      key,
      isLog
        ? `[INFO] scan from ${input.server_path}\n${idx % 15 === 0 ? '[ERROR] simulated compilation error' : '[INFO] no critical error'}`
        : `public class Imported_${idx} {\n  public static void main(String[] args) {\n    System.out.println("from scan ${nextRunId}");\n  }\n}`
    )
  }

  artifactFiles = [...newFiles, ...artifactFiles]

  return { run, importedFiles: newFiles.length }
}

export async function postGenerate(input: GenerateInput, onProgress: (event: GenerateProgressEvent) => void) {
  const progressPlan = [
    { percent: 18, message: '解析 Prompt...' },
    { percent: 42, message: '生成测试样例...' },
    { percent: 66, message: '编译并执行...' },
    { percent: 89, message: '归档产物并写入索引...' },
    { percent: 100, message: '完成。' }
  ]

  for (const step of progressPlan) {
    await wait(420)
    onProgress(step)
  }

  const baseVersion = promptVersions.find((item) => item.id === input.prompt_version_id && item.feature_id === input.feature_id)
  if (!baseVersion) throw new Error('Prompt version not found')

  const feature = mergedFeatures().find((item) => item.id === input.feature_id)
  if (!feature) throw new Error('Feature not found')

  const versions = getPromptVersionsByFeatureSync(input.feature_id)
  const nextNo = versions.length + 1
  const nextVersionId = Math.max(...promptVersions.map((item) => item.id), 100) + 1

  const newVersion: PromptVersion = {
    id: nextVersionId,
    feature_id: input.feature_id,
    version_no: `v${nextNo}`,
    module_scope: 'prompt',
    content: `${baseVersion.content}\nRefine for ${feature.name} @ ${new Date().toLocaleTimeString()}`,
    metrics_snapshot: {
      coverage: Math.min(97, baseVersion.metrics_snapshot.coverage + 4),
      bugCount: Math.max(0, baseVersion.metrics_snapshot.bugCount - 1)
    }
  }
  promptVersions = [...promptVersions, newVersion]

  const nextRunId = Math.max(...runRecords.map((item) => item.run_id), 5000) + 1
  const run: RunRecord = {
    run_id: nextRunId,
    feature_id: input.feature_id,
    jvm_name: feature.jvm_name,
    source: 'generate',
    created_at: new Date().toISOString(),
    summary: {
      fileCount: 8,
      totalSizeMB: 3.2,
      errorCount: newVersion.metrics_snapshot.bugCount > 0 ? 1 : 0
    }
  }
  runRecords = [run, ...runRecords]

  const caseStartId = Math.max(...testCases.map((item) => item.id), 1000) + 1
  const newCases: TestCase[] = [
    {
      id: caseStartId,
      prompt_version_id: newVersion.id,
      file_path: `cases/${feature.name.toLowerCase().replace(/\s+/g, '_')}/case_${caseStartId}.java`,
      status: 'SUCCESS',
      coverage_score: Math.min(100, newVersion.metrics_snapshot.coverage + 4),
      is_bug: false,
      run_id: nextRunId,
      artifact_root: `/artifacts/runs/${nextRunId}`,
      created_at: new Date().toISOString()
    },
    {
      id: caseStartId + 1,
      prompt_version_id: newVersion.id,
      file_path: `cases/${feature.name.toLowerCase().replace(/\s+/g, '_')}/case_${caseStartId + 1}.java`,
      status: newVersion.metrics_snapshot.bugCount > 0 ? 'CRASH' : 'SUCCESS',
      coverage_score: Math.max(40, newVersion.metrics_snapshot.coverage - 10),
      is_bug: newVersion.metrics_snapshot.bugCount > 0,
      run_id: nextRunId,
      artifact_root: `/artifacts/runs/${nextRunId}`,
      created_at: new Date().toISOString()
    }
  ]
  testCases = [...newCases, ...testCases]

  const fileStartId = Math.max(...artifactFiles.map((item) => item.id), 9000) + 1
  const genFiles: ArtifactFile[] = [
    {
      id: fileStartId,
      run_id: nextRunId,
      case_id: caseStartId,
      path: `src/case_${caseStartId}.java`,
      key: `runs/${nextRunId}/src/case_${caseStartId}.java`,
      hash: `sha1:${fileStartId.toString(16)}`,
      size: 2200,
      type: 'code'
    },
    {
      id: fileStartId + 1,
      run_id: nextRunId,
      case_id: caseStartId + 1,
      path: `logs/case_${caseStartId + 1}.log`,
      key: `runs/${nextRunId}/logs/case_${caseStartId + 1}.log`,
      hash: `sha1:${(fileStartId + 1).toString(16)}`,
      size: 1300,
      type: 'log'
    }
  ]
  artifactFiles = [...genFiles, ...artifactFiles]

  const firstGeneratedFile = genFiles.at(0)
  const secondGeneratedFile = genFiles.at(1)
  const secondCase = newCases.at(1)

  if (firstGeneratedFile) {
    fileContentMap.set(
      firstGeneratedFile.key,
      `public class Case_${caseStartId} {\n  public static void main(String[] args) {\n    System.out.println("generated");\n  }\n}`
    )
  }

  if (secondGeneratedFile && secondCase) {
    fileContentMap.set(
      secondGeneratedFile.key,
      secondCase.is_bug ? '[INFO] execute\n[ERROR] simulated crash from generated case' : '[INFO] execute\n[INFO] done'
    )
  }

  if (secondCase?.is_bug) {
    const nextBugId = Math.max(...bugs.map((item) => item.id), 0) + 1
    bugs = [
      {
        id: nextBugId,
        case_id: secondCase.id,
        feature_id: input.feature_id,
        description: `Generated run ${nextRunId} revealed unstable branch in ${feature.name}.`,
        severity: 'MEDIUM'
      },
      ...bugs
    ]
  }

  return { newVersion, run, newCases }
}

export async function getTrendStats(featureId: number) {
  await wait(100)
  const versions = getPromptVersionsByFeatureSync(featureId)
  return versions.map((item) => ({
    version: item.version_no,
    coverage: item.metrics_snapshot.coverage,
    bugs: item.metrics_snapshot.bugCount
  }))
}

export async function getBugDistributionByFeature(featureId: number) {
  await wait(100)
  const buckets: Record<'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL', number> = {
    LOW: 0,
    MEDIUM: 0,
    HIGH: 0,
    CRITICAL: 0
  }

  for (const bug of bugs.filter((item) => item.feature_id === featureId)) {
    buckets[bug.severity] += 1
  }

  return buckets
}
