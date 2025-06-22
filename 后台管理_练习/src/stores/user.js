import {defineStore} from 'pinia'
import {ref, computed} from 'vue'


export const useUserStore = defineStore('user', () => {
  const user = ref({
    username: null,
    password: null,
    roles: null
  })
  const isAuthenticated = computed(() => !!user.value)
  // 存储用户信息
  function setUser(newUser) {
    user.value = newUser
    // 存储用户到本地
  localStorage.setItem('user', JSON.stringify(user.value))
  }
// 取用户信息
  function getUser() {
    return user.value
  }
// 清除用户信息
  function clearUser() {
    user.value = {}
    // 清除本地存储的用户信息
    localStorage.removeItem('user')
  }

// 从本地存储中获取用户信息
function inituser(){
  const userData = localStorage.getItem('user')
  if (userData){
    user.value = JSON.parse(userData)
  }
}
inituser()

  return {
    user,
    isAuthenticated,
    setUser,
    getUser,
    clearUser
    ,inituser
  }
})