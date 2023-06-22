<template>
  <div class="ocr-result-page">
    <h1>OCR 결과</h1>
    <img :src="imageData" alt="Captured image" style="width: 50%;" />
    <div v-if="isLoading" class="loading-container">
      <div class="spinner"></div>
      <p>제품을 찾는 중입니다...</p>
    </div>
    <div v-else>
      <div v-if="productResults">
        <h2>인식된 제품 정보(유사도순)</h2>
        <div class="grid-container">
          <div v-for="(product, index) in productResults" :key="index" class="grid-item">
            <div class="product-card">
              <div class="product-image">
                <!-- 추후에 이미지를 여기에 추가하세요 -->
                <img src="#" alt="Product image" class="fill-image" />
              </div>
              <div class="product-details">
                <h5>{{ index + 1 }}. 품목명: {{ product.nutraceuticals_name }}</h5>
                <p>업소명: {{ product.업소명 }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <p>관련된 제품을 찾지 못했습니다.</p>
        <router-link to="/ocr/registration" class="request-link">
          <button class="request-btn">등록 요청</button>
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
.request-btn {
  background-color: #3498db;
  color: white;
  font-size: 1.125em;
  padding: 0.5em 1em;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.request-btn:hover {
  background-color: #2c80b9;
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
}

.grid-item {
  box-sizing: border-box;
  padding: 1rem;
}

.product-card {
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
