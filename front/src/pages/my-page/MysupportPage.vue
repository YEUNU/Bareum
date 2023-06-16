<template>
    <div class="container">
        <nav class="navbar fixed-top bg-light">
            <div class="container-fluid">
                <router-link to="/mypage" class="navbar-brand">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
              </svg>
          </router-link>
            </div>
            <div style="margin-top: 3%;">
                <span class="navbar-brand mb-0" style="padding: 2.2vh;">문의하기</span>
                <span class="navbar-brand mb-0" style="padding: 3vh;">카카오계정으로 답변이 도착합니다.</span>
            </div>
        </nav>
        
        <div class="content" style="margin-top: 20%;">
            <div class="row">
                <div class="col-9" style="padding-right: 51%;">
                    <h4>문의 유형</h4>
                </div>
                <div class="col-9">
                    <select class="form-select form-select-sm" aria-label=".form-select-sm example">
                        <option selected>문의 유형을 선택해주세요.</option>
                        <option value="1">One</option>
                        <option value="2">Two</option>
                        <option value="3">Three</option>
                    </select>
                </div>
                
                <div class="col-9" style="padding-right: 51%;">
                    <h4>문의 제목</h4>
                </div>
                <div class="col-9">
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="1" placeholder="제목을 입력해주세요."></textarea>
                </div>

                <div class="col-9" style="padding-right: 51%;">
                    <h4>문의 내용</h4>
                </div>
                <div class="col-9">
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="1" placeholder="내용을 입력해주세요."></textarea>
                </div>
            </div>
            </div>
            <div class="submit" style="padding-top: 10%;"><button style="background-color: #2dce89; color: white; border-radius: 5px;">제출하기</button></div>
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

.content {
    width: 100%;
    height:100%;
    display:block;
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

.col-9 {
    margin: 10%;
}
</style>