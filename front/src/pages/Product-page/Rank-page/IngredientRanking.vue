<template>
<div class="background bg-whitesmoke" style="padding-top: 56px; min-height: 100%; padding-bottom: 60px;">
    <div class="detail-ranking-head">
        <div class="dropdown" style="display: flex; align-items: center;">
            <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="margin: 0; font-size: 0.9em;">
                {{selectedIngredient}}  
            </button>
            <ul class="dropdown-menu">
                <li v-for="(ingredient, index) in nutrientCategories" :key="index" @click="fetchIngredientRanking(ingredient)">{{ ingredient }}</li>
            </ul>
            (이)가 함유된 제품의 랭킹 입니다.
        </div>
    </div>
    <router-link class="rank_box bg-white"
    v-for="(product,index) in ingredientRanking" :key="index"
    :to="`/product/${product.업체별_제품코드}`">
        <div class="rank_order">{{ index + 1 }}</div>
        <div class="rank_image">
            <img class="rank_image" :src='`/media/product_images/${product.업체별_제품코드}.png`' alt="상품이미지" style="height: min(25vh, 25vw); width: min(25vh, 25vw);" />
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
    <div ref="loader" class="loader"></div>
</div>
</template>

<script>
import { ref, computed,onMounted, onUnmounted } from 'vue';
import axios from "axios";
export default {
    setup() {
        const page = ref(1);
        const per_page = 10;
        const postTotalPages = ref(1);
        const loader = ref(null);
        const ingredientRanking = ref([]);
        const nutrientCategories = ref([
          '구리', '나이아신', '단백질', '루테인', '마그네슘', '망간', '몰리브덴', '비오틴', '비타민A', '비타민B1', '비타민B12', '비타민B2', '비타민B6', '비타민C', '비타민D', '비타민E', '비타민K', '셀레늄_셀렌', '식이섬유', '아연', '엽산', '요오드', '진세노사이드', '철', '칼륨', '칼슘', '프로바이오틱스'
        ]);
        const selectedIngredient = ref('비타민C');
        const fetchIngredientRanking = async(ingredient) => {
            if (selectedIngredient.value != ingredient){
                selectedIngredient.value = ingredient;
                page.value = 1; 
                ingredientRanking.value = [];                
            }
            if(page.value <= postTotalPages.value){
                try{
                const response = await axios.get(`/api/product/ingredient-ranking/${selectedIngredient.value}/?page=${page.value}`);
                ingredientRanking.value.push(...response.data.results);
                postTotalPages.value = Math.ceil(response.data.count/ per_page);
                page.value+=1;
                }catch(err){
                    console.error(err);
                }
            }
            
        }

        
        let observer;

        onMounted(async () => {
          await fetchIngredientRanking(selectedIngredient.value);
            
          observer = new IntersectionObserver(async (entries, observer) => {
            if (entries[0].isIntersecting) {
              await fetchIngredientRanking(selectedIngredient.value);
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
            ingredientRanking,
            fetchIngredientRanking,
            loader,
            nutrientCategories,
            selectedIngredient, 

        };
    }
}
</script>
<style>
    
</style>