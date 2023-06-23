<template>
  <div class="camera-wrapper">
    <div class="camera-container">
      <video v-if="!capturedImage" id="video" ref="videoRef" width="100%" height="100%" autoplay playsinline></video>
      <img v-else id="capturedImage" :src="capturedImage" width="100%" height="100%" />
    </div>
    <button class="cancel-button" @click="cancelCapture">취소</button>
    <button class="capture-button" @click="capturePhoto">
      <span class="inner-circle"></span>
    </button>
    <button class="submit-button" @click="submitPhoto">제출하기</button>
    <button class="retake-button" @click="retakePhoto">재촬영</button>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const router = useRouter();
    const videoRef = ref(null);
    const capturedImage = ref(null);

    const cancelCapture = () => {
      if (videoRef.value.srcObject) {
        videoRef.value.srcObject.getTracks().forEach((track) => track.stop());
      }
      router.back();
    };

    const startCamera = async () => {
      const constraints = { video: { facingMode: 'environment' }, audio: false };

      try {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        videoRef.value.srcObject = stream;
        await videoRef.value.play();
      } catch (error) {
        console.error(error);
      }
    };

    const capturePhoto = () => {
      const canvas = document.createElement("canvas");
      canvas.width = videoRef.value.videoWidth;
      canvas.height = videoRef.value.videoHeight;
      canvas.getContext("2d").drawImage(videoRef.value, 0, 0, canvas.width, canvas.height);
      videoRef.value.pause();
      capturedImage.value = canvas.toDataURL("image/png");
    };

    const retakePhoto = () => {
      if (capturedImage.value) {
        capturedImage.value = null;
        startCamera();
      }
    };
    const submitPhoto = () => {
      if (!capturedImage.value) {
      alert("제품을 촬영해주세요.");
      return;
    }
    if (videoRef.value.srcObject) {
      const stream = videoRef.value.srcObject;
      const tracks = stream.getTracks();
      tracks.forEach((track) => {
        track.stop();
      });
    router.push({ 
        path: router.currentRoute.value.query.returnPath, 
        query: { capturedImage: encodeURIComponent(capturedImage.value) } 
      });
    }
    };
    onMounted(() => {
      startCamera();
    });

    return {
      videoRef,
      retakePhoto,
      capturePhoto,
      cancelCapture,
      submitPhoto,
      capturedImage: capturedImage.value, 
    };
  },
};
</script>




<style scoped>
  .camera-wrapper { 
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    background-color: black;
  }
  .camera-container {
    width: 100%;
    height: calc(100% - 25%); 
    position: relative;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    overflow: hidden;
    margin: auto; 
  }
  #video {
    position: absolute;
    min-height: 100%;
    min-width: 100%;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    object-fit: cover;
  }
  .capture-button {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: white;
    position: fixed;
    bottom: 19px;
    left: 50%;
    transform: translateX(-50%);
    border: 3px solid black;
    z-index: 1;
    display:flex;
    justify-content: center;
    align-items: center;
    padding: 0; 
  }
  .inner-circle {
    width: 47px;
    height: 47px;
    border-radius: 50%;
    border: 3px solid black;
    box-sizing: border-box;
  }
  .cancel-button {
    background-color: black;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 30px;
    border: none;
    position: absolute;
    left: 20px; 
    top: 0;
    margin-top: 23px;
  }
  .submit-button {
    background-color: black;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 30px;
    border: none;
    position: absolute;
    right: 20px; 
    bottom: 0;
    margin-bottom: 23px;
  }
  .retake-button {
    background-color: black;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 30px;
    border: none;
    position: absolute;
    left: 20px; 
    bottom: 0;
    margin-bottom: 23px;
  }
</style>