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
                <svg xmlns="http://www.w3.org/2000/svg" v-else width="30" height="30" fill="#2dce89" class="bi bi-cart" viewBox="0 0 16 16" >
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

        <div class="fixed-bottom">
            <div style="width: 100%;">
                <div v-if="purchaseOption">
                    <div class="row">
                        <div class="col-5">
                            <div class="product_name" style="width: 100%; margin-left: 10%; text-align: left;"> {{ product.nutraceuticals_name }} </div>
                        </div>
                        <div class="col-7" style="text-align: right; margin-top: 1%;">
                            <button @click="closeOption" style="margin-right: 10%; padding: 0%; background-color: white;">
                                <svg style="position: absolute; width: 20px; top: 20px; right: 20px; margin: 0;" @click="delete_new_alarm()" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
                                </svg>
                            </button>
                        </div>
                    </div>
                
                    
                <div class="row">
                    <div class="col-5" style="text-align: left; margin-top: 5%; margin-bottom: 8%;">
                        <button @click="decrementQuantity()" style="border: none; display: inline-block; background-color: white;">-</button>
                        <p id="quantity" name="quantity" style="margin: 0; display: inline-block; font-weight: bold;">{{selectedQuantity}}</p>
                        <button @click="incrementQuantity()" style="border: none; display: inline-block; background-color: white;">+</button>
                    </div>
                <div class="col-7" style="text-align: right; margin-top: 5%; margin-bottom: 5%; ">
                    <h2>{{ amount.toLocaleString() }} 원</h2>
                </div>
            </div>
                </div>
                <div>
                    <button @click="getInCart()" style="border: none; background-color: #2dce89; border-radius: 5px; color:white;">장바구니 담기</button>
                    <button @click="goPurchase()" style="border: none; margin-left:30%; background-color: #2dce89; border-radius: 5px; color:white;">바로 구매 </button>                
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
    margin-bottom: calc(2.2em + 20px);
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