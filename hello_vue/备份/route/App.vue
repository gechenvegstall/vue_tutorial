<script setup lang="ts" name="App">
import { RouterView,RouterLink } from 'vue-router';
</script>

<template>
    <div class="app">
        <h2>vue3路由测试</h2>
        <!-- 导航区 -->
        <div>
            <router-link to="/home">Home</router-link>
            <router-link to="/news">News</router-link>
            <router-link to="/about">About</router-link>
        </div>
        <!-- 展示区 -->
        <div>
            <router-view></router-view>
        </div>
    </div>
</template>

<style>
</style> 