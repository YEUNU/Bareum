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
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Cookies from 'js-cookie'
import { useRoute } from 'vue-router'

export default {
  setup (props, { emit }) {
    const imageData = ref(null);
    const ocrResult = ref(null);
    const route = useRoute();
    const csrf_token = Cookies.get('csrftoken');
    async function sendImageToBackend() {
        try {
          // Adjust the url to match your backend OCR API
          const url = '/api/ocr/result'

          // Convert the base64 image data to a Blob
          const response = await fetch(imageData.value)
          const blob = await response.blob()

          // Create a FormData instance and append the image as a file
          const formData = new FormData()
          formData.append('image', blob, 'image.jpg')

          // Send the FormData to the backend
          const result = await axios.post(url, formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
              'X-CSRFToken': csrf_token
            },
          })

          // Store the recognized text result
          ocrResult.value = result.data.text
        } catch (error) {
          console.error('Error sending image to backend:', error)
          alert('서버와 통신 중 문제가 발생했습니다. 다시 시도해 주세요.')
        }
      }

    onMounted(async () => {
      imageData.value = decodeURIComponent(route.params.imageData)
      await sendImageToBackend()
    })

    return {
      imageData,
      ocrResult
    }
  }
}
</script>
