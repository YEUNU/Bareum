<template lang="">
    <div>
        <searchBar :placeholder=searchPlaceholder></searchBar>
    </div>
    <div>
        검색페이지임
    </div>
    <router-link to="/search/detail"> 상세 검색하기</router-link>
</template>
<script>
import { ref } from 'vue';
import searchBar from '../../components/Navbar/SearchBar.vue'
export default {
    components:{searchBar},
    setup() {
      const searchPlaceholder = ref('검색어를 입력해주세요');
  
      return {
        searchPlaceholder
      };
    }
}
</script>
<style>


</style>