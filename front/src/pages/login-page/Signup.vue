<template>
  <div>
    <form @submit.prevent="signup">

      <input type="text" v-model="userLoginid" required placeholder="userLoginid" />
      <input type="password" v-model="password" required placeholder="password" />
      <input v-model="userName" type="text" required placeholder="userName" />
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";

export default {
  setup() {
    const userLoginid = ref("");
    const password = ref("");
    const userName = ref("");

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

