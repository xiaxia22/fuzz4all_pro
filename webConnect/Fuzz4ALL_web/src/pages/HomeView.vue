<template>
  <div class="home-view">
    <el-row :gutter="14" class="top-grid">
      <el-col :span="5" class="panel-col">
        <el-card class="panel" shadow="never">
          <template #header>
            <div class="panel-title">JVM / 特性 / 模块</div>
          </template>

          <el-tree
            :data="navTree"
            node-key="id"
            default-expand-all
            :expand-on-click-node="false"
            :props="treeProps"
            highlight-current
            @node-click="handleTreeClick"
          >
            <template #default="{ data }">
              <div class="tree-row">
                <span class="tree-label">{{ data.label }}</span>
                <template v-if="data.nodeType === 'feature'">
                  <el-tag size="small" type="danger">Bug {{ data.bugCount ?? 0 }}</el-tag>
                  <el-tag size="small" type="success">{{ data.coverage ?? 0 }}%</el-tag>
                </template>
              </div>
            </template>
          </el-tree>
        </el-card>
      </el-col>

      <el-col :span="11" class="panel-col">
        <el-card class="panel" shadow="never">
          <template #header>
            <div class="panel-title panel-inline">
              <span>{{ moduleTitle }}</span>
              <el-tag type="info">{{ selectedJvmName || '-' }} / {{ selectedFeatureName || '-' }}</el-tag>
            </div>
          </template>

          <section v-if="selectedModule === 'prompt'" class="module-wrap">
            <el-steps :active="selectedVersionIndex" finish-status="success" align-center>
              <el-step v-for="version in promptVersions" :key="version.id" :title="version.version_no" />
            </el-steps>

            <div class="version-switch">
              <el-button
                v-for="(version, idx) in promptVersions"
                :key="version.id"
                size="small"
                :type="selectedVersionIndex === idx ? 'primary' : 'default'"
                @click="selectVersion(idx)"
              >
                {{ version.version_no }}
              </el-button>
            </div>

            <div class="actions-row">
              <input ref="moduleFileUploadInput" type="file" style="display: none" @change="uploadLocalModuleFile" />
              <el-button type="primary" :disabled="!selectedFeatureId" @click="triggerModuleFileUpload">上传本地 Prompt 文件</el-button>
              <el-button type="primary" :disabled="!selectedFeatureId" @click="reloadCurrentFeature">
                刷新展示
              </el-button>
              <span class="progress-text">Prompt 文件上传后入库，再在前端列表展示。</span>
            </div>

            <el-table :data="moduleFiles" border height="470" v-loading="moduleFilesLoading">
              <el-table-column prop="id" label="ID" width="80" />
              <el-table-column prop="file_name" label="文件名" min-width="220" />
              <el-table-column label="大小" width="120">
                <template #default="scope">{{ formatFileSize(scope.row.file_size) }}</template>
              </el-table-column>
              <el-table-column label="上传时间" min-width="180">
                <template #default="scope">{{ formatTime(scope.row.created_at) }}</template>
              </el-table-column>
              <el-table-column label="操作" width="100">
                <template #default="scope">
                  <el-button link type="primary" @click="openModuleFile(scope.row)">查看</el-button>
                </template>
              </el-table-column>
            </el-table>
          </section>

          <section v-else-if="selectedModule === 'code'" class="module-wrap">
            <el-alert title="代码模块：本地文件上传入库后表格展示，支持打开查看代码。" type="info" show-icon :closable="false" />
            <div class="actions-row">
              <input ref="moduleFileUploadInput" type="file" style="display: none" @change="uploadLocalModuleFile" />
              <el-button type="primary" :disabled="!selectedFeatureId" @click="triggerModuleFileUpload">上传本地代码文件</el-button>
            </div>
            <el-table :data="moduleFiles" border height="470" style="margin-top: 10px" v-loading="moduleFilesLoading">
              <el-table-column prop="id" label="ID" width="80" />
              <el-table-column prop="file_name" label="文件名" min-width="260" />
              <el-table-column label="大小" width="120">
                <template #default="scope">{{ formatFileSize(scope.row.file_size) }}</template>
              </el-table-column>
              <el-table-column label="上传时间" min-width="180">
                <template #default="scope">{{ formatTime(scope.row.created_at) }}</template>
              </el-table-column>
              <el-table-column label="操作" width="100">
                <template #default="scope">
                  <el-button link type="primary" @click="openModuleFile(scope.row)">查看</el-button>
                </template>
              </el-table-column>
            </el-table>
          </section>

          <section v-else-if="selectedModule === 'bugs'" class="module-wrap">
            <el-alert title="Bug 模块：与代码同结构，并增加“运行图片详情”列。" type="warning" show-icon :closable="false" />
            <div class="actions-row">
              <input ref="moduleFileUploadInput" type="file" style="display: none" @change="uploadLocalModuleFile" />
              <el-button type="primary" :disabled="!selectedFeatureId" @click="triggerModuleFileUpload">上传本地Bug文件</el-button>
            </div>
            <el-table :data="moduleFiles" border height="470" style="margin-top: 10px" v-loading="moduleFilesLoading">
              <el-table-column prop="id" label="ID" width="80" />
              <el-table-column prop="file_name" label="文件名" min-width="220" />
              <el-table-column label="大小" width="120">
                <template #default="scope">{{ formatFileSize(scope.row.file_size) }}</template>
              </el-table-column>
              <el-table-column label="上传时间" min-width="180">
                <template #default="scope">{{ formatTime(scope.row.created_at) }}</template>
              </el-table-column>
              <el-table-column label="运行图片详情" width="210">
                <template #default="scope">
                  <input type="file" accept="image/*" @change="uploadBugRunImage(scope.row, $event)" />
                  <el-button link type="primary" @click="viewRunImage(scope.row)">查看图片</el-button>
                </template>
              </el-table-column>
              <el-table-column label="操作" width="100">
                <template #default="scope">
                  <el-button link type="primary" @click="openModuleFile(scope.row)">查看</el-button>
                </template>
              </el-table-column>
            </el-table>
          </section>

          <section v-else-if="selectedModule === 'runs'" class="module-wrap">
            <el-row :gutter="10">
              <el-col :span="11">
                <div class="mini-title">运行批次时间线</div>
                <el-timeline class="timeline-box">
                  <el-timeline-item
                    v-for="run in runRecords"
                    :key="run.run_id"
                    :timestamp="formatTime(run.created_at)"
                    :type="selectedRunId === run.run_id ? 'primary' : 'info'"
                    placement="top"
                  >
                    <div class="run-item" @click="selectRun(run.run_id)">
                      <div>Run #{{ run.run_id }} · {{ run.source }}</div>
                      <div class="run-meta">{{ run.summary.fileCount }} files / {{ run.summary.totalSizeMB }} MB / error {{ run.summary.errorCount }}</div>
                    </div>
                  </el-timeline-item>
                </el-timeline>
              </el-col>

              <el-col :span="13">
                <div class="mini-title">文件索引（分页）</div>
                <div class="files-tools">
                  <el-input v-model="fileKeyword" placeholder="过滤文件名或类型" clearable @change="queryRunFiles(1)" />
                </div>
                <el-table :data="runFiles" border height="330">
                  <el-table-column prop="path" label="路径" min-width="180" />
                  <el-table-column prop="type" label="类型" width="90" />
                  <el-table-column prop="size" label="大小" width="90" />
                  <el-table-column label="查看" width="90">
                    <template #default="scope">
                      <el-button link type="primary" @click="openRunFile(scope.row)">打开</el-button>
                    </template>
                  </el-table-column>
                </el-table>
                <el-pagination
                  v-model:current-page="filePage"
                  v-model:page-size="filePageSize"
                  :total="fileTotal"
                  :page-sizes="[50, 100]"
                  layout="total, sizes, prev, pager, next"
                  @change="queryRunFiles(filePage)"
                />
              </el-col>
            </el-row>
          </section>

          <section v-else-if="selectedModule === 'upload'" class="module-wrap">
            <el-alert title="上传模块：第一版采用服务端扫描路径" type="success" show-icon :closable="false" />
            <el-form label-position="top" style="margin-top: 10px">
              <el-form-item label="服务器目录路径">
                <el-input v-model="scanPath" placeholder="例如: /data/fuzz4all/runs/2026-03-25" />
              </el-form-item>
              <el-button type="primary" :loading="scanLoading" @click="scanPathSubmit">扫描并入库</el-button>
              <span class="progress-text">{{ scanMessage }}</span>
            </el-form>
            <el-descriptions v-if="lastScanRun" border :column="2" style="margin-top: 10px">
              <el-descriptions-item label="Run ID">{{ lastScanRun.run_id }}</el-descriptions-item>
              <el-descriptions-item label="来源">{{ lastScanRun.source }}</el-descriptions-item>
              <el-descriptions-item label="文件数">{{ lastScanRun.summary.fileCount }}</el-descriptions-item>
              <el-descriptions-item label="总大小(MB)">{{ lastScanRun.summary.totalSizeMB }}</el-descriptions-item>
            </el-descriptions>
          </section>

          <section v-else class="module-wrap empty-tip">
            请选择左侧模块节点。
          </section>
        </el-card>
      </el-col>

      <el-col :span="8" class="panel-col">
        <el-card class="panel" shadow="never">
          <template #header>
            <div class="panel-title">实时结果流（当前特性）</div>
          </template>

          <el-scrollbar class="cases-scroll">
            <div v-for="item in recentCases" :key="item.id" class="case-card" @click="openCase(item)">
              <div class="case-head">
                <span class="case-file">{{ item.file_path }}</span>
                <el-tag :type="statusTagType(item.status)">{{ statusText(item.status) }}</el-tag>
              </div>
              <div class="case-sub">Run #{{ item.run_id }} · {{ formatTime(item.created_at) }}</div>
              <el-progress :percentage="item.coverage_score" :text-inside="true" :stroke-width="14" />
            </div>
          </el-scrollbar>
        </el-card>
      </el-col>
    </el-row>

    <el-card class="dashboard-panel" shadow="never">
      <template #header>
        <div class="panel-title">统计看板</div>
      </template>

      <div class="overview-stats">
        <el-statistic title="特性数" :value="overview.totalFeatures" />
        <el-statistic title="用例总数" :value="overview.totalCases" />
        <el-statistic title="缺陷总数" :value="overview.totalBugs" />
        <el-statistic title="平均覆盖率" :value="overview.avgCoverage" suffix="%" />
      </div>

      <el-row :gutter="14">
        <el-col :span="14">
          <div ref="trendChartRef" class="chart-box"></div>
        </el-col>
        <el-col :span="10">
          <div ref="bugChartRef" class="chart-box"></div>
        </el-col>
      </el-row>
    </el-card>

    <el-dialog v-model="detailVisible" title="用例详情" width="80%" destroy-on-close>
      <div class="detail-grid">
        <div class="code-pane">
          <h4>Java 代码</h4>
          <pre class="code-block"><code class="language-java" v-html="highlightedCode"></code></pre>
        </div>
        <div class="log-pane">
          <h4>控制台日志</h4>
          <div class="log-block">
            <p v-for="(line, idx) in logLines" :key="idx" :class="{ 'err-line': isErrorLine(line) }">{{ line }}</p>
          </div>
          <el-link type="primary" :href="caseDetail.coverage_html_url" target="_blank">打开覆盖率报告</el-link>
        </div>
      </div>
    </el-dialog>

    <el-dialog v-model="runFileVisible" title="文件内容" width="70%">
      <pre class="code-block"><code v-html="highlightedRunFile"></code></pre>
    </el-dialog>

    <el-dialog v-model="fileViewerVisible" :title="fileViewerTitle || '文件详情'" width="70%">
      <img v-if="fileViewerImage" :src="fileViewerImage" class="preview-image" />
      <pre v-else class="code-block"><code>{{ fileViewerText }}</code></pre>
    </el-dialog>

    <el-dialog v-model="runImageVisible" :title="runImageTitle || '运行图片详情'" width="70%">
      <img v-if="runImageUrl" :src="runImageUrl" class="preview-image" />
      <div v-else class="empty-tip">暂无运行图片</div>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref } from 'vue'
