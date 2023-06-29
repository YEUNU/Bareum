<template>
<div v-for="(brand,index) in brandRanking" :key="index" style="padding-top: 60px;">
    <p>업체명 : {{ brand.brand }}</p>
    <div v-for="(product,index) in brand.ranking" :key="index">
        <p>{{ index +1 }} 등</p>
        <p>제품명 : {{ product.nutraceuticals_name }}</p>
    </div>
</div>
<div ref="loader" class="loader"></div>
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

        const fetchBrandRanking = async() => {
            if(page.value <= postTotalPages.value){
                try{
                const response = await axios.get(`/api/product/brand-ranking/?page=${page.value}`);
                console.log(response.data);
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
            await fetchBrandRanking();
            
            observer = new IntersectionObserver(async (entries, observer) => {
            if (entries[0].isIntersecting) {
                await fetchBrandRanking();
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
            fetchBrandRanking,
            brandRanking,
            loader,

        };
    }
}
</script>

<style>
</style>