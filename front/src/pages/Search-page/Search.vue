<template lang="">
  <div v-if="popup">
    <customSearch :selected_option="selected_option" :popup="popup" @close_popup="(close_popup) => popup = close_popup" @selected_items="(option, item) => searchOptions(option, item)"></customSearch>
  </div>
  <div v-else>
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
          <span class="navbar-brand" @click="$router.back()">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"></path>
            </svg>
          </span>
      </div>
  </nav>
    <div>
      <searchBar :placeholder=searchPlaceholder></searchBar>
    </div>
    <div>
      검색페이지임
    </div>
    <router-link to="/search/detail"> 상세 검색하기</router-link>
    <div>
      <button @click="open_popup('personalize')">personalize</button>
      <button @click="open_popup('ingredient')">ingredient</button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import searchBar from '../../components/Navbar/SearchBar.vue';
import customSearch from '../../components/CustomSearch.vue';
import axios from "axios";

export default {
  components:{searchBar, customSearch},
  setup() {
    const searchPlaceholder = ref('검색어를 입력해주세요');
    
    const popup = ref(false);
    const selected_option = ref(null);
    
    const open_popup = (params) => {
      selected_option.value = params;
      popup.value = true;
    }
    
    const searchOptions = (selected_option, selected_items) => {
      if(selected_items.value.length != 0) {
        axios.get('/data', {
          params: {
            option: selected_option,
            detail: selected_items.join(","), // 체크한 항목들 걍 ','로 붙임
          }
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    }

    return {
      searchPlaceholder,
      popup,
      selected_option,
      open_popup,
      searchOptions,
    };
  }
}
</script>
<style>

</style>