<template>
    <div class="camera-page">
      <h1>☆영양제 촬영하기★</h1>
      <div class="video-container" ref="videoContainer">
        <video ref="cameraPreview" autoplay style="width:100%;"></video>
        <img ref="capturedImage" style="display:none;width:100%;"> <!-- Add this line -->
      </div>
      <div class="button-container">
        <button class="capture-button" @click="capturePhoto">촬영하기</button>
        <button class="submit-button" @click="submitPhoto">제출하기</button>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from "vue";
  
  export default {
    setup() {
      const cameraPreview = ref(null);
  
      onMounted(() => {
        openCamera();
      });
  
      const openCamera = async () => {
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
          try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            cameraPreview.value.srcObject = stream;
            cameraPreview.value.play();
          } catch (error) {
            console.error("Error accessing camera: ", error);
          }
        } else {
          console.error("getUserMedia not supported in this browser");
        }
      };
  
      return {
        cameraPreview,
        openCamera
      };
    },
    methods: {
        capturePhoto() {
      // Get video dimensions
      const video = this.$refs.cameraPreview;
      const capturedImage = this.$refs.capturedImage;
      const width = video.videoWidth;
      const height = video.videoHeight;

      // Create a temporary canvas to draw the current frame
      const canvas = document.createElement("canvas");
      canvas.width = width;
      canvas.height = height;

      // Draw current frame of video on the canvas
      const ctx = canvas.getContext("2d");
      ctx.drawImage(video, 0, 0, width, height);

      // Pause the video
      video.pause();

      // Get the image data as base64 encoded PNG
      const imageData = canvas.toDataURL("image/png");

      // Show captured image
      capturedImage.src = imageData;
      capturedImage.style.display = "block";

      // Hide video
      video.style.display = "none";
    },
    submitPhoto() {
      // Submit photo logic
    },
  },
};
</script>
  
<style lang="">
    
</style>