<template>
    <div>
        <nav class="navbar fixed-top bg-light">
            <div class="container-fluid">
                 <div class="search">
                    <input class="search-input" type="text" :placeholder="placeholder" v-model="searchQuery" @keydown.enter="search">
                    <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search">
                </div>
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
        const searchQuery = ref('')
        const placeholder = ref('')


        return{
            searchQuery,
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