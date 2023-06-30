<template>
    <div>
        <div>
            복용중인 영양제가 있으신가요?
            <button @click="yes">예</button>
            <button @click="no" >아니오</button>

        </div>
        <div v-if="userSelect==1">
            <router-link to="/taking/search">검색해서 추가하기</router-link>
            <router-link to="/ocr/camera">사진찍어서 추가하기</router-link>
        </div>
        <div v-if="userSelect==2">
            <router-link to="/recommend">영양제 추천 받으러 가기</router-link>
        </div>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';
import {ref} from 'vue';

export default {
    setup(){
        const router = useRouter();
        const userSelect = ref(0);

        const yes = () => {
            userSelect.value = 1;
        } 
        const no = () => {
            userSelect.value = 2;
        } 

        return{
            yes,
            no,
            userSelect

        }
    }
}
</script>
<style lang="">
    
</style>