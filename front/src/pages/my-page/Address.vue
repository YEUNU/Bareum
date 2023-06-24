<template>
    <div>
      주소입력받기
    </div>
    <div>
     <div>현재 우편번호   {{ currentPostcode }}</div>
     <div> 현재 주소      {{ currentAddress }}</div>
     <div> 현재 상세 주소 {{ currentExtraAddress }}</div>
     <div> 현재 참고 항목 {{ currentDetailed_address }}</div>
    </div>
    <form @submit.prevent="saveAddress">
        <input type="text" v-model="postcode" placeholder="우편번호" required>
        <input type="button" @click="execDaumPostcode" value="우편번호 찾기"><br>
        <input type="text" :value="address" placeholder="주소" readonly required><br>
        <input type="text" :value="detailed_address" placeholder="상세주소" required>
        <input type="text" :value="extraAddress" placeholder="참고항목" readonly required>
        <button> 주소 저장 </button>
    </form>

  </template>
  
  <script>
  import { reactive, toRefs } from 'vue';
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
      
      const currentAddress = reactive({
        currentPostcode: '',
        currentAddress: '',
        currentExtraAddress: '',
        currentDetailed_address:''

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
            currentAddress.currentPostcode = response.data.postcode;
            currentAddress.currentAddress = response.data.address;
            currentAddress.currentExtraAddress = response.data.extra_address;
            currentAddress.currentDetailed_address = response.data.detailed_address;
          } catch (error) {
            console.error(error);
          }
        };
      return {
        ...toRefs(state),
        execDaumPostcode,
        saveAddress,
        fetchAddress,
        ...toRefs(currentAddress),
        
      };
    }
  };
  </script>
  
  <style lang="">
      
  </style>
  