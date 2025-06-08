<script setup>
import { ElMessageBox } from "element-plus";
import {  ref } from "vue";

const dialogVisible = ref(false);

let list = ref([
  { type: "手机", desc: "手机类商品", canUse: true },
  { type: "电脑", desc: "电脑类商品", canUse: true },
  { type: "家电", desc: "家电类商品", canUse: true },
  { type: "服装", desc: "服装类商品", canUse: true },
  { type: "食品", desc: "食品类商品", canUse: true },
  { type: "家具", desc: "家具类商品", canUse: true },
]);
let form = ref({});
let dialogType = ref("add");

function addType() {
  // 弹出对话框，让用户添加
  dialogVisible.value = true;
  dialogType.value = "add";
  form.value = {};
}
function changType(row) {
  // 弹出对话框，让用户修改
  dialogVisible.value = true;
  dialogType.value = "chang";
  // 将当前行的数据浅拷贝赋值给form
  form.value = { ...row };
}
// 删除某条数据
function deleteType(row) {
  // 删除之前使用elementplus给个弹窗确认

  ElMessageBox.confirm(`此操作将永久删除--${row.type}, 是否继续?`, "警告", {
    confirmButtonText: "确定",
    cancelButtonText: "取消",
    type: "error",
  }).then(() => {
    // 删除当前行
    list.value.forEach((item, index) => {
      if (item.type == row.type) {
        list.value.splice(index, 1);
      }
    });
  });
}
// 提交，添加或者修改的分类
function submit() {
  dialogVisible.value = false;
  if (dialogType.value == "add") {
    list.value.push(form.value);
  } else {
    list.value.forEach((item, index) => {
      if (item.type == form.value.type) {
        list.value[index] = form.value;
      }
    });
  }
}
</script>
<template>
  <!-- 添加分类的按钮 -->
  <el-button type="primary" @click="addType" style="margin: 15px 0"
    >添加商品分类</el-button
  >
  <!-- 使用table表格显示分类列表 -->
  <el-table :data="list" border stripe>
    <el-table-column type="index" width="60" label="序号" />
    <el-table-column prop="type" label="商品分类" />
    <el-table-column prop="desc" label="分类描述" />
    <el-table-column prop="canUse" label="是否禁用">
      <template #default="scope">
        <el-tag :type="scope.row.canUse ? 'success' : 'danger'"
          >{{ scope.row.canUse ? "可用" : "禁用" }}
        </el-tag>
      </template>
    </el-table-column>
    <!-- 增加操作列 -->
    <el-table-column label="操作">
      <template #default="scope">
        <el-button
          type="primary"
          size="small"
          icon="edit"
          @click="changType(scope.row)"
          >编辑</el-button
        >
        <el-button
          type="danger"
          icon="delete"
          size="small"
          @click="deleteType(scope.row)"
          >删除</el-button
        >
      </template>
    </el-table-column>
  </el-table>

  <!-- 使用dialog对话框添加商品 -->
  <el-dialog
    v-model="dialogVisible"
    :title="dialogType == 'add' ? '添加商品分类' : '修改商品分类'"
    width="500"
    align-center
  >
    <!-- 添加商品的表单 -->
    <el-form :model="form" label-width="80px">
      <el-form-item label="商品分类">
        <el-input v-model="form.type" />
      </el-form-item>
      <el-form-item label="分类描述">
        <el-input v-model="form.desc" />
      </el-form-item>
      <el-form-item label="是否禁用">
        <el-switch v-model="form.canUse" />
      </el-form-item>
    </el-form>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="submit"> 确定 </el-button>
      </div>
    </template>
  </el-dialog>
</template>