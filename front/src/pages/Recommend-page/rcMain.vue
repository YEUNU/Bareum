<template>
  <div class="background" style="width: 100%; display: block; background-color: #eeeeee; margin-top: 10%; padding-bottom: 10%;">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <a href="javascript:history.back()" class="navbar-brand" style="margin-left: 2vh;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left"
            viewBox="0 0 16 16">
            <path fill-rule="evenodd"
              d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
          </svg>
        </a>
        <div style="margin-right: 2vh;">추천</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill"
            viewBox="0 0 16 16">
            <path
              d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
          </svg>
        </div>
      </div>
    </nav>
    <div style="width: 100%; border-radius: 6px; font-weight: bold; font-size: 20px; color: white; background-color: #2dce89; border:none; margin-top: 5%; margin-bottom: 0;">AI기반 건강기능식품 추천</div>
   
    <div style="width: 100%; background-color: white;" v-for="(r, index) in userNutraceuticals" :key="index">
      <router-link :to="`/product/${r.제품코드}`">
        <div class="item-box" style="margin-bottom: 0;" :class="{ 'ad-border': r.광고상품 }">
          <div class="d-flex align-items-center">
            <img :src="`../../../media/product_images/${r.제품코드}.png`" width="200" alt="제품 이미지" class="item-img" />
            <div class="flex-grow-1 ms-3" style="text-align: left; width: 100%;">
              <div class="text-container">
                <p v-if="r.광고상품" style="margin-left: 2%; color:#2dce89">바름's 추천.</p>
              </div>
              <div class="d-flex flex-row align-items-center">
                <div class="col-6 col-sm-3">
                  <h2 style="margin-top: 5%; margin-left: 5%; color:black; width:200%;">

                    {{ r.제품명 }}
                  </h2>
                  <p style="margin-left: 5%; color:#808080; width:200%;">{{ r.업소명 }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </router-link>
    </div>


    <div style="width: 100%; border-radius: 6px; font-weight: bold; font-size: 20px; color: white; background-color: #2dce89; border:none; margin-top: 0%; margin-bottom: 0;">연령 맞춤 건강기능식품 추천</div>
    <div style="width: 100%; background-color: white;" v-for="(r, index) in recommendByAgeList" :key="index">
      <router-link :to="`/product/${r.업체별_제품코드}`">
        <div class="item-box" style="margin-bottom: 0;">
          <div class="d-flex align-items-center">
            <img :src="`../../../media/product_images/${r.업체별_제품코드}.png`" width="200" alt="제품 이미지" class="item-img" />
            <div class="flex-grow-1 ms-3" style="text-align: left; width: 100%;">
              <div class="d-flex flex-row align-items-center">
                <div class="col-6 col-sm-3">
                  <h2 style="margin-top: 5%; margin-left: 5%; color:black; width:200%;">

                    {{ r.nutraceuticals_name }}
                  </h2>
                  <p style="margin-left: 5%; color:#808080; width:200%;">{{ r.업소명 }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        </router-link>
    </div>


    <div style="width: 100%; border-radius: 6px; font-weight: bold; font-size: 20px; color: white; background-color: #2dce89; border:none; margin-top: 0%; margin-bottom: 0;">건강관심항목 별 건강기능식품 추천
    </div>
    <div style="width: 100%; background-color: #eeeeee;" v-for="(r, index) in recommendByInterestList" :key="index">
      <div class="indexgroup" style="width: 100%; border-radius: 6px; font-weight: bold; font-size: 20px; color: white; background-color: #2dce89; border:none;">{{ index }}</div>
      
      <div style="background-color: white;" v-for="(product,index) in r" :key="index">
        <router-link :to="`/product/${product.업체별_제품코드}`">
        <div class="item-box" style="margin-bottom: 0;">
          <div class="d-flex align-items-center">
            <img :src="`../../../media/product_images/${product.업체별_제품코드}.png`" width="200" alt="제품 이미지" class="item-img" />
            <div class="flex-grow-1 ms-3" style="text-align: left; width: 100%;">
              <div class="d-flex flex-row align-items-center">
                <div class="col-6 col-sm-3">
                  <h2 style="margin-top: 5%; margin-left: 5%; color:black; width:200%;">

                    {{ product.nutraceuticals_name }}
                  </h2>
                  <p style="margin-left: 5%; color:#808080; width:200%;">{{ product.업소명 }}</p>
                </div>
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
import ageGroup from '../Product-page/Rank-page/age_group.js';
import nutra_presonal_mapping from '../Product-page/Rank-page/nutra_presonal_mapping.js';

export default {
  setup() {
    const userInfo = useUserInfo();
    const loginId = computed(() => userInfo.loginId);
    const userNutraceuticals = ref([]);
    const recommendByAgeList = ref([]);
    const recommendByInterestList = ref({});
    const userInterest = ref([]);
    
    async function fetchNutraceuticals() {
      try {
        const response = await axios.post("/api/recommend/", {
          loginId: loginId.value,
        });
        userNutraceuticals.value = response.data.nutraceuticals;
      } catch (error) {
        console.log("Error fetching user nutraceuticals:", error);
      }
    };
    const getUserInterest = async() => {
          try{
            const response = await axios.get('/api/account/interest/');
            userInterest.value = response.data.interest;
            console.log(userInterest)

          }catch(err){
            console.error(err);
          }
        }


        const recommendByAge = async () => {
          let ingredients;
          try {
            let age = userInfo.age;
            if (age <= 12) {
              ingredients = ageGroup["유아 및 어린이 (1-12세)"];
            } else if (age < 19) {
              ingredients = ageGroup["청소년 (13-18세)"];
            } else if (age < 39) {
              ingredients = ageGroup["성인 (19-39세)"];
            } else if (age < 65) {
              ingredients = ageGroup["중년 성인 (40-64세)"];
            } else if (age >= 65) {
              ingredients = ageGroup["노인 (65세 이상)"];
            }
            console.log(ingredients)
            const response = await axios.get('/api/recommend/age/', {
              params: { ingredients: JSON.stringify(ingredients) },
            });
            recommendByAgeList.value = response.data;
            console.log('age',recommendByAgeList.value);
          } catch (err) {
            console.error(err);
          }
        };

      const recommendByInterest = async () => {
        try {
            const promises = userInterest.value.map(async (interest) => {
              const ingredients = nutra_presonal_mapping[interest];
              const response = await axios.get("/api/recommend/interest/", {
                params: { ingredients: JSON.stringify(ingredients) },
              });
              return response.data;
            });

            const responses = await Promise.all(promises);
            const interestObj = userInterest.value.reduce((obj, interest, index) => {
              obj[interest] = responses[index];
              return obj;
            }, {});
            recommendByInterestList.value = interestObj;
            console.log("recommend", recommendByInterestList.value);
        } catch (err) {
          console.error(err);
        }
      };


    onMounted(async() => {
      await getUserInterest();
      recommendByInterest();
      recommendByAge();
      fetchNutraceuticals();
    });

    return {
      userNutraceuticals,
      recommendByInterest,
      recommendByAge,
      recommendByAgeList,
      recommendByInterestList,
      userInterest

    };
  },
};
</script>




<style>
.myrecommendcontainer {
  width: 100%;
  /* 화면 너비에 꽉 차도록 설정 */
  height: 100%;
  /* 화면 높이에 꽉 차도록 설정 */
  display: block;
  margin-bottom: 5%;
  padding-top: 10%;
  padding-bottom: 10%;
}

.item-box {
  padding: 20px;
  border: 2px solid #eeeeee;
  border-radius: 10px;
  margin-bottom: 10px;
}

.ad-border {
  padding: 20px;
  border: 2px solid #2dce89;
  border-radius: 10px;
  margin-bottom: 10px;
}
</style>