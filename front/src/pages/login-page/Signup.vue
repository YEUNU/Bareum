<template>
    <div>
      <input type="text" v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button @click="signup">Sign Up</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref } from 'vue';
  
  export default {
    setup() {
      const username = ref('');
      const password = ref('');
  
      const signup = () => {
        axios
          .post('/api/signup/', {
            username: username.value,
            password: password.value,
          })
          .then(response => {
            // 회원가입 성공 처리
          })
          .catch(error => {
            // 회원가입 실패 처리
          });
      };
  
      return {
        username,
        password,
        signup,
      };
    },
  };
  </script>
  