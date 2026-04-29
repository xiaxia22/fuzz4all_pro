<template>
  <div class="layout-wrapper">
    <aside class="sidebar">
      <div class="sidebar-header">
        <h2>Visualization System</h2>
      </div>

      <nav class="sidebar-nav">
        <ul>
          <li v-for="item in menuItems" :key="item.routeName">
            <router-link :to="{ name: item.routeName }" class="nav-item" active-class="active">
              <span class="icon">{{ item.icon }}</span>
              <span class="label">{{ item.name }}</span>
            </router-link>
          </li>
        </ul>
      </nav>

      <div class="sidebar-footer">
        <div class="user-info">
          <span class="avatar">U</span>
          <span class="username">{{ username }}</span>
        </div>
        <button class="logout-btn-small" @click="logout">退出登录</button>
      </div>
    </aside>

    <main class="main-content">
      <header class="top-bar">
        <h3>{{ currentTitle }}</h3>
      </header>

      <div class="content-body">
        <router-view />
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const username = ref('Admin')
const router = useRouter()
const route = useRoute()

const menuItems = [
  { name: '系统概览', routeName: 'Home', icon: 'H' },
  { name: '知识引导', routeName: 'Prompts', icon: 'K' },
  { name: '测试样例', routeName: 'TestCases', icon: 'T' },
  { name: '差分分析', routeName: 'Bugs', icon: 'D' }
] as const

const currentTitle = computed(() => {
  const item = menuItems.find((i) => i.routeName === route.name)
  return item ? item.name : '工作台'
})

onMounted(() => {
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true'
  if (!isLoggedIn) {
    router.push({ name: 'Login' })
    return
  }

  username.value = localStorage.getItem('username') || 'Admin'
})

const logout = () => {
  localStorage.removeItem('isLoggedIn')
  localStorage.removeItem('username')
  router.push({ name: 'Login' })
}
</script>

<style scoped>
.layout-wrapper {
  display: flex;
  min-height: 100vh;
  background-color: #f0f2f5;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.sidebar {
  width: 240px;
  background-color: #001529;
  color: #fff;
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  z-index: 100;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.15);
}

.sidebar-header {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #002140;
  font-size: 16px;
  font-weight: 700;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar-nav {
  flex: 1;
  padding-top: 20px;
  overflow-y: auto;
}

.sidebar-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 15px 24px;
  color: rgba(255, 255, 255, 0.65);
  text-decoration: none;
  transition: all 0.3s;
  font-size: 15px;
}

.nav-item:hover {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.08);
}

.nav-item.active {
  color: #fff;
  background-color: #1890ff;
}

.nav-item .icon {
  margin-right: 12px;
  font-size: 14px;
  width: 24px;
  text-align: center;
}

.sidebar-footer {
  padding: 20px;
  background-color: #002140;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.user-info {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.85);
}

.user-info .avatar {
  margin-right: 10px;
  font-size: 16px;
}

.logout-btn-small {
  width: 100%;
  padding: 8px;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  cursor: pointer;
  font-size: 13px;
  transition: all 0.3s;
}

.logout-btn-small:hover {
  background: #dc3545;
  border-color: #dc3545;
}

.main-content {
  margin-left: 240px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.top-bar {
  height: 64px;
  background: #fff;
  display: flex;
  align-items: center;
  padding: 0 24px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
  margin-bottom: 24px;
}

.top-bar h3 {
  margin: 0;
  color: #333;
  font-size: 18px;
}

.content-body {
  padding: 24px;
  flex: 1;
}
</style>
