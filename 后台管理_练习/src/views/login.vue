<script setup>
import { ref,reactive} from "vue";
import {useRouter} from "vue-router";
import axios from "axios";
import { ElMessage } from "element-plus";
const router=useRouter()
const form = reactive({
    username: "admin",
    password: "admin123"
})
// 定义表单规则
const rules=ref({
    username:[
        { required: true, message: "请输入用户名", trigger: "blur" },
        { min: 2, max: 10, message: "长度在 2 到 10 个字符", trigger: "blur" }
    ],
    password:[
        { required: true, message: "请输入密码", trigger: "blur" },
        { min: 3, max: 10, message: "长度在 3 到 10 个字符", trigger: "blur" }
    ]
})
// 校验是否符合规则
const loginForm = ref(null);
const login = ()=>{
    loginForm.value.validate((valid) => {
        if (valid) {
            // 添加登录逻辑
            axios.post("http://127.0.0.1:8080/login",form).then((response) => {
                console.log(response.data);
                // 登录成功跳转页面
                router.push("/home/stats");
            }).catch((error) => {
                // 登录失败提示
                console.error("登录失败:", error);
                ElMessage.error("登录失败，请检查用户名或密码");
            });
        } else {
            console.log("登录失败");
        }
    });
}
// 重置表单
const replace = ()=>{
    loginForm.value.resetFields();
}
</script>

<template>
  <div>
    <el-row>
        <el-col :span="16" class="left">
            <h1>Welcome</h1>
        </el-col>
        <el-col :span="8" class="right">
            <el-card shadow="always">
                <el-form label-position="top" :model="form" :rules="rules" status-icon ref="loginForm">
                    <el-form-item label="用户名" prop="username">
                        <el-input v-model="form.username"></el-input>
                    </el-form-item>
                    <el-form-item label="密码" prop="password">
                        <el-input v-model="form.password" type="password" show-password></el-input>
                    </el-form-item>
                </el-form>
                <div class="button">
                    <el-button type="primary" @click="login">登录</el-button>
                    <el-button type="info" @click="replace">重置</el-button>
                </div>
            </el-card>
        </el-col>
    </el-row>
  </div>
</template>

<style>
.left {
  background-color: #188be9a1;
  height: 100vh;
  color: #f1ebeb;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size:30px;
}
.right {
  background-color: #dfd9d9be;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.el-card {
  height: auto;
  width: 400px;
}
.button{
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>