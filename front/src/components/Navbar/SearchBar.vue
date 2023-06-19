<template>
    <div class="search">
        <input class="search-input" type="text" :placeholder="placeholder" v-model="searchQuery" @keydown.enter="search">
        <svg v-if=" searchQuery != '' " class="search-clear-icon" @click="search_clear" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
        </svg>
        <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search">
    </div>
</template>

<script>
import { ref } from 'vue';

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
    
    const search_clear = () => {
        searchQuery.value = '';
    }

    return {
        searchQuery,
        search,
        search_clear,
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

.search-clear-icon {
    position: absolute;
    width: 17px;
    right: 37px;
    margin: 0;
   	z-index: 1;
}

</style>