<template>
    <div>
        <h1>추천 제품</h1>
        <ul>
            <li v-for="(r, index) in userNutraceuticals" :key="index">
                <div class="item-box" :class="{ 'ad-border': r.광고상품 }">
                    <h3>{{ r.제품명 }}</h3>
                    <p>업소명: {{ r.업소명 }}</p>
                </div>
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




<style>
.item-box {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-bottom: 10px;
}
.ad-border {
  border-color: blue;
}
</style>