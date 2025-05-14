<script setup>
import {ref} from 'vue'
import axios from 'axios';

const newstuden=ref({id:'',name:'',clas:'',cre:''})
const NewStu=async ()=>{
    try{
        await axios.post('http://127.0.0.1:8000/post_stu',null,{params:newstuden.value})
        newstuden.value={id:'',name:'',clas:'',cre:''}
        alert("添加成功")
    }catch(error){
        console.log("创建失败",error)
    }
}

</script>

<template>
    <form @submit.prevent="NewStu">
        <input v-model="newstuden.id" placeholder="学号">
        <input v-model="newstuden.name" placeholder="姓名">
        <input v-model="newstuden.clas" placeholder="班级">
        <input v-model="newstuden.cre" placeholder="创建人">
        <button id="new_stu">添加</button>
    </form>
</template>