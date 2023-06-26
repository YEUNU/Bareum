<template>
    <div class="supportcontainer">
        <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/mysetting" class="navbar-brand" style="margin-left: 2vh;">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
        </router-link>
        <div style="margin-right: 2vh;">문의하기</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
            <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
          </svg>
        </div>
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