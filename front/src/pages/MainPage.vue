<template lang="">
    <div class="app">
        <router-view></router-view>
        <BottomNavBar></BottomNavBar>
    </div>

</template>

<script>

import { useStore } from '../stores';
import BottomNavBar from '../components/BottomNavBar.vue';

//예시코드 나중에 수정
export default {
    name:"MainPage",
    components:{BottomNavBar}
    ,
    setup() {
        const store = useStore();
        const { count, isLoggedIn } = store;

        //state는 직접수정이 불가능하고 무조건 함수를통해서 수정해야함
        const handleIncrement = () => {
            store.increment();
        };

        return {
            count,
            isLoggedIn,
            handleIncrement,
        };
  },
};
</script>
<style lang="">
    
</style>