<template>

    <div class="mycontainer">
      <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/taking/regist" class="navbar-brand" style="margin-left: 2vh;">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
        </router-link>
        <div style="margin-right: 2vh;">섭취 관리</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
            <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
          </svg>
        </div>
        </div>
      </nav>
    <div class="search-bar-wrapper">
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
    </div>
    <pr-result-page :searchResults="searchResults" />
  
</div>
</template>

<script>
import { ref, computed } from "vue";
import axios from "axios";
import PrResultPage from "/app/src/pages/Taking-page/pr_result.vue";
import {useUserInfo} from "../../stores.js"

export default {
  components: {
    PrResultPage,
  },
  setup() {
    const searchQuery = ref("");
    const searchResults = ref([]);
    const userInfo = useUserInfo();
    const loginId = computed(() => userInfo.loginId);


    async function handleSearch() {
      console.log("검색어: ", searchQuery.value);
      const response = await axios.get("/api/taking/search", {
        params: { search_query: searchQuery.value, login_id: loginId.value },
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
