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

export default {
  data() {
    return {
      posts: [],
      page: 1,
      postTotalPages: 1,
      loader: ref(null),
      observer: null,
    };
  },
  methods: {
    formatDate(date) {
    const dateObj = new Date(date);
    const formattedDate = `${dateObj.getFullYear()}. ${dateObj.getMonth() + 1}. ${dateObj.getDate()}. ${dateObj.getHours()}:${dateObj.getMinutes()}`;
    return formattedDate;
  },
    async fetchPosts(query) {
      try {
        const response = await axios.get(
          `http://localhost:5173/api/community-search/result?searchQuery=${query}&page=${this.page}`
        );
        this.posts = [
          ...this.posts,
          ...response.data.data.map((postData) => {
            const { pk, fields } = postData;
            return {
              post_id: pk,
              ...postData,
              author: postData.user.user_name,
            };
          }),
        ];
        this.postTotalPages = Math.ceil(response.data.count / 10);
        this.page++;
      } catch (error) {
        console.error("Error fetching filtered posts:", error);
      }
    },
  },
  mounted() {
    this.observer = new IntersectionObserver(async (entries, observer) => {
      if (entries[0].isIntersecting) {
        await this.fetchPosts(this.$route.query.searchQuery);
      }
    },
    {
        root: null,
        rootMargin: "0px",
        threshold: 1.0,
      }
    );

    if (this.loader) {
      this.observer.observe(this.loader);
    }
  },
  beforeUnmount() {
    if (this.loader) {
      observer.unobserve(this.loader);
    }
  },
  watch: {
    "$route.query.searchQuery": {
      immediate: true,
      handler(newQuery) {
        this.page = 1;
        this.posts = [];
        this.fetchPosts(newQuery);
      },
    },
  },
};
</script>


<style lang="">

</style>