<template lang="">
    <router-link to="/search">검색</router-link>
    <div>
        홈페이지임
    </div>
</template>
<script>
import { onMounted } from 'vue'
import { useRouter } from "vue-router";
import { useStore } from '../../stores';
export default {
    name:"HomePage",
    setup() {
        const store = useStore();
        const router = useRouter();
        const checkLogin = () => {
            if(!store.isLoggedIn){
                router.push({
                    path: "/signup",
                });
            }
        };
        onMounted(() => checkLogin());
        return {
            store,
            router,
            checkLogin,
        };
    },
}

</script>
<style lang="">
    
</style>