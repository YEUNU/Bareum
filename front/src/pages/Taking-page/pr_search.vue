<template>
    <div>
      <div class="search-bar">
        <input
          type="text"
          placeholder="검색어 입력"
          v-model="searchQuery"
          @keyup.enter="handleSearch"
        />
        <button @click="handleSearch">
          <i class="fas fa-search">검색</i>
        </button>
      </div>
      <pr-result-page :searchResults="searchResults" />
    </div>
  </template>

  <script>
  import { ref } from "vue";
  import axios from "axios";
  import PrResultPage from "/app/src/pages/Taking-page/pr_result.vue";
  
  
  export default {
    components: {
      PrResultPage,
    },
    setup() {
      const searchQuery = ref("");
      const searchResults = ref([]);
  
      async function handleSearch() {
        console.log("검색어: ", searchQuery.value);
        const response = await axios.get("/api/taking/search", {
          params: { search_query: searchQuery.value },
        });
        searchResults.value = response.data;
      }
  
      return {
        searchQuery,
        handleSearch,
        searchResults,
      };
    },
  };
  </script>
  
  
  <style scoped>
  .search-bar {
    display: flex;
    justify-content: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 60px;
    background-color: #ffffff;
    padding: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    z-index: 100;
  }
  
  .search-bar input {
    width: 100%;
    height: 40px;
    font-size: 16px;
    padding: 0 10px;
    border: 1px solid #ccc;
    outline: none;
  }
  
  .search-bar input:focus {
    border: 1px solid #0077ff;
  }
  </style>