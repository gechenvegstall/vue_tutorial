<template>
  <div ref="chartRef" style="width: 600px; height: 400px;"></div>
</template>

<script setup>
import * as echarts from 'echarts';
import { ref, onMounted } from 'vue';
// 初始化 ECharts 实例
const chartRef = ref(null);
onMounted(() => {
  const chart = echarts.init(chartRef.value);

  // 设置图表配置
  const option = {
    title: {
      text: '统计图表示例',
    },
    tooltip: {},
    legend: {
      data: ['数据']
    },
    xAxis: {
      data: ["A", "B", "C", "D", "E"]
    },
    yAxis: {},
    series: [{
      name: '数据',
      type: 'bar',
      data: [80, 50, 30, 40, 120]
    }]
  };

  // 渲染图表
  chart.setOption(option);
});

</script>