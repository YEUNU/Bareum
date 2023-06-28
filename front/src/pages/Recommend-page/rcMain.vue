<template>
  <div class="mycontainer">
    <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/" class="navbar-brand" style="margin-left: 2vh;">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
        </router-link>
        <div style="margin-right: 2vh;">추천 제품</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
            <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
          </svg>
        </div>
        </div>
      </nav>

    <div>
        <h1 style="text-align: left;">바름 MD's PICK</h1>
        
            <div v-for="(r, index) in userNutraceuticals" :key="index">
              <router-link :to="`/product/${r.제품코드}`">
                <div class="item-box"  :class="{ 'ad-border': r.광고상품 }">
                  <div class="d-flex align-items-center">
                    <div class="flex-shrink-0" style="margin: 5%;">
                      <img src="../../assets/alarm.png" width="50"
                      alt="제품 이미지" class="item-img"/>
                    </div>

                    <div class="flex-grow-1 ms-3" style="text-align: left; width: 100%;">
                      <div class="d-flex flex-row align-items-center">
                        <div class="col-6 col-sm-3" style="width: 100%;"><h3 style="margin-top: 5%;">{{ r.제품명 }}</h3></div>
                      </div>
                      <div>
                        <div class="col-6 col-sm-3"><p> {{r.업소명}}</p></div>
                      </div>
                    </div>
                  
                  </div>
              </div>
              </router-link>
            </div>
        
    </div>
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
  border: 2px solid #eeeeee;
  border-radius: 10px;
  margin-bottom: 10px;
}
.ad-border {
  border-color: #2dce89;
}
</style>