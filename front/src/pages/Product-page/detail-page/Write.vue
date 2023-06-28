<template>

<div class="background" style="display: flex; flex-direction: column; align-items: center;">
    <nav class="navbar fixed-top bg-white" style="box-shadow: 0 2px 1px -1px #EAEAEA;">
        <div class="container-fluid">
            <span class="navbar-brand" @click="$router.back()" style="margin-left: 2vh;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                </svg>
            </span>
            <div>리뷰쓰기</div>
            <button style="height: 40px;">a</button>
        </div>
    </nav>
    <div class="background bg-whitesmoke" style="display: flex; flex-direction: column; align-items: center; margin-top:56px; min-height: calc(100vh - 56px);">

        <div>
            <img :src="`/media/produt_images/${productCode}.png`"/>
            {{ product.nutraceuticals_name }}
            {{ product.업소명 }}
        </div>
        <form @submit.prevent="submitReview(product.업체별_제품코드)">
            <div class="form-group">
                <label>평점을 입력해주세요</label>
                <StarRating @update-rating="updateRating"/>
            </div>
            <div class="form-group">
                <label for="review-text">Review:</label>
                <textarea id="review-text" v-model="reviewText" required></textarea>
            </div>
            <div class="form-group"><input id="images" ref="imageInput" type="file" accept="image/*" multiple @change="previewImages" /></div>

            <div style="margin-top: 5%; text-align: left;" v-for="(url, index) in imagePreviewUrls" :key="index">
                <img :src="url" class="preview-image" style="width:100%; height:30%;" />
                <button @click="removeImage(index)">x</button>
            </div>

            <button type="submit">Submit</button>
        </form>

    </div>
</div>
</template>

<script>
import { ref,onMounted } from "vue";
import StarRating from "./StarRating.vue";
import axios from 'axios';
import { useRouter } from "vue-router";
import Cookies from 'js-cookie';

export default {
    components: { StarRating },
    props:{
        productCode:{
            type:String,
            require : true
        }
    },
    
    setup(props) {
        const csrf_token = Cookies.get('csrftoken');
        const router = useRouter();
        const reviewText = ref("");
        const rating = ref(0);
        const product = ref({});

        const imageInput = ref(null); // 이미지 input 참조를 위한 ref
        const selectedImageFiles = ref([]); // 선택된 이미지 파일 리스트 ref
        const imagePreviewUrls = ref([]); // 미리보기 이미지 URL ref

        function updateRating(newRating) {
            rating.value = newRating;
        }
        
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
  
        const submitReview = async(productCode) => {
            try{
                const formData = new FormData();
                formData.append("reviews", reviewText.value);
                formData.append("rating",  rating.value);
                // 이미지 파일 첨부 시 formData에 추가 (복수 파일 처리)
                selectedImageFiles.value.forEach((file, index) => {
                    formData.append(`image${index}`, file);
                });
                await axios.post(`/api/product/bareum-reviews/${productCode}/`, formData, {
                    headers: {
                        "Content-Type": "multipart/form-data", // 폼 데이터 전송을 위해 수정
                        "X-CSRFToken": csrf_token,
                    },
                });
        
                router.push(`/product/${productCode}/review`); 
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


        const fetchProductDetail = async (productCode) =>{
            try{
                const response = await axios.get(`/api/product/detail/${productCode}/`);
                product.value = response.data;

            } catch(error){
                console.error(error);
            }
        }

        onMounted(() => {
            fetchProductDetail(props.productCode);  
        })

        return {
            reviewText,
            rating,
            updateRating,
            submitReview,
            fetchProductDetail,       
            product,
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

</style>