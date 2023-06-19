<template lang="">

      <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
  Launch static backdrop modal
</button>

<div class="modal" v-if="modalopen==true" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div><h4>잠깐!</h4></div>
        <div><h4>촬영 전 가이드를 확인해볼까요?</h4></div>
        <div><h6>그만 보기를 선택하시면 촬영가이드를 다시 볼 수 없습니다.</h6></div>
        <button type="button" class="btn btn-primary">네, 확인할게요</button>
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">괜찬하요, 이제 그만 볼게요</button>
        
      </div>
      <div class="modal-footer">
      </div>
    </div>
  </div>
</div>



    <div class="navbar fixed-top bg-theme">
        <div class="box_search">
            <router-link to="/search"><SearchBar class="box_search_input" background-color="#FFFFFF" :placeholder="searchPlaceholder"></SearchBar></router-link>
        </div>
        
        <button class="box_alerts" @click="router.push({path: '/alerts'});">
            <img class="alerts_icon" src="\src\assets\bell.png"/>
        </button>
    </div>

    <div class="menu_container">
        <router-link to="/ranking" class="item menus">제품</router-link>
        <router-link to="/recommend" class="item menus">추천</router-link>
        <router-link to="/set_alarm" class="item menus">알람설정</router-link>
        <router-link to="/regular_delivery" class="item menus">정기배송신청</router-link>
        <router-link to="/ocr" class="item menus" @click="modalopen = true">영양제 촬영하기</router-link>
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
        return {
            store,
            router,
            searchPlaceholder,
            modalopen: false,
        };
    },
    };

</script>
<style>
.bg-theme {
    background-color: #2dce89;
}

.box_search {
    margin: 20px;
    flex-grow: 1;
}

.box_search_input {
    height: 8vh;
}

.box_alerts {
    border: 0;
    padding: 0;
    max-width: 85px;
    max-height: 85px;
    width: 12vw;
    height: 12vw;
    background-color: rgba(255,255,255,0);
    z-index: 1;
}

.alerts_icon {
    border: 0;
    padding: 0;
    width: 100%;
    height: 100%;
}

.menu_container {
    margin-top: 10vh;
    margin-bottom: 62px;
    position: static;
    display: grid;
    grid-template-columns: 40vw 40vw;
    grid-template-rows: 21vh 21vh 21vh;

    justify-content: center;
    align-items: center;

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
    
    line-height: min(25vw, 15vh);
    font-family: "paybooc-Light", sans-serif;
    color: #6e6e6e;
    font-size: 1.2em;
    text-decoration: none;
    font-weight: 750;
    transition: 0.25s;

    border: 2px solid #2dce89;
    border-radius: 5px;
}
.menus:hover {
    background-color: #2dce89;
    color: #d4dfe6;
}

</style>
