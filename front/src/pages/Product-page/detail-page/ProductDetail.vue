<template>
<div class="background" style="display: flex; flex-direction: column; align-items: center;">
    <nav class="navbar fixed-top bg-white" style="box-shadow: 0 2px 1px -1px #EAEAEA;">
        <div class="container-fluid">
            <span class="navbar-brand" @click="$router.back()" style="margin-left: 2vh;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                </svg>
            </span>
            <router-link to="/cart">
                <svg xmlns="http://www.w3.org/2000/svg" v-if="shop" width="30" height="30" fill="#2dce89" class="bi bi-cart-fill" viewBox="0 0 16 16">
                    <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" v-else width="30" height="30" fill="currentColor" class="bi bi-cart" viewBox="0 0 16 16" >
                    <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l1.313 7h8.17l1.313-7H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                </svg>
            </router-link>
        </div>
    </nav>
    
    <div class="background bg-whitesmoke" style="display: flex; flex-direction: column; align-items: center; margin-top:56px; min-height: calc(100vh - 56px);">

        <div class="product_card product_head">
            <div class="product_iamge bg-white">
                <img :src="`/media/product_images/${productCode}.png`" alt="(상품 이미지)"/>
            </div>
            <div class="set" style="box-shadow: 0 2px 1px -1px #EAEAEA;">
                <div class="manufacturer">
                    <img src="" alt="" class="manufacturer_logo"/>
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
        <div class="fixed-bottom">
            <div>
                <div v-if="purchaseOption">
                <button @click="closeOption">x</button>
                <div>
                    <label for="quantity">수량:</label>
                    <div style=";">
                        <button @click="incrementQuantity()">+</button>
                        <p id="quantity" name="quantity">{{selectedQuantity}}</p>
                        <button @click="decrementQuantity()">-</button>

                    </div>
                </div>
                <div>
                    <h2>주문금액</h2>
                    <h2>{{ amount }}</h2>
                </div>
                </div>
                <div>
                    <button @click="getInCart()">장바구니 담기</button>
                    <button @click="goPurchase()">바로 구매 </button>                
                </div>
            </div>

        </div>
       
    </div>
</div>
</template>

<script>
import axios from 'axios';
import {ref, onMounted} from 'vue';
import { useRouter } from 'vue-router';
import Cookies from 'js-cookie';
export default {
    props:{
        productCode:{
            type:String,
            required:true
        }
    },

    setup(props){
        const csrf_token = Cookies.get('csrftoken');
        const router = useRouter();
        const operator_info = ref(false);
        const product = ref({});
        const onlineReviews = ref([]);
        const BareumReviews = ref([]);
        const online_score = ref({ 'avg_rating': 0, 'cnt_review': 0 });
        const averageRating = ref(0.0);
        const purchaseOption = ref(false);
        const price = ref(0);
        const amount = ref(0);
        const selectedQuantity = ref(1);

        const fetchProductDetail = async () =>{
            try{
                const response = await axios.get(`/api/product/detail/${props.productCode}/`);
                product.value = response.data;


            }catch(error){
                console.error(error);
            }
        }
        function incrementQuantity() {
            selectedQuantity.value++;
            amount.value = price.value * selectedQuantity.value;
        }

        function decrementQuantity() {
          if (selectedQuantity.value > 1) {
            selectedQuantity.value--;
            amount.value = price.value * selectedQuantity.value;
          }
        }

        const getInCart = async() => {
          if (!purchaseOption.value) {
            purchaseOption.value = true
          }else{
            const code = product.value?.업체별_제품코드
            await axios.post('/api/shop/cart/' ,{
                  product_code: code ,
                  quantity: selectedQuantity.value,
                }, {
                  headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrf_token,
                  },
                });
            closeOption();
            
            window.alert('장바구니에 담겼습니다!');
          }
        }

        const goPurchase = async() => {
          if (!purchaseOption.value) {
            purchaseOption.value = true
          }else{
            router.push('/order');
          }
        }
        const fetchOnlineReview = async (productCode) => {
            try {
                const response = await axios.get(`/api/product/online-reviews/${productCode}/`);
                onlineReviews.value = response.data;
                online_score.value.avg_rating = onlineReviews.value[0]?.average_rating || 0;
                online_score.value.cnt_review = onlineReviews.value[0]?.total_reviews || 0;
                price.value = onlineReviews.value[0]?.lowest;
                amount.value= price.value
            } catch (error) {
                console.error('Error while fetching online review data:', error);
                online_score.value.avg_rating = 0;
                online_score.value.cnt_review = 0;
            }
        };
        
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
        const closeOption = () =>{
            purchaseOption.value = false;
            selectedQuantity.value = 1; 
            amount.value = price.value * selectedQuantity.value;

        }

        onMounted(() => {
            fetchProductDetail();
            fetchOnlineReview(props.productCode);
            fetchBareumReview(props.productCode);
        })

        return{
            closeOption,
            getInCart,
            goPurchase,
            operator_info,
            product,
            online_score,
            fetchProductDetail,
            fetchOnlineReview,
            fetchBareumReview,
            incrementQuantity,
            decrementQuantity,
            onlineReviews,
            BareumReviews,
            averageRating,
            purchaseOption,
            amount,
            selectedQuantity
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
    width: min(100vw, calc(100vh - 56px));
    height: min(100vw, calc(100vh - 56px));
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

.fixed-bottom {
    width: 100%;
    background-color: white;
    padding: 10px;
    box-shadow: 0px -3px 5px rgba(0,0,0,0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;

}

</style>