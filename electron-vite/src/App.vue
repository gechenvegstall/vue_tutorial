<script setup>
import Students from './components/students.vue';

</script>

<template>
  <h2>学生管理系统</h2>
  <el-menu :default-active="activeIndex" mode="horizontal" class="nav">
    <el-menu-item index="1">主页</el-menu-item>
    <el-sub-menu index="2">
      <template #title>学生信息</template>
      <el-menu-item index="2-1">添加学生</el-menu-item>
      <el-menu-item index="2-2">更新学生</el-menu-item>
      <el-menu-item index="2-3">删除学生</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="3">查看信息</el-menu-item>
    <el-menu-item index="3">关于</el-menu-item>
  </el-menu>
  <div id="app">
    <Students />
  </div>
</template>

<style>
.nav{
  background-color:#545c64
}
</style>