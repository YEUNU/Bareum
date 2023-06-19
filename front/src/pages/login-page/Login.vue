<template>
  <div class="logcontainer">
    <form @submit.prevent="login">

      <h1>Healthy Pal</h1>

      <input type="text" v-model="form.userLoginid" required placeholder="userLoginid" />
      <input type="password" v-model="form.password" required placeholder="Password" />
      <button type="submit">Login</button>
    </form>
    <router-link to="signup"><button style="margin-top:5%;">회원가입</button></router-link>
  </div>
  <div style="margin-top:5%;">
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
            const loginResult = response.data;
            if (loginResult!=null) {
              userLogin(loginResult.member_id,loginResult.login_id,loginResult.user_name);
              console.log(userInfo)
              router.push("/");
            } else {
              throw new Error("Login failed");

            }
          })
          .catch((err)=>{
            console.error(err)
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