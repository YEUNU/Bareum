<template>
<div class="background bg-whitesmoke" style="padding-top: 56px; min-height: 100%; padding-bottom: 60px;">
    <div v-show="menuVisible" style="height: calc(0.8em + 20px);">더미</div>
    <router-link class="rank_box bg-white"
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
    <div ref="loader" class="loader"></div>
</div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import axios from "axios";
export default {
    setup(props) {
        const page = ref(1);
        const per_page = 10;
        const postTotalPages = ref(1);
        const loader = ref(false);
        const totalRanking = ref([]);
        const menuVisible = ref(props.menuVisible);
        const pageTitle = ref("바름 종합 제품 랭킹");

        const fetchRanking = async() => {
            if(page.value <= postTotalPages.value){
                try{
                    const response = await axios.get(`/api/product/total-ranking/?page=${page.value}`);
                    totalRanking.value.push(...response.data.results);
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
            totalRanking,
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