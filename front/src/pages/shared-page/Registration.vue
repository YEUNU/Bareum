<template>
  <div class="registration-page" style="padding: 5%; margin-bottom: 10%; ">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <div @click="goBack" class="navbar-brand">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left"
            viewBox="0 0 16 16" style="margin-left: 2vh;">
            <path fill-rule="evenodd"
              d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
          </svg>
        </div>
        <div style="margin-right: 2vh;">영양제 등록 요청</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill"
            viewBox="0 0 16 16">
            <path
              d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
          </svg>
        </div>
      </div>
    </nav>

    <div class="regcontainer" style="padding: 5%; border:2px solid #eeeeee; box-shadow: 2px 2px 2px 2px #eeeeee">


      <form>
        <label for="productImage" style="text-align: left;">제품 사진 첨부</label>


        <div class="image-upload">
          <input type="file" id="productImage" @change="onFileChange" style="display: none;" accept="image/*">
          <label for="productImage" class="upload-button" style="display: flex; align-items: left; ">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-images"
              viewBox="0 0 16 16" style="margin-left:-0.7vh">
              <path d="M4.502 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z" />
              <path
                d="M14.002 13a2 2 0 0 1-2 2h-10a2 2 0 0 1-2-2V5A2 2 0 0 1 2 3a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-1.998 2zM14 2H4a1 1 0 0 0-1 1h9.002a2 2 0 0 1 2 2v7A1 1 0 0 0 15 11V3a1 1 0 0 0-1-1zM2.002 4a1 1 0 0 0-1 1v8l2.646-2.354a.5.5 0 0 1 .63-.062l2.66 1.773 3.71-3.71a.5.5 0 0 1 .577-.094l1.777 1.947V5a1 1 0 0 0-1-1h-10z" />
            </svg>
            <span class="upload-text">사진 앨범에서 선택</span>
          </label>
        </div>





        <router-link :to="{ path: '/cam', query: { returnPath: '/ocr/registration' } }" style="text-align: left;">
          <button type="button" class="camera-button" style="text-align: left; display: flex; "><svg
              xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-camera-fill"
              viewBox="0 0 16 16">
              <path d="M10.5 8.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z" />
              <path
                d="M2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4H2zm.5 2a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1zm9 2.5a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0z" />
            </svg>
            <span class="upload-text">제품 촬영하기</span>
          </button>
        </router-link>

        <img v-if="capturedImage" :src="capturedImage" style="width:100%; margin-top: 5%;" />

        <label for="productName" style="text-align: left; margin-top: 5%;">제품명</label>
        <input type="text" id="productName" v-model="productName" placeholder="제품명을 입력하세요" />

        <label for="brandName" style="text-align: left; margin-top: 5%;">브랜드</label>
        <input type="text" id="brandName" v-model="brandName" placeholder="브랜드를 입력하세요" />

        <button type="button" @click="submitForm">등록 요청하기</button>
      </form>
    </div>
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
    const goBack = () => {
      window.history.back(); // 이전 페이지로 이동
    };
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
    const dataURLtoFile = (dataurl, filename) => {
      let arr = dataurl.split(","),
        mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]),
        n = bstr.length,
        u8arr = new Uint8Array(n);

      while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
      }

      return new File([u8arr], filename, { type: mime });
    };
    const submitForm = () => {
      const filename = "captured_image.jpg";
      const file = dataURLtoFile(capturedImage.value, filename);

      const formData = new FormData();
      formData.append("productName", productName.value);
      formData.append("brandName", brandName.value);
      formData.append("image", file, filename);

      fetch('/api/ocr/regi', {
        method: 'POST',
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            alert('제품 등록이 완료되었습니다.');
            router.push('/'); // 모든 처리가 완료된 후 사용자를 원하는 페이지로 리디렉션합니다.
          } else {
            alert('제품 등록 중 오류가 발생했습니다. 다시 시도하십시오.');
          }
        })
        .catch((error) => {
          console.error(error);
          alert('제품 등록 중 오류가 발생했습니다. 다시 시도하십시오.');
        });
    };

    return {
      goBack,
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
.upload-button {
  display: inline-flex;
  align-items: left;
  justify-content: left;
  background-color: #2dce89;
  color: white;
  font-size: 1.125em;
  padding: 0.5em 1em;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
}


.upload-text {
  margin-left: 10px;
  font-size: 15px;
  /* 원하는 스타일을 적용하세요 */
  color: white;
  /* 원하는 스타일을 적용하세요 */
  font-weight: normal;
  text-align: left;
}

.regcontainer {
  width: 100%;
  height: 100%;
  margin: 0%;
  padding: 0%;
}

.registration-page {
  width: 100%;
  height: 100%;
  margin: 0%;
  padding: 0%;
}

.button-container {
  display: flex;
  justify-content: space-between;
}

.capture-button,
.submit-button,
.retake-button {
  padding: 0.5em;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  width: 32%;
  /* 폭을 32%로 설정하여 한 줄에 배치 */
  box-sizing: border-box;
  cursor: pointer;
}

input[type="text"],
input[type="file"],
.camera-button {
  padding: 0.5em;
  margin-bottom: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  width: 100%;
  /* 폭을 100%로 설정 */
  box-sizing: border-box;
}

.registration-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  height: auto;
  min-height: 100%;
  box-sizing: border-box;
  width: 100%;
  margin: 0 auto;
  padding-bottom: 90px;
}

.registration-title {
  color: black;
  font-size: 36px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 10%;
  width: 100%;
}

form {
  display: flex;
  flex-direction: column;
  width: 100%;
}

label {
  font-weight: bold;
  margin-bottom: 0.5rem;
}

button {
  background-color: #2dce89;
  color: white;
  font-size: 1.125em;
  padding: 0.5em 1em;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 1rem;
}
</style>
