<template>
  <nav class="bottom-nav-bar">
    <ul>
      <li><router-link to="/">홈</router-link></li>
      <li><router-link to="/shop">SHOP</router-link></li>
      <li><router-link to="/">사진찍는거</router-link></li>
      <li><router-link to="/community">커뮤니티</router-link></li>
      <li><router-link to="/mypage">마이페이지</router-link></li>
    </ul>
  </nav>
</template>

<script>

import { useStore } from '../stores';

//예시코드 나중에 수정
export default {
    name:"NavBar",
    setup() {
        const store = useStore();
        return { store };
  },
};
</script>

<style scoped>
.bottom-nav-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-around;
  background-color: #f0f0f0;
  padding: 10px;
  box-sizing: border-box;
}

.bottom-nav-bar ul {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
  width: 100%;
}

.bottom-nav-bar li {
  flex: 1;
  text-align: center;
}

.bottom-nav-bar router-link {
  display: block;
  padding: 10px;
  text-decoration: none;
  color: #333;
}

@media (max-width: 600px) {
  .bottom-nav-bar li {
    font-size: 12px;
  }
}
</style>
