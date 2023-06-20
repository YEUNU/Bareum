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
  import { useUserInfo } from '../../stores';
  import { useRouter } from 'vue-router';
  import Cookies from 'js-cookie';

  export default {
    setup() {
      const postTitle = ref('');
      const postContent = ref('');
      const userInfo = useUserInfo();
      const router = useRouter();
      console.log(userInfo)
      const csrf_token = Cookies.get('csrftoken');
 
      const submitPost = async () => {
        try {
          await axios.post('/api/community/write', {
          title: postTitle.value, content: postContent.value, memberId: userInfo.memberId
        }, {
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
          }
        });
          router.push('/community'); //  커뮤니티 페이지로 이동
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
  