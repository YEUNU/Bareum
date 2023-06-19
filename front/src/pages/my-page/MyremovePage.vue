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
        
        <div class="content">
            <div class="row">
                <div class="col-9">
                    <h4>정말 탈퇴하시겠습니까?</h4>
                    <h5>불편했던점을 알려주세요!</h5>
                </div>
                    <input  class="form-control" id="exampleFormControlInput1" placeholder="내용을 입력해주세요." style="margin-bottom: 5%;">
                    <input  class="form-control" id="exampleFormControlInput1" placeholder="내용을 입력해주세요." style="margin-bottom: 5%;">
                    <input  class="form-control" id="exampleFormControlInput1" placeholder="내용을 입력해주세요." style="margin-bottom: 5%;">
            </div>
            <router-link to="/myremovedetail"><button style="margin-top: 10%; background-color: #2dce89; border-radius: 5px; color:white;">다음</button></router-link>
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
}



</style>