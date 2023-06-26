<template>
  <div>
    <div class="search-bar-wrapper">
      <div class="search-bar">
        <input
          type="text"
          placeholder="검색어 입력"
          v-model="searchQuery"
          @keyup.enter="handleSearch"
          style="border-radius: 8px; padding-right: 30px;"
        >
          <svg @click="handleSearch" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#2dce89" class="bi bi-search" viewBox="0 0 16 16" style="position: absolute; top: 50%; transform: translateY(-50%); right: 20px;"  >
          <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
          </svg>
      </div>
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
.search-bar-wrapper {
  margin-bottom: 1rem;
}

.search-bar {
  display: flex;
  justify-content: center;
  width: 100%;
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
