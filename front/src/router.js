import { createWebHistory, createRouter } from "vue-router"
import { createApp } from 'vue';
import App from './App.vue';

import loginPage from './pages/login-page/Login.vue'
import signupPage from './pages/login-page/Signup.vue'
import agreesignupPage from './pages/login-page/Agreesignup.vue'
import searchPage from './pages/Search-page/SearchPage.vue'
import search from './pages/Search-page/Search.vue'
import DetailSearch from "./pages/Search-page/DetailSearch.vue";
import homePage from './pages/Home-page/Home.vue'
import cameraguidePage from './pages/Home-page/Cameraguide.vue'
import mainPage from './pages/MainPage.vue'
import myPage from './pages/my-page/MyPage.vue'
import regulardeliveryPage from './pages/Home-page/Regulardelivery.vue'
import mywishPage from './pages/my-page/MywishPage.vue'
import myorderPage from './pages/my-page/MyorderPage.vue'
import mypushPage from './pages/my-page/MypushPage.vue'
import mysupportPage from './pages/my-page/MysupportPage.vue'
import myremovePage from './pages/my-page/MyremovePage.vue'
import mytermsPage from './pages/my-page/MytermsPage.vue'
import myprivacyPage from './pages/my-page/MyprivacyPage.vue'
import mynewaddPage from './pages/my-page/MynewaddPage.vue'
import mysettingPage from './pages/my-page/MysettingPage.vue'
import myupdatePage from './pages/my-page/MyupdatePage.vue'
import myreviewPage from './pages/my-page/MyreviewPage.vue'
import mynutrientsPage from './pages/my-page/MynutrientsPage.vue'
import myalarmPage from './pages/my-page/MyalarmPage.vue'

import commuPage from './pages/Community-page/Community.vue'
import shopPage from './pages/Shopping-page/shop.vue'
import BottomNavBar from './components/NavBar/BottomNavBar.vue';
import writePage from './pages/Community-page/Write.vue';
import postDetailContent from './pages/Community-page/PostDetailContent.vue';
import postDetailPage from './pages/Community-page/postDetail.vue';
import CustomSearch from './components/CustomSearch.vue';
import rankingPage from './pages/Product-page/Rank-page/RankingPage.vue';
import postPage from './pages/Community-page/Post.vue'
import popularPostPage from './pages/Community-page/PopularPost.vue'
import newsPage from './pages/Community-page/HealthNews.vue'
import checkLogin from './checkLogin';
import TotalResult from './pages/Search-page/Result-page/TotalResult.vue';
import replyPage from './pages/Community-page/Reply.vue'
import commuSearchPage from './pages/Community-page/Search.vue'
import commuSearchResultPage from './pages/Community-page/SearchResult.vue'
import commuSearch from './components/CommuSearch.vue'
import ocrResultPage from './pages/Ocr-page/result.vue'
import ocrCameraPage from './pages/Ocr-page/camera.vue'
import registrationPage from './pages/shared-page/Registration.vue'
import camPage from './pages/shared-page/cam.vue'
import camCheckPage from './pages/shared-page/check.vue'
import PostList from './pages/Community-page/Community.vue';
import EditPostPage from './pages/Community-page/PostUpdatePage.vue';
import takeRegist from './pages/Taking-page/regist.vue';
import prSearchPage from './pages/Taking-page/pr_search.vue';
import prResultPage from './pages/Taking-page/pr_result.vue';
import rcMainPage from './pages/Recommend-page/rcMain.vue';
import addInfoPage from './pages/login-page/AddInfo.vue';
import addressPage from './pages/my-page/Address.vue';
import productDetailPage from './pages/Product-page/detail-page/ProductDetail.vue';
import productInfoPage from './pages/Product-page/detail-page/ProductInfo.vue';
import productReviewPage from './pages/Product-page/detail-page/ProductReview.vue';
import receivealarmPage from './pages/Home-page/Receivealarm.vue';
import productReviewWritePage from './pages/Product-page/detail-page/Write.vue';

