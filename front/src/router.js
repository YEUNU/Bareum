import { createWebHistory, createRouter } from "vue-router"

import loginPage from './pages/login-page/LoginPage.vue'
import signupPage from './pages/login-page/SignupPage.vue'
import mainPage from './pages/MainPage.vue'
import myPage from './pages/my-page/MyPage.vue'
const routes = [
    {
        path: "/signup",
        component:signupPage,
        name:'signupPage'
    },
    {
        //처음들어왔을때 보여주는 화면 넣어야할듯 경로도 나중에 첫화면 정해주면 넣어주고
        path:"/",
        name:'firstPage',
        component:mainPage,
        children:[{
            path:'',
            name:'myPage',
            component:signupPage
        },
        {
            path:'/search',
            name:'search',
            component:signupPage
        },
        {
            path:'/login',
            name:'loginPage',
            component:loginPage
        }
        ]
    },
    {
        //예시
        path:"/mypage",
        component:mainPage,
        name:'mypage',
        children:[
            {
                path:'',
                name:'',
                component:myPage
            },
            {
                //상대경로임 /mypage/main
                path:'main',
                name:'',
                component:myPage
            }
        ]

    }

]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router