import { ElMessage } from 'element-plus'
import * as echarts from 'echarts'
import Prism from 'prismjs'
import 'prismjs/components/prism-java'
import 'prismjs/themes/prism.css'
import {
  getBugDistributionByFeature,
  getBugsByFeature,
  getCaseDetail,
  getCasesByPromptVersion,
  getNavTree,
  getOverviewStats,
  getPromptVersionsByFeature,
  getRecentCasesByFeature,
  getRunFileContent,
  getRunFiles,
  getRunsByFeature,
  getModuleFiles,
  getModuleFileById,
  getTrendStats,
  scanArtifacts,
  uploadModuleFile,
  uploadModuleRunImage,
  type ArtifactFile,
  type BugRecord,
  type CaseStatus,
  type ModuleFileRecord,
  type ModuleKey,
  type NavTreeNode,
  type OverviewStats,
  type PromptVersion,
  type RunRecord,
  type TestCase,
  type UploadModuleKey
} from '../services/dataService'

const treeProps = { label: 'label', children: 'children' }

const navTree = ref<NavTreeNode[]>([])
const selectedFeatureId = ref<number | null>(null)
const selectedFeatureName = ref('')
const selectedJvmName = ref('')
const selectedModule = ref<ModuleKey | null>(null)

const promptVersions = ref<PromptVersion[]>([])
const selectedVersionIndex = ref(0)
const editablePrompt = ref('')
const moduleFiles = ref<ModuleFileRecord[]>([])
const moduleFilesLoading = ref(false)
const fileViewerVisible = ref(false)
const fileViewerTitle = ref('')
const fileViewerText = ref('')
const fileViewerImage = ref('')
const runImageVisible = ref(false)
const runImageTitle = ref('')
const runImageUrl = ref('')
const moduleFileUploadInput = ref<HTMLInputElement | null>(null)

