<script setup>
import {ref} from 'vue'
import axios from 'axios';
const updata=ref({list:'',data:'',id:''})
const UpData=async()=>{
    try{
        const list=updata.value.list
        const data=updata.value.data
        const id=updata.value.id
        await axios.put('http://127.0.0.1:8000/put_stu',null,{params:{list,data,id}})
        newstuden.value={id:'',name:'',clas:'',time:'',cre:''}
    }catch(error){
        console.log("更新失败",error)
    }
}
</script>

<template>
     <!-- <form @submit.prevent="UpData">
        <input v-model="updata.list" placeholder="字段">
        <input v-model="updata.data" placeholder="更新内容">
        <input v-model="updata.id" placeholder="学号">
        <button>更新</button>
    </form> -->
    <div class="putstu">
        <el-form label-width="auto"  style="max-width: 400px">
            <el-form-item label="字段">
                <el-input v-model="updata.list"/>
            </el-form-item>
            <el-form-item label="更新内容">
                <el-input v-model="updata.data"/>
            </el-form-item>
            <el-form-item label="学号">
                <el-input v-model="updata.id"/>
            </el-form-item>
            <el-button type='warning' @click="UpData">更新</el-button>
        </el-form>
    </div>
</template>

<style>
</style>