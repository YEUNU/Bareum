<template>
    <div class="camera-page">
      <h1>☆영양제 촬영하기★</h1>
      <div class="video-container" ref="videoContainer">
        <video ref="cameraPreview" autoplay style="width:100%;"></video>
        <img ref="capturedImage" style="display:none;width:100%;">
      </div>
      <div class="button-container">
        <button class="capture-button" @click="capturePhoto">촬영하기</button>
        <button class="submit-button" @click="submitPhoto">제출하기</button>
        <button class="retake-button" @click="retakePhoto">재촬영</button>
      </div>
    </div>
  </template>
  
<script>
import { ref, reactive, onMounted } from "vue";
import { useRouter } from 'vue-router';

export default {
  setup() {
    const cameraPreview = ref(null);
    const capturedImage = ref(null);
    const router = useRouter();
    const image = reactive({
      data: null
    });

    onMounted(() => {
      openCamera();
    });
  
    const openCamera = async () => {
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        try {
          const constraints = {
            video: {
              facingMode: "environment",
            },
          };
          const stream = await navigator.mediaDevices.getUserMedia(constraints);
          cameraPreview.value.srcObject = stream;
          cameraPreview.value.play();
        } catch (error) {
          console.error("Error accessing camera: ", error);
        }
      } else {
        console.error("getUserMedia not supported in this browser");
      }
    };

    const capturePhoto = () => {
      const width = cameraPreview.value.videoWidth;
      const height = cameraPreview.value.videoHeight;
      const canvas = document.createElement("canvas");

      canvas.width = width;
      canvas.height = height;

      const ctx = canvas.getContext("2d");
      ctx.drawImage(cameraPreview.value, 0, 0, width, height);

      cameraPreview.value.pause();

      image.data = canvas.toDataURL("image/png");
      capturedImage.value.src = image.data;
      capturedImage.value.style.display = "block";
      cameraPreview.value.style.display = "none";
    };

    const submitPhoto = () => {
      if (!image.data) {
      alert("제품을 촬영해주세요.");
      return;
    }
    if (cameraPreview.value.srcObject) {
      const stream = cameraPreview.value.srcObject;
      const tracks = stream.getTracks();
      tracks.forEach((track) => {
        track.stop();
      });
    }
      router.push("/ocr/result/" + encodeURIComponent(image.data));
    };

    const retakePhoto = () => {
      capturedImage.value.style.display = "none";
      cameraPreview.value.style.display = "block";
      cameraPreview.value.play();
      image.data = null;
    };

    return {
      cameraPreview,
      capturedImage,
      openCamera,
      capturePhoto,
      submitPhoto,
      retakePhoto,
    };
  },
};
</script>
  
  
<style lang="">
    
</style>