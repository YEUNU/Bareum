<template>
    <div>
      <div class="card" v-for="post in posts" :key="post.post_id">
        <router-link :to="{ name: 'postDetailPage', params: { postId: post.post_id }}">
          <div class="row">
            <div class="col-6">
              <div class="card-body">
                <p class="card-text">{{ post.post_date }}</p>
                <p class="card-text">제목 : {{ post.post_title }}</p>
                <p class="card-text">내용 : {{ post.post_contents }}</p>
              </div>
            </div>
            <div class="col-6">
              <img :src="post.image" class="card-img" alt="post image" />
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
      };
    },
    methods: {
      async fetchPosts(query) {
        try {
          const response = await axios.get(
            `http://localhost:8000/api/community-search/result?searchQuery=${query}&page=${this.page}`
          );
          this.posts = [
            ...this.posts,
            ...JSON.parse(response.data).map((postData) => {
              const { pk, fields } = postData;
              return {
                post_id: pk,
                ...fields,
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
      let observer;
      observer = new IntersectionObserver(async (entries, observer) => {
        if (entries[0].isIntersecting) {
          await this.fetchPosts(this.$route.query.searchQuery);
        }
      });
  
      if (this.loader) {
        observer.observe(this.loader);
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