const versionCases = ref<TestCase[]>([])
const recentCases = ref<TestCase[]>([])
const bugList = ref<BugRecord[]>([])

const runRecords = ref<RunRecord[]>([])
const selectedRunId = ref<number | null>(null)
const runFiles = ref<ArtifactFile[]>([])
const filePage = ref(1)
const filePageSize = ref(50)
const fileTotal = ref(0)
const fileKeyword = ref('')

const runFileVisible = ref(false)
const runFileRaw = ref('')
const runFileType = ref<'code' | 'log' | 'coverage' | 'misc'>('misc')

const scanPath = ref('')
const scanLoading = ref(false)
const scanMessage = ref('')
const lastScanRun = ref<RunRecord | null>(null)

const overview = ref<OverviewStats>({
  totalFeatures: 0,
  totalCases: 0,
  totalBugs: 0,
  avgCoverage: 0
})

const detailVisible = ref(false)
const caseDetail = ref({
  code_content: '',
  log_content: '',
  coverage_html_url: ''
})

const trendChartRef = ref<HTMLElement | null>(null)
const bugChartRef = ref<HTMLElement | null>(null)
let trendChart: echarts.ECharts | null = null
let bugChart: echarts.ECharts | null = null

const currentVersion = computed(() => promptVersions.value[selectedVersionIndex.value])
const moduleTitle = computed(() => {
  if (selectedModule.value === 'prompt') return 'Prompt 模块'
  if (selectedModule.value === 'code') return '代码模块'
  if (selectedModule.value === 'bugs') return 'Bug 模块'
  if (selectedModule.value === 'runs') return '运行记录模块'
  if (selectedModule.value === 'upload') return '上传模块'
  return '工作台'
})

