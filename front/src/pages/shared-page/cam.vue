<template>
    <div class="camera-wrapper">
      <div class="camera-container">
        <video id="video" ref="videoRef" width="100%" height="100%" autoplay playsinline></video>
      </div>
    <button class="cancel-button" @click="cancelCapture">취소</button>
    <button class="capture-button" @click="capturePhoto">
        <span class="inner-circle"></span>
    </button>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  
  export default {
    setup() {
      const cameraIsVisible = ref(false);
      const videoRef = ref(null);
  
      const startCamera = async () => {
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
  
      const capturePhoto = () => {
       
      };
  
      onMounted(() => {
        startCamera();
      });
  
      return {
        videoRef,
        capturePhoto,
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
    bottom: 20px;
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
    bottom: 0;
    margin-bottom: 25px;
  }
</style>