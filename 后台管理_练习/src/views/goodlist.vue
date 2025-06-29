<template>
  <!-- 添加订单按钮 -->
   <el-button type="primary" @click="addgood" style="margin: 15px 0;">添加商品</el-button>
   <!-- 点击添加按钮弹出对话框 -->
    <el-dialog
    v-model="dialogVisible"
    :title="addtype == 'add' ? '添加商品' : '修改商品'"
    width="30%"
    align-center>
    <el-form :model="posttable" label-width="80px">
      <el-form-item label="商品名">
        <el-input v-model="posttable.goods"></el-input>
      </el-form-item>
      <el-form-item label="产地">
        <el-input v-model="posttable.address"></el-input>
      </el-form-item>
      <el-form-item label="状态">
        <el-select v-model="posttable.state" placeholder="请选择状态">
          <el-option label="在售" value="1"></el-option>
          <el-option label="下架" value="-1"></el-option>
          <el-option label="预售" value="0"></el-option>
          <el-option label="缺货" value="-2"></el-option>
        </el-select>
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="dialogVisible = false">取消</el-button>
      <el-button type="primary" @click="posttables">确定</el-button>
    </template>
  </el-dialog>
   <div style="float: right;">
    <el-input placeholder="搜索商品" 
      v-model="search" 
      style="width: 280px;" 
      @keyup.enter="searchgood" 
      clearable
      @clear="searchgood"></el-input>
      <el-button type="primary" @click="searchgood">搜索</el-button>
    </div> 
  <el-table :data="tableslist" stripe style="width: 100%">
    <el-table-column prop="date" label="日期" width="180"  sortable />
    <el-table-column prop="goods" label="商品名" width="180" />
    <el-table-column prop="address" label="产地" />
    <el-table-column prop="state" label="状态" :filters="[
        { text: '在售', value: '1' },
        { text: '下架', value: '-1' },
        { text: '预售', value: '0' },
        { text: '缺货', value: '-2' }
    ]"
    :filter-method="fillertag">
        <!-- 插槽 -->
         <template #default="scope">
            <el-tag :type="tag(scope.row.state)">{{ statustext(scope.row.state) }}</el-tag>
         </template>
    </el-table-column>
    <!-- 操作 列 -->
    <el-table-column label="操作">
      <template #default="scope">
        <el-button
          type="primary"
          size="small"
          icon="edit"
          @click="postgood(scope.row)">
          编辑
        </el-button>
        <el-button 
          type="danger"
          size="small"
          icon="delete"
          @click="deletegood(scope.row)">
          删除
        </el-button>
      </template>
    </el-table-column>
  </el-table>
  <!-- 分页 -->
   <el-pagination
      v-model:current-page="currentPage4"
      v-model:page-size="pageSize4"
      :page-sizes="[2, 4, 6, 8]"
      layout="total, sizes, prev, pager, next, jumper"
      :total="tableData.length"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
</template>

<script setup>
import { ElMessage, ElMessageBox } from 'element-plus'
import { computed, ref,onMounted} from 'vue'
import axios from 'axios'
// 生命周期函数
onMounted(() => {
  // 页面加载在获取订单表
  getlist()
})
let addtype = ref('add')
// 对话框状态
const dialogVisible = ref(false)
// 添加按钮
function addgood() {
  addtype.value = 'add'
  dialogVisible.value = true
  tablelist.value = {}
}
// 操作编辑订单
function postgood(row) {
  addtype.value = 'post'
  dialogVisible.value = true
  tableslists.value = { ...row }
}
// 操作删除订单
function deletegood(row){
  // 确认框
  ElMessageBox.confirm(`此操作将永久删除--${row.goodname}, 是否继续?`, "警告", {
    confirmButtonText: "确定",
    cancelButtonText: "取消",
    type: "error",
  }).then(() => {
    // 点击确认删除数据放回服务器
    return axios.delete("http://127.0.0.1:8080/delete_table",{data:{goods:row.goods}}).then((res) => {
      ElMessage.success("删除成功")
    })
  }).then(() => {
    // 删除成功后重新获取订单表
    getlist()
  }).catch((err) => {
      ElMessage.error("删除失败，请联系后台管理人员")
      console.error("删除失败:", err)
    })
    }

// 查询后端订单表
const tableslist = ref([])
const getlist= async () => {
  try {
    await axios.get("http://127.0.0.1:8080/tables").then((res)=>{
      tableslist.value=res.data
      console.log("获取后端数据",tableslist.value)
    })
  } catch (error) {
    console.error('获取商品列表失败:', error)
    ElMessage.confirm("获取商品列表失败，请联系后台管理人员", "警告", {
      confirmButtonText: "确定",
      cancelButtonText: "取消",
      type: "error",
    })
  }
}
// const tablelist = ref({})

let tableData = ref(tableslist.value)
// 状态文本转换
// 1 在售 -1 下架 0 预售 -2 缺货
function statustext(state) {
  if (state == 1) {
    return '在售'
  } else if (state == -1) {
    return '下架'
  } else if (state == 0) {
    return '预售'
  } else if(state==-2){
    return "缺货"
  }
}
// 标签
function tag(state){
    if(state==1){
        return "primary"
    }else if(state==-1){
        return "danger"
    }else if(state==0){
        return "warning"
    }else if(state==-2){
        return "info"
    }
}
// 筛选
const fillertag = (value, row) => {
  return row.status === value
}
// 搜索
let search = ref('')

const searchgood=()=>{
    if (search.value){
        let list=tableData.value.filter(item=>item.name.includes(search.value))
        tableData.value=list
    }else{
        ElMessage.warning('请输入搜索内容')
        tableData.value=list.value
    }
}

// 提交/更新订单
const posttable = ref({})
function posttables() {
  if (addtype.value === 'add') {
    // 添加商品
    axios.post("http://127.0.0.1:8080/post_tables", posttable.value).then((res) => { 
    })
      .then(() => {
        ElMessage.success("添加成功")
        dialogVisible.value = false
        getlist()
        posttable.value = {} // 清空表单数据
      })
      .catch((error) => {
        console.error('添加商品失败:', error)
        ElMessage.error("添加商品失败，请联系后台管理人员")
      })}
      // else{
      //   axios.put("http://127.0.0.1:8080/put_tables", posttable.value).then((res) => {
      //     ElMessage.success("更新成功")
      //     dialogVisible.value = false
      //     getlist()
      //   })
      //   .catch((error) => {
      //     console.error('更新商品失败:', error)
      //     ElMessage.error("更新商品失败，请联系后台管理人员")
      //   })
      }



// const posttables=async()=>{
//   try {
//     await axios.post("http://127.0.0.1:8080/post_tables",posttable.value).then((res)=>{
//       ElMessage.success("添加成功")
//       dialogVisible.value=false
//       getlist()
//       posttable.value = {} // 清空表单数据
//     })
//   } catch (error) {
//     console.error('添加商品失败:', error)
//     ElMessage.confirm("添加商品失败，请联系后台管理人员", "警告", {
// })
//   }
// }

// // 删除商品
</script>
