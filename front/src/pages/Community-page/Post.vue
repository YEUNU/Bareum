<template>
    <div>
      <div class="card" v-for="post in posts" :key="post.post_id">
          <router-link :to="{ name: 'postDetailContentPage', params: { postId: post.post_id }}">
          <div class="row">
            <div class="col-6">
              <div class="card-body">
                <p class="card-text">{{ post.post_date }}</p>
                <p class="card-text">제목 : {{ post.post_title }}</p>
                <p class="card-text">내용 : {{ post.post_contents }}</p>
                <p class="card-text">작성자 : {{ post.user.user_name }}</p>

              </div>
            </div>
            <div class="col-6">
              <img :src="post.image" class="card-img" alt="post image" />
            </div>
          </div>
        </router-link>
      </div>
      <div ref="loader" class="loader"></div>
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
import { ref, onMounted, onUnmounted } from 'vue';

export default {

  setup() {
    const posts = ref([]);
    const page = ref(1);
    const per_page = 10;
    const postTotalPages = ref(1);
    const loader = ref(null);

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

    let observer;
    
    onMounted(async () => {
      await fetchPosts();

      observer = new IntersectionObserver(async (entries, observer) => {
        if (entries[0].isIntersecting) {
          await fetchPosts();
        }
      });

      if (loader.value) {
        observer.observe(loader.value);
      }
    });

    onUnmounted(() => {
      if (loader.value) {
        observer.unobserve(loader.value);
      }
    });

    return {
      posts,
      loader,
    };
  },
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
  