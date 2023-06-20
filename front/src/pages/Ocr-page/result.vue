<template>
    <div class="ocr-result-page">
      <h1>OCR 결과</h1>
      <img :src="imageData" alt="Captured image" style="width: 50%;" />
      <div v-if="ocrResult">
        <h2>인식된 텍스트</h2>
        <!-- <pre>{{ ocrResult }}</pre> -->
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    async created() {
      this.imageData = decodeURIComponent(this.$route.params.imageData);
      await this.sendImageToBackend();
    },
    data() {
      return {
        imageData: null,
        ocrResult: null,
      };
    },
    methods: {
      async sendImageToBackend() {
        try {
          // Adjust the url to match your backend OCR API
          const url = "/api/ocr/result";
  
          // Convert the base64 image data to a Blob
          const response = await fetch(this.imageData);
          const blob = await response.blob();
  
          // Create a FormData instance and append the image as a file
          const formData = new FormData();
          formData.append("image", blob, "image.jpg");
  
          // Send the FormData to the backend
          const result = await axios.post(url, formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          });
  
          // Store the recognized text result
          this.ocrResult = result.data.text;
  
        } catch (error) {
          console.error("Error sending image to backend:", error);
          alert("서버와 통신 중 문제가 발생했습니다. 다시 시도해 주세요.");
        }
      },
    },
  };
  </script>

<style>
    
</style>