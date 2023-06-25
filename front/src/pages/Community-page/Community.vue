<template>
    <div>
        <nav class="navbar fixed-top bg-light">
            <div class="container-fluid">
              <router-link to="/community-search" style="width: 100%;">
                <div class="search">
                    <input class="search-input" type="text" :placeholder="placeholder" v-model="searchQuery" @keydown.enter="search">
                    <svg v-show="searchQuery" class="search-clear-icon" @click="searchbar_clear" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
                    </svg>
                    <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search()">
                </div>
              </router-link>

            </div>
            <ul class="commu-menu mt-3">
                <li class="commu-item">
                  <router-link class="commu-link" to="/community" >전체 글 보기</router-link>
                </li>
                <li class="commu-item" >
                  <router-link class="commu-link" to="/community/popular-posts">인기 글 보기</router-link>
                </li>
                <li class="commu-item">
                  <router-link class="commu-link" to="/community/news">영양 뉴스</router-link>
                </li>
            </ul>
        </nav>
        
        <div class="container">
            <router-view></router-view>        
        </div>
        
    </div>
</template>

<script>
import {ref} from 'vue'
export default {
    setup(){
        const placeholder = ref('검색어를 입력하세요')


        return{
            placeholder
        }
    }
}
</script>



<style lang="css">
.container {
 /* fixed-top navbar의 높이만큼 여백 추가 */
  padding-top: 30%;
  padding-bottom: 10%;
  width: 100%;
  height: 100%;
  display: block;
}

.commu-menu {
    display: flex;
    list-style: none;
    padding-left: 0;
    width: 100%;
}

.commu-item {
  margin-right: 1rem;
  flex:1;
  
}
.commu-link {
  text-decoration: none;
  color: black;
}
.commu-menu .router-link-exact-active {
  background: #2dce89; /* 배경색 변경 */
  color: #fff; /* 글자색 변경 */
  border-radius: 4px; /* 가장자리를 둥글게 */
  padding: 6px 12px; /* 패딩 추가 */
  text-decoration: none; /* 밑줄 제거 */
  transition: all 0.3s ease; /* 변환 효과 */
}

.commu-menu .router-link-exact-active:hover {
  background: #2dce89; /* 마우스 오버 시 배경색 변경 */
  color: #fff; /* 글자색 유지 */
}



.search-navbar {
  margin-top: 10%; /* 검색 navbar의 위쪽 여백 조정 */
  width: 100%;
  height: 100%;
}

.c {
    margin-top: 40%
}

.d {
    margin-top: 10%;
}

.e {
    margin-top: 10%;
}

.write-button {
  margin-left: auto;
  padding-right: 15px;
}

.card {
    margin-top: 10%;
}

</style>