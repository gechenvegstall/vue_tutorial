<template>
  <div class="login-container">
    <h2>系统登录</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label>用户名</label>
        <input 
          type="text" 
          v-model="form.username" 
          required
          placeholder="请输入用户名"
        />
      </div>
      <div class="form-group">
        <label>密码</label>
        <input 
          type="password" 
          v-model="form.password" 
          required
          placeholder="请输入密码"
        />
      </div>
      <button type="submit" :disabled="loading">
        {{ loading ? '登录中...' : '登录' }}
      </button>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const form = ref({
  username: '',
  password: ''
})
const loading = ref(false)
const errorMessage = ref('')

const handleSubmit = async () => {
  loading.value = true
  errorMessage.value = ''
  
  try {
    const response = await axios.post('http://localhost:8000/token', 
      `username=${form.value.username}&password=${form.value.password}`,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    )
    
    // 存储token
    localStorage.setItem('auth_token', response.data.access_token)
    
    // 跳转到首页
    router.push('/')
  } catch (error) {
    if (error.response) {
      errorMessage.value = error.response.data.detail || '登录失败'
    } else {
      errorMessage.value = '网络错误，请重试'
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 5rem auto;
  padding: 2rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

button {
  width: 100%;
  padding: 0.75rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.error-message {
  margin-top: 1rem;
  color: #ff4d4f;
  text-align: center;
}
</style>