<script setup>
import { ref,onMounted} from 'vue';
import axios, { Axios } from 'axios';
// API地址http://127.0.0.1:8000
// 组件加载后立即获取
onMounted(async ()=>{
    await GetStu();
})
// http://127.0.0.1/get_stu 获取数据库
const students =ref([])    //储存信息列表
const GetStu =async ()=>{
    try{
        const rep=await axios.get('http://127.0.0.1:8000/get_stu')
        students.value=rep.data.data;
    }catch(error){
        alert('页面获取失败')
        console.log(error)
    };
    
}

// 添加
const newstuden=ref({id:'',name:'',clas:'',time:'',cre:''})
const NewStu=async ()=>{
    try{
        await axios.post('http://127.0.0.1:8000/post_stu',null,{params:newstuden.value})
        await GetStu()   //添加完新数据，重新更新一遍页面
        // clearFrom(newstuden.value)
        
    }catch(error){
        console.log("创建失败",error)
    }
}
// 删除
const delstu=ref({id:''})
const DelStu=async ()=>{
    try{
        await axios.delete('http://127.0.0.1:8000/delete_stu',null,{params:delstu.value})
        await GetStu()

    }catch(error){
        console.log("删除失败",error)
    }
}

</script>

<template>
    <h1 id="h">FastAPI_Stu</h1>
<!-- 表格 -->
<table border="2px" cellpadding="8" id="stu_table">
    <thead>
        <tr>
            <th>学号</th>
            <th>姓名</th>
            <th>班级</th>
            <th>时间</th>
            <th>创建人</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="student in students" :key="student.STUDENT_ID">
            <td>{{student.STUDENT_ID}}</td>
            <td>{{ student.NAME }}</td>
            <td>{{ student.CLASS }}</td>
            <td>{{ student.CREATED_TIME }}</td>
            <td>{{ student.CREATOR }}</td>
        </tr>
    </tbody>
</table>

  <!-- 添加 -->
 <div>
    <form @submit.prevent="NewStu">
        <input v-model="newstuden.id" placeholder="学号">
        <input v-model="newstuden.name" placeholder="姓名">
        <input v-model="newstuden.clas" placeholder="班级">
        <input v-model="newstuden.time" placeholder="创建时间">
        <input v-model="newstuden.cre" placeholder="创建人">
        <button id="new_stu">添加</button>
    </form>
 </div>
 <br>
 <!-- 删除 -->
 <div>
    <form @submit.prevent="DelStu">
        <input v-model="delstu.id" placeholder="删除学号">
        <button id="del_stu">删除</button>
    </form>
 </div>
</template>



<style>
#h{
    text-shadow: 5px 5px 5px #00ffb3;
}
#del_div{
    margin: 0 auto;
}
#new_stu{
    background-color: chartreuse;
}
#del_stu{
    background-color: brown;
}
#stu_table{
    background-color:rgba(9, 235, 216, 0.945);
    margin: auto;
}
</style>