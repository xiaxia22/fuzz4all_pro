import * as mock from './mockApi'
import type {
  ArtifactFile,
  BugRecord,
  CaseDetail,
  CaseStatus,
  Feature,
  GenerateInput,
  GenerateProgressEvent,
  ModuleKey,
  NavTreeNode,
  OverviewStats,
  PromptVersion,
  RunFilesResult,
  RunRecord,
  ScanArtifactsInput,
  ScanArtifactsResult,
  TestCase,
  UploadModuleKey,
  ModuleFileRecord,
} from './mockApi'

export type {
  ArtifactFile,
  BugRecord,
  CaseDetail,
  CaseStatus,
  Feature,
  GenerateInput,
  GenerateProgressEvent,
  ModuleKey,
  NavTreeNode,
  OverviewStats,
  PromptVersion,
  RunFilesResult,
  RunRecord,
  ScanArtifactsInput,
  ScanArtifactsResult,
  TestCase,
  UploadModuleKey,
  ModuleFileRecord,
}

type ApiMode = 'mock' | 'live' | 'hybrid'

const apiMode = ((import.meta.env.VITE_API_MODE as ApiMode | undefined) || 'hybrid').toLowerCase() as ApiMode
const apiBaseUrl = (import.meta.env.VITE_API_BASE_URL as string | undefined) || ''
const wsBaseUrl =
  (import.meta.env.VITE_WS_BASE_URL as string | undefined) ||
  (typeof window !== 'undefined'
    ? `${window.location.protocol === 'https:' ? 'wss' : 'ws'}://${window.location.host}`
    : '')

async function requestJson<T>(path: string, init?: RequestInit): Promise<T> {
  const url = `${apiBaseUrl}${path}`
  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      ...(init?.headers || {}),
    },
    ...init,
  })

  if (!response.ok) {
    throw new Error(`HTTP ${response.status} ${response.statusText} @ ${path}`)
  }

  const contentType = response.headers.get('content-type') || ''
  if (contentType.includes('application/json')) {
    return (await response.json()) as T
  }

  return (await response.text()) as T
}

async function withFallback<T>(liveCall: () => Promise<T>, mockCall: () => Promise<T>, opName: string): Promise<T> {
  if (apiMode === 'mock') {
    return mockCall()
  }

  if (apiMode === 'live') {
    return liveCall()
  }

  try {
    return await liveCall()
  } catch (error) {
    console.warn(`[dataService] fallback to mock for ${opName}:`, error)
    return mockCall()
  }
}

function buildProgressWsUrl(runId: number) {
  if (!wsBaseUrl) {
    return ''
  }
  return `${wsBaseUrl}/api/generate/${runId}/events`
}

async function consumeGenerateProgress(runId: number, onProgress: (event: GenerateProgressEvent) => void) {
  const wsUrl = buildProgressWsUrl(runId)
  if (!wsUrl || typeof WebSocket === 'undefined') {
    return
  }

  await new Promise<void>((resolve, reject) => {
    let finished = false
    const ws = new WebSocket(wsUrl)
    const timer = setTimeout(() => {
      if (!finished) {
        finished = true
        ws.close()
        resolve()
      }
    }, 30000)

    ws.onmessage = (evt) => {
      try {
        const data = JSON.parse(String(evt.data)) as Partial<GenerateProgressEvent> & { done?: boolean; status?: string }
        const percent = typeof data.percent === 'number' ? data.percent : 0
        const message = data.message || '处理中...'
        onProgress({ percent, message })
        if (percent >= 100 || data.done || data.status === 'DONE') {
          if (!finished) {
            finished = true
            clearTimeout(timer)
            ws.close()
            resolve()
          }
        }
      } catch {
        // ignore malformed ws message
      }
    }

    ws.onerror = () => {
      if (!finished) {
        finished = true
        clearTimeout(timer)
        ws.close()
        reject(new Error('generate websocket error'))
      }
    }

    ws.onclose = () => {
      if (!finished) {
        finished = true
        clearTimeout(timer)
        resolve()
      }
    }
  })
}

export async function getNavTree() {
  return withFallback(
    async () => requestJson<NavTreeNode[]>('/api/nav/tree'),
    () => mock.getNavTree(),
    'getNavTree',
  )
}

export async function getOverviewStats(params?: { jvm?: string; featureId?: number }) {
  return withFallback(
    async () => {
      const query = new URLSearchParams()
      if (params?.jvm) query.set('jvm', params.jvm)
      if (params?.featureId) query.set('feature', String(params.featureId))
      const suffix = query.toString() ? `?${query.toString()}` : ''
      return requestJson<OverviewStats>(`/api/stats/overview${suffix}`)
    },
    () => mock.getOverviewStats(params),
    'getOverviewStats',
  )
}

export async function getPromptVersionsByFeature(featureId: number) {
  return withFallback(
    async () => requestJson<PromptVersion[]>(`/api/features/${featureId}/prompts`),
    () => mock.getPromptVersionsByFeature(featureId),
    'getPromptVersionsByFeature',
  )
}

export async function updatePromptVersion(versionId: number, content: string) {
  return withFallback(
    async () =>
      requestJson<void>(`/api/prompts/${versionId}`, {
        method: 'PUT',
        body: JSON.stringify({ content }),
      }),
    () => mock.updatePromptVersion(versionId, content),
    'updatePromptVersion',
  )
}

export async function getCasesByPromptVersion(promptVersionId: number) {
  return withFallback(
    async () => requestJson<TestCase[]>(`/api/prompts/${promptVersionId}/cases`),
    () => mock.getCasesByPromptVersion(promptVersionId),
    'getCasesByPromptVersion',
  )
}

