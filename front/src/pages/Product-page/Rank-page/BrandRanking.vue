<template>
    <div class="background bg-whitesmoke" style="padding-top: 100px; min-height: 100%; padding-bottom: 60px;">
        <router-link class="rank_box bg-white"
            v-for="(product,index) in brandRanking" :key="index"
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
export default {
    setup() {
        const page = ref(1);
        const per_page = 10;
        const postTotalPages = ref(1);
        const loader = ref(null);
        const brandRanking = ref([]);
        const menuVisible = ref(false);
        const pageTitle = ref("바름 종합 제품 랭킹");

        const fetchRanking = async() => {
            if(page.value <= postTotalPages.value){
                try{
                const response = await axios.get(`/api/product/brand-ranking/`);
                brandRanking.value.push(...response.data.results);
                postTotalPages.value = Math.ceil(response.data.count/ per_page);
                page.value+=1;
                }catch(err){
                    console.error(err);
                }
            }
        }

        
        let observer;

        onMounted(async () => {
      await fetchRanking();

      observer = new IntersectionObserver(async (entries, observer) => {
        if (entries[0].isIntersecting) {
          await fetchRanking();
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
            brandRanking,
            fetchRanking,
            loader,
            menuVisible,
            pageTitle,

        };
    }
}
</script>
<style lang="">
    
</style>