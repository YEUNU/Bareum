<template>
    <div>
        <router-link :to="{name:'productReviewWritePage', param:{productCode}}"><button>리뷰 작성 하러 가기</button></router-link>
    </div>
    <div>
        평점 리뷰 보여주기
         {{ onlineReviews  }}
    </div>
    <hr>
    <div>
        {{ BareumReviews }}
    </div>
</template>
<script>
import axios from 'axios';
import {ref, onMounted} from 'vue';

export default {
    props:{
        productCode:{
            type:String,
            required:true
        }
    },
    setup(props){
        const onlineReviews = ref([]);
        const BareumReviews = ref([]);

        const fetchOnlineReview = async(productCode) =>{
            const respnse = await axios.get(`/api/product/online-reviews/${productCode}/`);
            onlineReviews.value = respnse.data
        }
        const fetchBareumReview = async (productCode) => {
            const respnse = await axios.get(`/api/product/bareum-reviews/${productCode}/`);
            BareumReviews.value = respnse.data
        }

        onMounted(() => {
            fetchOnlineReview(props.productCode);
            fetchBareumReview(props.productCode);
        });

        return{
            fetchOnlineReview,
            fetchBareumReview,
            onlineReviews,
            BareumReviews,


        }
    }
}
</script>
<style>
    
</style>