import { createWebHistory, createRouter } from "vue-router"

import loginPage from './pages/login-page/Login.vue'
import signupPage from './pages/login-page/Signup.vue'
import searchPage from './pages/Search-page/SearchPage.vue'
import search from './pages/Search-page/Search.vue'
import detailSearchPage from './pages/Search-page/DetailSearch.vue'
import homePage from './pages/Home-page/Home.vue'
import mainPage from './pages/MainPage.vue'
import myPage from './pages/my-page/MyPage.vue'
import commuPage from './pages/Community-page/Community.vue'
import shopPage from './pages/Shopping-page/shop.vue'
import BottomNavBar from './components/NavBar/BottomNavBar.vue';
import IngredientSearch from './components/IngredientSearch.vue';
import PersonalizedSearch from './components/PersonalizedSearch.vue';


const routes = [
    {
        path: "/test",
        component: IngredientSearch,
        name: 'test'
    },
    {
        path: "/login",
        component: loginPage,
        name:'loginPage'
    },
    {
        path: "/signup",
        component:signupPage,
        name:'signupPage'
    },
    {
        path:"/search",
        component:searchPage,
        name:'searchPage',
        children:[
            {
                path:'',
                component:search,
                name:"searchPageMain"
            },
            {
                path:'detail',
                component:detailSearchPage,
                name:'detailSerachPage'
        },
        ]
    },
    {
        path:"/",
        component:mainPage,
        name:'homePage',
        children:[{
            path:'',
            name:'homePageMain',
            component:homePage
        }
        ]
    },
    {
        //예시
        path:"/shop",
        component:mainPage,
        name:'shoppingPage',
        children:[
            {
                path:'',
                name:'shoppingPage',
                component:shopPage
            }
        ]

    },
    {
        //예시
        path:"/community",
        component:mainPage,
        name:'community',
        children:[
            {
                path:'',
                name:'communityMain',
                component:commuPage
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
                name:'myMainPage',
                component:myPage
            }
        ]

    },
    

]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router