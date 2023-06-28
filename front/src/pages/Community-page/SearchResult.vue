<template>
  <div>
    <div class="card" v-for="post in posts" :key="post.post_id" style="box-shadow: 2px 2px 2px 2px #eeeeee">
      <router-link :to="{ name: 'postDetailContentPage', params: { postId: post.post_id }}">
        <div class="row">
          <div class="flex-shrink-0">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-2.webp"
                  alt="Generic placeholder image" class="img-fluid rounded-circle border border-dark border-3"
                  style="width: 70px;">
              </div>

            <div class="card-body">
              <p class="card-text" style=" color: black; font-weight: bold;">제목 : {{ post.post_title }}</p>
              <p class="card-text" style=" color: black; font-size: 13px; margin-top: -2%;">작성자 : {{ post.author }}</p>
              <p class="card-text" style=" color:black;">{{ formatDate(post.post_date) }}</p>

          
          </div>
        </div>
      </router-link>
    </div>
    <div ref="loader" class="loader"></div>
  </div>
</template>

<script>
import axios from "axios";
import { ref, watch, onMounted, onUnmounted } from "vue";
import { useRoute } from 'vue-router';

export default {
  setup() {
    const posts = ref([]);
    const page = ref(1);
    const postTotalPages = ref(1);
    const loader = ref(null);
    const route = useRoute();

    const formatDate = (date) => {
      const dateObj = new Date(date);
      const formattedDate = `${dateObj.getFullYear()}. ${dateObj.getMonth() + 1}. ${dateObj.getDate()}. ${dateObj.getHours()}:${dateObj.getMinutes()}`;
      return formattedDate;
    };

    const fetchPosts = async (query) => {
      try {
        const response = await axios.get(
          `http://localhost:5173/api/community-search/result?searchQuery=${query}&page=${page.value}`
        );
        posts.value = [
          ...posts.value,
          ...response.data.data.map((postData) => {
            const { pk, fields } = postData;
            return {
              post_id: pk,
              ...postData,
              author: postData.user.user_name,
            };
          }),
        ];
        postTotalPages.value = Math.ceil(response.data.count / 10);
        page.value++;
      } catch (error) {
        console.error("Error fetching filtered posts:", error);
      }
    };

    let observer;

    onMounted(() => {
      observer = new IntersectionObserver(async (entries, observer) => {
        if (entries[0].isIntersecting) {
          await fetchPosts(route.query.searchQuery);
        }
      },
      {
          root: null,
          rootMargin: "0px",
          threshold: 1.0,
        }
      );

      if (loader.value) {
        observer.observe(loader.value);
      }
    });

    onUnmounted(() => {
      if (loader.value) {
        observer.unobserve(loader.value);
      }
    });

    watch(() => route.query.searchQuery, (newQuery) => {
      page.value = 1;
      posts.value = [];
      fetchPosts(newQuery);
    }, { immediate: true });

    return {
      posts,
      page,
      postTotalPages,
      loader,
      formatDate,
      fetchPosts,
    };
  },
};
</script>


<style lang="">

</style>