<script setup lang="ts" name="'App'">
import { RouterView,RouterLink } from 'vue-router';
import students  from './components/students.vue';
</script>

<template>
    
    <div>
        <h1 id="h">Fast_API</h1>
        <students></students>
        <!-- 导航区 -->
        <div class="nav">
            <router-link :to="{path:'/into'}">添加用户</router-link>
            <router-link :to="{path:'/del'}">删除用户</router-link>
            <router-link :to="{path:'/up'}">更新用户</router-link>
        </div>

        <!-- 展示区 -->
        <RouterView></RouterView>
    </div>
</template>

<style>
#h{
    text-shadow: 5px 5px 5px #00ffb3;
}
.nav{
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
    background-color: #f3f4f6;
    border-radius: 0.5rem;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}
</style>