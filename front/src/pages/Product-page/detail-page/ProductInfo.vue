<template>
    <div class="product_card product_head">
        <h4>섭취방법</h4>
        {{ product.섭취방법 }}
    </div>
    <div class="product_card">
        <h4>섭취시주의사항</h4>
        {{ product.섭취시주의사항 }}
    </div>
    <div class="product_card">
        <h4>주된기능성</h4>
        {{ product.주된기능성 }}
    </div>
    <div class="product_card">
        <div class="set">
            <h4>유통기한</h4>
            <div>{{ product.유통기한 }}</div>
            <h4>보관방법</h4>
            <div>{{ product.보관방법 }}</div>
            <h4>원재료</h4>
            <div>{{ product.원재료 }}</div>
        </div>
    </div>
    <div class="product_card set">
        <h4>성분정보</h4>
        <div>비타민D: {{ product.비타민D }}</div>
        <div>비타민E: {{ product.비타민E }}</div>
        <div>비타민k: {{ product.비타민k }}</div>
        <div>비타민B1: {{ product.비타민B1 }}</div>
        <div>비타민B2: {{ product.비타민B2 }}</div>
        <div>나이아신: {{ product.나이아신 }}</div>
        <div>비타민B6: {{ product.비타민B6 }}</div>
        <div>엽산: {{ product.엽산 }}</div>
        <div>비타민B12: {{ product.비타민B12 }}</div>
        <div>비오틴: {{ product.비오틴 }}</div>
        <div>비타민C: {{ product.비타민C }}</div>
        <div>칼슘: {{ product.칼슘 }}</div>
        <div>마그네슘: {{ product.마그네슘 }}</div>
        <div>철: {{ product.철 }}</div>
        <div>아연: {{ product.아연 }}</div>
        <div>구리: {{ product.구리 }}</div>
        <div>셀레늄_셀렌: {{ product.셀레늄_셀렌 }}</div>
        <div>요오드: {{ product.요오드 }}</div>
        <div>망간: {{ product.망간 }}</div>
        <div>몰리브덴: {{ product.몰리브덴 }}</div>
        <div>칼륨: {{ product.칼륨 }}</div>
        <div>식이섬유: {{ product.식이섬유 }}</div>
        <div>단백질: {{ product.단백질 }}</div>
        <div>프로바이오틱스: {{ product.프로바이오틱스 }}</div>
        <div>진세노사이드: {{ product.진세노사이드 }}</div>
        <div>루테인: {{ product.루테인 }}</div>
        <div>EPA_DHA_Sum: {{ product.EPA_DHA_Sum }}</div>
        <div>비타민A: {{ product.비타민A }}</div>
    </div>

</template>
<script>
import axios from 'axios';
import {ref, onMounted} from 'vue';
export default {
    props:{
        productCode:{
            type:String,
            required:true
        }
    },
    setup(props){
        const product = ref({})
        const fetchProductDetail = async () =>{
            try{
                const response = await axios.get(`/api/product/detail/${props.productCode}/`);
                product.value = response.data;


            }catch(error){
                console.error(error);
            }
        }

        onMounted(() => {
          fetchProductDetail();  
        })

        return{
            fetchProductDetail,
            product
        }
    }
}
</script>

<style>



</style>