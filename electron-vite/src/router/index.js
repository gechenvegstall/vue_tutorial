import { createRouter,createWebHashHistory } from "vue-router";

import Home from "../pages/Home.vue";
import Post from "../pages/Poststu.vue";
import Put from "../pages/Putstu.vue";
import Del from "../pages/Delstu.vue";
import Watchstu from "../pages/Watchstu.vue";
import About from "../pages/About.vue";


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
    },
    {
        name:"delstu",
        path:"/delstu",
        component:Del
    },
    {
        name:"watchstu",
        path:"/watchstu",
        component:Watchstu
    },
    {
        name:"about",
        path:"/about",
        component:About
    }


]})

export default routes