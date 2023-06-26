<template>
    <ul class="commu-menu mt-3">
        <li class="commu-item">
          <router-link class="commu-link" :to="{name:'productInfoPage',params:{productId}}" >제품 정보</router-link>

        </li>
        <li class="commu-item" >
          <router-link class="commu-link" :to="{name:'productReviewPage',params:{productId}}">제품 리뷰</router-link>
        </li>
    </ul>
        
    <div class="container">
            <router-view></router-view>        
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

    setup(props){
        return{

        }
    }
}
</script>
<style>
    
</style>