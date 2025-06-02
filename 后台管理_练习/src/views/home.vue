<script setup>
import { ref, watch, watchEffect } from "vue"
import { useRoute } from "vue-router";

const route = useRoute();
const titlelist = ref([]);
// 监听路由变化，更新标题
watchEffect(()=>{
  titlelist.value = route.matched
})
console.log(titlelist.value);

</script>

<template>
  <div class="common-layout">
    <!-- 导航区 -->
    <el-container style="height: 100vh">
      <el-aside width="200px" style="height: 100%">
        <el-menu style="height: 100%;"
        active-text-color="#ffd04b"
        background-color="#545c64"
        :default-active="$route.path"
        text-color="#fff"
        router
        >
          <el-menu-item index="/home/stats">
            <el-icon><House /></el-icon>
            <span>首页</span>
          </el-menu-item>

          <el-menu-item index="/home/oder">
            <el-icon><Document /></el-icon>
            <span>订单管理</span>
          </el-menu-item>
          
          <el-sub-menu index="3">
            <template #title>
              <el-icon><Location /></el-icon>
              <span>商品管理</span>
            </template>
            <el-menu-item index="/home/goodtype">
              <el-icon><Operation /></el-icon>
              <span>商品分类</span>
            </el-menu-item>
            <el-menu-item index="/home/goodlist">
              <el-icon><Grid /></el-icon>
              <span>订单列表</span>
            </el-menu-item>
          </el-sub-menu>

          <el-menu-item index="/home/user">
            <el-icon><Avatar /></el-icon>
            <span>用户管理</span>
          </el-menu-item>
          </el-menu>
      </el-aside>

      <el-container>

        <!-- 头部 -->
        <el-header>
          <el-breadcrumb separator="/">
            <el-breadcrumb-item v-for="item in titlelist" :key="item.path">
              {{ item.meta.title }}
            </el-breadcrumb-item>
          </el-breadcrumb>
        </el-header>


        <!-- 内容 -->
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>


<style >
.el-header {
  background-color: #82868a;
  color: #fff;
  line-height: 45px;
  height: 45px;
  display: flex;
  align-items: center;
}
</style>