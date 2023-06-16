<template lang="">
        <div class="card" v-for="post in posts" :key = "post.id">
            <router-link :to="{ name: 'postDetailPage', params: { postId: Number(post.id) } }">

                <div class="row">
                    <div class="col-6">
                        <div class="card-body">
                            <p class="card-text">{{post.title }}</p>
                            <p class="card-text">{{post.author }}</p>
                            <p class="card-text">{{post.extra }}</p>
                        </div>
                    </div>
                    <div class="col-6">
                        <img src="post.image" class="card-img" alt="post image">
                    </div>

                </div>
            </router-link>
        </div>
        <router-link to="/community/write" tag="button" class="fixed-button"><img src="/icons/pen.png" alt="글 작성하기"></router-link>
</template>
<script>
import axios from 'axios';
import {ref, onMounted} from 'vue';

export default {
    setup(){
        const posts = ref([]);
        // async function fetchPosts(pageNumber){
        //     try{
                // const response = await axios.get(`api/community/list?page=${pageNumber}`);
        //         posts.value = response.data.results;
        //         postTotalPages.value = Math.ceil(response.data.count / 10);
        //     }catch(err){
        //         console.error("err:",err);
        //     }

        // };

        posts.value=[
            {
                id:1,
                title:"hello",
                author:"Js"
            },
            {
                id:2,
                title:"world",
                author:"jg"
            },
            {
                id:3,
                title:"hello",
                author:"Js"
            },
            {
                id:4,
                title:"world",
                author:"jg"
            },            {
                id:5,
                title:"hello",
                author:"Js"
            },
            {
                id:6,
                title:"world",
                author:"jg"
            },
            {
                id:1,
                title:"hello",
                author:"Js"
            },
            {
                id:2,
                title:"world",
                author:"jg"
            },
            {
                id:3,
                title:"hello",
                author:"Js"
            },
            {
                id:4,
                title:"world",
                author:"jg"
            },            {
                id:5,
                title:"hello",
                author:"Js"
            },
            {
                id:6,
                title:"world",
                author:"jg"
            },

    ]

        // onMounted(()=> fetchPosts(1));
        return{
            posts,
            // fetchPosts
            // fetchNews

        }
    }
}
</script>
<style lang="css">
.fixed-button {
  position: fixed;
  bottom: 10vh;
  right: 5vw;
  background-color: #2dce89;
  color: #fff;
  font-size: 18px;
  padding: 12px 20px;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  z-index: 1000; /* 다른 요소 위에 표시됩니다 */
}
.fixed-button img{
    width: 40px;     
  height: 40px;   
}
.fixed-button:hover {
  background-color: #0056b3;
}
</style>