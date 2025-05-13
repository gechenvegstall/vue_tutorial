<script setup>
import { ref,onMounted } from 'vue';
import axios from 'axios';
onMounted(async ()=>{
    await getStu()
})
const students = ref([]);
const getStu = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/get_stu');
        students.value = response.data.data;
    } catch (error) {
        alert("页面获取失败",error)
    }
};
</script>

<template>
    <div>
        <el-table :data="students" border>
        <el-table-column prop="STUDENT_ID" label="学号"></el-table-column>
        <el-table-column prop="NAME" label="姓名"></el-table-column>
        <el-table-column prop="CLASS" label="班级"></el-table-column>
        <el-table-column prop="CREATED_TIME" label="创建时间"></el-table-column>
        <el-table-column prop="CREATOR" label="创建人"></el-table-column>
   </el-table>
    </div>
</template>

<style></style>