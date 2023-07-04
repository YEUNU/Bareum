<template>
<div class="background bg-whitesmoke" style="margin-top: 101px; padding-top: 2vh; padding-bottom: calc(2vh + 66px); min-height: calc(105vh - 207px); display: flex; flex-direction: column; align-items: center;">
  <div class="card" v-for="post in popularPosts" :key="post.id" style="box-shadow: 2px 2px 2px 2px #eeeeee; width: 90vw; margin: 1vh; padding: 2vh;">
    <router-link :to="{ name: 'postDetailContentPage', params: { postId: post.id }}">
      <div class="post_box">
        <!-- <img :src="post.image" class="card-img" alt="post image" /> -->
        <div class="card-body" style="padding: 1vh 5vw 1vh 3vw; width: calc(100% - 78px); flex-grow: 1;">
          <div class="card-text" style="color: black; font-weight: bold; text-align: start;">{{ post.post_title }}</div>
          <div class="card-text" style="color: black; font-size: 13px; text-align: start;">작성자 : {{ post.user.nickname }}</div>
          <div class="card-text" style="color: black; font-size: 13px; text-align: start;">{{ formatDate(post.post_date) }}</div>
          <!-- <p class="card-text">내용 : {{ post.post_contents }}</p> -->
        </div>
        <div v-if="post.post_images.image" style="width: 78px; height: 78px;">
          <img :src="post.user.post_images.image"
          alt="thumbnail" style="width: 78px; height: 78px;  border-radius: 10%;">
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
