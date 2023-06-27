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
        <div v-for="review in BareumReviews" :key="review.bareum_review_number">
            <img :src="review.user_info.profile_image"/>
            <p>작성자: {{ review.user_info.nickname }}</p>
            <p>내용 : {{ review.reviews }}</p>
            <p>별점 : {{ review.rating }}</p>
            사진 :
            <div v-for="(image, index) in review.images" :key="index">
                <img :src="image.review_img_url" :alt="'Image ' + (index + 1)" class="review-image"/>
            </div>
        </div>
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