const activeUploadModule = computed<UploadModuleKey | null>(() => {
  if (selectedModule.value === 'prompt') return 'prompt'
  if (selectedModule.value === 'code') return 'code'
  if (selectedModule.value === 'bugs') return 'bugs'
  return null
})

const highlightedCode = computed(() => {
  const grammar = Prism.languages.java || Prism.languages.clike || {}
  return Prism.highlight(caseDetail.value.code_content || '', grammar, 'java')
})

const highlightedRunFile = computed(() => {
  const grammar = runFileType.value === 'code' ? Prism.languages.java || Prism.languages.clike || {} : Prism.languages.clike || {}
  return Prism.highlight(runFileRaw.value || '', grammar, runFileType.value === 'code' ? 'java' : 'clike')
})

const logLines = computed(() => caseDetail.value.log_content.split('\n').filter(Boolean))

function statusText(status: CaseStatus) {
  if (status === 'SUCCESS') return '成功'
  if (status === 'COMPILE_ERROR') return '编译错'
  return '崩溃/Bug'
}

function statusTagType(status: CaseStatus) {
  if (status === 'SUCCESS') return 'success'
  if (status === 'COMPILE_ERROR') return 'warning'
  return 'danger'
}

function isErrorLine(line: string) {
  return /error|exception|crash|failed/i.test(line)
}

function formatTime(value: string) {
  return new Date(value).toLocaleString()
}

function formatFileSize(size: number) {
  if (size < 1024) return `${size} B`
  if (size < 1024 * 1024) return `${(size / 1024).toFixed(1)} KB`
  return `${(size / (1024 * 1024)).toFixed(2)} MB`
}

