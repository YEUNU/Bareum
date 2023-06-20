<template lang="">


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



    <div class="navbar fixed-top bg-theme" style="padding: 10px;">
        <div class="box_search">
            <router-link to="/search"><SearchBar class="box_search_input" background-color="#FFFFFF" :placeholder="searchPlaceholder"></SearchBar></router-link>
        </div>
        
        <button class="box_alerts" @click="router.push({path: '/alerts'});">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bell-fill" viewBox="0 0 16 16">
                <path d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2zm.995-14.901a1 1 0 1 0-1.99 0A5.002 5.002 0 0 0 3 6c0 1.098-.5 6-2 7h14c-1.5-1-2-5.902-2-7 0-2.42-1.72-4.44-4.005-4.901z"/>
            </svg>
        </button>
    </div>
    <div class="background bg-whitesmoke" style="padding-top: 7vh;">
        <div class="menu_container">
            <router-link to="/ranking" class="item menus">
            <div id="menu_comment">많은 사람들이 구매한</div>
            <div id="menu_name">제품</div>
            <div id="menu_icon"><img height="" src="../../assets/product.png" alt=""></div>
        </router-link>
        <router-link to="/recommend" class="item menus">
            <div id="menu_comment">당신을 위한 맞춤</div>
            <div id="menu_name">추천</div>
            <div id="menu_icon"><img src="../../assets/recommand.png" alt=""></div>
        </router-link>
        <router-link to="/set_alarm" class="item menus">
            <div id="menu_comment">규칙적인 나만의 비서</div>
            <div id="menu_name">알림설정</div>
            <div id="menu_icon"><img src="../../assets/alarm.png" alt=""></div>
        </router-link>
        <router-link to="/regular_delivery" class="item menus">
            <div id="menu_comment">내가 까먹어도 기사님은 안까먹는</div>
            <div id="menu_name">정기배송신청</div>
            <div id="menu_icon"><img src="../../assets/delivery.png" alt=""></div>
        </router-link>
    </div>
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
.background {
    display: flex;
    flex-direction: column;
    position: fixed;
    left: 0;
    top: 0;
    width: 100vw;
    min-height: 100%;
    z-index: 0;
}

.bg-theme {
    background-color: #2dce89;
}

.bg-whitesmoke {
    background-color: whitesmoke;
}

.box_search {
    margin: 10px 10px 10px 8vw;
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
    margin: 5px;
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

    position: static;
    display: grid;
    grid-template-columns: 45vw 45vw;
    grid-template-rows: 50% 50%;
    padding: 5%;
    justify-content: center;
    align-items: center;

}

.menus {
    position: relative;
    background-color: white;

    color: #6e6e6e;
    font-size: 1.2em;
    text-decoration: none;
    font-weight: 750;
    transition: 0.25s;

    border: 2px solid #2dce89;
    border-radius: 5px;
    
    flex-direction: column;
    display: flex;
    justify-content: space-evenly;
    margin: 1vw;
}

#menu_comment {
    align-self: start;
    padding: 2.5% 0 0 2.5%;
    color: gray;
    font-size: min(1.7vw, 1.7vh);
}

#menu_name {
    align-self: start;
    padding: 0.5% 0 0 2.5%;
    color: black;
    font-size: min(5vw, 5vh);
}

#menu_icon {
    margin: 0 5% 5% 0;
    align-self: end;
}

#menu_icon img {
    height: min(15vw, 15vh);
}

.roundbox {
    width: 100%;
    border-radius: 10px;
    border: none;
    background-color: #2dce89;
    color: white;
    font-size: 1.1em;
    text-decoration: none;
    font-weight: 750;
}

</style>
