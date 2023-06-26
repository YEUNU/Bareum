<template>
    <div>
        {{ product }}
    </div>
</template>
<script>
import axios from 'axios';
import {ref} from 'vue';
export default {
    props:{
        product:{
            type:String,
            required:true
        }
    },
    setup(props){
        const product = ref({})
        const fetchProductDetail = async () =>{
            try{
                const response = await axios.get(`/api/product/detail/${props.productId}`);
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