function isImageMime(mimeType?: string) {
  return Boolean(mimeType && mimeType.startsWith('image/'))
}

function triggerModuleFileUpload() {
  moduleFileUploadInput.value?.click()
}

async function bootstrap() {
  navTree.value = await getNavTree()
  const firstModule = navTree.value
    .flatMap((jvm) => jvm.children || [])
    .flatMap((feature) => feature.children || [])
    .find((node) => node.nodeType === 'module')

  if (firstModule?.featureId && firstModule.moduleKey && firstModule.jvmName) {
    await selectFeatureModule(firstModule.jvmName, firstModule.featureId, firstModule.moduleKey)
  }

  await nextTick()
  await renderCharts()
}

async function handleTreeClick(node: NavTreeNode) {
  if (node.nodeType === 'module' && node.featureId && node.moduleKey && node.jvmName) {
    await selectFeatureModule(node.jvmName, node.featureId, node.moduleKey)
    return
  }

  if (node.nodeType === 'feature' && node.featureId && node.jvmName) {
    await selectFeatureModule(node.jvmName, node.featureId, 'prompt')
  }
}

async function selectFeatureModule(jvmName: string, featureId: number, moduleKey: ModuleKey) {
  selectedJvmName.value = jvmName
  selectedFeatureId.value = featureId
  selectedFeatureName.value = navTree.value
    .flatMap((jvm) => jvm.children || [])
    .find((feature) => feature.featureId === featureId)?.label || `Feature-${featureId}`
  selectedModule.value = moduleKey

  await Promise.all([loadFeatureData(), loadOverview(), renderCharts()])
}

async function loadFeatureData() {
  if (!selectedFeatureId.value) return

  const [versions, bugsRes, runsRes, recent] = await Promise.all([
    getPromptVersionsByFeature(selectedFeatureId.value),
    getBugsByFeature(selectedFeatureId.value),
    getRunsByFeature(selectedFeatureId.value),
    getRecentCasesByFeature(selectedFeatureId.value, 25)
  ])

  promptVersions.value = versions
  selectedVersionIndex.value = Math.max(0, versions.length - 1)
  editablePrompt.value = currentVersion.value?.content || ''
  await loadCurrentModuleFiles()

  bugList.value = bugsRes
  runRecords.value = runsRes
  recentCases.value = recent

  const firstRun = runsRes.at(0)
  if (firstRun) {
    selectedRunId.value = firstRun.run_id
    await queryRunFiles(1)
  } else {
    selectedRunId.value = null
    runFiles.value = []
    fileTotal.value = 0
  }

  await refreshVersionCases()
}

async function loadCurrentModuleFiles() {
  if (!selectedFeatureId.value || !activeUploadModule.value) {
    moduleFiles.value = []
    return
  }
  moduleFilesLoading.value = true
  try {
    moduleFiles.value = await getModuleFiles(selectedFeatureId.value, activeUploadModule.value)
  } finally {
    moduleFilesLoading.value = false
  }
}

async function uploadLocalModuleFile(event: Event) {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (!file) return
  if (!selectedFeatureId.value || !activeUploadModule.value) {
    ElMessage.warning('请先选择特性和模块')
    target.value = ''
    return
  }

  const text = await file.text()
  await uploadModuleFile({
    feature_id: selectedFeatureId.value,
    module: activeUploadModule.value,
    file_name: file.name,
    file_size: file.size,
    mime_type: file.type || 'text/plain',
    file_content: text
  })
  await loadCurrentModuleFiles()
  target.value = ''
  ElMessage.success('文件已上传入库')
}

async function openModuleFile(record: ModuleFileRecord) {
  const detail = await getModuleFileById(record.id)
  if (!detail) {
    ElMessage.warning('文件不存在')
    return
  }
  fileViewerTitle.value = detail.file_name
  if (isImageMime(detail.mime_type)) {
    fileViewerImage.value = detail.file_content
    fileViewerText.value = ''
  } else {
    fileViewerImage.value = ''
    fileViewerText.value = detail.file_content
  }
  fileViewerVisible.value = true
}

