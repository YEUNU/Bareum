<template>
  <div class="ocr-result-page">
    <nav class="navbar fixed-top bg-white">
        <div>
          <router-link to="/" class="navbar-brand" style="margin-left: 2vh;">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
          </router-link>
        </div>
      </nav>

   
    <img :src="imageData" alt="Captured image" style="width: 100%; " />
    <div v-if="isLoading" class="loading-container" style="margin-top: 10%; box-shadow: 2px 2px 2px 2px #eeeeee">
      <div class="spinner" style="margin-top: 10%;"></div>
      <p style="margin-top: 10%;">제품을 찾는 중입니다...</p>
    </div>

    <div v-else>
      <div v-if="productResults" style="width:100%;">
        <h2 style="margin-top: 10%;">제품을 선택해주세요.</h2>
        <div class="grid-container" style="width: 100%; margin-top: 10%;">
          <div v-for="(product, index) in productResults" :key="index" >
            <div class="product-card" style="width: 100%;">
              <div class="product-image">
                <!-- 추후에 이미지를 여기에 추가하세요 -->
                <img src="../../assets/lactofit.png" alt="Product image" class="fill-image" />
              </div>
              <div class="product-details" style="text-align: left; margin-left: 5%; width: 100%;">
                <p style="font-weight: bold; font-size: 20px;">{{ product.nutraceuticals_name }}</p>
                <p>{{ product.업소명 }}</p>
              </div>
            </div>
            
          </div>
        </div>
        <router-link to="/ocr/registration" class="request-link">
          <button class="request-btn" style="width: 100%; margin-top: 5%; margin-bottom: 10%;">등록 요청</button>
        </router-link>
      </div>
      <div v-else style="margin-top: 10%; border:2px solid #eeeeee; box-shadow: 2px 2px 2px 2px #eeeeee">
        <p style="margin-top: 10%;">관련된 제품을 찾지 못했습니다.</p>
        <router-link to="/ocr/registration" class="request-link">
          <button class="request-btn" style="margin-bottom: 10%;">등록 요청</button>
        </router-link>
      </div>
    </div>
  </div>
</template>


<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Cookies from 'js-cookie'
import { useRoute } from 'vue-router'

export default {
  setup(props, { emit }) {
    const imageData = ref(null);
    const productResults = ref(null);
    const route = useRoute();
    const csrf_token = Cookies.get('csrftoken');
    const isLoading = ref(true);

    async function sendImageToBackend() {
      try {
        const url = '/api/ocr/result';

        const response = await fetch(imageData.value);
        const blob = await response.blob();

        const formData = new FormData();
        formData.append('image', blob, 'image.jpg');

        const result = await axios.post(url, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'X-CSRFToken': csrf_token,
          },
        });

        if (result.data.results === 'success') {
          productResults.value = result.data.products;
        } else {
          productResults.value = null;
        }
      } catch (error) {
        console.error('Error sending image to backend:', error);
        alert('서버와 통신 중 문제가 발생했습니다. 다시 시도해 주세요.');
      }finally {
        isLoading.value = false; // 동작 완료 후, 로딩 인디케이터를 숨김
      }
    }

    onMounted(async () => {
      imageData.value = decodeURIComponent(route.params.imageData);
      await sendImageToBackend();
    });

    return {
      imageData,
      productResults,
      isLoading,
    };
  },
};
</script>


<style scoped>
.ocr-result-page {
  width: 100%;
  height: 100%;
  padding-bottom: 30%;
  margin-top: 5%;
}
.ocr-title {
  font-weight: bold;
  font-size: 36px;
  margin-bottom: 10%;
  border-bottom: 2px solid #eeeeee;
}

.request-btn {
  background-color: #2dce89;
  color: white;
  border-radius: 5px;
  font-size: 1.125em;
  padding: 0.5em 1em;
  border: none;
  cursor: pointer;
}

.request-btn:hover {
  background-color: #2dce89;
}
.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.spinner {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 5px solid #f3f3f3;
  border-top-color: #3498db;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  100% {
    transform: rotate(360deg);
  }
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  column-gap: 1rem;
  row-gap: 1rem;
  width: 100%;
}

.grid-item {
  box-sizing: border-box;
  padding: 1rem;
  width: 100%;
}

.product-card {
  width: 100%;
  display: flex;
  align-items: center;
  border: 1px solid #ddd;
  background-color: #fff;
  padding: 1rem;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.product-image {
  flex: 0 0 100px;
  margin-right: 1rem;
}

.fill-image {
  object-fit: cover;
  width: 100%;
  height: 100px;
}

.product-details {
  flex: 1;
}
</style>
