<template>
    <div class="search-container">
      <router-link to="/search">
        <SearchBar :placeholder="searchPlaceholder"></SearchBar>
      </router-link>
    </div>
    <div>
      홈페이지임
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import SearchBar from '../../components/Navbar/SearchBar.vue';
  
  export default {
    components: {
      SearchBar
    },
    setup() {
      const searchPlaceholder = ref('건강기능식품을 검색해보세요');
  
      return {
        searchPlaceholder
      };
    }
  };
  </script>
  
  <style>
  /* 스타일 정의 */
  </style>
  