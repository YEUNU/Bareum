<template>
<div class="background bg-whitesmoke" style="margin-top: 101px; padding-top: 2vh; padding-bottom: 60px; min-height: calc(100vh - 161px); display: flex; flex-direction: column; align-items: center;">
  <div class="card" v-for="post in posts" :key="post.post_id" style="box-shadow: 2px 2px 2px 2px #eeeeee; width: 90vw; margin: 1vh; padding: 2vh;">
    <router-link :to="{ name: 'postDetailContentPage', params: { postId: post.post_id }}">
      <div class="post_box">
        <!-- <img :src="post.image" class="card-img" alt="post image" /> -->
        <div class="card-body" style="padding: 1vh 5vw 1vh 3vw; width: calc(100% - 78px); flex-grow: 1;">
          <div class="card-text" style="color: black; font-weight: bold; text-align: start;">{{ post.post_title }}</div>
          <div class="card-text" style="color: black; font-size: 13px; text-align: start;">작성자 : {{ post.user.nickname }}</div>
          <div class="card-text" style="color: black; font-size: 13px; text-align: start;">{{ formatDate(post.post_date) }}</div>
          <!-- <p class="card-text">내용 : {{ post.post_contents }}</p> -->
        </div>
        <div v-if="post.post_images.image" style="width: 78px; height: 78px;">
          <img :src="post.post_images.image"
          alt="thumbnail" style="width: 78px; height: 78px; border-radius: 10%;">
        </div>
      </div>
    </router-link>
  </div>
  <!--
    <div ref="loader" class="loader"></div>
  -->
</div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted, onUnmounted } from 'vue';

export default {
  methods: {
  formatDate(date) {
    const dateObj = new Date(date);
    const formattedDate = `${dateObj.getFullYear()}. ${dateObj.getMonth() + 1}. ${dateObj.getDate()}. ${dateObj.getHours()}:${dateObj.getMinutes()}`;
    return formattedDate;
  }
},
  setup() {
    const posts = ref([]);
    const page = ref(1);
    const per_page = 10;
    const postTotalPages = ref(1);
    const loader = ref(null);
    

    async function fetchPosts() {
      if (page.value <= postTotalPages.value) {
        try {
          const response = await axios.get(`api/community/list/?page=${page.value}`);
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

.post_box {
  display: flex;
  align-items: center;
}

</style>
  
