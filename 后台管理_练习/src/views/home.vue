<script setup>
import { ref, watch, watchEffect } from "vue"
import { useRoute } from "vue-router";
import { useRouter } from "vue-router";
import {useUserStore} from '../stores/user';

const route = useRoute();
const routes = useRouter();
const titlelist = ref([]);
// 监听路由变化，更新标题
watchEffect(()=>{
  titlelist.value = route.matched
})
// console.log(titlelist.value);

// 获取pinia存储用户
const userStore = useUserStore();
// console.log("首页用户信息:", userStore.getUser().roles);
const roles = ref(userStore.getUser().roles);

// 退出登录
const loginout = () => {
  userStore.clearUser(); // 清空用户信息
  routes.push('/');
}
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
        <!-- 权限：0超级管理员，1普通管理员，2普通用户 -->
          <el-menu-item index="/home/stats" v-if="roles==1 || roles==2 || roles==0">
            <el-icon><House /></el-icon>
            <span>首页</span>
          </el-menu-item>

          <el-menu-item index="/home/oder" v-if="roles==0 || roles==1">
            <el-icon><Document /></el-icon>
            <span>订单管理</span>
          </el-menu-item>
          
          <el-sub-menu index="3" v-if="roles==0">
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

          <el-menu-item index="/home/user" v-if="roles==0">
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
          <el-button class="loginout" type="info" @click="loginout">退出登录</el-button>
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
.loginout {
  position: absolute;
  right: 30px;
}
</style>