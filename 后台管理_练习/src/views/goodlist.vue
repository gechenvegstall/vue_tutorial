<template>
  <!-- 添加订单按钮 -->
   <el-button type="primary" @click="addgood" style="margin: 15px 0;">添加商品</el-button>
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
import { ElMessage } from 'element-plus'
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
// 添加订单
function addgood() {
  addtype.value = 'add'
  dialogVisible.value = true
  tableData.value = {}
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

</script>
