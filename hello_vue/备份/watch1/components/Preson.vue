<script lang="ts" setup name="person">
    import {ref,watch} from 'vue'
    // 数据
    let sum = ref(0)
    // 方法
    function changeSum(){
        sum.value += 1
    }
    // 监视，情况一：监视【ref】定义的【基本类型】数据
    const stopWatch = watch(sum,(newValue,oldValue)=>{
        console.log('sum变化了',newValue,oldValue)
        // 判断
        if(newValue >= 10){
        stopWatch()
        }
    })
</script>

<template>
  <div class="person">
    <h1>情况一:监视【ref】定义的【基本类型】数据</h1>
    <h2>当前求和为：{{sum}}</h2>
    <button @click="changeSum">+1</button>
  </div>
</template>

<style>
    .person{
        background-color: aqua;
    }
</style>