import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import("../views/LoginVite.vue")
  },
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeVite.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router