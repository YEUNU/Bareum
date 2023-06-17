<template >
            <nav class="navbar fixed-top bg-light">
            <div class="container-fluid">
    <div class="search">
      <input class="search-input" type="text" :placeholder="placeholder" v-model="searchQuery" @keydown.enter="search">
        <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search"> 
    </div>
    </div>
    </nav>
    <router-view></router-view>
</template>
<script>
export default {
    
}
</script>
<style>
    
</style>