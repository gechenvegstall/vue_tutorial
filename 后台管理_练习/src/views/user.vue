<script setup>
import { ref,onMounted} from 'vue';
import { ElMessageBox } from 'element-plus';
import axios from 'axios';
// 对话框显示状态
const dialogVisible = ref(false);
onMounted(async () => {
    // 获取用户列表
    await getuser();
});


// 用户列表
let userList = ref([]);
const getuser=async()=>{
    try{
            await axios.get("http://127.0.0.1:8080/users").then((res) => {
            userList.value = res.data;
            // console.log("获取后端数据",userList.value);
        })
    } catch(err){
        console.error("获取用户列表失败:", err);
        ElMessageBox.confirm("获取用户列表失败，请联系后台管理人员", "警告", {
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            type: "error",
        });
    }
}


let dialogType = ref("add");
// 添加用户获取表单内容
let form=ref({})
// 添加用户按钮
function adduser() {
    dialogVisible.value = true;
    dialogType.value = "add";
    form.value = {};
}
// 操作
function postuser(row) {
    dialogVisible.value = true;
    dialogType.value = "chang";
    // 将当前行的数据浅拷贝赋值给form
    form.value = { ...row };
}

// 删除用户
// row 当前行数据
function deleteUser(row) {
    // 先显示确认对话框
    ElMessageBox.confirm(
        `此操作将永久删除--${row.username}, 是否继续?`,
        "警告",
        {
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            type: "error",
        }
    )
    .then(() => {
        // 用户点击了"确定"，此时再发送删除请求
        return axios.delete("http://127.0.0.1:8080/delete_user", { 
            data: { id: row.id } 
        });
    })
    .then((res) => {
        // 删除请求成功返回
        // console.log("删除用户成功:", res.data);
        getuser(); // 刷新用户列表
    })
    .catch((err) => {
        // 如果是用户取消了操作，err会包含特定信息
        if (err && err.toString() === "cancel") {
            console.log("取消删除用户");
        } else {
            // 处理删除请求失败的情况
            console.error("删除用户失败:", err);
        }
    });
}

// 提交，添加或者修改的用户
function subUser(){
    dialogVisible.value = false;
    if(dialogType.value == "add"){
        axios.post("http://127.0.0.1:8080/post_user",form.value).then((res)=>{
            // console.log("添加用户成功:", res.data);
            getuser();
        }).catch((err) => {
            ElMessageBox.confirm("添加用户失败，请联系后台管理人员", "警告", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "error",
            }).then(() => {
                console.error("添加用户失败:", err);
            });
        });
    } else {
        axios.put("http://127.0.0.1:8080/put_user", form.value).then((res) => {
            // console.log("修改用户成功:", res.data);
            getuser();
        }).catch((err) => {
            ElMessageBox.confirm("修改用户失败，请联系后台管理人员", "警告", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "error",
            }).then(() => {
                console.error("修改用户失败:", err);
            });
        });
    }
}
</script>

<template>
    <!-- 添加用户的按钮 -->
    <el-button type="primary" @click="adduser" style="margin: 15px 0;">添加用户</el-button>
    <!-- 用户列表 -->
     <el-table :data="userList" border stripe>
        <el-table-column prop="id" label="序号" width="60"></el-table-column>
        <el-table-column prop="username" label="用户"></el-table-column>
        <el-table-column prop="password" label="密码"></el-table-column>
        <el-table-column prop="roles" label="权限">
            <!-- 标签,插槽 -->
            <template #default="scope">
              <el-tag v-if="scope.row.roles == 2" type="warning">普通管理员</el-tag>
              <el-tag v-else-if="scope.row.roles == 1" type="info">普通用户</el-tag>
              <el-tag v-else="scope.row.roles == 0">超级管理员</el-tag>
            </template>
        </el-table-column>
        <!-- 操作列 -->
        <el-table-column label="操作">
            <template #default="scope">
                <el-button
                type="primary"
                size="small"
                icon="edit"
                @click="postuser(scope.row)">
                编辑
                </el-button>
                <el-button 
                type="danger"
                size="small"
                icon="delete"
                @click="deleteUser(scope.row)">
                删除
                </el-button>
            </template>
        </el-table-column>
     </el-table>

     <!--点击添加用户按钮弹出对话框  -->
     <el-dialog
        v-model="dialogVisible"
        :title="dialogType == 'add' ? '添加用户' : '修改用户'"
        width="30%"
        align-center
        >
        <el-form :model="form" label-width="80px">
            <el-form-item label="用户">
              <el-input v-model="form.username"></el-input>
            </el-form-item>
            <el-form-item label="密码">
              <el-input v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item label="用户权限">
                <el-radio-group v-model="form.roles">
                  <el-radio label=0>超级管理员</el-radio>
                  <el-radio label=1>普通管理员</el-radio>
                  <el-radio label=2>普通用户</el-radio>
                </el-radio-group>
            </el-form-item>
        </el-form>
        <template #footer>
            <el-button @click="dialogVisible = false">取消</el-button>
            <el-button type="primary" @click="subUser">添加</el-button>
        </template>
    </el-dialog>
</template>