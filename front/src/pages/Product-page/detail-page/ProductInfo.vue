<template>
    <div>
        제품정보 보여주기 {{ productCode }}
    </div>
</template>
<script>
import axios from 'axios';
import {ref} from 'vue';
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
                const response = await axios.get(`/api/product/detail/${props.productCode}`);
                product = response.data;


            }catch(error){
                console.error(error);
            }
        }

        return{
            fetchProductDetail,
            product
        }
    }


}
</script>
<style>
    
</style>