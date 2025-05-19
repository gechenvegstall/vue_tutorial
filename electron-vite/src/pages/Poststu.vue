<script setup>
import {ref} from 'vue'
import axios from 'axios';

const newstuden=ref({id:'',name:'',clas:'',cre:''})
const NewStu=async ()=>{
    try{
        await axios.post('http://127.0.0.1:8000/post_stu',null,{params:newstuden.value})
        newstuden.value={id:'',name:'',clas:'',cre:''}
    }catch(error){
        console.log("创建失败",error)
    }
}

</script>

<template>
    <!-- <form @submit.prevent="NewStu">
        <input v-model="newstuden.id" placeholder="学号">
        <input v-model="newstuden.name" placeholder="姓名">
        <input v-model="newstuden.clas" placeholder="班级">
        <input v-model="newstuden.cre" placeholder="创建人">
        <button>添加</button>
    </form> -->
    <div>
        <el-form label-width="auto"  style="max-width: 400px">
            <el-form-item label="学号">
                <el-input v-model="newstuden.id"/>
            </el-form-item>
            <el-form-item label="姓名">
                <el-input v-model="newstuden.name"/>
            </el-form-item>
            <el-form-item label="班级">
                <el-input v-model="newstuden.clas"/>
            </el-form-item>
            <el-form-item label="创建人">
                <el-input v-model="newstuden.cre"/>
            </el-form-item>
            <el-button type='primary' @click="NewStu">添加</el-button>
        </el-form>
    </div>
</template>