export async function getRecentCasesByFeature(featureId: number, limit = 20) {
  return withFallback(
    async () => requestJson<TestCase[]>(`/api/features/${featureId}/cases/recent?limit=${limit}`),
    () => mock.getRecentCasesByFeature(featureId, limit),
    'getRecentCasesByFeature',
  )
}

export async function getBugsByFeature(featureId: number) {
  return withFallback(
    async () => requestJson<BugRecord[]>(`/api/features/${featureId}/bugs`),
    () => mock.getBugsByFeature(featureId),
    'getBugsByFeature',
  )
}

export async function getCaseDetail(id: number) {
  return withFallback(
    async () => requestJson<CaseDetail>(`/api/cases/${id}`),
    () => mock.getCaseDetail(id),
    'getCaseDetail',
  )
}

export async function getRunsByFeature(featureId: number) {
  return withFallback(
    async () => requestJson<RunRecord[]>(`/api/features/${featureId}/runs`),
    () => mock.getRunsByFeature(featureId),
    'getRunsByFeature',
  )
}

export async function getRunFiles(params: { run_id: number; page: number; pageSize: number; keyword?: string }) {
  return withFallback(
    async () => {
      const query = new URLSearchParams({
        page: String(params.page),
        pageSize: String(params.pageSize),
      })
      if (params.keyword) query.set('keyword', params.keyword)
      return requestJson<RunFilesResult>(`/api/runs/${params.run_id}/files?${query.toString()}`)
    },
    () => mock.getRunFiles(params),
    'getRunFiles',
  )
}

export async function getRunFileContent(fileKey: string) {
  return withFallback(
    async () => requestJson<string>(`/api/files/content?key=${encodeURIComponent(fileKey)}`),
    () => mock.getRunFileContent(fileKey),
    'getRunFileContent',
  )
}

export async function getModuleFiles(featureId: number, module: UploadModuleKey) {
  return withFallback(
    async () => requestJson<ModuleFileRecord[]>(`/api/features/${featureId}/modules/${module}/files`),
    () => mock.getModuleFiles(featureId, module),
    'getModuleFiles',
  )
}

export async function uploadModuleFile(input: {
  feature_id: number
  module: UploadModuleKey
  file_name: string
  file_size: number
  mime_type: string
  file_content: string
}) {
  return withFallback(
    async () =>
      requestJson<ModuleFileRecord>(`/api/features/${input.feature_id}/modules/${input.module}/files`, {
        method: 'POST',
        body: JSON.stringify(input),
      }),
    () => mock.uploadModuleFile(input),
    'uploadModuleFile',
  )
}

export async function getModuleFileById(id: number) {
  return withFallback(
    async () => requestJson<ModuleFileRecord | null>(`/api/module-files/${id}`),
    () => mock.getModuleFileById(id),
    'getModuleFileById',
  )
}

export async function uploadModuleRunImage(input: {
  id: number
  image_name: string
  image_mime_type: string
  image_content: string
}) {
  return withFallback(
    async () =>
      requestJson<ModuleFileRecord>(`/api/module-files/${input.id}/run-image`, {
        method: 'POST',
        body: JSON.stringify(input),
      }),
    () => mock.uploadModuleRunImage(input),
    'uploadModuleRunImage',
  )
}

export async function scanArtifacts(input: ScanArtifactsInput) {
  return withFallback(
    async () =>
      requestJson<ScanArtifactsResult>('/api/artifacts/scan', {
        method: 'POST',
        body: JSON.stringify({
          feature_id: input.feature_id,
          server_path: input.server_path,
        }),
      }),
    () => mock.scanArtifacts(input),
    'scanArtifacts',
  )
}

export async function postGenerate(input: GenerateInput, onProgress: (event: GenerateProgressEvent) => void) {
  return withFallback(
    async () => {
      onProgress({ percent: 5, message: '已提交生成任务...' })

      const startResp = await requestJson<{ run_id?: number; runId?: number; done?: boolean }>('/api/generate', {
        method: 'POST',
        body: JSON.stringify({
          feature_id: input.feature_id,
          prompt_version_id: input.prompt_version_id,
        }),
      })

      const runId = startResp.run_id ?? startResp.runId
      if (runId) {
        try {
          await consumeGenerateProgress(runId, onProgress)
        } catch {
          onProgress({ percent: 100, message: '任务完成（WebSocket未连接，已转轮询）' })
        }
      } else {
        onProgress({ percent: 100, message: '任务完成' })
      }

      const now = new Date().toISOString()
      return {
        newVersion: {
          id: -1,
          feature_id: input.feature_id,
          version_no: 'v?',
          content: '',
          module_scope: 'prompt' as ModuleKey,
          metrics_snapshot: { coverage: 0, bugCount: 0 },
        },
        run: {
          run_id: runId || -1,
          feature_id: input.feature_id,
          jvm_name: '',
          source: 'generate' as const,
          created_at: now,
          summary: { fileCount: 0, totalSizeMB: 0, errorCount: 0 },
        },
        newCases: [] as TestCase[],
      }
    },
    () => mock.postGenerate(input, onProgress),
    'postGenerate',
  )
}

export async function getTrendStats(featureId: number) {
  return withFallback(
    async () => requestJson<Array<{ version: string; coverage: number; bugs: number }>>(`/api/features/${featureId}/trend`),
    () => mock.getTrendStats(featureId),
    'getTrendStats',
  )
}

export async function getBugDistributionByFeature(featureId: number) {
  return withFallback(
    async () => requestJson<Record<'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL', number>>(`/api/features/${featureId}/bug-distribution`),
    () => mock.getBugDistributionByFeature(featureId),
    'getBugDistributionByFeature',
  )
}
