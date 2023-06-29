<template>
<div class="background" style="display: flex; flex-direction: column; align-items: center;">
    <nav class="navbar fixed-top bg-white" style="box-shadow: 0 2px 1px -1px #EAEAEA;">
        <div class="container-fluid" style="font-weight: bold;">
            <span class="navbar-brand" @click="$router.back()" style="margin-left: 2vh;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                </svg>
            </span>
            <div>리뷰쓰기</div>
            <label for="review_submit" style="padding: 0 16px; font-weight: bold;">등록</label>
            <button id="review_submit" form="review" type="submit" style="display: none;"></button>
        </div>
    </nav>

    
    <div class="background bg-whitesmoke" style="display: flex; flex-direction: column; align-items: center; margin-top:56px; min-height: calc(100vh - 56px);">
        <div class="product_card product_head">
            <div style="display: flex;">
                <img :src="`/media/product_images/${productCode}.png`" style="width: 80px; height: 80px;"/>
                <div style="display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1; padding-left: 1rem;">
                    <span style="font-size: 0.8em;">{{ product.업소명 }}</span>
                    <span style="font-weight: bold;">{{ product.nutraceuticals_name }}</span>
                    <button @click="$router.push('/search')" style="width: 90px; font-size: 0.8em; padding: 0.3em 1em; background-color: white; border: 2px solid whitesmoke; border-radius: 5px; color: #333;">제품 변경</button>
                </div>
            </div>
        </div>

        <form id="review" @submit.prevent="submitReview(product.업체별_제품코드)">
            
            <div class="form-group product_card" style="text-align: center;">
                <label style="font-size: 1em;">평점을 선택해주세요</label>
                <StarRating @update-rating="updateRating" style="margin-top: -0.5em;"/>
            </div>

            <div class="form-group product_card">
                <label for="review-text">좋았던 점</label>
                <textarea id="review-text" v-model="reviewText" rows="3" required placeholder="복용하신 제품의 자세한 리뷰를 남겨주세요." style="border: none; resize: none; background-color: white; color: #333;"></textarea>
            </div>

            <div class="form-group product_card">
                <label for="images">사진등록</label>
                <input id="images" ref="imageInput" type="file" accept="image/*" multiple @change="previewImages" style="display: none;"/>
                <label for="images" style="border: 2px solid whitesmoke; border-radius: 2em; width: 75%; padding: 0.5em; align-self: center; text-align: center; color: #333; font-weight: bold;">
                    사진 첨부
                </label>

                <div style="position: relative; margin-top: 5%; text-align: left;" v-for="(url, index) in imagePreviewUrls" :key="index">
                    <img :src="url" class="preview-image" style="width:100%; height:30%;" />
                    <svg class="clear-icon" style="width: 17px; top: 15px; right: 15px;" @click="removeImage(index)" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
                    </svg>
                </div>
                
            </div>
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

.form-group {
    font-weight: bold;
}

</style>