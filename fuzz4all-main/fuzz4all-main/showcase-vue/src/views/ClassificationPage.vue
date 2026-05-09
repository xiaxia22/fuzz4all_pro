<script setup>
import { CATS } from '../data/cats.js'
import TagPill from '../components/TagPill.vue'

const tagDescriptions = [
  { tag: 'SECURITY', desc: '加密、签名、密钥与 provider 相关 API（如 Cipher）' },
  { tag: 'REFLECT', desc: '反射查询、签名匹配与调用相关 API（如 Method）' },
  { tag: 'FILE', desc: '文件、路径与状态操作相关 API（如 File）' },
  { tag: 'CONCURRENT', desc: '线程生命周期与并发控制相关 API（如 Thread）' },
  { tag: 'NETWORK', desc: '网络端点、URI 与连接相关 API（如 Socket、URI）' },
  { tag: 'CALLBACK', desc: '监听器注册与回调触发相关 API（如 PropertyChangeSupport）' },
  { tag: 'TIME', desc: '时间跨度与边界运算相关 API（如 Duration）' },
  { tag: 'JVM_MGMT', desc: 'JVM 运行时与内存管理相关 API（如 MemoryMXBean、ManagementFactory）' },
  { tag: 'RESOURCE', desc: '输入输出流与资源生命周期相关 API（如 BufferedInputStream）' }
]
</script>

<template>
  <div class="page-inner">
    <div class="page-header">
      <div class="page-title">离线分类对应表</div>
      <div class="page-subtitle">系统先离线构建分类知识库，再在运行时按分类结果加载对应的变异策略和反馈规则</div>
    </div>
    <div class="info-box info-blue" style="margin-bottom:16px">
      分类结果存储在 <code>outputs/api_classification/java_api_5d_classification.json</code>，
      运行时会依据该表加载对应的 mutation profile、active profiles 与 repair / filter 规则。
    </div>
    <div class="g3" style="margin-bottom:16px">
      <div class="card card-sm" style="text-align:center">
        <div style="font-size:22px;font-weight:700;color:var(--primary)">13</div>
        <div style="font-size:12px;color:var(--muted)">领域分类标签</div>
      </div>
      <div class="card card-sm" style="text-align:center">
        <div style="font-size:22px;font-weight:700;color:var(--primary)">12</div>
        <div style="font-size:12px;color:var(--muted)">变异策略配置</div>
      </div>
      <div class="card card-sm" style="text-align:center">
        <div style="font-size:22px;font-weight:700;color:var(--primary)">38+</div>
        <div style="font-size:12px;color:var(--muted)">变异算子</div>
      </div>
    </div>
    <div class="card" style="overflow-x:auto;margin-bottom:16px">
      <div class="card-title">10 类代表 API 分类结果</div>
      <table class="tbl">
        <thead>
          <tr>
            <th>API 全名</th>
            <th>模块</th>
            <th>主标签</th>
            <th>全部标签</th>
            <th>变异策略</th>
            <th>说明</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="c in CATS" :key="c.id">
            <td style="font-family:monospace;font-size:12px">{{ c.fullName }}</td>
            <td style="font-size:12px">{{ c.module }}</td>
            <td><span class="badge" :class="c.badge">{{ c.tagTxt }}</span></td>
            <td><TagPill v-for="t in c.allTags" :key="t" :tag="t" /></td>
            <td style="font-family:monospace;font-size:11.5px;color:var(--muted)">{{ c.profile }}</td>
            <td style="color:var(--muted);font-size:12px">{{ c.desc }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="card">
      <div class="card-title">主要领域标签说明</div>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px;font-size:12.5px">
        <div v-for="td in tagDescriptions" :key="td.tag" style="padding:8px 12px;border-radius:6px;border:1px solid var(--border);background:var(--surface2)">
          <span class="badge" :class="{
            'b-sec': td.tag === 'SECURITY', 'b-refl': td.tag === 'REFLECT', 'b-file': td.tag === 'FILE',
            'b-conc': td.tag === 'CONCURRENT', 'b-net': td.tag === 'NETWORK', 'b-cb': td.tag === 'CALLBACK',
            'b-time': td.tag === 'TIME', 'b-jvm': td.tag === 'JVM_MGMT', 'b-res': td.tag === 'RESOURCE'
          }" style="margin-bottom:4px;display:inline-block">{{ td.tag }}</span>
          <div style="color:var(--muted)">{{ td.desc }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
