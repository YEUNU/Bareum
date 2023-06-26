<template>
    <div>
        평점 리뷰 보여주기 {{ productId }}
    </div>
</template>
<script>
export default {
    props:{
        productId:{
            type:String,
            required:true
        }
    },
    
}
</script>
<style>
    
</style>