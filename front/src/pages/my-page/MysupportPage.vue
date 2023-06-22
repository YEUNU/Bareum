<template>
    <div class="supportcontainer">
        <nav class="navbar fixed-top bg-white">
            <div class="container-fluid">
                <router-link to="/mysetting" class="navbar-brand" style="margin-left: 2vh;">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
              </svg>
          </router-link>
            </div>
            
        </nav>
        
        <div class="supcontent" style="margin-top: 10%; padding-bottom: 20%;">
                <div class="col-9" style="text-align: left;">
                    <h4>문의 유형</h4>
                </div>
                <div class="col-9">
                    <select class="form-select form-select-sm" aria-label=".form-select-sm example">
                        <option selected>문의 유형을 선택해주세요.</option>
                        <option value="1">서비스 문의</option>
                        <option value="2">서비스 요청</option>
                        <option value="3">서비스 오류 제보</option>
                    </select>
                </div>
                
                <div class="col-9" style="text-align: left;">
                    <h4>문의 제목</h4>
                </div>
                <div class="col-9">
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="1" placeholder="제목을 입력해주세요."></textarea>
                </div>

                <div class="col-9" style="text-align: left;">
                    <h4>문의 내용</h4>
                </div>
                <div class="col-9">
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="5" placeholder="내용을 입력해주세요."></textarea>
                </div>
                <div class="submit"><button style="background-color: #2dce89; color: white; border-radius: 5px;">제출하기</button></div>
            </div>
            
    </div>
</template>

<script>
export default {
    components: {}
}
</script>
  
<style>
.supportcontainer {
    width: 100%; /* 화면 너비에 꽉 차도록 설정 */
    height: 100%; /* 화면 높이에 꽉 차도록 설정 */
    display: block;
    margin-bottom: 10%;
    padding-bottom: 20%;
}

.content {
    
    display:block;
}







.col-9 {
    margin-left: 10%;
    margin-bottom: 5%;

}
</style>