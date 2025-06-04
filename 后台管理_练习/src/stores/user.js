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
  }
// 取用户信息
  function getUser() {
    return user.value
  }
// 清除用户信息
  function clearUser() {
    user.value = {}
  }

  return {
    user,
    isAuthenticated,
    setUser,
    getUser,
    clearUser
  }
})