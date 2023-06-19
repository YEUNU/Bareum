<template>
  <div class="container">
    <nav class="navbar fixed-top bg-light">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
          </svg>
        </router-link>
      </div>
      <div style="margin-top: 3%;">
        <span class="navbar-brand mb-0" style="padding: 2.2vh;">제품 촬영 가이드</span>
      </div>
    </nav>

    <div class="cameracontent">
        <div style="margin-left: 5%;">
        <h4>01</h4>
        <p>주의사항주의사항주의사항주의사항주의사항주의사항주의사항주의사항</p>
        </div>
    </div>

    <div class="cameracontent">
        <div style="margin-left: 5%;">
        <h4>02</h4>
        <p>주의사항주의사항주의사항주의사항주의사항주의사항주의사항주의사항</p>
        </div>
    </div>

        <button class="yesbutton">촬영 시작하기</button>
    
  </div>
  
</template>

<script>
export default {
  components: {},
};
</script>

<style>
.container {
  width: 100%;
  height: 100%;
  display: block;
  margin-bottom: 10%;
  background-color: white;;
}

.cameracontent {
    text-align: left;
    width: 100%;
    height: 100%;
    border-radius: 8px;
    border: 1px solid #CCCCCC;
    margin-bottom: 10%;
}
</style>