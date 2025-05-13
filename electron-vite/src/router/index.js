import { createRouter,createWebHashHistory } from "vue-router";

import Home from "@/pages/Home.vue";
import Post from "@/pages/Post.vue";
import Put from "@/pages/Put.vue";
import Del from "@/pages/Del.vue";
import watchstu from "@/pages/watchstu.vue";
import About from "@/pages/About.vue";


const routes = createRouter({
    history: createWebHashHistory(),
    routes: [{
        name:"home",
        path:"/",
        component:Home
    },
    {
        name:"poststu",
        path:"/poststu",
        component:Post
    },
    {
        name:"putstu",
        path:"/putstu",
        component:Put
    }


]})