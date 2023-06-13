<template lang="">
    <div>
        <input type="text" id="id" name="id" placeholder="아이디" title="아이디" class="input_text" maxlength="41" value=""><br>
        <input type="password" id="pw" name="pw" placeholder="비밀번호" title="비밀번호" class="input_text" maxlength="16"><br>
        <button @click="userLogin()" type="submit" class="btn_login" id="log.login">
            <span class="btn_text">로그인</span>
        </button>
        <button @click="router.push({path: '/signup'});" class="btn_signup" id="sign.signup">
            <span class="btn_text">회원가입</span>
        </button>
    </div>
</template>

<script>
import { useRouter } from "vue-router";
import { useStore } from '../../stores';
import BottomNavBar from '../../components/NavBar/BottomNavBar.vue';

//예시코드 나중에 수정
export default {
    name:"LoginPage",
    components:{BottomNavBar},
    setup() {
        const store = useStore();
        const router = useRouter();

        const userLogin = () => {
            store.login();
            console.log('Login?:', store.isLoggedIn);
            router.push({
                path: "/mypage",
            });
        };
        return {
            store,
            router,
            userLogin,
        };
  }
};
</script>


<style lang="">
    
</style>