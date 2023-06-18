import { createWebHistory, createRouter } from "vue-router"

import loginPage from './pages/login-page/Login.vue'
import signupPage from './pages/login-page/Signup.vue'
import searchPage from './pages/Search-page/SearchPage.vue'
import search from './pages/Search-page/Search.vue'
import detailSearchPage from './pages/Search-page/DetailSearch.vue'
import homePage from './pages/Home-page/Home.vue'
import mainPage from './pages/MainPage.vue'
import myPage from './pages/my-page/MyPage.vue'
import myupdatePage from './pages/my-page/MyupdatePage.vue'
import mywishPage from './pages/my-page/MywishPage.vue'
import myorderPage from './pages/my-page/MyorderPage.vue'
import mypushPage from './pages/my-page/MypushPage.vue'
import mysupportPage from './pages/my-page/MysupportPage.vue'
import myremovePage from './pages/my-page/MyremovePage.vue'
import myremovedetailPage from './pages/my-page/MyremovedetailPage.vue'
import mytermsPage from './pages/my-page/MytermsPage.vue'
import myprivacyPage from './pages/my-page/MyprivacyPage.vue'
import commuPage from './pages/Community-page/Community.vue'
import shopPage from './pages/Shopping-page/shop.vue'
import BottomNavBar from './components/NavBar/BottomNavBar.vue';
import writePage from './pages/Community-page/Write.vue';
import postDetailPage from './pages/Community-page/PostDetail.vue';
import CustomSearch from './components/CustomSearch.vue';
import TotalRanking from './pages/Product-page/Rank-page/TotalRanking.vue';
import TotalResult from './pages/Search-page/Result-page/TotalResult.vue';

const routes = [
    //로그인 페이지
    {
        path: "/login",
        component: loginPage,
        name:'loginPage'
    },
    //회원가입 페이지
    {
        path: "/signup",
        component:signupPage,
        name:'signupPage'
    },
    //건강기능식품 검색 페이지
    {
        path:"/search",
        component:searchPage,
        name:'searchPage',
        children:[
            {
                path:'',
                component:search,
                name:"searchPageMain",
            },
            //성분, 개인관심사 로 검색하기 위한 디테일 페이지
            {
                path:'detail',
                component:detailSearchPage,
                name:'detailSerachPage',
            },
            {
                path:'result',
                component:TotalResult,
                name:'resultPage',
                props: (route) => ({ query: route.query.q }),
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
        path:"/Ranking",
        component:mainPage,
        name:'Ranking',
        children:[
            {
                path:'',
                name:'TotalRanking',
                component:TotalRanking
            }
        ]

    },
    
    //쇼핑페이지
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
            },
            {
                path:'write',
                name:'writePage',
                component:writePage
            },
            {
                path:'detail/:postId',
                name:'postDetailPage',
                component:postDetailPage,
                props:true
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

    {   
        // 개인정보수정
        path:'/myupdate',
        name:'myupdatePage',
        component:myupdatePage
    },
    {   
        // 찜 목록
        path:'/mywish',
        name:'mywishPage',
        component:mywishPage
    },
    {   
        // 주문 / 배송 내역
        path:'/myorder',
        name:'myorderPage',
        component:myorderPage
    },
    {   
        // 푸시 알람 설정
        path:'/mypush',
        name:'mypushPage',
        component:mypushPage
    },
    {   
        // 문의하기 
        path:'/mysupport',
        name:'mysupportPage',
        component:mysupportPage
    },
    {   
        // 회원탈퇴 
        path:'/myremove',
        name:'myremovePage',
        component:myremovePage
    },
    {   
        // 회원탈퇴 약관
        path:'/myremovedetail',
        name:'myremovedetailPage',
        component:myremovedetailPage
    },
    {   
        // 이용 약관
        path:'/myterms',
        name:'mytermsPage',
        component:mytermsPage
    },
    {   
        // 개인정보 처리방침
        path:'/myprivacy',
        name:'myprivacyPage',
        component:myprivacyPage
    },
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router