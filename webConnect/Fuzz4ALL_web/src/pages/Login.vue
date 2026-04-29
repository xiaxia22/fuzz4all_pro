<template>
  <div class="login-container">
    <h2>用户登录</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">用户名</label>
        <input
          id="username"
          v-model.trim="username"
          type="text"
          placeholder="请输入用户名"
          required
        />
      </div>

      <div class="form-group">
        <label for="password">密码</label>
        <input
          id="password"
          v-model="password"
          type="password"
          placeholder="请输入密码"
          required
        />
      </div>

      <button type="submit" class="login-btn">登录</button>
    </form>

    <p v-if="error" class="error">{{ error }}</p>
    <p class="hint">演示账号：admin / 123456</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()
const route = useRoute()

const handleLogin = () => {
  if (username.value === 'admin' && password.value === '123456') {
    localStorage.setItem('isLoggedIn', 'true')
    localStorage.setItem('username', username.value)
    error.value = ''

    const redirect = typeof route.query.redirect === 'string' ? route.query.redirect : '/home'
    router.push(redirect)
    return
  }

  error.value = '用户名或密码错误'
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 80px auto;
  padding: 40px 30px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 30px;
  font-size: 24px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #555;
}

input {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  box-sizing: border-box;
  font-size: 14px;
  transition: border-color 0.3s;
}

input:focus {
  outline: none;
  border-color: #007bff;
}

.login-btn {
  width: 100%;
  padding: 14px;
  background: linear-gradient(135deg, #007bff, #0056b3);
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
  transition: transform 0.2s, box-shadow 0.2s;
}

.login-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
}

.error {
  color: #dc3545;
  text-align: center;
  margin-top: 15px;
  font-size: 14px;
}

.hint {
  margin-top: 10px;
  text-align: center;
  color: #6b7280;
  font-size: 13px;
}
</style>
