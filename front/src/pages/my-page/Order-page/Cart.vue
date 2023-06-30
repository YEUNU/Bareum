<template>
    <div class="container">
        <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/mypage" class="navbar-brand" style="margin-left: 2vh;">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
        </router-link>
        <div style="margin-right: 2vh;">장바구니</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
            <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
          </svg>
        </div>
        </div>
      </nav>
  
        <div class="card" v-for="(product, index) in shoppingCart" :key="index">
            <div class="row">
              <p class="card-text" style="text-align: left; padding-bottom: 3%; border-bottom: 2px solid #eeeeee;">{{product.product.업소명}}</p>
                <div class="row" style="padding: 0;">
              <div class="col-4">
                  <img :src="`/media/product_images/${product.product.업체별_제품코드}.png`">
                </div>

                <div class="col-8">
                        <p class="card-text" style="display: inline-block;">{{product.product.nutraceuticals_name}}</p>
                    
                    <button @click="deleteCart(product.id)" style="display: inline-block;" >x</button>                    
                    
                        <button @click="decrementQuantity(product)">-</button>
                        <div>{{ product.quantity }} 개 </div>
                        <button @click="incrementQuantity(product)" style="display: inline-block;">+</button>
                    <div>{{ product.lowest * product.quantity }}</div>
                </div>
              </div>
            </div>
        </div>
        <hr/>
        <p>총 상품 금액 {{ totalAmount }}</p>
        <p>배송비 {{ 0 }}</p>
        <h1>결제 예정금액  {{ totalAmount }}</h1>
    </div>
      <div>
        <button> 구매하기 </button>
      </div>
  </template>
  
  <script>
import axios from 'axios';
import {ref, onMounted} from 'vue';
import { useRouter } from 'vue-router';
import Cookies from 'js-cookie';
export default {
      components: {},

      setup(){
        const csrf_token = Cookies.get('csrftoken');
        const router = useRouter();
        const shoppingCart = ref([]);
        const totalAmount = ref(0);

        const getTotal = () => {
          var result = 0;
          for (let index = 0; index < shoppingCart.value.length; index++) {
            result += shoppingCart.value[index].lowest * shoppingCart.value[index].quantity;
            
          }
          return result;
        }
        const fetchCart = async() =>{
            try{
              const response = await axios.get('/api/shop/cart/');
              shoppingCart.value = response.data;
              totalAmount.value = getTotal();
            }catch(err){
              console.error(err);
            }

        }

        const deleteCart = async (cartId) => {
          // 사용자에게 삭제 확인 메시지를 표시합니다.
          if (window.confirm("정말 삭제하시겠습니까?")) {
            try {
              await axios.delete("/api/shop/cart/", {
                params: {
                  cartId: cartId,
                },
                headers: {
                  "Content-Type": "application/json",
                  "X-CSRFToken": csrf_token,
                },
              });
              fetchCart();
            } catch (err) {
              console.error(err);
            }
          }
        };

        const updateQuantity = async (cartId,quantity) => {
          try {
            await axios.put("/api/shop/cart/", {
              cartId: cartId,
              quantity: quantity
            }, {
              headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token,
              },
            });
            fetchCart();
          } catch (err) {
            console.error(err);
          }
        }
        const incrementQuantity = async (product) => {
          try {
            product.quantity += 1;
            updateQuantity(product.id,product.quantity);
          } catch (err) {
            console.error(err);
          }
        }

        const decrementQuantity = async (product) => {
          try {
            if (product.quantity > 1) {
              product.quantity -= 1;
              updateQuantity(product.id,product.quantity);
            
            } else {

            }
          } catch (err) {
            console.error(err);
          }
        }
        onMounted(() => {
          fetchCart()
        })

        return{
          incrementQuantity,
          decrementQuantity,
          shoppingCart,
          fetchCart,
          totalAmount,
          deleteCart,
          updateQuantity,
        }
      }
  }
  </script>
  
  <style>
  .container {
      width: 100%; /* 화면 너비에 꽉 차도록 설정 */
      height: 100%; /* 화면 높이에 꽉 차도록 설정 */
      display: block;
      margin-bottom: 10%;
    }
  
    .card {
    margin-top: 10%;
}
  
  </style>