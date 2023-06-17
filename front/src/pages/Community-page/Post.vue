<template>
    <div>
      <div class="card" v-for="post in posts" :key="post.id">
        <router-link :to="{ name: 'postDetailPage', params: { postId: Number(post.id) } }">
          <div class="row">
            <div class="col-6">
              <div class="card-body">
                <p class="card-text">{{ post.post_title }}</p>
                <p class="card-text">{{ post.post_content }}</p>
                <p class="card-text">{{ post.post_like }}</p>
              </div>
            </div>
            <div class="col-6">
              <img :src="post.image" class="card-img" alt="post image" />
            </div>
          </div>
        </router-link>
      </div>
      <router-link
        to="/community/write"
        tag="button"
        class="fixed-button"
      >
        <img src="/icons/pen.png" alt="글 작성하기" />
      </router-link>
    </div>
</template>

<script>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  export default {
    setup() {
      const posts = ref([]);
      const page = ref(1);
      const per_page = 10;
      const postTotalPages = ref(1);
  
      async function fetchPosts() {
        if (page.value <= postTotalPages.value) {
          try {
            const response = await axios.get(`api/community/list?page=${page.value}`);
            posts.value.push(...response.data.results);
            postTotalPages.value = Math.ceil(response.data.count / per_page);
            page.value += 1;
          } catch (err) {
            console.error('err:', err);
          }
        }
      }
  
      onMounted(() => fetchPosts());
      return {
        posts,
        fetchPosts
      }
    },
    directives: {
      infiniteScroll: {
        mounted(el, binding) {
          const { value } = binding;
          window.addEventListener('scroll', async () => {
            let scrollHeight = document.documentElement.scrollHeight;
            let scrollTop = document.documentElement.scrollTop;
            let clientHeight = document.documentElement.clientHeight;
  
            if (scrollTop + clientHeight >= scrollHeight) {
              await value();
            }
          });
        }
      }
    }
  };
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
    z-index: 1000;
  }
  .fixed-button img {
    width: 40px;
    height: 40px;
  }
  .fixed-button:hover {
    background-color: #0056b3;
  }
  </style>
  