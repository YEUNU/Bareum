<template>
  <div>
    <h1>게시물 수정 페이지</h1>
    <form @submit.prevent="updatePost">
      <div>
        <label for="title">제목</label>
        <input id="title" v-model="post.post_title" required />
      </div>
      <div>
        <label for="content">내용</label>
        <textarea id="content" v-model="post.post_contents" required></textarea>
      </div>
      <button type="submit">수정 완료</button>
    </form>
  </div>
</template>

  
  <script>
  import { ref, reactive, onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import axios from 'axios';
  
  export default {
    setup() {
      const router = useRouter();
      const route = useRoute();
      const post = reactive({ post_title: '', post_contents: '' });
  
      const fetchPost = async () => {
        const postId = route.params.postId;
        try {
          const response = await axios.get(`/api/community/detail/${postId}`);
          post.post_title = response.data.post_title;
          post.post_contents = response.data.post_contents;
        } catch (error) {
          console.error('Error fetching the post:', error);
        }
      };
  
      const updatePost = async () => {
  const csrfToken = getCookie("csrftoken");
  const config = {
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
  };
  const postId = route.params.postId;
  try {
    await axios({
      method: "put",
      url: `/api/community/update/${postId}`,
      headers: {
        "X-CSRFToken": csrfToken,
      },
      data: {
        post_title: post.post_title,
        post_contents: post.post_contents,
      },
    });
    router.push({
      name: "postDetailContentPage",
      params: { postId: postId },
    }); // 수정된 게시물로 이동
  } catch (error) {
    console.error("Error updating the post:", error);
  }
};

  
      const getCookie = (name) => {
        const value = '; ' + document.cookie;
        const parts = value.split('; ' + name + '=');
        if (parts.length === 2) return parts.pop().split(';').shift();
      };
  
      onMounted(fetchPost);
  
      return {
        post,
        updatePost,
      };
    },
  };
  </script>
  
  
  <style>
  </style>