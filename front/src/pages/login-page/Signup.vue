<template>
    <div>
      <input type="text" v-model="userLoginid" placeholder="userLoginid" />
      <input type="password" v-model="password" placeholder="Password" />
      <input type="text" v-model="userName" placeholder="userName" />
      <button @click="signup">Sign Up</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref } from 'vue';
  
  export default {
    setup() {
      const userLoginid = ref('');
      const password = ref('');
      const userName = ref('');
  
      const signup = () => {
        axios
          .post('/api/signup/', {
            userLoginid: userLoginid.value,
            password: password.value,
            userName: userName.value
          })
          .then(response => {
            // 회원가입 성공 처리
          })
          .catch(error => {
            // 회원가입 실패 처리
          });
      };
  
      return {
        userLoginid,
        password,
        userName,
        signup,
      };
    },
  };
  </script>
  