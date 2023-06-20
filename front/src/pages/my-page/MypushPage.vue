<template>

  <div class="pushcontainer">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
          </svg>
      </router-link>
      </div>
    </nav>

<div class="mycard-container" style="align-items: left; text-align: left;">
<div class="card" style="width: 100%; display:block; margin-bottom: -5%; padding-top: 0; padding-left: 0; padding-bottom: 0; box-shadow: 2px 2px 2px 2px #eeeeee">
  <div class="card-body">
    <h3 style="text-align: left;  margin-top: 1%;">세부설정</h3>
    <div class="row">
  <div class="col-sm-8" style="padding-top: 5%;">
    <div class="d-flex justify-content-between" style="align-items:center;">
      <p class="card-text mb-2" style="padding-top: 5%;">혜택 알림</p>
      <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
                  </div>
    </div>
  </div>
  <div class="col-sm-8" style="padding-top: 5%;">
    <div class="d-flex justify-content-between" style="align-items:center;">
      <p class="card-text mb-2" style="padding-top: 5%;">건강 상태, 복용 약물</p>
      <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
                  </div>
    </div>
  </div>
  <div class="col-sm-8" style="padding-top: 5%;">
    <div class="d-flex justify-content-between" style="align-items:center;">
      <p class="card-text mb-2" style="padding-top: 5%;">알람 알림</p>
      <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
                  </div>
    </div>
  </div>
  
</div>
  </div>
</div>
</div>
<button type="button" class="btn" style="background-color: #2dce89; color: white; margin-top: 5%;">설정하러가기</button>
  </div>
  
  
</template>

<script>
import { useUserInfo } from '../../stores.js';
import {ref} from 'vue'
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

.pushcontainer {
  width: 100%; /* 화면 너비에 꽉 차도록 설정 */
  height: 100%; /* 화면 높이에 꽉 차도록 설정 */
  display: block;
  margin-bottom: 130%;
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
