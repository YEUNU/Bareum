<template>
<div class="background bg-whitesmoke" style="margin-top: 95px; padding-bottom: 66px; min-height: calc(105vh - 201px); display: flex; flex-direction: column; align-items: center;">
    <div class="card" v-for="post in posts" :key="post.post_id" style="box-shadow: 2px 2px 2px 2px #eeeeee; width: 80%; margin: 1vh; padding: 3vh;">
      <router-link :to="{ name: 'postDetailContentPage', params: { postId: post.post_id }}">
          <div class="post_box">
            <div style="grid-row: 1/4; grid-column: 1/2;">
                <img v-if="post.post_images.image" :src="post.post_images.image"
                  alt="post img" class="img-fluid rounded-circle border border-dark border-3"
                  style="width: 100%;">
                  <svg v-else xmlns="http://www.w3.org/2000/svg" width="50%" height="50%" fill="currentColor" class="bi bi-card-image" viewBox="0 0 16 16">
                    <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
                    <path d="M1.5 2A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-13zm13 1a.5.5 0 0 1 .5.5v6l-3.775-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12v.54A.505.505 0 0 1 1 12.5v-9a.5.5 0 0 1 .5-.5h13z"/>
                  </svg>
              </div>

              <!-- <img :src="post.image" class="card-img" alt="post image" /> -->
            
              <div class="card-body">
                <div class="card-text" style="color: black; font-weight: bold; text-align: start;">{{ post.post_title }}</div>
                <div class="card-text" style="color: black; font-size: 13px;  text-align: start;">작성자 : {{ post.user.nickname }}</div>
                <div class="card-text" style="color: black; text-align: start;">{{ formatDate(post.post_date) }}</div>
                <!-- <p class="card-text">내용 : {{ post.post_contents }}</p> -->
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
    display: grid;
    grid-template-rows: 50% 20% 25%;
    grid-template-columns: 25% 75%;
  }

  </style>
  