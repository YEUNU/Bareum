<template>
    <div>
      주소입력받기
    </div>
    <input type="text" v-model="postcode" placeholder="우편번호">
    <input type="button" @click="execDaumPostcode" value="우편번호 찾기"><br>
    <input type="text" :value="address" placeholder="주소" readonly><br>
    <input type="text" id="detailAddress" placeholder="상세주소">
    <input type="text" :value="extraAddress" placeholder="참고항목" readonly>
  </template>
  
  <script>
  import { reactive, toRefs } from 'vue';
  
  export default {
    setup() {
      const state = reactive({
        postcode: '',
        address: '',
        extraAddress: ''
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
      }
  
      return {
        ...toRefs(state),
        execDaumPostcode
      };
    }
  };
  </script>
  
  <style lang="">
      
  </style>
  