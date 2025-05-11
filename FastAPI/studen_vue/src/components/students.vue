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
</script>

<template>
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
</template>



<style>
#stu_table{
    background-color:rgba(9, 235, 216, 0.945);
    margin: auto;
}
</style>