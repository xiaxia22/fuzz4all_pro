<template>
  <section class="page-wrap">
    <div class="table-card">
      <div class="head-row">
        <h1>缺陷分析</h1>
        <div class="actions">
          <el-button type="primary" @click="openCreateDialog">新增</el-button>
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
        <el-table-column prop="name" label="名称" min-width="160" />
        <el-table-column prop="description" label="描述" min-width="280" show-overflow-tooltip />
        <el-table-column label="截图" width="120">
          <template #default="scope">{{ scope.row.imagePath ? '已上传' : '无' }}</template>
        </el-table-column>
        <el-table-column label="创建时间" min-width="200">
          <template #default="scope">
            {{ formatTime(scope.row.createdAt) }}
          </template>
        </el-table-column>
      </el-table>
    </div>

    <el-dialog v-model="createDialogVisible" title="新增缺陷" width="520px">
      <el-form label-position="top">
        <el-form-item label="名称">
          <el-input v-model.trim="createForm.name" placeholder="例如：空指针崩溃" />
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model.trim="createForm.description" type="textarea" :rows="4" placeholder="请输入缺陷描述" />
        </el-form-item>
        <el-form-item label="运行截图（可选）">
          <input type="file" accept="image/*" @change="onPickImage" />
          <div class="image-tip" v-if="createForm.image">已选择：{{ createForm.image.name }}</div>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="createDialogVisible = false">取消</el-button>
        <el-button type="primary" :loading="creating" @click="submitCreate">新增</el-button>
      </template>
    </el-dialog>
  </section>
</template>

<script setup lang="ts">
import { reactive, ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { deleteBug, getBugs, uploadBug, type BugRecord } from '../services/backendApi'

const loading = ref(false)
const creating = ref(false)
const error = ref('')
const rows = ref<BugRecord[]>([])
const selectedRows = ref<BugRecord[]>([])
const createDialogVisible = ref(false)

const createForm = reactive({
  name: '',
  description: '',
  image: null as File | null,
})

function formatTime(value: string) {
  if (!value) return '-'
  return new Date(value).toLocaleString()
}

async function loadData() {
  loading.value = true
  error.value = ''
  try {
    rows.value = await getBugs()
  } catch (e) {
    const message = e instanceof Error ? e.message : '请求失败'
    error.value = `加载 Bug 列表失败：${message}`
    rows.value = []
  } finally {
    loading.value = false
  }
}

function onSelectionChange(selection: BugRecord[]) {
  selectedRows.value = selection
}

async function deleteSelected() {
  if (selectedRows.value.length === 0) return

  await ElMessageBox.confirm(`确认删除选中的 ${selectedRows.value.length} 条缺陷吗？`, '删除确认', {
    type: 'warning',
  })

  await Promise.all(selectedRows.value.map((item) => deleteBug(item.id)))
  ElMessage.success('删除成功')
  selectedRows.value = []
  await loadData()
}

function openCreateDialog() {
  createForm.name = ''
  createForm.description = ''
  createForm.image = null
  createDialogVisible.value = true
}

function onPickImage(event: Event) {
  const target = event.target as HTMLInputElement
  createForm.image = target.files?.[0] || null
}

async function submitCreate() {
  if (!createForm.name || !createForm.description) {
    ElMessage.warning('请先填写名称和描述')
    return
  }

  creating.value = true
  try {
    await uploadBug({
      name: createForm.name,
      description: createForm.description,
      image: createForm.image,
    })
    ElMessage.success('新增成功')
    createDialogVisible.value = false
    await loadData()
  } catch (e) {
    ElMessage.error(`新增失败：${e instanceof Error ? e.message : '未知错误'}`)
  } finally {
    creating.value = false
  }
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

.image-tip {
  margin-top: 8px;
  color: #4b5563;
  font-size: 13px;
}
</style>
