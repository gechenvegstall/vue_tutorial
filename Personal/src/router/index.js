import {createRouter, createWebHistory} from 'vue-router'

const routes=[
    {
        path:'/',
        name:'Home',
        component: () => import('../App.vue')
    },
    {
        path:'/home',
        name:'Home',
        component: () => import('../views/home.vue')
    },
    {
        path:'/Login',
        name:'Login',
        component: () => import('../views/Login.vue')

    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
