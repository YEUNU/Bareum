<template>
<div class="background" style="display: flex; flex-direction: column; align-items: center;">
    <nav class="navbar fixed-top bg-white" style="box-shadow: 0 2px 1px -1px #EAEAEA;">
        <div class="container-fluid">
            <span class="navbar-brand" @click="$router.back()" style="margin-left: 2vh;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                </svg>
            </span>
            <div style="font-weight: bold;">제품 리뷰</div>
            <div style="opacity: 0;">dummy</div>
        </div>
    </nav>
        
        <div class="background bg-whitesmoke" style="display: flex; flex-direction: column; align-items: center; margin-top:56px; min-height: calc(100vh - 56px);">

        <div class="product_card product_head">
            <div class="score_box">
                <div class="star_score">
                    <div style="font-size: 2em; font-weight: bold;">{{ averageRating ? averageRating : '-' }}</div>
                    <div style="height: 2em; margin: -1em 0 0 0;">
                        <p class="product_star star_baruem" data-split="★★★★★">★★★★★</p>
                    </div>
                </div>
            </div>
        </div>            

        <div v-if="BareumReviews.length == 0" style="display: flex; align-items: center; min-height: calc(90vh - 56px - 5em); font-weight: bold; color: gainsboro;">
            등록된 바름 리뷰가 없어요.
        </div>

        <div v-else class="product_card">
            <div style="display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 1px -1px #EAEAEA;">
                <div style="font-weight: bold; color: gray;">총 {{ BareumReviews.length }}개</div>
            </div>
            <div v-for="review in BareumReviews" :key="review.bareum_review_number" class="review_box ms-3">
                <div class="d-flex flex-row align-items-center" style="width: 100%;">
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
        const averageRating = ref(0.0);

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
            fetchBareumReview(props.productCode);
        });

        return{
            fetchBareumReview,
            BareumReviews,
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
    margin-bottom: 1em;
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

.sentiment_online_reviews {
    justify-self: center;
    align-self: center;
}

</style>