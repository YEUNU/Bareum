<template>
    <nav class="navbar fixed-top bg-theme" style="padding: 10px 0;">
      <div class="container-fluid">
        <span class="navbar-brand" @click="goBack" style="margin-right: 0px">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="white" class="bi bi-arrow-left"
            viewBox="0 0 16 16">
            <path fill-rule="evenodd"
              d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
          </svg>
        </span>
        <searchBar :placeholder="searchPlaceholder" @searchQuery="search" style="width: calc(100% - 37px)" />
      </div>
    </nav>

    <div class="background">
    <div style=" margin-top: 50px;  background-color: white; border:1px solid rgba(235, 242, 233, 1); border-radius: 6px; box-shadow: 1px 1px 1px 1px #eeeeee; text-align: left; padding: 5%; padding-bottom: 0;">최근검색어
      <div style="padding-left:5%; margin-top: 2%;">
        <div style="display: flex; justify-content: space-between;">
            <p @click="search('소화 잘되는')" style="text-align: left;">소화 잘되는</p>
            <p style="text-align: right;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
            <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"/>
            </svg></p>
        </div>
      </div>

      <div style="padding-left:5%;">
        <div style="display: flex; justify-content: space-between;">
            <p @click="search('눈 아플때')" style="text-align: left;">눈 아플때</p>
            <p style="text-align: right;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
            <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"/>
            </svg></p>
        </div>
      </div>
    </div>

    <div style="margin-top: 5%; background-color: white; border:1px solid rgba(235, 242, 233, 1); border-radius: 6px; box-shadow: 1px 1px 1px 1px #eeeeee; text-align: left; padding: 5%; padding-bottom: 0;">인기 키워드 (수정)
      <div style=" margin-top: 2%;">
        <p @click="search('아르기닌')">1. 아르기닌</p>
        <p @click="search('단백질')">2. 단백질</p>
        <p @click="search('맛있는')">3. 맛있는</p>
      </div>
    </div>

    <div style="margin-top: 5%; font-weight: bold; background-color: white; border:1px solid rgba(235, 242, 233, 1); border-radius: 6px; box-shadow: 1px 1px 1px 1px #eeeeee; text-align: left; padding: 5%; padding-bottom: 0;">바름's Ranking
      <router-link class="rank_box bg-white" style="width:100%; margin-bottom: 3%;"
    v-for="(product,index) in totalRanking" :key="index"
    :to="`/product/${product.업체별_제품코드}`">
        <div class="rank_order">{{ index + 1 }}</div>
        <div class="rank_image">
            <img class="rank_image" :src='`/media/product_images/${product.업체별_제품코드}.png`' alt="상품이미지" />
        </div>
        <div class="rank_manufacturer">{{ product.업소명 }}</div>
        <div class="rank_name">{{ product.nutraceuticals_name }}</div>
        <div class="rank_score">
            온라인 <span style="color: #FFCC21;">★</span>{{ product.review.average_rating }}({{ product.review.total_reviews }}) 
            <span style="color: gainsboro;"> | </span>
            바름 <span style="color: #FFCC21;">★</span>{{ product.bareum_review.average_rating }}({{ product.bareum_review.total_reviews }})
        </div>
        <div class="rank_price">최저가 : {{ product.review.lowest }}원</div>
    </router-link>
    </div>

  </div>

  

  
    
  

    <router-view :key="$route.fullPath" :query="searchQuery" />
  </template>
  
  <script>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import searchBar from "../../components/Navbar/SearchBar.vue";
import { onMounted } from 'vue';
import axios from 'axios';
  export default {
    components: { searchBar },
  
    setup() {
      const router = useRouter();
      const searchPlaceholder = ref("검색어를 입력해주세요");
      const searchQuery = ref("");
      const totalRanking = ref([]);

      const fetchRanking = async() => {

          try{
              const response = await axios.get(`/api/product/total-ranking/?page=${1}`);
              totalRanking.value.push(...response.data.results);
          }catch(err){
              console.error(err);
          }
            
        }
  
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
      onMounted(()=>{
        fetchRanking();
      })
  
      return {
        fetchRanking,
        totalRanking,
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
  