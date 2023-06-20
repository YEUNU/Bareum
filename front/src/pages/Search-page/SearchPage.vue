<template lang="">
<nav class="navbar fixed-top bg-white">
    <div class="container-fluid">
        <span class="navbar-brand" @click="() => {$router.back(); searchbarClear();}">
        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"></path>
        </svg>
        </span>
        <searchBar ref="searchbarAPI" :placeholder=searchPlaceholder @searchQuery="(searchQuery) => search(searchQuery)" style="width: calc(95% - 42px)"></searchBar>
    </div>
</nav>
<router-view/>

</template>


<script>
import { ref } from 'vue';
import { useRouter } from "vue-router";
import searchBar from '../../components/Navbar/SearchBar.vue';
export default {
    components:{searchBar},

    setup() {
        const router = useRouter();
        const searchPlaceholder = ref('검색어를 입력해주세요');
        const searchbarAPI = ref(null);
        const search = (searchQuery) => {
            console.log(searchQuery);
            if(searchQuery) {
                searchbarAPI.value.getQuery(searchQuery);

                router.push({name: 'resultPage', query: { q: searchQuery }});
            }
        };

        const searchbarClear = () => {
            searchbarAPI.value.searchbar_clear();
        };

        return {
            searchPlaceholder,
            search,
            searchbarAPI,
            searchbarClear,
        };
    }
}
</script>


<style>
    
</style>