<template >
<div class="background bg-whitesmoke" style="margin-top: 95px; padding-bottom: 66px; min-height: calc(105vh - 201px); display: flex; flex-direction: column; align-items: center;">
        <div class="card" v-for="news in newsList" :key="news.id" style="box-shadow: 2px 2px 2px 2px #eeeeee">
          <router-link :to="{ name: 'postDetailContentPage', params: { postId: news.post_id }}">
          <div class="row">
            <div class="flex-shrink-0">
                <!-- <img :src="post.user.user_profile_img.image"
                  alt="user profile img" class="img-fluid rounded-circle border border-dark border-3"
                  style="width: 70px;"> -->
              </div>

              <!-- <img :src="post.image" class="card-img" alt="post image" /> -->
            
              <div class="card-body">
                <p class="card-text" style=" color: black; font-weight: bold;">제목 : {{ news.post_title }}</p>
                <p class="card-text" style=" color: black; font-size: 13px; margin-top: -2%;">작성자 : {{ }}</p>
                <p class="card-text" style=" color: black;">{{ formatDate(news.post_date) }}</p>
                <!-- <p class="card-text">내용 : {{ post.post_contents }}</p> -->
              </div>
            
          </div>
        </router-link>
      </div>
    </div>
</template>
<script>
import axios from 'axios';
import {ref,onMounted} from 'vue';

export default {
    methods: {
  formatDate(date) {
    const dateObj = new Date(date);
    const formattedDate = `${dateObj.getFullYear()}. ${dateObj.getMonth() + 1}. ${dateObj.getDate()}. ${dateObj.getHours()}:${dateObj.getMinutes()}`;
    return formattedDate;
  }
},
    setup(){
        const page = ref(1);
        const per_page = 10;
        const postTotalPages = ref(1);
        const newsList  = ref([]);
      const loader = ref(null);

        async function fetchNews() {
            if (page.value <= postTotalPages.value) {
              try {
                const response = await axios.get(`/api/community/newslist/?page=${page.value}`);
                newsList.value.push(...response.data.results);
                postTotalPages.value = Math.ceil(response.data.count / per_page);
                page.value += 1;
              } catch (err) {
                console.error('err:', err);
              }
            }
    }
    let observer;
    
    onMounted(async () => {
      await fetchNews();

      observer = new IntersectionObserver(async (entries, observer) => {
        if (entries[0].isIntersecting) {
          await fetchNews();
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


        return{
          loader,
            newsList,
            fetchNews
        }
    }
}
</script>
<style lang="">
    
</style>