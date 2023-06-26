<template>
  
        <div class="mycontainer">
            <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/" class="navbar-brand" style="margin-left: 2vh;">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
        </router-link>
        <div style="margin-right: 2vh;">섭취 관리</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
            <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
          </svg>
        </div>
        </div>
      </nav>
        <div class="d-flex justify-content-between align-items-center">
            <h1>내가 먹는 영양제 관리</h1>
            <router-link to="/taking/search" >
                <button class="btn btn-primary" @click="openRegistration">영양제 등록</button>
            </router-link>
        </div>
        <div class="nutraceutical-list">
            <ul>
                <li v-for="nutraceutical in nutraceuticals" :key="nutraceutical.checking_number">
                    {{ nutraceutical.nutraceuticals_name }}
                </li>
            </ul>
        </div>
        </div>
</template>

<script>
export default {
    data() {
        return {
            nutraceuticals: [],
            login_id: '' // 로그인한 사용자의 ID를 저장할 변수입니다. 로그인 시스템에 맞게 수정해주세요.
        }
    },
    methods: {
        // 등록 버튼 클릭 시 실행되는 함수입니다. 실제 등록 기능을 구현해주세요.
        openRegistration() {
            console.log("영양제 등록 버튼이 클릭되었습니다.");
        }
    },
    created() {
        // 페이지가 생성되면 사용자의 영양제 목록을 가져옵니다. 실제 데이터를 가져오는 API를 호출하는 코드로 수정해주세요.
        this.nutraceuticals = [
            { checking_number: 1, nutraceuticals_name: '임시 생성1', login_id: this.login_id },
            { checking_number: 2, nutraceuticals_name: '임시 생성2', login_id: this.login_id }
        ]
    }
}
</script>

<style scoped>
.nutraceutical-list {
    padding: 0;
    list-style-type: none;
}
.nutraceutical-list ul li {
    margin: 10px;
    border-bottom: 1px solid #ccc;
    padding: 10px 0;
}
</style>
