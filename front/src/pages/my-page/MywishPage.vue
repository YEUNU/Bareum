<template>
    <div class="mywishcontainer">
        <nav class="navbar fixed-top bg-white">
          <div class="container-fluid">
            <router-link to="/mypage" class="navbar-brand">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16" style="margin-left: 2vh;">
                <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
              </svg>
          </router-link>
          </div>
        </nav>
  
        <div class="mycard-container">
        <div class="card" style="width: 100%; padding:0; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
          <div class="card-body">
            <div class="d-flex align-items-center mb-4">
              <div class="flex-shrink-0">
                <img src="https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcR3h8B7MrzEI3wg-A8_FArF5oQlBGzRrtr8F-PN-MI41_LsiInYYB7_JkFxbrY1XTGGcbbI-W8Or2ymn4cXLM2wS3xW_Y3Ii0EJ4lPnniZSeHyZ2OahUqGrBCix8Ki3IoQw_A&usqp=CAc"
                  alt=""
                  style="height: min(25vh, 25vw); width: min(25vh, 25vw);">
              </div>
              <div class="flex-grow-1 ms-3">
                <div class="d-flex flex-row align-items-center mb-2">
                  <h4 class="mb-0 me-2" style="text-align: left; font-weight: bold;">닥터린 덴마크 락토지지 유산균</h4>
                </div>
                <div>
                  <p class="mb-0 me-2" style="text-align: left; margin-top: 10%;">58000원</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mycard-container">
        <div class="card" style="width: 100%; padding:0; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
          <div class="card-body">
            <div class="d-flex align-items-center mb-4">
              <div class="flex-shrink-0">
                <img src="https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSdLUrGJYVpSCoxC9SENnc6gk3vtdt1ppZD-2Wt4fIM24LCmmlJwTAoCcC7csepDE6qnzrEShb_Ipbd_EimvyvPfWz9K0FlIDlY-dNvjw5mMkZ7rRySeHtdnKtvzs6QeTccag&usqp=CAc"
                  alt=""
                  style="height: min(25vh, 25vw); width: min(25vh, 25vw);">
              </div>
              <div class="flex-grow-1 ms-3">
                <div class="d-flex flex-row align-items-center mb-2">
                  <h4 class="mb-0 me-2" style="text-align: left; font-weight: bold;">닥터린 비타민C</h4>
                </div>
                <div>
                  <p class="mb-0 me-2" style="text-align: left; margin-top: 10%;">48000원</p>
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
  .mywishcontainer {
      width: 100%; /* 화면 너비에 꽉 차도록 설정 */
      height: 100%; /* 화면 높이에 꽉 차도록 설정 */
      display: block;
      margin-bottom: 10%;
      padding-bottom: 80%;
    }
  
    .card {
    margin-top: 10%;
}
  
  </style>