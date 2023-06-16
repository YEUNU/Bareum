<template>
  <div>
    <form @submit.prevent="login">
      <input type="text" v-model="form.userLoginid" required placeholder="userLoginid" />
      <input type="password" v-model="form.password" required placeholder="Password" />
      <button type="submit">Login</button>
    </form>
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
import axios from "axios";
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { loginWithKakao } from "/src/kakaoLogin.js";
import {useUserInfo} from "../../stores.js"

export default {
  setup() {
    const userInfo = useUserInfo();
    const {userLogin} = userInfo;

    const form = reactive({
      userLoginid: "",
      password: "",
    });

    const error = ref(null);
    const router = useRouter();


    const login = () => {
      axios
        .post("/api/account/login", {
          userLoginid: form.userLoginid,
          password: form.password,
          withCredentials: true,
        })
        .then((response) => {
          const loginResult = response.data;
          if (loginResult!=null) {
            userLogin(loginResult.login_id,loginResult.user_name);
            console.log(userInfo)
            router.push("/");
          } else {
            throw new Error("Login failed");
            
          }
        })
        .catch((error) => {
          console.error("Error during login:", error);
          alert("아이디 또는 비밀번호가 틀림");
          form.userLoginid = "";
          form.password = "";
        });
    };


    const kakaoLogin = () => {
      loginWithKakao()
        .then((authObj) => {
          console.log(authObj)
          axios.post("/api/account/kakao/login", authObj, {
                headers: {
                    "Content-Type": "application/json",
                    withCredentials: true,
                },
            })
          .then((response)=>{

            router.push("/");

          })
          .catch((err)=>{

          })
        })
        .catch((error) => {
          console.error("Error during Kakao login:", error);
        });
    };

    return {
      form,
      login,
      loginWithKakao: kakaoLogin, 
      error,
    };
  },
};
</script>
