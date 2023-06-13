<template lang="">
    <div class="header-main">
        <div class="box_search">
            <!--
                <input type="search" title="검색어 입력" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" class="form__input" placeholder="건강기능식품을 검색해보세요">
            -->
            <router-link to="/search"><SearchBar background-color="#FFFFFF" :placeholder="searchPlaceholder"></SearchBar></router-link>
        </div>
        
        <button class="alerts"><img class="alerts_icon" src="https://w7.pngwing.com/pngs/321/985/png-transparent-bell-computer-icons-bell-handbell-alert-school-bell.png"/></button>
    </div>

    <div class="menu_container">
        <router-link to="/test" class="item menus">제품</router-link>
        <router-link to="/test" class="item menus">추천</router-link>
        <router-link to="/test" class="item menus">알람설정</router-link>
        <router-link to="/test" class="item menus">정기배송신청</router-link>
        <router-link to="/test" class="item menus">영양제 촬영하기</router-link>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from "vue-router";
import { useStore } from '../../stores';
import SearchBar from '../../components/Navbar/SearchBar.vue';

export default {
    name:"HomePage",
    components: {
        SearchBar
    },
    setup() {
        const store = useStore();
        const router = useRouter();
        const searchPlaceholder = ref('건강기능식품을 검색해보세요');
        const checkLogin = () => {
            if(!store.isLoggedIn){
                router.push({
                    path: "/signup",
                });
            }
        };
        onMounted(() => checkLogin());
        return {
            store,
            router,
            searchPlaceholder,
            checkLogin,
        };
    },
    };

</script>
<style>
.header-main {
    position: fixed;
    top: 0;
    left: 0;
    padding: 3px;
    display: flex;
    width: 100vw;
    height: 15vw;
    align-items: center;
    background-color: #2dce89;
}

.box_search {
    margin: 5vw;
    flex-grow: 1;
}


.alerts {
    margin: 5vw;
    border: 0;
    padding: 0;
    width: 10vw;
    height: 10vw;
}

.alerts_icon {
    border: 0;
    padding: 0;
    width: 100%;
    height: 100%;
}

.menu_container {
    padding-top: 10vw;
    position: static;
    align-items: center;

    display: grid;
    /* display: inline-flex; */
    grid-template-columns: 40vw 40vw;
    grid-template-rows: 30vw 30vw 30vw;
}

.item:nth-child(5) {
	grid-column: 1 / 3;
	grid-row: 3 / 4;
}

.menus {
    margin: 2vw;
    position: relative;
    
    justify-content: center;
    align-items: center;
    
    line-height: 25vw;
    font-family: "paybooc-Light", sans-serif;
    color: #6e6e6e;
    font-size: 1.2em;
    text-decoration: none;
    font-weight: 750;
    transition: 0.25s;

    border: 3px solid #2dce89;
    border-radius: 5px;
}
.menus:hover {
    background-color: #2dce89;
    color: #d4dfe6;
}
</style>