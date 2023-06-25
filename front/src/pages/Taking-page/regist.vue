<template>
    <div>
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
