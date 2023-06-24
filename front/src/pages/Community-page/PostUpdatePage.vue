<template>
    <div class="PostUpdate">
      <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/community" class="navbar-brand" style="margin-left: 2vh;">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
            <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"/>
            </svg>
            
        </router-link>
        
        </div>
        
      </nav>

      <form @submit.prevent="updatePost">
        <div class="updatetitle">
          <input id="title" style="width:100%; border: none; border-bottom: 1px solid #eeeeee;" v-model="post.post_title" required />
        </div>
        <div class="updatecontent">
          <textarea id="content" style=" width:100%; height: 20vh; border: none; border-bottom: 1px solid #eeeeee;" v-model="post.post_contents" required></textarea>
        </div>
        <div style="margin-top: 10%; text-align: left;">
            
            <div><input id="images" ref="imageInput" type="file" accept="image/*" multiple @change="previewImages" /></div>
          </div>
          <div style="margin-top: 5%; text-align: left;" v-for="(url, index) in imagePreviewUrls" :key="index">
            <img :src="url" class="preview-image" style="width:100%; height:30%;" />
            <button @click="removeImage(index)">x</button>
          </div>
        <button type="submit" style="margin-top: 5%; border-radius: 10px; width:30%; background-color:#2dce89; color:white;">수정 완료</button>
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
    .preview-image {
  width: 100px;
  height: 100px;

  object-fit: cover;
}
  .PostUpdate {
    width: 100%; /* 화면 너비에 꽉 차도록 설정 */
    height: 100%; /* 화면 높이에 꽉 차도록 설정 */
    display: block;
    border-radius: 10px;
    padding-top:10%;
    padding-bottom: 20%;
  }
  .updatetitle{
    width:100%;
    height:100%;
    display: block;
  }
  </style>