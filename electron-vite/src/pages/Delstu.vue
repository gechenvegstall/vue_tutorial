<script setup>
import {ref} from 'vue'
import axios from 'axios';
const delstu=ref({id:''})
const DelStu=async()=>{
    try{
        const id=delstu.value.id
        await axios.delete('http://127.0.0.1:8000/delete_stu',{params:{id}})
    }catch(error){
        console.log("删除失败",error)
    }
}
</script>

<template>
    <form @submit.prevent="DelStu">
        <input v-model="delstu.id" placeholder="学号">
        <button>删除</button>
    </form>
</template>

<style></style>