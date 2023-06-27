<template >

            <nav class="navbar fixed-top bg-light">
            <div class="container-fluid">
    <div class="search">
        <router-link to="/community" class="navbar-brand" style="margin-left: 2vh;">
      <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
      </svg>
      </router-link>
      <input class="search-input" type="text" :placeholder="placeholder" v-model="searchQuery" @keydown.enter="search" >
        <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search"> 
    </div>
    </div>
    </nav>
    <router-view></router-view>
</template>
<script>
export default {
  data() {
    return {
      searchQuery: '',
      placeholder: '검색어를 입력하세요',
    };
  },
  methods: {
    search() {
      this.$router.push({
        name: 'commuSearchResult', 
        query: { searchQuery: this.searchQuery }, 
      });
    },
  },
};
</script>
<style>

</style>