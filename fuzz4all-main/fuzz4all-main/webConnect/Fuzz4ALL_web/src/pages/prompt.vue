<template>
  <section class="page-wrap">
    <div class="table-card">
      <div class="head-row">
        <h1>提示词库</h1>
        <div class="actions">
          <input ref="fileInput" type="file" style="display: none" @change="onPickFile" />
          <el-button type="primary" @click="triggerUpload">新增（上传文件）</el-button>
          <el-button type="danger" :disabled="selectedRows.length === 0" @click="deleteSelected">删除选中</el-button>
          <el-button :loading="loading" @click="loadData">刷新</el-button>
        </div>
      </div>

      <el-alert v-if="error" :title="error" type="error" :closable="false" show-icon />

      <el-table
        :data="rows"
        border
        stripe
        v-loading="loading"
        empty-text="暂无数据"
        style="margin-top: 12px"
        @selection-change="onSelectionChange"
      >
        <el-table-column type="selection" width="52" />
        <el-table-column prop="id" label="ID" width="90" />
        <el-table-column prop="name" label="文件名" min-width="260" />
        <el-table-column label="创建时间" min-width="200">
          <template #default="scope">
            {{ formatTime(scope.row.createdAt) }}
          </template>
        </el-table-column>
      </el-table>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { deletePrompt, getPrompts, uploadPrompt, type PromptRecord } from '../services/backendApi'

const loading = ref(false)
const error = ref('')
const rows = ref<PromptRecord[]>([])
const selectedRows = ref<PromptRecord[]>([])
const fileInput = ref<HTMLInputElement | null>(null)

function formatTime(value: string) {
  if (!value) return '-'
  return new Date(value).toLocaleString()
}

async function loadData() {
  loading.value = true
  error.value = ''
  try {
    rows.value = await getPrompts()
  } catch (e) {
    const message = e instanceof Error ? e.message : '请求失败'
    error.value = `加载 Prompt 列表失败：${message}`
    rows.value = []
  } finally {
    loading.value = false
  }
}

function triggerUpload() {
  fileInput.value?.click()
}

async function onPickFile(event: Event) {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (!file) return

  try {
    await uploadPrompt(file)
    ElMessage.success('上传成功')
    await loadData()
  } catch (e) {
    ElMessage.error(`上传失败：${e instanceof Error ? e.message : '未知错误'}`)
  } finally {
    target.value = ''
  }
}

function onSelectionChange(selection: PromptRecord[]) {
  selectedRows.value = selection
}

async function deleteSelected() {
  if (selectedRows.value.length === 0) return

  await ElMessageBox.confirm(`确认删除选中的 ${selectedRows.value.length} 条记录吗？`, '删除确认', {
    type: 'warning',
  })

  await Promise.all(selectedRows.value.map((item) => deletePrompt(item.id)))
  ElMessage.success('删除成功')
  selectedRows.value = []
  await loadData()
}

onMounted(loadData)
</script>

<style scoped>
.page-wrap {
  max-width: 1200px;
}

.table-card {
  background: #fff;
  border-radius: 10px;
  border: 1px solid #e5e7eb;
  padding: 16px;
}

.head-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.head-row h1 {
  margin: 0;
  font-size: 20px;
}

.actions {
  display: flex;
  gap: 8px;
}
</style>
