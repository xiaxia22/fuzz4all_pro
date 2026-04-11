export interface PromptRecord {
  id: number
  name: string
  filePath: string
  createdAt: string
}

export interface CodeRecord {
  id: number
  name: string
  filePath: string
  createdAt: string
}

export interface BugRecord {
  id: number
  name: string
  description: string
  imagePath?: string | null
  createdAt: string
}

const apiBaseUrl = (import.meta.env.VITE_API_BASE_URL as string | undefined) || 'http://localhost:8080'

async function requestJson<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${apiBaseUrl}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(init?.headers || {}),
    },
    ...init,
  })

  if (!response.ok) {
    throw new Error(`HTTP ${response.status} ${response.statusText}`)
  }

  if (response.status === 204) {
    return undefined as T
  }

  return (await response.json()) as T
}

async function requestFormData<T>(path: string, formData: FormData): Promise<T> {
  const response = await fetch(`${apiBaseUrl}${path}`, {
    method: 'POST',
    body: formData,
  })

  if (!response.ok) {
    throw new Error(`HTTP ${response.status} ${response.statusText}`)
  }

  return (await response.json()) as T
}

export function getPrompts() {
  return requestJson<PromptRecord[]>('/api/prompts')
}

export function uploadPrompt(file: File) {
  const formData = new FormData()
  formData.append('file', file)
  return requestFormData<PromptRecord>('/api/prompts/upload', formData)
}

export function deletePrompt(id: number) {
  return requestJson<void>(`/api/prompts/${id}`, { method: 'DELETE' })
}

export function getCodes() {
  return requestJson<CodeRecord[]>('/api/codes')
}

export function uploadCode(file: File) {
  const formData = new FormData()
  formData.append('file', file)
  return requestFormData<CodeRecord>('/api/codes/upload', formData)
}

export function deleteCode(id: number) {
  return requestJson<void>(`/api/codes/${id}`, { method: 'DELETE' })
}

export function getBugs() {
  return requestJson<BugRecord[]>('/api/bugs')
}

export function uploadBug(input: { name: string; description: string; image?: File | null }) {
  const formData = new FormData()
  formData.append('name', input.name)
  formData.append('description', input.description)
  if (input.image) {
    formData.append('image', input.image)
  }
  return requestFormData<BugRecord>('/api/bugs/upload', formData)
}

export function deleteBug(id: number) {
  return requestJson<void>(`/api/bugs/${id}`, { method: 'DELETE' })
}
