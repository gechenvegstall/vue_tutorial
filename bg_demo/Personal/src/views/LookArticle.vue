<template>
  <div v-if="article">
    <el-card shadow="never">
      <h1>{{ article.title }}</h1>
      <p>作者：{{ article.user }}</p>
      <span>{{ article.time }}</span>
      <hr />
      <p>{{ article.content }}</p>
    </el-card>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
import request from '../utils/request'

request.get('/api/article/'+this.$route.params.id).then(res=>{
    this.article=res.data
})
</script>