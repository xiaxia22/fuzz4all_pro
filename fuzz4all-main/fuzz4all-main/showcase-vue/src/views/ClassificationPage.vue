<script setup>
import { CATS, tagColor, tagBg } from '../data/cats.js'
import TagPill from '../components/TagPill.vue'

const tagDescriptions = [
  { tag: 'SECURITY', desc: '加密、签名、密钥等安全相关API（如Cipher、KeyStore）' },
  { tag: 'REFLECT', desc: '反射API（Method、Field、Constructor等）' },
  { tag: 'FILE', desc: '文件和路径操作（File、Path、Files等）' },
  { tag: 'CONCURRENT', desc: '线程和并发API（Thread、Lock、Future等）' },
  { tag: 'NETWORK', desc: '网络API（Socket、URL、URI等）' },
  { tag: 'CALLBACK', desc: '监听器和回调API（PropertyChangeSupport等）' },
  { tag: 'TIME', desc: '时间和日期API（Duration、Instant等）' },
  { tag: 'JVM_MGMT', desc: 'JVM运行时管理API（ManagementFactory等）' },
  { tag: 'RESOURCE', desc: '资源流API（InputStream、OutputStream等）' }
]
</script>

<template>
  <div class="page-inner">
    <div class="page-header">
      <div class="page-title">离线分类对应表</div>
      <div class="page-subtitle">系统离线阶段通过规则匹配为每个 API 分配领域标签和变异策略配置</div>
    </div>
    <div class="info-box info-blue" style="margin-bottom:16px">
      💡 离线分类结果存储于 <code>outputs/api_classification/java_api_5d_classification.json</code>，
      系统运行时根据此表自动加载对应的变异算子组合。
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
      <div class="card-title">10类API分类结果</div>
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
      <div class="card-title">13种领域标签说明</div>
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
