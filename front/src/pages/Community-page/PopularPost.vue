<template>
    <div>
      <div class="card" v-for="post in popularPosts" :key="post.id" style="box-shadow: 2px 2px 2px 2px #eeeeee">
        <router-link :to="{ name: 'postDetailPage', params: { postId: post.id }}">
          <div class="row">
            <div class="flex-shrink-0">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-2.webp"
                  alt="Generic placeholder image" class="img-fluid rounded-circle border border-dark border-3"
                  style="width: 70px;">
              </div>
              <!-- <img :src="post.image" class="card-img" alt="post image" /> -->

              <div class="card-body">
                <p class="card-text" style=" color: black; font-weight: bold;">제목 : {{ post.post_title }}</p>
                
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
          const parsedData = JSON.parse(response.data.data).map(post => {
            return {
              id: post.pk,
              post_date: post.fields.post_date,
              post_title: post.fields.post_title,
              post_contents: post.fields.post_contents,
              image: post.fields.image,
              post_like: post.fields.post_like
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