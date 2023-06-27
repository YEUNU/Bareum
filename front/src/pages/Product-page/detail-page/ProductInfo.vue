<template>

        {{ product }}
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