import totalRankingPage from './pages/Product-page/Rank-page/TotalRanking.vue';
import ageRankingPage from './pages/Product-page/Rank-page/AgeRanking.vue';
import ingredientRankingPage from './pages/Product-page/Rank-page/IngredientRanking.vue';
import barandRankingpage from './pages/Product-page/Rank-page/BrandRanking.vue';
import categoryRankingPage from './pages/Product-page/Rank-page/CategoryRanking.vue';

import cartPage from './pages/my-page/Order-page/Cart.vue';
import orderPage from './pages/my-page/Order-page/Order.vue';

import ReviewList from './pages/review-page/ReviewList.vue';
import guidePage from './pages/login-page/Guide.vue';
import categoryPage from './pages/login-page/Category.vue';

const routes = [
    //로그인 페이지
    {
        path: "/login",
        component: loginPage,
        name:'loginPage',
    },
    {
        path:"/addInfo",
        component:addInfoPage,
        name:'addInfoPage'
    },
    //회원가입 페이지
    {
        path: "/signup",
        component:signupPage,
        name:'signupPage'
    },
    //회원가입 약관 페이지
    {
        path: "/agreesignup",
        component:agreesignupPage,
        name:'agreesignupPage'
    },
    
    {
        path:'/guide',
        component:guidePage,
        name:'guidePage'
    }
    ,
    //건강기능식품 검색 페이지
    {
        path: "/search",
    component: searchPage,
    name: "searchPage",
    children: [
      {
        path: "result",
        component: TotalResult,
        name: "resultPage",
        props: (route) => ({ query: route.query.q }),
      },
      {
        path: "result/:productId",
        component: DetailSearch, // 수정
        name: "DetailSearch",
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
    // 건강기능식품 리뷰 페이지
    {
        path: '/reviews', // 원하는 URL 주소를 할당합시다
        name: 'ReviewList',
        component: ReviewList
    },
    // 촬영 가이드 페이지
    {
        path: "/cameraguide",
        component:cameraguidePage,
        name:'cameraguidePage'
    },
    // 정기 배송 신청 페이지
    {
        path: "/regulardelivery",
        component:regulardeliveryPage,
        name:'regulardeliveryPage'
    },
  // 메인페이지 - 알람
  {
    path: "/receivealarm",
    component:receivealarmPage,
    name:'receivealarmPage'
},
    {
        //예시
        path:"/Ranking",
        component:mainPage,
        name:'Ranking',
        children:[
            {
                path:'',
                name:'rankingPage',
                component:rankingPage,
                children:[
                    {
                        path:'',
                        name:'totalRankingPage',
                        component:totalRankingPage
                    },
                    {
                        path:'age',
                        name:'AgeRankingPage',
                        component:ageRankingPage
                    },
                    {
                        path:'brand',
                        name:'BrandRankingPage',
                        component:barandRankingpage
                    },
                    {
                        path:'category',
                        name:'CategoryRankingPage',
                        component:categoryRankingPage
                    },
                    {
                        path:'ingredient',
                        name:'IngredientRankingPage',
                        component:ingredientRankingPage
                    },
                ]
            }
        ]
    },
    {
        path:"/product/:productCode",
        name:"productDetailPage",
        component:productDetailPage,
        props:true,
        children:[
            {
                path:'',
                name:'productInfoPage',
                component:productInfoPage,
                props:true,
            },
            {
                path:'review',
                name:'productReviewPage',
                component:productReviewPage,
                props:true,

            }
        ]
    },
    {
        path:'/prouct/review/write/:productCode',
        name:'productReviewWritePage',
        component:productReviewWritePage,
        props:true,
    },
    //게시물 수정 페이지
    {
        path: "/community/update/:postId",
        name: "EditPostPage",
        component: EditPostPage,
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
        path:"/community",
        component:mainPage,
        name:'community',
        children:[
            {
                path:'',
                name:'communityMain',
                component:commuPage,
                children:[
                    {
                        path:'',
                        name:'postPage',
                        component:postPage
                    },
                    {
                        path:'popular-posts',
                        name:'popularPostPage',
                        component:popularPostPage
                    },
                    {
                        path:'news',
                        name:'newsPage',
                        component:newsPage
                    }
                ]
            },
            {
                path:'write',
                name:'writePage',
                component:writePage
            },
        ]
    },
    {
        path:'/community/detail/:postId',
        name:'postDetailPage',
        component:postDetailPage,
        props:true,
        children:[
            {
                path:'',
                name:"postDetailContentPage",
                component:postDetailContent,
                props:true
            },
            {
                path: 'replyPage/:commentsId',
                name: 'postReplyPage',
                component: replyPage,
                props: true,
              },
        ]
    },
    {
        path:'/cam',
        component:camPage
    },
    {
        path:'/ocr/camera',
        component:ocrCameraPage
    },
    {
        path:'/ocr',
        name:'ocrReultPage',
        component:mainPage,
        children:[
            {
                path:'result/:imageData',
                component:ocrResultPage
            },
            {
                path:'registration',
                component:registrationPage
            },
        ]
    },
    {
        path:'/recommend',
        component:mainPage,
        children:[
            {
                path:'',
                component:rcMainPage
            },
        ]
    },
    {
        path:'/taking',
        name:'mynutrientsPage',
        component:mainPage,
        children:[
            {
                path:'',
                component:mynutrientsPage,
                name:'mynutrientsMain'
            },
            {
                path:'regist',
                component:takeRegist,
            },
            {
                path:'search',
                component:prSearchPage,
            },
        ]
    },
    {
        path:"/community-search",
        name:"commuSearchMainPage",
        component:mainPage,
        children:[{
            path:'',
            name:'commuSearchPage',
            component:commuSearchPage,
            children:[
            {
                path:'',
                name:'commuSearch',
                component:commuSearch
            },
            {
                path:'result',
                name:'commuSearchResult',
                component:commuSearchResultPage
            }
        ]
        }]
    },
    {
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
        name:'myWishPage',
        component:mywishPage
    },
    {  
        // 주문 / 배송 내역
        path:'/myorder',
        name:'myOrderPage',
        component:myorderPage
    },
    {
        // 알림 설정 페이지
        path:'/alarm',
        name:'alarmPage',
        component:myalarmPage
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
        // 이용 약관
        path:'/myterms',
        name:'mytermsPage',
        component:mytermsPage
    },
    {
        path:'/cart',
        name:'cartPage',
        component:cartPage
    },
    {
        path:'/order',
        name:'orderPage',
        component:orderPage,
    },
    {  
        // 개인정보 처리방침
        path:'/myprivacy',
        name:'myprivacyPage',
        component:myprivacyPage
    },
    {  
        // 영양제 등록 요청
        path:'/mynewadd',
        name:'mynewaddPage',
        component:mynewaddPage
    },
    {  
        // 환경설정
        path:'/mysetting',
        name:'mysettingPage',
        component:mysettingPage
    },
    {  
        // 내 리뷰 관리
        path:'/myreview',
        name:'myreviewPage',
        component:myreviewPage
    },
    // {   
    //     // 복용중인 영양제
    //     path:'/mynutrients',
    //     name:'mynutrientsPage',
    //     component:mynutrientsPage
    // },
    {
        path:'/address',
        name:'userAddressMain',
        component:mainPage,
        children:[
        {
            path:'',
            name:'userAddressPage',
            component:addressPage,
        }
        ]
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

router.beforeEach(async (to, from, next) => {
    const isLoggedIn = await checkLogin();
  
    if (!isLoggedIn && to.path !== '/login' && to.path !== '/agreesignup' && to.path !== '/signup') {
      next('/login');
    } else if(isLoggedIn && (to.path === '/login' || to.path === '/agreesignup' || to.path === '/signup')) {
      next('/');
    } else {
      next();
    }
});

export default router