async function uploadBugRunImage(record: ModuleFileRecord, event: Event) {
  const input = event.target as HTMLInputElement
  const file = input.files?.[0]
  if (!file) return
  const isImage = file.type.startsWith('image/')
  if (!isImage) {
    ElMessage.warning('请上传图片文件')
    input.value = ''
    return
  }
  const imageDataUrl = await new Promise<string>((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = () => resolve(String(reader.result || ''))
    reader.onerror = () => reject(new Error('图片读取失败'))
    reader.readAsDataURL(file)
  })

  await uploadModuleRunImage({
    id: record.id,
    image_name: file.name,
    image_mime_type: file.type,
    image_content: imageDataUrl
  })
  await loadCurrentModuleFiles()
  input.value = ''
  ElMessage.success('运行图片已上传')
}

function viewRunImage(record: ModuleFileRecord) {
  if (!record.run_image_content) {
    ElMessage.info('暂无运行图片')
    return
  }
  runImageTitle.value = record.run_image_name || `${record.file_name} 运行图片`
  runImageUrl.value = record.run_image_content
  runImageVisible.value = true
}

async function refreshVersionCases() {
  if (!currentVersion.value) {
    versionCases.value = []
    return
  }
  versionCases.value = await getCasesByPromptVersion(currentVersion.value.id)
}

async function loadOverview() {
  overview.value = await getOverviewStats({ featureId: selectedFeatureId.value ?? undefined, jvm: selectedJvmName.value || undefined })
}

async function selectVersion(index: number) {
  selectedVersionIndex.value = index
  editablePrompt.value = currentVersion.value?.content || ''
  await refreshVersionCases()
  await renderCharts()
}

async function reloadCurrentFeature() {
  if (!selectedFeatureId.value) return
  await Promise.all([loadFeatureData(), loadOverview(), refreshNavTree()])
  await renderCharts()
  ElMessage.success('已从后端上传结果刷新')
}

async function refreshNavTree() {
  navTree.value = await getNavTree()
}

async function openCase(item: TestCase) {
  caseDetail.value = await getCaseDetail(item.id)
  detailVisible.value = true
}

async function selectRun(runId: number) {
  selectedRunId.value = runId
  await queryRunFiles(1)
}

async function queryRunFiles(page: number) {
  if (!selectedRunId.value) return
  const result = await getRunFiles({
    run_id: selectedRunId.value,
    page,
    pageSize: filePageSize.value,
    keyword: fileKeyword.value
  })
  filePage.value = result.page
  fileTotal.value = result.total
  runFiles.value = result.items
}

async function openRunFile(file: ArtifactFile) {
  runFileRaw.value = await getRunFileContent(file.key)
  runFileType.value = file.type
  runFileVisible.value = true
}

async function scanPathSubmit() {
  if (!selectedFeatureId.value) {
    ElMessage.warning('请先选择特性节点')
    return
  }
  if (!scanPath.value.trim()) {
    ElMessage.warning('请输入服务器目录路径')
    return
  }

  scanLoading.value = true
  scanMessage.value = '正在扫描并建立索引...'

  try {
    const result = await scanArtifacts({
      feature_id: selectedFeatureId.value,
      server_path: scanPath.value.trim()
    })

    lastScanRun.value = result.run
    scanMessage.value = `扫描完成，导入 ${result.importedFiles} 个文件`

    await Promise.all([loadFeatureData(), loadOverview(), refreshNavTree()])
    if (selectedModule.value === 'runs') {
      selectedRunId.value = result.run.run_id
      await queryRunFiles(1)
    }

    ElMessage.success('目录扫描完成')
  } catch (error) {
    const message = error instanceof Error ? error.message : '未知错误'
    scanMessage.value = `扫描失败: ${message}`
    ElMessage.error(scanMessage.value)
  } finally {
    scanLoading.value = false
  }
}

