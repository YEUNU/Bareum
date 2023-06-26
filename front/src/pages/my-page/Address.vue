<template>
    <div class="mycontainer">
      <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/mypage" class="navbar-brand" style="margin-left: 2vh;">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
        </router-link>
        <div style="margin-right: 2vh;">내 주소 관리</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
            <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
          </svg>
        </div>
        </div>
      </nav>
    </div>
<form @submit.prevent="saveAddress">    
    <div class="mycard-container">
      <div class="card" style="width: 100%; padding:0;  display:block; box-shadow: 2px 2px 2px 2px #eeeeee">
        <div class="card-body">
          <div class="flex-grow-1 ms-3">
            <div class="d-flex flex-row align-items-center mb-2">
              <h2 class="mb-0 me-3" style="font-weight: bold;">배송지 정보</h2>
            </div>
          </div>
        <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 5%;">
          <div style="width: 10vh; color:gray;"><span>수령인</span></div>
          <input type="text" placeholder=" " style="width: 80%; color: black; background-color: white; border: none; border-bottom: 1px solid gray;">
        </div>

        <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 6%;">
          <div style="width: 10vh; color:gray;"><span>전화번호</span></div>
          <input type="text" placeholder=" " style="width: 80%; color: black; background-color: white; border: none; border-bottom: 1px solid gray;">
        </div>

        <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 6%;">
          <div style="width: 10vh; color:gray;"><span>우편번호</span></div>
          <input type="text" v-model="postcode" placeholder=" " style="width: 60%; background-color: white; color: black; border: none; border-bottom: 1px solid gray;">
          <input type="button" @click="execDaumPostcode" value="찾기" style="width: 9vh; background-color: #2dce89; color:white; border: 1px solid; border-radius: 5px; margin-left: 5%;">
        </div>

        <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 6%;">
          <div style="width: 10vh; color:gray;"><span>주소</span></div>
          <input type="text" :value="address" readonly style="width: 80%; background-color: white; color:black; border: none; border-bottom: 1px solid gray;">
        </div>

        <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 6%; margin-bottom: 2%">
          <div style="width: 10vh; color:gray;"><span>상세주소</span></div>
          <input type="text" id="detailAddress" placeholder=" " style="width: 80%; background-color: white; color:black; border: none; border-bottom: 1px solid gray;" v-model="detailed_address">
        </div>
      </div>
      </div>
    </div>

    <div class="mycard-container">
      <div class="card" style="width: 100%; padding:0;  display:block; box-shadow: 2px 2px 2px 2px #eeeeee"> 
        <div class="card-body">
          <div class="flex-grow-1 ms-3">
            <div class="d-flex flex-row align-items-center mb-2">
              <h2 class="mb-0 me-3" style="font-weight: bold;">주문자 정보</h2>
            </div>
          </div>
      
        <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 5%;">
          <div style="width: 10vh; color:gray;"><span>이름</span></div>
          <input type="text" placeholder=" " style="width: 80%; color: black; background-color: white; border: none; border-bottom: 1px solid gray;" :value="userInfo.name" readonly>
        </div>

        <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 6%;">
          <div style="width: 10vh; color:gray;"><span>이메일</span></div>
          <input type="email" placeholder="example@example.com" style="width: 80%; color: black; background-color: white; border: none; border-bottom: 1px solid gray;" readonly>
        </div>


        <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 6%; margin-bottom: 2%">
          <div style="width: 10vh; color:gray;"><span>전화번호</span></div>
          <input type="text" placeholder=" " style=" width: 80%; color: black; background-color: white; border: none; border-bottom: 1px solid gray;" readonly>
        </div>
      </div>
      </div>

    </div>
    <button style="width:100%; margin-bottom: 50%; background-color: #2dce89; border-radius: 5px; color:white; box-shadow: 2px 2px 2px 2px #eeeeee">저장</button>
    </form>


  </template>
  
  <script>
  import { reactive, toRefs,onMounted } from 'vue';
  import axios from 'axios';
import Cookies from 'js-cookie';
import { useUserInfo } from '../../stores';
import { useRouter } from 'vue-router';
  export default {
    setup() {
        const csrf_token = Cookies.get("csrftoken");
      const userInfo = useUserInfo();
      const router = useRouter();
        const state = reactive({
        postcode: '',
        address: '',
        extraAddress: '',
        detailed_address:''
      });
        
      const execDaumPostcode = async () => {
        await new Promise((resolve) => {
          new window.daum.Postcode({
            oncomplete: (data) => {
              if (state.extraAddress !== '') {
                state.extraAddress = '';
              }
              if (data.userSelectedType === 'R') {
                state.address = data.roadAddress;
              } else {
                state.address = data.jibunAddress;
              }
              if (data.userSelectedType === 'R') {
                if (data.bname !== '' && /[동|로|가]$/g.test(data.bname)) {
                  state.extraAddress += data.bname;
                }
                if (data.buildingName !== '' && data.apartment === 'Y') {
                  state.extraAddress += state.extraAddress !== ''
                    ? `, ${data.buildingName}`
                    : data.buildingName;
                }
                if (state.extraAddress !== '') {
                  state.extraAddress = `(${state.extraAddress})`;
                }
              } else {
                state.extraAddress = '';
              }
              state.postcode = data.zonecode;
              resolve();
            }
          }).open();
        });
      };

      const saveAddress = async () => {
      try {
        await axios.post(`/api/account/address/${userInfo.memberId}/`, {
          postcode: state.postcode,
          address: state.address,
          extra_address: state.extraAddress,
          detailed_address: state.detailed_address,
        },
        {
            headers:{
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token,
            }
        });
        alert('주소 저장 완료');
        router.push('/');
      } catch (error) {
        console.error(error);
        alert('주소 저장 실패');
      }
    };

    const fetchAddress = async () => {
          try {
            const response = await axios.get(`/api/account/address/${userInfo.memberId}/`);
            state.postcode = response.data.postcode;
            state.address = response.data.address;
            state.extraAddress = response.data.extra_address;
            state.detailed_address = response.data.detailed_address;
          } catch (error) {
            console.error(error);
          }
        };

        onMounted(() => {
          fetchAddress(userInfo.memberId);
        })
      return {
        ...toRefs(state),
        execDaumPostcode,
        saveAddress,
        fetchAddress,
        userInfo
      };
    }
  };
  </script>
  
  <style>
  .mycontainer {
    width: 100%; /* 화면 너비에 꽉 차도록 설정 */
    height: 100%; /* 화면 높이에 꽉 차도록 설정 */
    display: block;
    margin-bottom: 10%;
    border-radius: 10px;
  }
  
  .mycard-container {
    margin-bottom: 10%;
  }

  .btn {
  margin-right: 0.6vw; /* 버튼들 사이의 간격을 조절 */
  margin-top: 5px;
}


  </style>
  