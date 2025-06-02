<template>
    <el-input placeholder="搜索商品" 
    v-model="search" 
    style="width: 280px;" 
    @keyup.enter="searchgood" 
    clearable
    @clear="searchgood"></el-input>
    <el-button type="primary" @click="searchgood">搜索</el-button>
  <el-table :data="tableData" stripe style="width: 100%">
    <el-table-column prop="date" label="日期" width="180"  sortable />
    <el-table-column prop="name" label="商品名" width="180" />
    <el-table-column prop="address" label="产地" />
    <el-table-column prop="status" label="状态" :filters="[
        { text: '在售', value: 1 },
        { text: '下架', value: -1 },
        { text: '预售', value: 0 },
        { text: '缺货', value: -2 }
    ]"
    :filter-method="fillertag">
        <!-- 插槽 -->
         <template #default="scope">
            <el-tag :type="tag(scope.row.status)">{{ statustext(scope.row.status) }}</el-tag>
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
import { computed, ref } from 'vue'
// 商品列表数据
const list = ref([
  {
    date: '2016-05-03',
    name: 'Zom',
    address: 'No. 189, Grove St, Los Angeles',
    status:1
  },
  {
    date: '2016-05-02',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    status: -1
  },
  {
    date: '2016-05-04',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    status: -2
  },
  {
    date: '2016-05-01',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    status: 0
  },
])
let tableData = ref(list.value)
// 状态文本转换
// 1 在售 -1 下架 0 预售 -2 缺货
function statustext(status) {
  if (status === 1) {
    return '在售'
  } else if (status === -1) {
    return '下架'
  } else if (status === 0) {
    return '预售'
  } else if(status===-2){
    return "缺货"
  }
}
// 标签
function tag(status){
    if(status===1){
        return "primary"
    }else if(status===-1){
        return "danger"
    }else if(status===0){
        return "warning"
    }else if(status===-2){
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
