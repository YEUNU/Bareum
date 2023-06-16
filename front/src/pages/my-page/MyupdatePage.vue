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

      <div class="card-container">
  <div class="card" style="width: 100%; display:block;">
    <img src="" class="card-img-top" alt="...">
    <div class="card-body">
      <div class="row">
    <div class="col-sm-8" style="padding-top: 5%;">
      <div class="d-flex justify-content-between" style="align-items:center;">
        <p class="card-text" style="padding-top: 5%;">이름 / 닉네임</p>
      </div>
      <div><h6>내용<button>수정</button></h6>
        </div>
    </div>
    <div class="col-sm-8" style="padding-top: 5%;">
      <div class="d-flex justify-content-between" style="align-items:center;">
        <p class="card-text" style="padding-top: 5%;">생년월일</p>
      </div>
      <div><h6>내용<button>수정</button></h6>
        </div>
    </div>
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

  .card-container {
    margin-top: 2%;
  }

  .name {
    width: 100%;
    height: 100%;
    margin-top: 50%;
    
  }

</style>