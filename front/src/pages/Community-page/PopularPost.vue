<template lang="">
    <div>
        인기게시글 모음
    </div>
    <div v-for="post in popularPostList" :key="post.id">

    </div>
</template>
<script>
import axios from 'axios';
import {ref} from 'vue';

export default {
    setup(){
        const popularPostList  = ref([]);
        // async function fetchPopularPost(pageNumber){
        //     try{
        //         const response = await axios.get(`api/community/popularlist?page=${pageNumber}`);
        //         popularPostList.value = response.data.results;
        //     }catch(err){
        //         console.error("err:",err);
        //     }

        // };
        return{
            popularPostList,

        }
    }
}
</script>
<style lang="css">
    
</style>