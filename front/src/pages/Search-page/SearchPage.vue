<template>
    <nav class="navbar fixed-top bg-theme" style="padding: 10px 0;">
      <div class="container-fluid">
        <span class="navbar-brand" @click="goBack" style="margin-right: 0px">
          <!-- SVG Element -->
        </span>
        <searchBar :placeholder="searchPlaceholder" @searchQuery="search" style="width: calc(100% - 37px)" />
      </div>
    </nav>
    <router-view :key="$route.fullPath" :query="searchQuery" />
  </template>
  
  <script>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import searchBar from "../../components/Navbar/SearchBar.vue";
  export default {
    components: { searchBar },
  
    setup() {
      const router = useRouter();
      const searchPlaceholder = ref("검색어를 입력해주세요");
      const searchQuery = ref("");
  
      const search = (receivedSearchQuery) => {
            searchQuery.value = receivedSearchQuery;
            if (receivedSearchQuery) {
            router.push({ name: "resultPage", query: { q: receivedSearchQuery } });
            console.log(receivedSearchQuery);
            } else {
            router.push({ name: "searchPageMain" });
            }
        };
  
  
      const goBack = () => {
        router.back();
      };
  
      return {
        searchPlaceholder,
        search,
        goBack,
        searchQuery,
        };
    },
  };
  </script>
  
  <style>
</style>
  