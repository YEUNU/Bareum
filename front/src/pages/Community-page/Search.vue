<template >

<nav class="navbar fixed-top bg-theme" style="padding: 10px 0;">
      <div class="container-fluid">
        <span class="navbar-brand" @click="goBack" style="margin-right: 0px">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="white" class="bi bi-arrow-left"
            viewBox="0 0 16 16">
            <path fill-rule="evenodd"
              d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
          </svg>
        </span>
        <div class="search"  style="width: calc(100% - 37px)">
                    <input class="search-input" type="text" :placeholder="placeholder" @keydown.enter="search">
                    <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search()">
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

    const goBack = () => {
        router.back();
      };

    return {
      searchQuery,
      placeholder,
      search,
      goBack,
   };
  },
};
</script>
<style>

</style>