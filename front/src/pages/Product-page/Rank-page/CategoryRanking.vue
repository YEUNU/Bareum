<template>
<div class="background bg-whitesmoke" style="padding-top: 56px; min-height: 100%; padding-bottom: 60px;">
    <div class="detail-ranking-head">
        <div class="dropdown" style="display: flex; align-items: center;">
            <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="margin: 0; font-size: 0.9em;">
                {{selectedCategory}}
            </button>
            <ul class="dropdown-menu">
                <li v-for="(category, index) in nutrientCategories" :key="index" @click="fetchCategoryRanking(category)">{{ category }}</li>
            </ul>
            에 도움을 줄 수 있는
        </div>
        {{ nutra_presonal_mapping[selectedCategory].join(', ') }}(이)가 함유된 제품들 입니다.
    </div>
    <router-link class="rank_box bg-white"
    v-for="(product,index) in categoryRanking" :key="index"
    :to="`/product/${product.업체별_제품코드}`">
        <div class="rank_order">{{ index + 1 }}</div>
        <div class="rank_image">
            <img class="rank_image" :src='`/media/product_images/${product.업체별_제품코드}.png`' alt="상품이미지" style="height: min(25vh, 25vw); width: min(25vh, 25vw);" />
        </div>
        <div class="rank_manufacturer">{{ product.업소명 }}</div>
        <div class="rank_name">{{ product.nutraceuticals_name }}</div>
        <div class="rank_mount">온라인 평점:{{ product.review.average_rating }}({{ product.review.total_reviews }}) </div>
        <div class="rank_price">온라인 최저가 :{{ product.review.lowest }} 원</div>
        <div class="rank_score">바름 평점:{{ product.bareum_review.average_rating }}({{ product.bareum_review.total_reviews }}) </div>
    </router-link>
    <div ref="loader" class="loader"></div>
</div>
</template>

<script>
import { ref, computed,onMounted, onUnmounted } from 'vue';
import axios from "axios";
import nutra_presonal_mapping from './nutra_presonal_mapping.js';

export default {
    setup() {
        const page = ref(1);
        const per_page = 10;
        const postTotalPages = ref(1);
        const loader = ref(null);
        const categoryRanking = ref([]);
        const nutrientCategories = ref(Object.keys(nutra_presonal_mapping));
        const selectedCategory = ref('혈중 콜레스테롤');

        const fetchCategoryRanking = async(category) => {
            if (selectedCategory.value != category){
                selectedCategory.value = category;
                page.value = 1; 
                categoryRanking.value = [];                
            }
            if(page.value <= postTotalPages.value){
                try{
                    const response = await axios.get(`/api/product/category-ranking/?page=${page.value}&ingredients=${nutra_presonal_mapping[category]}`);
                    categoryRanking.value.push(...response.data.results);
                    postTotalPages.value = Math.ceil(response.data.count/ per_page);
                    page.value+=1;
                }catch(err){
                    console.error(err);
                }
            }
        }

        let observer;

        onMounted(async () => {
            await fetchCategoryRanking(selectedCategory.value);
            
            observer = new IntersectionObserver(async (entries, observer) => {
                if (entries[0].isIntersecting) {
                    await fetchCategoryRanking(selectedCategory.value);
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
            categoryRanking,
            fetchCategoryRanking,
            loader,
            nutrientCategories,
            selectedCategory, 
            nutra_presonal_mapping

        };
    }
}
</script>

<style>
  
</style>