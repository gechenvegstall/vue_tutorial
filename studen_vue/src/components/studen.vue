<template>
    <div class="container">
      <h1>学生管理系统</h1>
  
      <!-- 添加学生表单 -->
      <div class="form-group">
        <input
          v-model="newStudent.id"
          type="text"
          placeholder="学号"
          class="input"
        />
        <input
          v-model="newStudent.name"
          type="text"
          placeholder="姓名"
          class="input"
        />
        <input
          v-model="newStudent.clas"
          type="text"
          placeholder="班级"
          class="input"
        />
        <input
          v-model="newStudent.time"
          type="text"
          placeholder="时间"
          class="input"
        />
        <input
          v-model="newStudent.cre"
          type="text"
          placeholder="创建者"
          class="input"
        />
        <button @click="createStudent">添加学生</button>
      </div>
  
      <!-- 学生列表 -->
      <table class="student-table">
        <thead>
          <tr>
            <th>学号</th>
            <th>姓名</th>
            <th>班级</th>
            <th>时间</th>
            <th>创建者</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="student in students" :key="student.STUDENT_ID">
            <td>{{ student.STUDENT_ID }}</td>
            <td>{{ student.NAME }}</td>
            <td>{{ student.CLASS }}</td>
            <td>{{ student.TIME }}</td>
            <td>{{ student.CREATOR }}</td>
            <td>
              <button @click="editStudent(student)" class="btn-edit">编辑</button>
              <button @click="deleteStudent(student.STUDENT_ID)" class="btn-delete">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
  
      <!-- 编辑模态框 -->
      <div v-if="showEditModal" class="modal">
        <div class="modal-content">
          <span @click="showEditModal = false" class="close">&times;</span>
          <h2>编辑学生信息</h2>
          <input
            v-model="editedStudent.id"
            type="text"
            placeholder="学号"
            class="input"
          />
          <input
            v-model="editedStudent.name"
            type="text"
            placeholder="姓名"
            class="input"
          />
          <input
            v-model="editedStudent.clas"
            type="text"
            placeholder="班级"
            class="input"
          />
          <input
            v-model="editedStudent.time"
            type="text"
            placeholder="时间"
            class="input"
          />
          <input
            v-model="editedStudent.cre"
            type="text"
            placeholder="创建者"
            class="input"
          />
          <button @click="updateStudent">保存修改</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  // 配置 API 基础地址
  const API_BASE_URL = 'http://localhost:8000'; // 确保和你的 FastAPI 端口一致
  
  // 状态管理
  const students = ref([]);
  const newStudent = ref({
    id: '',
    name: '',
    clas: '',
    time: '',
    cre: ''
  });
  const editedStudent = ref({
    id: '',
    name: '',
    clas: '',
    time: '',
    cre: ''
  });
  const showEditModal = ref(false);
  
  // 生命周期钩子：组件挂载后获取学生列表
  onMounted(async () => {
    await fetchStudents();
  });
  
  // 获取学生列表
  const fetchStudents = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/get_stu`);
      students.value = response.data.data;
    } catch (error) {
      console.error('获取学生列表失败', error);
    }
  };
  
  // 创建学生
  const createStudent = async () => {
    try {
      await axios.post(`${API_BASE_URL}/post_stu`, {
        id: newStudent.value.id,
        name: newStudent.value.name,
        clas: newStudent.value.clas,
        time: newStudent.value.time,
        cre: newStudent.value.cre
      });
      await fetchStudents();
      clearForm(newStudent.value);
    } catch (error) {
      console.error('创建学生失败', error);
    }
  };
  
  // 删除学生
  const deleteStudent = async (id) => {
    try {
      await axios.delete(`${API_BASE_URL}/delete_stu`, {
        params: { id }
      });
      await fetchStudents();
    } catch (error) {
      console.error('删除学生失败', error);
    }
  };
  
  // 编辑学生（打开模态框）
  const editStudent = (student) => {
    editedStudent.value = {
      id: student.STUDENT_ID,
      name: student.NAME,
      clas: student.CLASS,
      time: student.TIME,
      cre: student.CREATOR
    };
    showEditModal.value = true;
  };
  
  // 更新学生
  const updateStudent = async () => {
    try {
      // 这里需要根据不同字段调用对应的更新接口
      // 示例：更新姓名
      await axios.put(`${API_BASE_URL}/put_stu`, {
        list: 'NAME', // 可以扩展为选择不同字段
        data: editedStudent.value.name,
        id: editedStudent.value.id
      });
      await fetchStudents();
      showEditModal.value = false;
    } catch (error) {
      console.error('更新学生失败', error);
    }
  };
  
  // 清空表单
  const clearForm = (form) => {
    form.id = '';
    form.name = '';
    form.clas = '';
    form.time = '';
    form.cre = '';
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .form-group {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  .input {
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  .student-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  .student-table th,
  .student-table td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  .student-table td {
    white-space: nowrap;
  }
  
  .btn-edit {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 4px;
    margin-right: 5px;
    cursor: pointer;
  }
  
  .btn-delete {
    background-color: #f44336;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .modal {
    display: none; /* 初始隐藏 */
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0,0,0,0.4);
  }
  
  .modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 50%;
    position: relative;
  }
  
  .close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    position: absolute;
    top: 10px;
    right: 15px;
    cursor: pointer;
  }
  </style>