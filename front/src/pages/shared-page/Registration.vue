<template>
    <div class="registration-page">
      <h1>영양제 등록 요청</h1>
  
      <form>
        <label for="productName">제품명</label>
        <input type="text" id="productName" v-model="productName" placeholder="제품명을 입력하세요" />
  
        <label for="brandName">브랜드</label>
        <input type="text" id="brandName" v-model="brandName" placeholder="브랜드를 입력하세요" />
  
        <label for="productImage">제품 사진 첨부</label>
        <input type="file" id="productImage" @change="onFileChange" accept="image/*" />
        <router-link :to="{ path: '/cam', query: { returnPath: '/ocr/registration' } }">
          <button type="button" class="camera-button">제품 직접 촬영하기</button>
        </router-link>
        <img v-if="capturedImage" :src="capturedImage" width="100" />
        <button type="button" @click="submitForm">등록 요청하기</button>
      </form>
    </div>
  </template>
  
  
<script>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';

export default {
  setup() {
    const router = useRouter();
    const route = useRoute();
    const productName = ref('');
    const brandName = ref('');
    const cameraIsVisible = ref(false);
    const capturedImage = ref(null);

    onMounted(() => {
      const imageUrl = decodeURIComponent(route.query.capturedImage || '');
      if (imageUrl) {
        capturedImage.value = imageUrl;
      }
    });

    const onFileChange = (event) => {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          capturedImage.value = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    };

    const openCamera = () => {
      cameraIsVisible.value = true;

      const constraints = { video: { facingMode: "environment" }, audio: false };
      const video = document.getElementById('video');

      navigator.mediaDevices
        .getUserMedia(constraints)
        .then(stream => {
          video.srcObject = stream;
        })
        .catch(error => {
          console.error(error);
        });
    };

    const closeCamera = () => {
      const video = document.getElementById('video');
      const tracks = video.srcObject.getTracks();

      tracks.forEach(track => track.stop());
      cameraIsVisible.value = false;
    };

    const capturePhoto = () => {
      const video = document.getElementById('video');
      const canvas = document.createElement('canvas');

      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

      const dataUrl = canvas.toDataURL('image/jpeg');
      capturedImage.value = dataUrl;

      closeCamera();
    };

    const submitForm = () => { 
      
    };

    return {
      productName,
      brandName,
      cameraIsVisible,
      onFileChange,
      openCamera,
      closeCamera,
      capturePhoto,
      submitForm,
      capturedImage,
    };
  },
};

</script>
  
  
  
  
  
<style scoped>
  .button-container {
    display: flex;
    justify-content: space-between;
  }

  .capture-button, .submit-button, .retake-button {
    padding: 0.5em;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
    width: 32%; /* 폭을 32%로 설정하여 한 줄에 배치 */
    box-sizing: border-box;
    cursor: pointer;
  }
  input[type="text"], input[type="file"], .camera-button {
    padding: 0.5em;
    margin-bottom: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
    width: 100%; /* 폭을 100%로 설정 */
    box-sizing: border-box;
  }

.registration-page {
display: flex;
flex-direction: column;
align-items: center;
padding: 2rem;
max-width: 600px;
height: auto;
min-height: 100%;
box-sizing: border-box;
width: 100%;
margin: 0 auto;
padding-bottom: 90px;
}

h1 {
  color: #3498db;
  font-size: 1.5rem;
  font-weight: bold;
  margin: 0 0 1.5rem;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  width: 100%;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

button {
  background-color: #3498db;
  color: white;
  font-size: 1.125em;
  padding: 0.5em 1em;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 1rem;
}

button:hover {
  background-color: #2c80b9;
}
</style>
