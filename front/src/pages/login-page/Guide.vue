<template>
    <div class="guides">
            <h3 class="guideh3">복용 중인 영양제가 있으신가요?</h3>
            <button class="guidebutton" @click="no">복용 중인 영양제가 없어요</button>
            <button class="guidebutton" @click="yes">복용 중인 영양제가 있어요</button>
        <div class="guidenolink" v-if="userSelect==1">
            <router-link class="guidenobutton" to="/recommend">영양제 추천 받으러 가기</router-link>
        </div>
        <div class="guideyeslink" v-if="userSelect==2">
            <router-link class="guideyesbutton" to="/taking/search">검색해서 추가하기</router-link>
            <router-link class="guideyesbutton" to="/ocr/camera">사진찍어서 추가하기</router-link>
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
<style>
.guides {
    width: 100%;
    height: 100%;
}

.guideh3 {
    font-weight: bold;
}

.guidebutton {
    margin-top: 5%;
    width: 100%;
    padding-top: 5%;
    padding-bottom: 5%;
    text-align: center;
    background-color:  #2dce89;
    color: white;
    font-size: 20px;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    box-shadow: 2px 2px 2px 2px #eeeeee;
}

.guideyeslink {
    display: flex;
    margin-top: 10%;
    justify-content: space-between;
}

.guideyesbutton {
    width: 40%;
    text-align: center;
    padding-top: 5%;
    padding-bottom: 5%;
    background-color:  #2dce89;
    color: white;
    font-size: 14px;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    box-shadow: 2px 2px 2px 2px #eeeeee;
}

.guidenolink {
    display: flex;
    margin-top: 10%;
    justify-content: center;
}

.guidenobutton {
    width: 50%;
    text-align: center;
    padding-top: 5%;
    padding-bottom: 5%;
    background-color:  #2dce89;
    color: white;
    font-size: 14px;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    box-shadow: 2px 2px 2px 2px #eeeeee;
}


</style>