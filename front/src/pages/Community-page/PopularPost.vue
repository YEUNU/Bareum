<template>
  <div>
    <div class="card" v-for="post in popularPosts" :key="post.id" style="box-shadow: 2px 2px 2px 2px #eeeeee">
      <router-link :to="{ name: 'postDetailContentPage', params: { postId: post.id }}">
        <div class="row">
          <div class="flex-shrink-0">
            <img :src="post.user.user_profile_img"
            alt="user profile img" class="img-fluid rounded-circle border border-dark border-3"
                style="width: 70px;">
            </div>
            <!-- <img :src="post.image" class="card-img" alt="post image" /> -->

            <div class="card-body">
              <p class="card-text" style=" color: black; font-weight: bold;">제목 : {{ post.post_title }}</p>
              <p class="card-text" style=" color: black; font-size: 13px; margin-top: -2%;">작성자 : {{ post.user.nickname }}</p>
              <p class="card-text" style=" color:black;">{{ formatDate(post.post_date) }}</p>
              <!-- <p class="card-text">내용 : {{ post.post_contents }}</p> -->
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