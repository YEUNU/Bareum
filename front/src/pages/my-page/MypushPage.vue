<template>
    <div class="container">
        <nav class="navbar fixed-top bg-white">
          <div class="container-fluid">
            <router-link to="/mypage" class="navbar-brand">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
              </svg>
          </router-link>
          </div>
        </nav>
        
        <div class="push container-fluid border pb-2 mb-2" style="border-radius:  10px;">
            <h3>시스템 알람 설정</h3>
            <button type="button" class="btn" style="background-color: #2dce89;">설정하러가기</button>
        </div>

        <div class="select container-fluid border pb-2 mb-2" style="border-radius:  10px;">
            <div><h3>세부설정</h3></div>
            <div class="row">
  <div class="col-sm-8" style="padding-top: 5%;">
    <div class="d-flex justify-content-between align-items-center">
      <p class="card-text mb-2" style="padding-top: 5%;">혜택 알림</p>
      <button type="button" class="btn ms-3" style="background-color: #2dce89;">켜기/끄기</button>
    </div>
    <div class="d-flex justify-content-between align-items-center">
      <p class="card-text mb-2" style="padding-top: 5%;">정기배송</p>
      <button type="button" class="btn ms-3" style="background-color: #2dce89;">켜기/끄기</button>
    </div>
    <div class="d-flex justify-content-between align-items-center">
      <p class="card-text mb-2" style="padding-top: 5%;">알람알림</p>
      <button type="button" class="btn ms-3" style="background-color: #2dce89;">켜기/끄기</button>
    </div>
  </div>
</div>
    </div>
    </div>
</template>

<script>
export default {
    components: {}
}
</script>
  
<style>
.container {
    width: 100%; /* 화면 너비에 꽉 차도록 설정 */
    height: 100%; /* 화면 높이에 꽉 차도록 설정 */
    display: block;
    margin-bottom: 10%;
}

.card {
    margin-top: 10%;
}

.push {
    width: 100%;
    height: 100%;
    padding: 20%;
}

.select {
    width: 100%;
    height: 100%;
    margin-top: 10%;
    padding: 20%;
    border-bottom: 2px;
}

</style>