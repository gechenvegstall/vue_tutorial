import { createRouter, createWebHistory } from 'vue-router';
import { useUserStore } from '../stores/user'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import('../views/login.vue')
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('../views/home.vue'),
    meta: {
      title: '后台管理系统',
    },
    children:[
      {
        path:'/home/stats',
        name: 'Stats',
        component: () => import('../views/stats.vue'),
        meta: {
          title: '首页'
        }
      },
      {
        path:'/home/oder',
        name: 'Order',
        component: () => import('../views/oder.vue'),
        meta: {
          title: '订单管理'
        }
      },
      {
        path:'/home/goodtype',
        name: 'GoodType',
        component: () => import('../views/goodtype.vue'),
        meta: {
          title: '商品分类'
        }
      },
      {
        path:'/home/goodlist',
        name: 'GoodList',
        component: () => import('../views/goodlist.vue'),
        meta: {
          title: '商品列表'
        }
      },
      {
        path:'/home/user',
        name: 'User',
        component: () => import('../views/user.vue'),
        meta: {
          title: '用户管理'
        }
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// 全局前置守卫
router.beforeEach((to, from, next) => {
  const userStore = useUserStore();
  if (to.path === '/') {
    next();
  } else {
    if (userStore.user.username || userStore.user.password) {
      // 如果用户已登录，允许访问其他路由
      next();
    } else {
      next('/');
    }
  }
});
export default router;
