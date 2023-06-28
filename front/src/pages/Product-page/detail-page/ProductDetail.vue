<template>
<div class="background" style="display: flex; flex-direction: column; align-items: center;">
    <nav class="navbar fixed-top bg-white" style="box-shadow: 0 2px 1px -1px #EAEAEA;">
        <div class="container-fluid">
            <span class="navbar-brand" @click="$router.back()" style="margin-left: 2vh;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                </svg>
            </span>
        </div>
    </nav>
    
    <div class="background bg-whitesmoke" style="display: flex; flex-direction: column; align-items: center; margin-top:56px; min-height: calc(100vh - 56px);">

        <div class="product_card product_head">
            <div class="product_iamge bg-white">
                <img src="https://product.hstatic.net/1000343598/product/381fc8e899a54b16853cfd35117bd052_85c1af13783d419c8dbf90bd51742397_master.png" alt="(상품 이미지)"/>
            </div>
            <div class="set" style="box-shadow: 0 2px 1px -1px #EAEAEA;">
                <div class="manufacturer">
                    <img src="data:image/png;base64,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" alt="(제조사 로고)" class="manufacturer_logo"/>
                    <span class="manufacturer_name"> {{ product.업소명 }} </span>
                </div>
                <div class="product_name"> {{ product.nutraceuticals_name }} </div>
                <div class="product_score"> <span style="color: #FFCC21; font-size: 1.3em;">★</span> {{ online_score.avg_rating }} ({{ online_score.cnt_review }})</div>
            </div>
        </div>
        

        <ul class="product_menu bg-white" style="position: sticky; top: 56px;">
            <li class="product_item">
                <router-link class="product_link" :to="{name:'productInfoPage', params:{productCode}}" >제품 정보</router-link>
            </li>
            <li class="product_item">
                <router-link class="product_link" :to="{name:'productReviewPage', params:{productCode}}">제품 리뷰</router-link>
            </li>
        </ul>
        <router-view></router-view>
        <div class="product_card">
            <h4>베스트 10</h4>
        </div>
        <div class="product_card">
            <h4>카테고리 내 인기제품</h4>
        </div>
        <div class="product_card">
            <h4>비슷한 제품</h4>
        </div>
        <div class="product_card product_tail">
            <div @click="operator_info = !operator_info" style="padding: 0.5em;">{{ operator_info? '사업자 정보 △' : '사업자 정보 ▽' }}</div>
            <div v-show="operator_info" class="card" style="display: grid; grid-template-rows: repeat(1fr); grid-template-columns: 3fr 4fr; margin: 0.5em; padding: 0.5em; text-align: start; align-self: center; width: 80vw; max-width: 480px;">
                <span>대표자</span>
                <span>뤼튼</span>
                <span>주소</span>
                <span>대전광역시 서구 탄방로 56</span>
                <span>고객센터</span>
                <span>042-534-7283</span>
                <span>고객센터운영시간</span>
                <span>연중전휴</span>
                <span>사업자등록번호</span>
                <span>123-45-67890</span>
                <span>전자우편</span>
                <span>abc@de.fgh</span>
                <span>입점문의</span>
                <span>stu@vw.xyz</span>
                <span>통신판매업신고</span>
                <span>안했서용</span>
            </div>
            <div style="padding: 0.5em;">대충 엄청 길어서 잘 안읽게되는 머 중개서비스 제공자로 판매당사자가 아니어서 제공 정보 오류 때문에 생기는 모든 의무와 책임은 각 판매자에게 있다는 내용</div>
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
        const operator_info = ref(false);
        const product = ref({});
        const onlineReviews = ref([]);
        const BareumReviews = ref([]);
        const online_score = ref({ 'avg_rating': 0, 'cnt_review': 0 });
        const averageRating = ref(0.0);

        const fetchProductDetail = async () =>{
            try{
                const response = await axios.get(`/api/product/detail/${props.productCode}/`);
                product.value = response.data;


            }catch(error){
                console.error(error);
            }
        }

        const fetchOnlineReview = async(productCode) =>{
            const respnse = await axios.get(`/api/product/online-reviews/${productCode}/`);
            onlineReviews.value = respnse.data
            online_score.value.avg_rating = onlineReviews.value[0].average_rating
            online_score.value.cnt_review = onlineReviews.value[0].total_reviews
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

        }
        onMounted(() => {
            fetchProductDetail();
            fetchOnlineReview(props.productCode);
            fetchBareumReview(props.productCode);
        })

        return{
            operator_info,
            product,
            online_score,
            fetchProductDetail,
            fetchOnlineReview,
            fetchBareumReview,
            onlineReviews,
            BareumReviews,
            averageRating
        }
    }
}

</script>

<style>

.product_card {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    width: 100vw;
    background-color: white;
    margin: 0.5vh 0;
    padding: 3vh 5vw;
    text-align: start;
}

.product_card .set {
    padding: 1vh 0;
}

.product_head {
    margin-top: 0;
}

.product_tail {
    margin-bottom: 0;
    color: gray;
    font-size: 0.7em;
    text-align: center;
}

.product_iamge {
    align-self: center;
}

.product_iamge img {
    width: min(100vw, calc(100vh - 56px));
    height: min(100vw, calc(100vh - 56px));
    object-fit: cover;
}

.manufacturer {
    margin: 0.3em;
}

.manufacturer_logo {
    width: 2em;
    height: 2em;
}

.manufacturer_name {
    color: gray;
    font-size: 0.8em;
    margin: 0.3em;
}

.product_name {
    font-size: 1.2em;
    margin: 0.3em;
}

.product_score {
    font-size: 0.8em;
    color: gray;
    font-weight: bold;
    margin: 0.3em;
}

.product_menu {
    display: flex;
    list-style: none;
    padding: 0;
    margin: 0.5vh 0 0 0;
    width: 100%;
    color: #333;
    text-decoration: none;
    align-items: stretch;
    box-shadow: 0 2px 1px -1px #EAEAEA;
    z-index: 560;
    background-color: white;
}

.product_item {
    flex-grow: 1;
    display: flex;
    justify-content: center;
    align-items: stretch;
}

.product_link {
    flex-grow: 1;
    text-decoration: none;
    color: #333;
    text-align: center;
    padding: 10px 0;
}

.product_menu .router-link-exact-active {
    font-weight: bold;
    transition: all 0.3s ease; /* 변환 효과 */
    color: #333;
    box-shadow: 0 3px 1px -1px #111;
}

</style>