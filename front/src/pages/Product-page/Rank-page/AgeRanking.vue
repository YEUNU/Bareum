<template>
    <div class="background bg-whitesmoke" style="padding-top: 56px; min-height: 100%; padding-bottom: 60px;">
        <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
        {{selectedAgegroup}}
        </button>
        <ul class="dropdown-menu">
          <li v-for="(age, index) in ageGroup" :key="index" @click="fetchAgeGroupRanking(age)">{{ age }}</li>
        </ul>
          </div>
          <p>{{ selectedAgegroup }} 에게 도움을 줄 수 있는 {{ nutrientsByAgeGroup[selectedAgegroup] }} 가 함유된 제품들 입니다. </p>
          <router-link class="rank_box bg-white"
              v-for="(product,index) in ageRanking" :key="index"
              :to="`/product/${product.업체별_제품코드}`">
              <div class="rank_order">{{ index + 1 }}위</div>
              <div class="rank_image"><img class="rank_image" :src='`/media/product_images/${product.업체별_제품코드}.png`' alt="상품이미지"
                      style="height: min(25vh, 25vw); width: min(25vh, 25vw);" /></div>
              <div class="rank_manufacturer">{{ product.업소명 }}</div>
              <div class="rank_name">{{ product.nutraceuticals_name }}</div>
              <div class="rank_mount">온라인 평점:{{ product.review.average_rating }}({{ product.review.total_reviews }}) </div>
              <div class="rank_price">온라인 최저가 :{{ product.review.lowest }} 원</div>
              <div class="">바름 평점:{{ product.bareum_review.average_rating }}({{ product.bareum_review.total_reviews }}) </div>
          </router-link>
        <div ref="loader" class="loader"></div>
  
    </div>
    
  </template>
  
  <script>
  import { ref, computed,onMounted, onUnmounted } from 'vue';
  import axios from "axios";
  import nutrientsByAgeGroup from './age_group.js';
  
  export default {
    setup() {
        const page = ref(1);
        const per_page = 10;
        const postTotalPages = ref(1);
        const loader = ref(null);
        const ageRanking = ref([]);
        const ageGroup = ref(Object.keys(nutrientsByAgeGroup));
        const selectedAgegroup = ref('성인 (19-39세)');
  
        const fetchAgeGroupRanking = async(age_group) => {
            if (selectedAgegroup.value != age_group){
                selectedAgegroup.value = age_group;
                page.value = 1; 
                ageRanking.value = [];                
            }
            if(page.value <= postTotalPages.value){
                try{
                const response = await axios.get(`/api/product/age-ranking/?page=${page.value}&ingredients=${nutrientsByAgeGroup[age_group]}`);
                ageRanking.value.push(...response.data.results);
                postTotalPages.value = Math.ceil(response.data.count/ per_page);
                page.value+=1;
                }catch(err){
                    console.error(err);
                }
            }
            
        }
  
        
        let observer;
  
        onMounted(async () => {
          await fetchAgeGroupRanking(selectedAgegroup.value);
            
          observer = new IntersectionObserver(async (entries, observer) => {
            if (entries[0].isIntersecting) {
              await fetchAgeGroupRanking(selectedAgegroup.value);
            }
          });
        
          if (loader.value) {
            observer.observe(loader.value);
          }
        });
    
        onUnmounted(() => {
          if (loader.value) {
            observer.unobserve(loader.value);
          }
        });
  
        return {
            ageRanking,
            fetchAgeGroupRanking,
            loader,
            ageGroup,
            selectedAgegroup, 
            nutrientsByAgeGroup
  
        };
    }
  }
  </script>
  <style>
    
  </style>