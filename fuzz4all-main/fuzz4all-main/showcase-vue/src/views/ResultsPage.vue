<script setup>
import { computed } from 'vue'
import { Bar, Doughnut } from 'vue-chartjs'
import {
  Chart as ChartJS, CategoryScale, LinearScale, BarElement,
  ArcElement, Tooltip, Legend
} from 'chart.js'
import { CATS } from '../data/cats.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, ArcElement, Tooltip, Legend)

const sorted = [...CATS].sort((a, b) => (b.safe / b.total) - (a.safe / a.total))

const barData = computed(() => ({
  labels: sorted.map(d => d.short),
  datasets: [
    { label: 'SAFE', data: sorted.map(d => +(d.safe / d.total * 100).toFixed(1)), backgroundColor: '#16A34A', borderRadius: 3 },
    { label: 'ERROR', data: sorted.map(d => +(d.err / d.total * 100).toFixed(1)), backgroundColor: '#D97706', borderRadius: 3 },
    { label: 'TIMEOUT', data: sorted.map(d => +(d.to / d.total * 100).toFixed(1)), backgroundColor: '#F59E0B', borderRadius: 3 },
    { label: 'FAILURE', data: sorted.map(d => +(d.fail / d.total * 100).toFixed(1)), backgroundColor: '#DC2626', borderRadius: 3 }
  ]
}))

const barOpts = {
  responsive: true, maintainAspectRatio: false,
  plugins: {
    legend: { labels: { color: '#64748B', font: { size: 11 } } },
    tooltip: { callbacks: { label: c => ` ${c.dataset.label}: ${c.parsed.y}%` } }
  },
  scales: {
    x: { stacked: true, ticks: { color: '#64748B', font: { size: 11 } }, grid: { color: 'rgba(226,232,240,.6)' } },
    y: { stacked: true, max: 100, ticks: { color: '#64748B', font: { size: 11 }, callback: v => v + '%' }, grid: { color: 'rgba(226,232,240,.6)' } }
  }
}

const pieData = {
  labels: ['SAFE', 'FAILURE', 'ERROR', 'TIMEOUT'],
  datasets: [{ data: [886, 389, 5, 0], backgroundColor: ['#16A34A', '#DC2626', '#D97706', '#F59E0B'], borderWidth: 2, borderColor: '#fff', hoverOffset: 4 }]
}

const pieOpts = {
  responsive: true, maintainAspectRatio: false, cutout: '62%',
  plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` ${c.label}: ${c.parsed} (${(c.parsed / 1280 * 100).toFixed(1)}%)` } } }
}

function rateColor (r) {
  return r >= 50 ? 'var(--green)' : r >= 30 ? 'var(--orange)' : 'var(--red)'
}
</script>

<template>
  <div class="page-inner">
    <div class="page-header">
      <div class="page-title">测试结果</div>
      <div class="page-subtitle">10 类 Java API · 1280 个测试用例 · MemoryMXBean 92.5% / File 86.5% / Duration 74.5%</div>
    </div>
    <div style="display:grid;grid-template-columns:2fr 1fr;gap:14px;margin-bottom:14px">
      <div class="card">
        <div class="card-title">各 API 类别编译通过率</div>
        <div class="chart-wrap"><Bar :data="barData" :options="barOpts" /></div>
      </div>
      <div class="card">
        <div class="card-title">结果总体分布</div>
        <div class="chart-sm"><Doughnut :data="pieData" :options="pieOpts" /></div>
        <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:10px;font-size:12px">
          <span><span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--green);margin-right:4px"></span>SAFE 886</span>
          <span><span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--red);margin-right:4px"></span>FAILURE 389</span>
          <span><span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--orange);margin-right:4px"></span>ERROR 5</span>
          <span><span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:#F59E0B;margin-right:4px"></span>TIMEOUT 0</span>
        </div>
      </div>
    </div>
    <div class="card" style="overflow-x:auto">
      <table class="tbl">
        <thead>
          <tr>
            <th>API 类别</th>
            <th>领域</th>
            <th>总数</th>
            <th style="color:var(--green)">SAFE</th>
            <th style="color:var(--red)">FAIL</th>
            <th style="color:var(--orange)">ERROR</th>
            <th style="color:#F59E0B">TO</th>
            <th>通过率</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="c in sorted" :key="c.id">
            <td style="font-weight:500">{{ c.display }}</td>
            <td><span class="badge" :class="c.badge">{{ c.tagTxt }}</span></td>
            <td style="color:var(--muted)">{{ c.total }}</td>
            <td style="color:var(--green);font-weight:600">{{ c.safe }}</td>
            <td style="color:var(--red)">{{ c.fail }}</td>
            <td style="color:var(--orange)">{{ c.err }}</td>
            <td style="color:#F59E0B">{{ c.to }}</td>
            <td>
              <div class="pbar"><div class="pfill" :style="{ width: (c.safe / c.total * 100).toFixed(1) + '%', background: rateColor(c.safe / c.total * 100) }"></div></div>
              <span :style="{ color: rateColor(c.safe / c.total * 100), fontWeight: 600 }">{{ (c.safe / c.total * 100).toFixed(1) }}%</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
