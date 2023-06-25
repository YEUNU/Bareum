<template>

  <div class="pushcontainer">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <router-link to="/mypage" class="navbar-brand"  style="margin-left: 2vh;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
          </svg>
      </router-link>
      </div>
    </nav>

<div class="mycard-container" style="align-items: left; text-align: left;">
<div class="card" style="width: 100%; display:block; margin-bottom: -5%; padding-top: 0; padding-left: 0; padding-bottom: 0; box-shadow: 2px 2px 2px 2px #eeeeee">
  <div class="card-body">
    <h3 style="text-align: left;">세부설정</h3>
    <div class="row">
  
    <div class="d-flex justify-content-between" style="align-items:center; margin-top: 2%;">
      <p class="card-text mb-2">혜택 알림</p>
      <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" style="margin-left: 100%;">
                  </div>
    </div>
  
  
    <div class="d-flex justify-content-between" style="align-items:center; margin-top: 2%;">
      <p class="card-text mb-2">건강 상태, 복용 약물</p>
      <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" style="margin-left: 100%;">
                  </div>
    </div>
  
  
    <div class="d-flex justify-content-between" style="align-items:center; margin-top: 2%;">
      <p class="card-text mb-2">알람 알림</p>
      <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault"  style="margin-left: 100%;">
                  </div>
    </div>
  
  
</div>
  </div>
</div>
</div>
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
mounted() {
    window.scrollTo(0, 0);
  },

components: {}
};
</script>

<style lang="css">


.pushcontainer {
  width: 100%; /* 화면 너비에 꽉 차도록 설정 */
  height: 100%; /* 화면 높이에 꽉 차도록 설정 */
  display: block;
  border-radius: 10px;
  padding-bottom: 180%;
}

.mycard-container {
  margin-bottom: 5%;
}


</style>
