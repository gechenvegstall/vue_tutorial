<script setup>
import { ref } from "vue";

</script>

<template>
  <div class="common-layout">
    <!-- 导航区 -->
    <el-container style="height: 100vh">
      <el-aside width="200px" style="height: 100%">
        <el-menu style="height: 100%;"
        active-text-color="#ffd04b"
        background-color="#545c64"
        default-active="2"
        text-color="#fff"
        >
          <el-menu-item index="1">
            <el-icon><icon-menu /></el-icon>
            <span>首页</span>
          </el-menu-item>

          <el-menu-item index="2">
            <el-icon><icon-menu /></el-icon>
            <span>订单管理</span>
          </el-menu-item>
          
          <el-sub-menu index="3">
            <template #title>
              <el-icon><location /></el-icon>
              <span>商品管理</span>
            </template>
              <el-menu-item index="3-1">商品分类</el-menu-item>
              <el-menu-item index="3-2">商品列表</el-menu-item>
          </el-sub-menu>

          <el-menu-item index="4">
            <el-icon><setting /></el-icon>
            <span>用户管理</span>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <el-container>
        <!-- 头部 -->
        <el-header>Header</el-header>
        <!-- 内容 -->
        <el-main>Main</el-main>
      </el-container>
    </el-container>
  </div>
</template>


<style scoped>

</style>