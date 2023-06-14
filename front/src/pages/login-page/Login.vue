<template>
  <div>
    <input type="text" v-model="form.userLoginid" placeholder="userLoginid" />
    <input type="password" v-model="form.password" placeholder="Password" />
    <button @click="login">Login</button>
    <p v-if="form.showErrorMessage">모든 필드를 입력하세요.</p>
    <router-link to="signup">회원가입</router-link>
  </div>
  <div>
    <img
    src="@assets/kakao_login_medium.png"
    alt="Kakao Login"
    @click="loginWithKakao"
  />
  </div>
</template>

<script>
import axios from 'axios';
import { reactive, inject } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const form = reactive({
      userLoginid: '',
      password: '',
      showErrorMessage: false,
    });

    const router = useRouter();

    const Kakao = inject('kakao'); // Kakao 객체를 가져옴

    const login = () => {
      if (form.userLoginid === '' || form.password === '') {
        form.showErrorMessage = true;
        return;
      }

      axios
        .post('/api/account/login', {
          userLoginid: form.userLoginid,
          password: form.password,
        })
        .then(response => {
          const loginResult = response.data;
          if (loginResult === 'Login successful') {
            router.push('/');
          } else {
            throw new Error('Login failed');
          }
        })
        .catch(error => {
          console.error('Error during login:', error);
        });
    };

    const loginWithKakao = () => {
      Kakao.Auth.login({
        success: (authObj) => {
          axios
            .post('/api/account/login-kakao', authObj)
            .then((response) => {
              console.log(response);
            })
            .catch((error) => {
              console.log(error);
            });
        },
        fail: (err) => {
          console.log(err);
        },
      });
    };

    return {
      form,
      login,
      loginWithKakao,
    };
  },
};
</script>
