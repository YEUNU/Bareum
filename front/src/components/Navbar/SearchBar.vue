<template>
    <div class="search">
        <input class="search-input" type="text" :placeholder="placeholder" v-model="searchQuery" @keydown.enter="search">
    <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search">
    </div>
</template>

<script>
import { ref, defineProps } from 'vue';

export default {
    props: {
        placeholder: {
            type: String,
            default: '검색어 입력'
        }
    },
    setup(props) {
        const searchQuery = ref('');
    
    const search = () => {
        // 검색 로직
        console.log('검색어:', searchQuery.value);
    };
    
    return {
        searchQuery,
        search
    };
    }
};
</script>

<style>
.search {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
}

.search-input {
    width: 100%;
    border: 1px solid #bbb;
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 14px;
    box-sizing : border-box;
}

.search-icon {
    position: absolute;
    width: 17px;
    right: 12px;
    margin: 0;
   	z-index: 1;
}

</style>