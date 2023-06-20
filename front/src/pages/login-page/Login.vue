<template>
  <div class="logcontainer">
    <form @submit.prevent="login">

      <h1>바름</h1>

      <input type="text" v-model="form.userLoginid" required placeholder=" 아이디" />
      <input type="password" v-model="form.password" required placeholder=" 비밀번호" />
      <button type="submit">로그인</button>
    </form>
    <div style="margin-top: 5vh; transition:.2s linear; font-weight: lighter;">또는</div>
    <hr style="width: 80%; margin: auto; text-align: center;">
    <div style="margin-top: 3vh;">소셜 로그인</div>
    <div style="display: flex; justify-content: center;">
      <div style="margin: 2vh 2vh;">
        <img style="height: 45px;"
        src="@assets/kakao_login_icon.png"
        alt="Kakao Login"
        @click="loginWithKakao"
        />
      </div>
      <div style="margin: 2vh 2vh;">
        <img style="height: 45px;"
        src="@assets/naver_login_icon.png"
        alt="Naver Login"
        @click=""
        />
      </div>
      <div style="margin: 2vh 2vh;">
        <img style="height: 45px; border: 0.75px solid #999999; border-radius: 5px;"
        src="@assets/google_login_icon.png"
        alt="Google Login"
        @click=""
        />
      </div>
    </div>
    <div style="margin-top: 3vh;">아직 회원이 아니신가요?</div>
    <router-link to="signup"><button>회원가입</button></router-link>
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
.logcontainer h1 {
  color:#2dce89;
  font-size:52px;
  text-align:center;
  transition:.2s linear;
  letter-spacing: 6px;
  margin: 3vh auto 30px auto;
  font-weight: bold;
}

.logcontainer input {
  width: 80%;
  padding: 2vh;
  margin-bottom: 1vh;
  border-radius: 8px;
  border:white;
  background-color:#E1E1E1;
}


.logcontainer button {
  cursor: pointer;
  width: calc(160px + 10vh);
  border-radius: 8px;
  border: none;
  background-color: #2dce89;
  color: white;
  font-size: 15px;
  box-shadow:0px 10px 10px -6px #2dce89;
  margin: 2vh;
}
</style>