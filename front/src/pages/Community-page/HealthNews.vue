<template lang="">
    <div>
        영양뉴스
    </div>
    <div v-for="news in newsList" :key="news.id">

    </div>
</template>
<script>
import axios from 'axios';
import {ref} from 'vue';

export default {
    setup(){
        const newsList  = ref([]);
        // async function fetchNews(pageNumber){
        //     try{
        //         const response = await axios.get(`api/community/newslist?page=${pageNumber}`);
        //         newsList.value = response.data.results;
        //     }catch(err){
        //         console.error("err:",err);
        //     }

        // };
        return{
            newsList,

        }
    }
}
</script>
<style lang="">
    
</style>