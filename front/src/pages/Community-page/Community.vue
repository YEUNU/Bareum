<template>
    <div>
        <nav class="navbar fixed-top bg-light">
            <div class="container-fluid">
                <span class="navbar-brand mb-0 h1">커뮤니티</span>
                 <div class="search">
                    <input class="search-input" type="text" :placeholder="placeholder" v-model="searchQuery" @keydown.enter="search">
                    <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search">
                </div>
            </div>
        </nav>
        
        <div class="container">
            <nav class="navbar  bg-light c">
                <router-link to="/">
                    <button type="button" class="btn btn-light">자유게시판</button>
                </router-link>
                <router-link to="/">
                    <button type="button" class="btn btn-light">영양 뉴스</button>
                </router-link>
            </nav>

            <nav class="navbar  bg-light d">
                <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
                    <input type="radio" class="btn-check visually-hidden" name="btnradio" id="btnradio1" autocomplete="off" checked>
                    <label class="btn btn-outline-primary" for="btnradio1">전체 글 보기</label>

                    <input type="radio" class="btn-check visually-hidden" name="btnradio" id="btnradio2" autocomplete="off">
                    <label class="btn btn-outline-primary" for="btnradio2">10추</label>

                    <router-link to="/community/write">
                        <button type="button" class="btn btn-light write">글쓰기</button>
                    </router-link>
                </div>
            </nav>

            <nav class="navbar bg-light e">
            <router-link to="/">
                <div class="alert alert-light" role="alert">[공지]</div>
                    </router-link>
        </nav>

        <div class="card" v-for="post in posts" :key="post.id">
            <router-link :to="{ name: 'postDetailPage', params: { postId: post.id } }">{{ post.title }}</router-link>
        </div>
        <div class="pagination">
            <button v-for="number in totalPages" @click="fetchPosts(number)">
              {{ number }}
            </button>
        </div>

        <div class="card">
            <div class="row">
                <div class="col-6">
                    <img src="..." class="card-img" alt="...">
                </div>
                <div class="col-6">
                    <div class="card-body">
                        <router-link to="/community/detail"><p class="card-text">제목</p></router-link>
                        
                        <p class="card-text">작성자</p>
                        <p class="card-text">기타등등</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="card" v-for="post in posts" :key = "post.id">
            <div class="row">
                <div class="col-6">
                    <img src="post.image" class="card-img" alt="post image">
                </div>
                <div class="col-6">
                    <div class="card-body">
                        <p class="card-text">{{post.title}}</p>
                        <p class="card-text">{{post.author }}</p>
                        <p class="card-text">{{post.extra }}</p>
                    </div>
                </div>
            </div>
        </div>
        
        </div>
        
    </div>
</template>

<script>
import axios from 'axios';
import {ref, onMounted} from 'vue';

export default {
    setup(){
        const posts = ref([]);
        const totalPages = ref(0);

        async function fetchPosts(pageNumber){
            try{
                const response = await axios.get(`https://your-api-url-here/api/community?page=${pageNumber}`);
                posts.value = response.data.results;
                totalPages.value = Math.ceil(response.data.count / 10);
            }catch(err){
                console.error("err:",err);
            }

        }
        posts.value=[
            {
            id:1,
            title:"hello"
        },
        {
            id:2,
            title:"world"
        }
    ]

        onMounted(()=> fetchPosts(1));
        return{
            posts,
            totalPages,
            fetchPosts
        }
    }
}
</script>



<style lang="css">
.container {
 /* fixed-top navbar의 높이만큼 여백 추가 */
  padding-top: 1%;
  padding-bottom: 10%;
  width: 100%;
  height: 100%;
  display: block;
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

.visually-hidden {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border: 0 !important;
}

.card {
    margin-top: 10%;
}
</style>