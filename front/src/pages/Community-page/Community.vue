<template>
    <div>
        <nav class="navbar fixed-top bg-theme" style="padding: 10px 5vw 0 5vw;">
              <router-link to="/community-search" style="width: 100%;">
                <div class="search">
                    <input class="search-input" type="text" :placeholder="placeholder" @keydown.enter="search">
                    <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search()">
                </div>
              </router-link>
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
        
        <router-view></router-view>        
        

        <router-link
        to="/community/write"
          tag="button"
          class="fixed-button"
        >
          <img src="/icons/pen_white.png" alt="글 작성하기" />
        </router-link>
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
  margin-bottom: 0;
  padding: 0;
  width: calc(100% - 12px);
  height: 33px;
  flex-grow: 1;
}

.commu-item {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}
.commu-link {
  font-weight: bold;
  text-decoration: none;
  color: whitesmoke;
}
.commu-menu .router-link-exact-active {
  flex-grow: 1;
  background: whitesmoke; /* 배경색 변경 */
  color: #333; /* 글자색 변경 */
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  padding: 4.5px; /* 패딩 추가 */
  text-decoration: none; /* 밑줄 제거 */
  transition: all 0.3s ease; /* 변환 효과 */
  height: 33px;
  align-items: center;
}

.fixed-button {
    position: fixed;
    bottom: 10vh;
    right: 5vw;
    background-color: #2dce89;
    color: #fff;
    font-size: 18px;
    padding: 12px;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    z-index: 1100;
  }
  .fixed-button img {
    width: 40px;
    height: 40px;
  }
  .fixed-button:hover {
    background-color: #0056b3;
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