async function renderCharts() {
  if (!selectedFeatureId.value || !trendChartRef.value || !bugChartRef.value) return

  if (!trendChart) trendChart = echarts.init(trendChartRef.value)
  if (!bugChart) bugChart = echarts.init(bugChartRef.value)

  const trend = await getTrendStats(selectedFeatureId.value)
  trendChart.setOption({
    title: { text: '迭代效果趋势', left: 'center' },
    tooltip: { trigger: 'axis' },
    legend: { bottom: 0, data: ['平均覆盖率', '发现 Bug 数'] },
    grid: { left: 40, right: 30, top: 50, bottom: 50 },
    xAxis: { type: 'category', data: trend.map((item) => item.version) },
    yAxis: [
      { type: 'value', name: '覆盖率', min: 0, max: 100 },
      { type: 'value', name: 'Bug 数', minInterval: 1 }
    ],
    series: [
      {
        name: '平均覆盖率',
        type: 'line',
        smooth: true,
        data: trend.map((item) => item.coverage),
        areaStyle: { opacity: 0.15 }
      },
      {
        name: '发现 Bug 数',
        type: 'line',
        smooth: true,
        yAxisIndex: 1,
        data: trend.map((item) => item.bugs)
      }
    ]
  })

  const distribution = await getBugDistributionByFeature(selectedFeatureId.value)
  bugChart.setOption({
    title: { text: '缺陷分布', left: 'center' },
    tooltip: { trigger: 'item' },
    series: [
      {
        type: 'pie',
        radius: ['45%', '72%'],
        center: ['50%', '55%'],
        label: { formatter: '{b}: {c}' },
        data: [
          { name: 'LOW', value: distribution.LOW },
          { name: 'MEDIUM', value: distribution.MEDIUM },
          { name: 'HIGH', value: distribution.HIGH },
          { name: 'CRITICAL', value: distribution.CRITICAL }
        ]
      }
    ]
  })
}

function handleResize() {
  trendChart?.resize()
  bugChart?.resize()
}

onMounted(async () => {
  await bootstrap()
  window.addEventListener('resize', handleResize)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', handleResize)
  trendChart?.dispose()
  bugChart?.dispose()
})
</script>

<style scoped>
.home-view {
  min-height: 100vh;
  padding: 12px;
  background: #f5f7fb;
}

.top-grid {
  min-height: 68vh;
}

.panel-col,
.panel {
  height: 100%;
}

.panel {
  border: 1px solid #e5e7eb;
}

.panel-title {
  font-size: 15px;
  font-weight: 700;
  color: #1f2937;
}

.panel-inline {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tree-row {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 6px;
}

.tree-label {
  flex: 1;
  color: #111827;
}

.module-wrap {
  min-height: 560px;
}

.version-switch {
  margin: 10px 0;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.actions-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 6px 0 12px;
}

.progress-text {
  color: #4b5563;
  font-size: 13px;
}

.empty-tip {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6b7280;
}

.cases-scroll {
  height: 62vh;
}

.case-card {
  margin-bottom: 10px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 10px;
  background: #fff;
  cursor: pointer;
}

.case-card:hover {
  border-color: #93c5fd;
  box-shadow: 0 6px 20px rgba(29, 78, 216, 0.08);
}

.case-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.case-file {
  max-width: 76%;
  font-size: 13px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.case-sub {
  color: #6b7280;
  font-size: 12px;
  margin-bottom: 8px;
}

.mini-title {
  font-weight: 600;
  margin-bottom: 8px;
}

.timeline-box {
  max-height: 420px;
  overflow: auto;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 10px;
}

.run-item {
  cursor: pointer;
}

.run-meta {
  font-size: 12px;
  color: #6b7280;
  margin-top: 4px;
}

.files-tools {
  margin-bottom: 8px;
}

.dashboard-panel {
  margin-top: 14px;
}

.overview-stats {
  display: grid;
  grid-template-columns: repeat(4, minmax(120px, 1fr));
  gap: 12px;
  margin-bottom: 12px;
}

.chart-box {
  height: 300px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  background: #fff;
}

.detail-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.code-pane,
.log-pane {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 10px;
  background: #fff;
}

.code-block {
  margin: 0;
  max-height: 420px;
  overflow: auto;
}

.preview-image {
  display: block;
  max-width: 100%;
  max-height: 70vh;
  margin: 0 auto;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
}

.log-block {
  background: #0f172a;
  color: #e5e7eb;
  border-radius: 6px;
  padding: 8px;
  height: 390px;
  overflow: auto;
  margin-bottom: 10px;
}

.log-block p {
  margin: 0 0 4px;
  font-family: Consolas, monospace;
  font-size: 12px;
}

.err-line {
  color: #f87171;
  font-weight: 600;
}

@media (max-width: 1200px) {
  .top-grid {
    display: block;
  }

  .module-wrap {
    min-height: auto;
  }

  .cases-scroll {
    height: 380px;
  }

  .overview-stats {
    grid-template-columns: repeat(2, minmax(120px, 1fr));
  }

  .detail-grid {
    grid-template-columns: 1fr;
  }
}
</style>
