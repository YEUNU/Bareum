<template>
  <div class="logcontainer">
    <form @submit.prevent="signup">

      <h1>Healthy Pal</h1>

      <div class="back">
      <input type="text" v-model="userLoginid" required placeholder="userLoginid"/>
      <input type="password" v-model="password" required placeholder="password" />
      <input v-model="userName" type="text" required placeholder="userName" />
      <button type="submit">Sign Up</button>
    </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
import {useRouter} from 'vue-router';

export default {
  setup() {
    const userLoginid = ref("");
    const password = ref("");
    const userName = ref("");
    const router = useRouter();


    const signup = () => {
      axios
        .post("/api/account/signup", {
          userLoginid: userLoginid.value,
          password: password.value,
          userName: userName.value,
          withCredentials: true,
        })
        .then((response) => {
          if (response.data.result === "success") {
            console.log(response.data.message);
            // 회원가입 성공 및 로그인 페이지로 이동
            alert("회원가입에 성공했습니다. 로그인 페이지로 이동합니다.");
            router.push('/login');
          } else {
            console.error("회원가입 실패:", response.data.message);
            alert("회원가입 실패");

          }
        })
        .catch((error) => {
          console.error("회원가입 중 오류 발생:", error);
          alert("회원가입 중 오류 발생");

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

<style>

.logcontainer h1{
  color:#2dce89;
  font-size:52px;
  letter-spacing:-3px;
  text-align:center;
  margin:120px 0 80px 0 ;
  transition:.2s linear;
}

.logcontainer input {
  padding: 2%;
  margin-bottom: 5%;
  border-radius: 10px;
  border:white;
  background-color:#E1E1E1;
}



.logcontainer button {
    cursor: pointer;
    width: 50%;
    border-radius: 10px;
    border: none;
    background-color: #2dce89;
    color: white;
    font-size: 15px;
    box-shadow:0px 10px 10px -6px #2dce89;
}
</style>

