<template>
    <div>
        
        카테고리페이지

        <button @click="saveCategory">다음</button>
    </div>
</template>
<script>
import { useRouter } from 'vue-router';
export default {
    setup(){
        const router = useRouter();

        const saveCategory = () => {
            router.push('/guide');
        }

        return{
            saveCategory,
        }
    }
}
</script>
<style lang="">
    
</style>