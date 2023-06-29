<template>
    <nav class="navbar fixed-top bg-white" style="box-shadow: 0 2px 1px -1px #EAEAEA;">
        <div class="container-fluid">
            <router-link to="/">
                <span class="navbar-brand" style="margin-left: 2vh;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left"
                    viewBox="0 0 16 16">
                    <path fill-rule="evenodd"
                        d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
                </svg>
            </span>
            </router-link>
            <div @click="toggleMenu" style="margin-right: 2vh; cursor: pointer; font-weight: bold;">{{ pageTitle }}</div>
            
            <div to="/mysetting" class="navbar-brand" @click="toggleMenu">
                <svg v-if="menuVisible" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-filter-square-fill" viewBox="0 0 16 16">
                    <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm.5 5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1 0-1zM4 8.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm2 3a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5z"/>
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-filter-square" viewBox="0 0 16 16">
                    <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
                    <path d="M6 11.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z"/>
                </svg>
            </div>
        </div>
        <div v-if="menuVisible" class="ranking-menu-container">
          <div @click="navigateRanking('/ranking', '바름 종합 랭킹')">종합 랭킹</div>
          <div @click="navigateRanking('/ranking/ingredient', '영양소 별 랭킹')">영양소 별</div>
          <div @click="navigateRanking('/ranking/category', '관심항목 별 랭킹')">관심항목 별</div>
          <div @click="navigateRanking('/ranking/age', '연령대 별 랭킹')">연령대 별</div>
          <div @click="navigateRanking('/ranking/brand', '브랜드 별 랭킹')">브랜드 별</div>
        </div>
    </nav>
    <router-view :menuVisible.sync=menuVisible></router-view>
</template>

<script>
import { ref, computed,onMounted, onUnmounted } from 'vue';
import { useRouter } from "vue-router";
import axios from "axios";

import searchBar from '../../../components/Navbar/SearchBar.vue';
import customSearch from '../../../components/CustomSearch.vue';

export default {
    components: { searchBar, customSearch },
    setup() {
        const router = useRouter();
        const menuVisible = ref(false);
        const pageTitle = ref("바름 종합 제품 랭킹");

        function toggleMenu() {
            menuVisible.value = !menuVisible.value;
        }

        function navigateRanking(path, title) {
            router.push(path);
            pageTitle.value = title;
            menuVisible.value = false;
        }


        return {
            router,
            menuVisible,
            pageTitle,
            toggleMenu,
            navigateRanking,
        };
    }
}
</script>

<style scope>

.detail-ranking-head {
    display: flex;
    flex-direction: column;
    background-color: white;
    box-shadow: 2px 2px 2px 2px #eeeeee;
    margin-bottom: 0.5vh;
    padding: 5vw;
    font-size: 0.9em;
    text-align: start;
}

.rank_box {
    align-self: center;
    justify-self: center;
    display: grid;
    width: 100vw;
    grid-template-columns: 5vw min(21vh, 21vw) 65vw;
    align-content: center;
    margin-bottom: 1vh;
    padding: 5vw;
    font-weight: bold;
    box-shadow: 2px 2px 2px 2px #eeeeee;
    color: #333;
    text-decoration:none;
}

.rank_order {
    grid-column: 1 / 2;
    grid-row: 1 / 5;
    align-self: center;
}

.rank_image {
    grid-column: 2 / 3;
    grid-row: 1 / 5;
    align-self: center;
    justify-self: center;
    padding: 2vw;
}
.rank_image img {
    height: min(20vh, 20vw);
    width: min(20vh, 20vw);
}

.rank_manufacturer {
    grid-column: 3 / 4;
    grid-row: 1 / 2;
    align-self: center;
    justify-self: start;
    font-size: 0.75em;
    color: gray;
}

.rank_name {
    grid-column: 3 / 4;
    grid-row: 2 / 3;
    align-self: center;
    justify-self: start;
    font-size: 1em;
    text-align: start;
}

.rank_score {
    grid-column: 3 / 4;
    grid-row: 3 / 4;
    align-self: center;
    justify-self: start;
    font-size: 0.8em;
    font-weight: normal;
}

.rank_price {
    grid-column: 3 / 4;
    grid-row: 4 / 5;
    align-self: center;
    justify-self: start;
}

.ranking-menu-container {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin-top: 5px;
  font-size: 0.8em;
  background-color: #f8f9fa;
}

.ranking-menu-container div {
  padding: 10px;
  cursor: pointer;
}

</style>