<template>
    <!--
        <div>
            평점 리뷰 보여주기
            {{ onlineReviews  }}
        </div>
    -->
    
    <div class="product_card product_head">
        <router-link to="/" class="review_header" style="color: #333;">
            <div style="font-size: 1.2em; font-weight: bold;"> <span>리뷰</span> <span style="color: #2dce89;">{{ online_score.cnt_review }}</span> </div>
            <div>></div>
        </router-link>

        <router-link :to="{name:'productReviewWritePage', param:{productCode}}" style="align-self: center; margin: 1vh 0;"><button class="roundbox">리뷰 작성 하러 가기</button></router-link>
        
        <div class="score_box">
            
            <div class="star_score">
                <div style="font-size: 2em; font-weight: bold;">{{ online_score.avg_rating }}</div>
                <div style="height: 2em; margin: -1em 0 0 0;">
                    <p class="product_star star_online" data-split="★★★★★">★★★★★</p>
                </div>
                <div>(온라인 평균 평점)</div>
            </div>
            
            <div class="star_score">
                <div style="font-size: 2em; font-weight: bold;">{{ averageRating }}</div>
                <div style="height: 2em; margin: -1em 0 0 0;">
                    <p class="product_star star_baruem" data-split="★★★★★">★★★★★</p>
                </div>
                <div>(바름 평균 평점)</div>
            </div>

        </div>
       
       
        <div v-for="review in BareumReviews" :key="review.bareum_review_number" class="review_box">
            <div>
                <div class="flex-grow-1 ms-3">
                    <div class="d-flex flex-row align-items-center" style="width:100%;">
                        <img :src="review.user_info.profile_image"
                        alt="profile" class="img-fluid rounded-circle border border-dark border-3"
                        style="width: 50px; margin-bottom: 1rem;">
                        <div style="text-align: left; font-weight: bold; flex-grow: 1; margin-left: 1rem;">
                            <div>{{ review.user_info.nickname }}</div>
                            <div style="display: flex;">
                                <p style="color: #FFCC21;">{{ "★".repeat(review.rating) }}</p> <p style="color: gainsboro;"> {{ "★".repeat(5 - review.rating) }}</p>
                            </div>
                        </div>
<!-- 리뷰 삭제
    <div v-if="review.user.member_id == userInfo.memberId" style="margin-top: 2%; margin-bottom: 5%;">
        <button class="postbutton" @click="deleteComment(comment.comments_id)">삭제</button>
    </div>
-->
                    </div>
                    <div style="display: flex; margin-bottom: 1em;">
                        <div style="width: 50px;">내용 :</div>
                        <div style="margin-left: 1em;">{{ review.reviews }}</div>
                    </div>
                    
                    <div v-for="(image, index) in review.images" :key="index" style="margin-left: calc(50px + 1em);">
                        <img :src="image.review_img_url" :alt="'Image ' + (index + 1)" class="review-image"/>
                    </div>
                </div>
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
        const online_score = ref({ 'avg_rating': 0, 'cnt_review': 0 });
        const averageRating = ref(0.0);

        const fetchOnlineReview = async(productCode) =>{
            const respnse = await axios.get(`/api/product/online-reviews/${productCode}/`);
            onlineReviews.value = respnse.data
            online_score.value.avg_rating = onlineReviews.value[0].average_rating
            online_score.value.cnt_review = onlineReviews.value[0].total_reviews
            document.documentElement.style.setProperty("--score-for-star-online", (onlineReviews.value[0].average_rating / 0.05) + '%');
        }
        const fetchBareumReview = async (productCode) => {
            const respnse = await axios.get(`/api/product/bareum-reviews/${productCode}/`);
            BareumReviews.value = respnse.data
            let totalRating = 0;
            let reviewCount = BareumReviews.value.length;

            for (let review of BareumReviews.value) {
                totalRating += review.rating;
            }
        
            averageRating.value = totalRating / reviewCount;
            document.documentElement.style.setProperty("--score-for-star-baruem", (averageRating.value / 0.05) + '%');

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
            online_score,
            averageRating,
        }
    }
}
</script>

<style>

:root {
    --score-for-star-online: 0;
    --score-for-star-bareum: 0;
}

.score_box {
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 1vh 0;
    box-shadow: 0 2px 1px -1px #EAEAEA;
}

.star_score {
    width: 45%;
    display: flex;
    flex-direction: column;
    align-items: center; 
}

.product_star {
    position: relative;
    margin: 0;
    color: gainsboro;
    font-size: 1.5em;
    font-family: 'Open Sans', sans-serif;
    font-weight: 700;
    text-transform: uppercase;
    white-space: nowrap;
}

.product_star::before {
    position: absolute;
    top: 0;
    left: 0;
    content: attr(data-split);
    color: #FFCC21;
    overflow: hidden;
}

.star_online {
    transform: translate( -1 * var(--score-for-star-online), -1 * var(--score-for-star-online) );
}


.star_online::before {
    width: var(--score-for-star-online);
}

.star_bareum {
    transform: translate( -1 * var(--score-for-star-bareum), -1 * var(--score-for-star-bareum) );
}


.star_bareum::before {
    width: var(--score-for-star-bareum);
}

.review_header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 0 1vh 0;
}

.review_box {
    padding: 2vh 0 1vh 0;
    box-shadow: 0 2px 1px -1px #EAEAEA;
}

</style>