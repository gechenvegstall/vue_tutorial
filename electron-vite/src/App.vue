<script setup>

</script>

<template>
    <div class="header">
      <h2>学生管理系统</h2>
    </div>
    <!-- 导航区 -->
    <div>
    <el-menu :default-active="activeIndex" mode="horizontal" class="nav" router>
      <el-menu-item index="/">主页</el-menu-item>
      <el-sub-menu index="">
        <template #title>学生信息</template>
        <el-menu-item index="/poststu">添加学生</el-menu-item>
        <el-menu-item index="/putstu">更新学生</el-menu-item>
        <el-menu-item index="/delstu">删除学生</el-menu-item>
      </el-sub-menu>
      <el-menu-item index="/watchstu">查看信息</el-menu-item>
      <el-menu-item index="/about">关于</el-menu-item>
    </el-menu>
    </div>
    <!-- 展示区 -->
    <div>
      <router-view></router-view>
    </div>
</template>

<style>
.nav{
  background-color:#2d80d3
}
.header {
  background-color: #F1F1F1;
  text-align: center;
  padding: 20px;
}

</style>