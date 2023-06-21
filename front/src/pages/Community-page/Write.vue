<template>
    <div>
      <h1>글쓰기 페이지</h1>
      <form @submit.prevent="submitPost">
        <div>
          <label for="title">제목</label>
          <input id="title" v-model="postTitle" required />
        </div>
        <div>
          <label for="content">내용</label>
          <textarea id="content" v-model="postContent" required ></textarea>
        </div>
        <div>
          <label for="image">이미지 첨부</label>
          <input id="images" ref="imageInput" type="file" accept="image/*" multiple @change="previewImages" />
        </div>
        <div v-for="(url, index) in imagePreviewUrls" :key="index">
          <img :src="url" class="preview-image" />
          <button @click="removeImage(index)">x</button>
        </div>
        <button type="submit">글쓰기</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  import axios from 'axios';
  import { useUserInfo } from '../../stores';
  import { useRouter } from 'vue-router';
  import Cookies from 'js-cookie';

  export default {
    setup() {
      const postTitle = ref('');
      const postContent = ref('');
      const userInfo = useUserInfo();
      const router = useRouter();
      console.log(userInfo)
      const csrf_token = Cookies.get('csrftoken');

      const imageInput = ref(null); // 이미지 input 참조를 위한 ref
      const selectedImageFiles = ref([]); // 선택된 이미지 파일 리스트 ref
      const imagePreviewUrls = ref([]); // 미리보기 이미지 URL ref
      const resizeImage = (file) => {
        const maxWidth = 800;
        const maxHeight = 800;
        const img = new Image();
        const canvas = document.createElement('canvas');
            
        return new Promise((resolve, reject) => {
          img.onload = () => {
            let width = img.width;
            let height = img.height;
          
            if (width > height) {
              if (width > maxWidth) {
                height *= maxWidth / width;
                width = maxWidth;
              }
            } else {
              if (height > maxHeight) {
                width *= maxHeight / height;
                height = maxHeight;
              }
            }
          
            canvas.width = width;
            canvas.height = height;
            canvas.getContext('2d').drawImage(img, 0, 0, width, height);
          
            canvas.toBlob(blob => {
              resolve(new File([blob], file.name, { type: file.type }));
            }, file.type);
          };
          img.onerror = (err) => reject(err);
          img.src = URL.createObjectURL(file);
        });
      };
      
      const previewImages = async () => {
        const files = Array.from(imageInput.value.files);
        const resizedFiles = [];
      
        for (const file of files) {
          try {
            const resizedFile = await resizeImage(file);
            resizedFiles.push(resizedFile);
          } catch (err) {
            console.error('Image resize failed:', err);
          }
        }
        
        selectedImageFiles.value = resizedFiles;
        imagePreviewUrls.value = resizedFiles.map(file => URL.createObjectURL(file));
      };
    const submitPost = async () => {
      try {
        const formData = new FormData();
        formData.append("title", postTitle.value);
        formData.append("content", postContent.value);
        formData.append("memberId", userInfo.memberId);
        // 이미지 파일 첨부 시 formData에 추가 (복수 파일 처리)
        selectedImageFiles.value.forEach((file, index) => {
          formData.append(`image${index}`, file);
        });
      
        await axios.post("/api/community/write", formData, {
          headers: {
            "Content-Type": "multipart/form-data", // 폼 데이터 전송을 위해 수정
            "X-CSRFToken": csrf_token,
          },
        });
      
        router.push("/community"); // 커뮤니티 페이지로 이동
      } catch (error) {
        console.error("글 작성 중 에러가 발생했습니다:", error);
      }
    };

      const removeImage = (index) => {
      // 미리보기 이미지 URL 리스트에서 해당 이미지 제거
      imagePreviewUrls.value.splice(index, 1);

      // 선택된 이미지 파일 리스트에서 해당 파일 제거
      selectedImageFiles.value.splice(index, 1);
    };

  
      return {
        postTitle,
        postContent,
        submitPost,
        
        imageInput,
        selectedImageFiles,
        imagePreviewUrls,
        previewImages,
        removeImage
        
      };
    },
  };
  </script>
  
  <style>
  .preview-image {
  width: 100px;
  height: 100px;

  object-fit: cover;
}
  </style>
  