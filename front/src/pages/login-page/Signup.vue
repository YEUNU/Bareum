<template lang="">
    <div>
        <input type="text" id="id" name="id" placeholder="아이디" title="아이디" class="input_text" maxlength="41" value=""><br/>
        <input type="password" id="pw" name="pw" placeholder="비밀번호" title="비밀번호" class="input_text" maxlength="16"><br/>
        <input type="password" id="ckpw" name="ckpw" placeholder="비밀번호 확인" title="비밀번호 확인" class="input_text" maxlength="16"><br/>
        <p>대충 약관 및 개인정보 입력하라는 내용</p>
        <input type="checkbox" v-model="agree"><span>동의</span><br/>

        <button @click="userSignup">가입하기</button><br/>
        <router-link to="/login">이미 회원이신가요?</router-link>
    </div>
</template>
<script>
import { ref } from 'vue'
import { useRouter } from "vue-router";
import { useStore } from '../../stores';

export default {
    name:"SignupPage",
    setup() {
        const agree = ref(false);
        const store = useStore();
        const router = useRouter();

        const userSignup = () => {
            if(agree.value){
                store.login();
                router.push({
                    path: "/",
                });
            }
            else{
                alert("약관에 동의 해야 함 ㅎㅎ;");
            };

        };
        return {
            store,
            router,
            agree,
            userSignup,
        };
  },
}
</script>
<style lang="">
    
</style>