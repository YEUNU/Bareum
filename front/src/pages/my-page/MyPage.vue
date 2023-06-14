<template>
   <div class="container">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <a class="navbar-brand" href="/mypage">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
          </svg>
        </a>
      </div>
    </nav>
    <div class="content-container">
      <div class="content">
        <div class="hello">hello</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    components:{  }
}
</script>

<style lang="css">

.container {
  width: 100vw; /* 화면 너비에 꽉 차도록 설정 */
  height: 100vh; /* 화면 높이에 꽉 차도록 설정 */
}

.content-container {
  width: 100%; /* 부모 요소 너비를 100%로 설정 */
  height: 100%; /* 부모 요소 높이를 100%로 설정 */
  display: flex; /* 내부 컨텐츠를 가로로 정렬하기 위해 flex 사용 */
  justify-content: flex-start; /* 왼쪽 정렬 */
  align-items: center; /* 수직 가운데 정렬 */
}

.content {
  text-align: left;
  width: 100%; /* 내부 컨텐츠를 가로로 정렬하기 위해 너비를 100%로 설정 */
}

.hello {
  display: inline-block; /* 텍스트를 가로로 정렬하기 위해 inline-block 사용 */
}
</style>