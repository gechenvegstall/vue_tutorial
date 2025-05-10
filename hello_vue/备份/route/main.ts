// 引入createAPP用于创建应用
import { createApp } from "vue";
// 引入APP组件
import App from "./App.vue";
// 引入路由器
import router from "./router/index";
// 创建应用
const app=createApp(App)
// 使用路由器
app.use(router)
// 挂载应用
app.mount('#app')