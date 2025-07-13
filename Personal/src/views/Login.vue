<template>
    <div class="login-container">
        <h3>登录</h3>
        <el-form label-width="80px" :model="UserForm" :rules="LoginRules" ref="loginForm">
            <el-form-item label="用户名" prop="username">
                <el-input v-model="UserForm.username" placeholder="请输入用户名" ></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="UserForm.password" placeholder="请输入密码"></el-input>
            </el-form-item>
            <!-- <el-form-item label="验证码">
                <el-input v-model="captcha" placeholder="请输入验证码"></el-input>
                <img src="captcha_url" alt="验证码" @click="refreshCaptcha" style="cursor: pointer;">
            </el-form-item> -->
            <el-form-item>
                <el-button type="primary" @click="login">登录</el-button>
            </el-form-item>
            <el-form-item>
            <div class="flex justify-between w-full">
                <el-button type="primary" @click="register">注册</el-button>
                <el-button type="info" @click="forget">忘记密码</el-button>
            </div>
            </el-form-item>
        </el-form>
    </div>
</template>

<script setup>
import { ElMessage } from 'element-plus';
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
// 使用路由
const router = useRouter();
// 定义表单变量
const UserForm = reactive({
    username: '',
    password: ''
});
// 定义表单规则
const LoginRules=({
    username: [
        { required: true, message: '请输入用户名', trigger: 'red' },
        { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'red' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'red' },
        { min: 6, max: 10, message: '长度在 6 到 10 个字符', trigger:'red'}
    ]
})
// 校验是否符合规则
const loginForm = ref(null);
const login=()=>{
    loginForm.value.validate((valid)=>{
        if(valid){
            axios.post("http://127.0.0.1:8000/login", UserForm).then((response)=>{
              console.log("aaaaaaaa");
            }).catch((error)=>{
                console.error(error);
                ElMessage.error('登录失败，请稍后再试');
            })
        }
    })
}
</script>

<style>
.login-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 40px;
    border: 1px solid #ece2e2;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(199, 194, 194, 0.1);
}
.login-container h1 {
    text-align: center;
    margin-bottom: 16px;
}
.login-container .el-form-item {
    margin-bottom: 15px;
}
.login-container .el-button {
    width: 100%;
}
.flex {
  display: flex;
}

.justify-between {
  justify-content: space-between;
}

.w-full {
  width: 100%;
}
</style>