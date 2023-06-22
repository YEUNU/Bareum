<template>
    <div class="registration-page">
      <h1>영양제 등록 요청</h1>
  
      <form>
        <label for="productName">제품명</label>
        <input type="text" id="productName" v-model="productName" placeholder="제품명을 입력하세요">
  
        <label for="brandName">브랜드</label>
        <input type="text" id="brandName" v-model="brandName" placeholder="브랜드를 입력하세요">
  
        <label for="productImage">제품 사진 첨부</label>
        <input type="file" id="productImage" @change="onFileChange">
  
        <button type="button" class="camera-button" @click="openCamera">제품 직접 촬영하기</button>
        <button type="button" @click="submitForm">완료하기</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  
  export default {
    setup() {
      const productName = ref("");
      const brandName = ref("");
      const productImage = ref("");
  
      const openCamera = () => {
        navigator.mediaDevices
          .getUserMedia({
            video: true,
            audio: false
          })
          .then(stream => {
            const video = document.createElement("video");
            const canvas = document.createElement("canvas");
            const videoWrapper = document.createElement("div");
            video.setAttribute("autoplay", "autoplay");
            
            const captureButton = document.createElement("button");
            captureButton.innerText = "사진 찍기";
            const closeButton = document.createElement("button");
            closeButton.innerText = "취소하기";
            
            videoWrapper.appendChild(video);
            videoWrapper.appendChild(canvas);
            videoWrapper.appendChild(captureButton);
            videoWrapper.appendChild(closeButton);
          
            document.body.appendChild(videoWrapper);
  
            video.srcObject = stream;
            video.play();
  
            const ctx = canvas.getContext("2d");
  
            captureButton.addEventListener("click", () => {
              canvas.width = video.videoWidth;
              canvas.height = video.videoHeight;
              ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
              const imageDataUrl = canvas.toDataURL("image/png");
              productImage.value = imageDataUrl;
            });
  
            closeButton.addEventListener("click", () => {
              video.srcObject.getTracks()[0].stop();
              document.body.removeChild(videoWrapper);
            });
          })
          .catch(err => {
            console.log(err);
          });
      };
  
      const onFileChange = e => {
        const files = e.target.files || e.dataTransfer.files;
        if (!files.length) return;
        const reader = new FileReader();
        reader.onload = e => {
          productImage.value = e.target.result;
        };
        reader.readAsDataURL(files[0]);
      };
  
      const submitForm = () => {
        console.log(productImage.value);
      };
  
      return {
        productName,
        brandName,
        productImage,
        openCamera,
        onFileChange,
        submitForm
      };
    }
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
