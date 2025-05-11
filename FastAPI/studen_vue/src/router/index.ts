import {createRouter,createWebHashHistory} from "vue-router"

import Into from "@/pages/into.vue"
import Del from "@/pages/del.vue"
import Up from "@/pages/up.vue"


const router= createRouter({
    history:createWebHashHistory(),
    routes:[{
        name:'intouser',
        path:"/into",
        component:Into
    },
    {
        name:'deluser',
        path:'/del',
        component:Del
    },
    {
        name:'upuser',
        path:'/up',
        component:Up
    }
    ]
})

export default router