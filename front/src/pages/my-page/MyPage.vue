<template>
  
    <div class="container">
      <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/" class="navbar-brand">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
        </router-link>
        </div>
      </nav>
      <div v-if="isLoggedIns.getIsLoggedIn">
      <div class="card-container" style="margin-top: 10%;">
  <div class="card" style="width: 100%; display:block;">
    <img src="" class="card-img-top" alt="">
    <div class="card-body" style="padding: 20px;">
      <h5 style="text-align: left;  margin-top: -5%;">닉네임</h5>
      <p class="card-text" style="padding-top: 5%;">나이 / 성별</p>
      <router-link to="/myupdate">개인정보 수정</router-link>
      <router-link to="/">내 리뷰 관리</router-link>
      <router-link to="/mywish">찜 목록</router-link>
    </div>
  </div>
</div>

<div class="card-container">
  <div class="card" style="width: 100%; display:block;">
    <img src="" class="card-img-top" alt="">
    <div class="card-body">
      <h5 style="text-align: left;  margin-top: -5%;">건강데이터</h5>
      <div class="row">
    <div class="col-sm-8" style="padding-top: 5%;">
      <div class="d-flex justify-content-between" style="align-items:center;">
        <p class="card-text mb-2" style="padding-top: 5%;">나의 건강검진 기록</p>
        <router-link to="/">수정</router-link>
      </div>
    </div>
    <div class="col-sm-8" style="padding-top: 5%;">
      <div class="d-flex justify-content-between" style="align-items:center;">
        <p class="card-text mt-3">건강 상태, 복용 약물</p>
        <router-link to="/">수정</router-link>
      </div>
    </div>
  </div>
    </div>
  </div>
</div>

<div class="card-container">
  <div class="card" style="width: 100%; display:block;">
    <img src="" class="card-img-top" alt="">
    <div class="card-body">
      <h5 style="text-align: left;  margin-top: -5%;">내 영양제</h5>
      <p class="card-text">등록 등록 등록</p>
      <div class="col-sm-8">
      <div class="d-flex justify-content-between" style="align-items:center;">
        <p class="card-text mt-3">건강 고민 & 섭취 목적</p>
        <router-link to="/">수정</router-link>
      </div>
    </div>
    </div>
  </div>
</div>

<div class="card-container">
  <div class="card" style="width: 100%; display:block;">
    <div class="card-body">
            <router-link to="/myorder"><h5 style="text-align: left;">주문 / 배송 내역</h5></router-link>
            <router-link to="/mypush"><h5 style="text-align: left;  margin-top: 10%;">알람 설정</h5></router-link>
    </div>
  </div>
</div>

<div class="card-container">
  <div class="card" style="width: 100%; display:block;">
    <div class="card-body">
        <h5 style="text-align: left; margin-top: -5%;">고객지원</h5>
        <div class="m-title" style="margin-top: 5%">
            <router-link to="/myterms"><h5 style="text-align: left; margin-top: 10%;">이용약관</h5></router-link>
            <router-link to="/myprivacy"><h5 style="text-align: left; margin-top: 10%;">개인정보 처리방침</h5></router-link>
            <router-link to="/"><h5 style="text-align: left; margin-top: 10%;">로그아웃</h5></router-link>
            <router-link to="/myremove"><h5 style="text-align: left; margin-top: 10%;">회원탈퇴</h5></router-link>
            <router-link to="/mysupport" style=" margin-top: 10%; margin-right: 15vh;">문의하기</router-link>
            <router-link to="/" style=" margin-top: 10%;">영양제 등록 요청</router-link>
        </div>
    </div>
  </div>
</div>
    </div>
    <div v-else>
      
      <h5>로그인이 필요합니다.</h5>
      <router-link to="/login"><button style="margin-top: 5%;">로그인</button></router-link>
    
    </div>
    </div>
  
    
  </template>

  <script>
  import { useUserInfo } from '../../stores.js';

  export default {
    setup() {
    const isLoggedIns = useUserInfo();

    return {
      isLoggedIns,
    };
  },

  components: {}
};
  </script>

  <style lang="css">

  .container {
    width: 100%; /* 화면 너비에 꽉 차도록 설정 */
    height: 100%; /* 화면 높이에 꽉 차도록 설정 */
    display: block;
    margin-bottom: 10%;
  }

  .card-container {
    margin-top: 2%;
  }

  .btn {
  margin-right: 0.6vw; /* 버튼들 사이의 간격을 조절 */
  margin-top: 5px;
}
  </style>
