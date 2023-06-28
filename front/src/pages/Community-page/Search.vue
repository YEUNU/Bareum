<template >
            <nav class="navbar fixed-top bg-light">
            <div class="container-fluid">
    <div class="search">
      <input class="search-input" type="text" :placeholder="placeholder" v-model="searchQuery" @keydown.enter="search">
        <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search"> 
    </div>
    </div>
    </nav>
    <router-view></router-view>
</template>
<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const searchQuery = ref('');
    const placeholder = '검색어를 입력하세요';
    const router = useRouter();

    const search = () => {
      router.push({
        name: 'commuSearchResult',
        query: { searchQuery: searchQuery.value },
      });
    };

    return {
      searchQuery,
      placeholder,
      search,
   };
  },
};
</script>
<style>

</style>