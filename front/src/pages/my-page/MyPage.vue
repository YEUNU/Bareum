<template>
  <div class="mycontainer">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand" style="margin-left: 2vh;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left"
            viewBox="0 0 16 16">
            <path fill-rule="evenodd"
              d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
          </svg>
        </router-link>
        <div style="margin-right: 2vh;">마이페이지</div>
        <router-link to="/mysetting" class="navbar-brand">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill"
            viewBox="0 0 16 16">
            <path
              d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
          </svg>
        </router-link>
      </div>
    </nav>

    <div class="mycard-container">
      <div class="card" style="width: 100%; padding:0; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
        <div class="card-body">
          <div class="d-flex align-items-center mb-4">
            <div class="flex-shrink-0">
              <img :src="userInfo.profileImgUrl" alt="profile Image"
                class="img-fluid rounded-circle border border-dark border-3" style="width: 70px;">
            </div>
            <div class="flex-grow-1 ms-3">
              <div class="d-flex flex-row align-items-center mb-2">
                <h4 class="mb-0 me-2" style="font-weight: bold;">{{ userInfo.nickName }}</h4>
              </div>
              <div>
                <p class="mb-0 me-2" style="text-align: left;">{{ userInfo.age }} 세 / {{ userInfo.gender }}</p>
              </div>
            </div>
          </div>
          <div style="text-align: left; margin-left: -1%; margin-bottom: 2%;"><router-link to="/myupdate"><button
                type="button" class="btn btn-outline-white btn-rounded btn-sm" style="margin-right: 5%; color:black;">
                <h6>개인정보 수정</h6>
              </button></router-link></div>
          <div style="text-align: left; margin-left: -1%; margin-bottom: 2%;"><router-link to="/myreview"><button
                type="button" class="btn btn-outline-white btn-rounded btn-sm" style="margin-right: 5%; color:black;">
                <h6>내 리뷰 관리</h6>
              </button></router-link></div>
          <div style="text-align: left; margin-left: -1%; margin-bottom: 2%;"><router-link to="/mywish"><button
                type="button" class="btn btn-outline-white btn-rounded btn-sm" style="color:black;">
                <h6>찜 목록</h6>
              </button></router-link></div>
          <div style="text-align: left; margin-left: -1%;"><router-link to="/address"><button type="button"
                class="btn btn-outline-white btn-rounded btn-sm" style="color:black;">
                <h6>내 주소 관리</h6>
              </button></router-link></div>
        </div>
      </div>
    </div>

    <div class="mycard-container">
      <div class="card"
        style="width: 100%; padding:0;  display:block; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
        <div class="card-body">
          <h5 style="text-align: left; font-weight: bold;">건강 데이터</h5>
          <div class="row">
            <div class="d-flex justify-content-between" style="align-items:center; margin-top: 2%;">
              <router-link to="/taking">
                <p class="card-text mt-3" style="color:black;">섭취 관리</p>
              </router-link>
            </div>
          </div>
          <div class="row">
            <div class="d-flex justify-content-between" style="align-items:center; margin-top: 2%;">
              <router-link to="/manage-category">
                <p class="card-text mt-3" style="color:black;">건강 관심항목 관리</p>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="mycard-container">
    <div class="card"
         style="width: 100%; padding:0;  display:block; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
        <div class="card-body">
            <div class="d-flex justify-content-between align-items-center">
                <h5 style="text-align: left; font-weight: bold;">내 영양제</h5>
                <div class="add-nutrient-btn" style="margin-top:1rem;">
                    <router-link to="/taking" >
                        <button class="btn btn-primary"
                                style="margin-top: -25%; border: none; background-color: #2dce89; color: white; border-radius: 5px;"
                                @click="openRegistration">관리하기
                        </button>
                    </router-link>
                </div>
            </div>
          <div class="horizontal-scroll-container">
            <div class="d-flex align-items-center mt-4 mb-2">
              <div class="flex-shrink-0" style="text-align: left; width: 10%; margin-right: 5%; margin-left: 5%;"
                v-for="(product, index) in userEating" :key="index">
                <div style="position: relative; display: flex; flex-direction: column; align-items: center;">
                  <img :src="`/media/product_images/${product.제품코드}.png`" alt=""
                    style="height: min(20vh, 20vw); width: min(20vh, 20vw); display:block;">
                  <p style="text-align:center; word-wrap: break-word; width: min(20vh, 20vh); margin-top:10%">{{
                    product.제품명 }}</p>

                </div>
              </div>
            </div>
          </div>
          <div class="d-flex justify-content-between" style="align-items:center;">
            <router-link to="/">
              <p class="card-text mt-3" style="margin-top: 2%; margin-bottom: 2%; color: black;">건강 고민 & 섭취 목적</p>
            </router-link>
          </div>

          <router-link to="/ocr/registration"><button
              style="width: 100%; margin-top: 2%; background-color: #2dce89; border-radius: 5px; color:white;">영양제 등록
              요청</button></router-link>

        </div>
      </div>
    </div>

    <div class="mycard-container">
      <div class="card"
        style="width: 100%; padding:0;  display:block; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
        <div class="card-body">
          <router-link to="/cart">
            <h5 style="text-align: left; font-weight: bold; color:black;">장바구니</h5>
          </router-link>
          <router-link to="/myorder">
            <h5 style="text-align: left; font-weight: bold; margin-top: 8%; color:black;">주문 / 배송 내역</h5>
          </router-link>
          <router-link to="/mypush">
            <h5 style="text-align: left;  margin-top: 8%; margin-bottom: 0;font-weight: bold; color:black;">알람 설정</h5>
          </router-link>
        </div>
      </div>
    </div>

    <button @click="logout"
      style="width:100%; margin-top: 5%; margin-bottom: 10%; background-color: #2dce89; border-radius: 5px; color:white; box-shadow: 2px 2px 2px 2px #eeeeee">로그아웃</button>
  </div>
</template>

<script>
import axios from 'axios';
import { useUserInfo } from '../../stores.js';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const userInfo = useUserInfo();
    const { userLogout } = userInfo;
    const router = useRouter();
    const userEating = ref([]);
    const isLoggedIns = userInfo.isLoggedIns;

    const logout = async () => {

      try {
        userLogout();
        router.push('/login');
      } catch (error) {
        console.error(error);
      }
    };
    async function getUserProductsData() {
      try {
        const response = await axios.get("/api/taking/", {
          params: {
            user_id: userInfo.loginId
          },
        });
        userEating.value = response.data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }
    onMounted(() => {
      getUserProductsData();
    })


    return {
      isLoggedIns,
      userInfo,
      logout,
      userEating
    };
  },




  components: {}
};
</script>

<style lang="css">
.mycontainer {
  width: 100%;
  /* 화면 너비에 꽉 차도록 설정 */
  height: 100%;
  /* 화면 높이에 꽉 차도록 설정 */
  display: block;
  margin-bottom: 10%;
  border-radius: 10px;
}

.mycard-container {
  margin-bottom: 5%;
}

.btn {
  margin-right: 0.6vw;
  /* 버튼들 사이의 간격을 조절 */
  margin-top: 5px;
}

.horizontal-scroll-container {
  display: flex;
  overflow-x: auto;
  white-space: nowrap;
}
</style>
