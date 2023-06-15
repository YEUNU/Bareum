<template lang="">
  
  <div v-if="popup">
      <customSearch :selected_option="selected_option" :popup="popup" @close_popup="(close_popup) => popup = close_popup"></customSearch>
  </div>
  <div v-else>
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
import searchBar from '../../components/Navbar/SearchBar.vue'
import customSearch from '../../components/CustomSearch.vue'

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

        return {
            searchPlaceholder,
            popup,
            selected_option,
            open_popup,
        };
    }
}
</script>
<style>

</style>