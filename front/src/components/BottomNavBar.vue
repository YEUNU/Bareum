<template>
  <nav class="bottom-nav-bar">
    <ul>
      <li><router-link to="/">홈</router-link></li>
      <li><router-link to="/search">검색</router-link></li>
      <li><router-link to="/mypage">마이 페이지</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {

}
</script>

<style scoped>
.bottom-nav-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  background-color: #f0f0f0;
  padding: 10px;
}

.bottom-nav-bar ul {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
}

.bottom-nav-bar li {
  flex: 1;
  text-align: center;
}

.bottom-nav-bar a {
  display: block;
  padding: 10px;
  text-decoration: none;
  color: #333;
}
</style>
