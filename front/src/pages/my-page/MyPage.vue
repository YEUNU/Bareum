<template>

    <div class="mycontainer">
      <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/" class="navbar-brand">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
        </router-link>
        </div>
      </nav>

      <div class="mycard-container">
        <div class="card" style="width: 100%; margin-bottom: -5%;">
          <div class="card-body">
            <div class="d-flex align-items-center mb-4">
              <div class="flex-shrink-0">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-2.webp"
                  alt="Generic placeholder image" class="img-fluid rounded-circle border border-dark border-3"
                  style="width: 70px;">
              </div>
              <div class="flex-grow-1 ms-3">
                <div class="d-flex flex-row align-items-center mb-2">
                  <p class="mb-0 me-2">닉네임</p>
                </div>
                <div>
                  <p class="mb-0 me-2" style="text-align: left;">나이 / 성별</p>
                </div>
              </div>
            </div>
            <router-link to="/myupdate"><button type="button" class="btn btn-outline-white btn-rounded btn-sm" style="margin-right: 10%; color:black;">개인정보 수정</button></router-link>
            <router-link to="/myupdate"><button type="button" class="btn btn-outline-white btn-rounded btn-sm" style="margin-right: 10%; color:black;">내 리뷰 관리</button></router-link>
            <router-link to="/myupdate"><button type="button" class="btn btn-outline-white btn-rounded btn-sm" style="color:black;">찜 목록</button></router-link>
          </div>
        </div>
      </div>

<div class="mycard-container">
  <div class="card" style="width: 100%; display:block; margin-bottom: -5%;">
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

<div class="mycard-container">
  <div class="card" style="width: 100%; display:block; margin-bottom: -5%;">
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

<div class="mycard-container">
  <div class="card" style="width: 100%; display:block; margin-bottom: -5%;">
    <div class="card-body">
            <router-link to="/myorder"><h5 style="text-align: left;">주문 / 배송 내역</h5></router-link>
            <router-link to="/mypush"><h5 style="text-align: left;  margin-top: 10%;">알람 설정</h5></router-link>
    </div>
  </div>
</div>

<div class="mycard-container">
  <div class="card" style="width: 100%; display:block;">
    <div class="card-body">
        <h5 style="text-align: left; margin-top: -5%;">고객지원</h5>
        <div class="m-title" style="margin-top: 5%">
            <router-link to="/myterms"><h5 style="text-align: left; margin-top: 10%;">이용약관</h5></router-link>
            <router-link to="/myprivacy"><h5 style="text-align: left; margin-top: 10%;">개인정보 처리방침</h5></router-link>
            <router-link to="/" @click="userLogout"><h5 style="text-align: left; margin-top: 10%;">로그아웃</h5></router-link>
            <router-link to="/myremove"><h5 style="text-align: left; margin-top: 10%;">회원탈퇴</h5></router-link>
            <router-link to="/mysupport" style=" margin-top: 10%; margin-right: 15vh;">문의하기</router-link>
            <router-link to="/mynewadd" style=" margin-top: 10%;">영양제 등록 요청</router-link>
        </div>
    </div>
  </div>
</div>
    </div>
  
    
  </template>

<script>
import { useUserInfo } from '../../stores.js';
  export default {
    setup() {
      const userInfo = useUserInfo()
      const {userLogout} = userInfo
    const isLoggedIns = userInfo.isLoggedIns;
    return {
      isLoggedIns,
      userInfo,
      userLogout
    };
  },

  components: {}
};
  </script>

  <style lang="css">

  .mycontainer {
    width: 100%; /* 화면 너비에 꽉 차도록 설정 */
    height: 100%; /* 화면 높이에 꽉 차도록 설정 */
    display: block;
    margin-bottom: 10%;
    background-color: #E1E1E1;
    border-radius: 10px;
  }
  
  .mycard-container {
    margin-bottom: 5%;
  }

  .btn {
  margin-right: 0.6vw; /* 버튼들 사이의 간격을 조절 */
  margin-top: 5px;
}


  </style>
