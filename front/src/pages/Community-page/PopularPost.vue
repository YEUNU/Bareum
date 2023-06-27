<template>
<div class="background bg-whitesmoke" style="margin-top: 101px; padding-top: 2vh; padding-bottom: calc(2vh + 66px); min-height: calc(105vh - 207px); display: flex; flex-direction: column; align-items: center;">
  <div class="card" v-for="post in popularPosts" :key="post.id" style="box-shadow: 2px 2px 2px 2px #eeeeee; width: 90vw; margin: 1vh; padding: 2vh;">
    <router-link :to="{ name: 'postDetailContentPage', params: { postId: post.id }}">
      <div class="post_box">
        <img v-if="post.user.user_profile_img.image !== null" :src="post.user.user_profile_img.image"
        alt="user profile img" class="img-fluid rounded-circle border border-dark border-3" style="width: 78px; height: auto;">
        <svg v-else xmlns="http://www.w3.org/2000/svg" width="78" height="78" fill="currentColor" class="bi bi-card-image" viewBox="0 0 16 16">
          <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
          <path d="M1.5 2A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-13zm13 1a.5.5 0 0 1 .5.5v6l-3.775-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12v.54A.505.505 0 0 1 1 12.5v-9a.5.5 0 0 1 .5-.5h13z"/>
        </svg>

        <!-- <img :src="post.image" class="card-img" alt="post image" /> -->

        <div class="card-body" style="padding: 1vh 5vw 1vh 3vw; flex-grow: 1;">
          <div class="card-text" style="color: black; font-weight: bold; text-align: start;">{{ post.post_title }}</div>
          <div class="card-text" style="color: black; font-size: 13px; text-align: start;">작성자 : {{ post.user.nickname }}</div>
          <div class="card-text" style="color: black; font-size: 13px; text-align: start;">{{ formatDate(post.post_date) }}</div>
        <!-- <p class="card-text">내용 : {{ post.post_contents }}</p> -->
        </div>
      </div>
    </router-link>
  </div>
</div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
  
export default {
   methods: {
    formatDate(date) {
      const dateObj = new Date(date);
      const formattedDate = `${dateObj.getFullYear()}. ${dateObj.getMonth() + 1}. ${dateObj.getDate()}. ${dateObj.getHours()}:${dateObj.getMinutes()}`;
      return formattedDate;
    }
  },
  setup() {
    const popularPosts = ref([]);

    async function fetchPopularPosts(pageNumber = 1) {
      try {
        const response = await axios.get(`/api/community/popularlist?page=${pageNumber}`); 
        const parsedData = response.data.data.map(post => {
          return {
            id: post.post_id,
            post_date: post.post_date,
            post_title: post.post_title,
            post_contents: post.post_contents,
            // 이미지 필드가 누락되어 있어서 추가합니다.
            image: post.image, 
            post_like: post.post_like,
            user: post.user, 
          };
        });
        popularPosts.value = parsedData;
      } catch (err) {
        console.error('err:', err);
      }
    }

    onMounted(async () => {
      await fetchPopularPosts();
    });

    return {
      popularPosts,
    };
  },
};
</script>

<style lang="css">
  
</style>