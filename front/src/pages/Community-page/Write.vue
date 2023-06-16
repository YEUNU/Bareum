<template>
    <div>
      <h1>글쓰기 페이지</h1>
      <form @submit.prevent="submitPost">
        <div>
          <label for="title">제목</label>
          <input id="title" v-model="postTitle" required />
        </div>
        <div>
          <label for="content">내용</label>
          <textarea id="content" v-model="postContent" required ></textarea>
        </div>
        <button type="submit">글쓰기</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  import axios from 'axios';
  
  export default {
    setup() {
      const postTitle = ref('');
      const postContent = ref('');
  
      const submitPost = async () => {
        try {
          await axios.post('/api/comminity/write', { title: postTitle.value, content: postContent.value });
          this.$router.push('/community'); //  커뮤니티 페이지로 이동
        } catch (error) {
          console.error('글 작성 중 에러가 발생했습니다:', error);
        }
      };
  
      return {
        postTitle,
        postContent,
        submitPost,
      };
    },
  };
  </script>
  
  <style>
  </style>
  