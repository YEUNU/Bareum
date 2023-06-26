<template>
    <div>
        <h1>추천 제품</h1>
        <ul>
            <li v-for="(r, index) in userNutraceuticals" :key="index">
                {{ r.제품명 }} ({{ r.업소명 }})
            </li>
        </ul>
    </div>
</template>
  
  <script>
  import { ref, onMounted, computed } from "vue";
  import { useUserInfo } from "../../stores.js";
  import axios from "axios";
  
  export default {
    setup() {
      const userInfo = useUserInfo();
      const loginId = computed(() => userInfo.loginId);
      const userNutraceuticals = ref([]);
  
      async function fetchNutraceuticals() {
        try {
          const response = await axios.post("/api/recommend/", {
            loginId: loginId.value, 
          });
          userNutraceuticals.value = response.data.nutraceuticals;
        } catch (error) {
          console.log("Error fetching user nutraceuticals:", error);
        }
      }
  
      onMounted(() => {
        console.log(loginId.value); 
        fetchNutraceuticals();
      });
  
      return {
        userNutraceuticals,
      };
    },
  };
  </script>




<style scoped>
    
</style>