<template>

    <div class="mycontainer">
  
        <nav class="navbar fixed-top bg-white">
  
          <div class="container-fluid">
  
            <router-link to="/mypage" class="navbar-brand" style="margin-left: 2vh;">
  
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
  
                <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
  
              </svg>
  
          </router-link>
  
          </div> 
  
        </nav>
  
  
  
  
        <div class="mycard-container">
  
          <div class="card" style="width: 100%; padding:0; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
  
            <div class="card-body">
  
                <div>
  
                  <input type="file" accept="image/*" @change="handleFileUpload" style="display: none" ref="fileInput">
  
                  <img :src="imageUrl" alt="Profile image" class="img-fluid rounded-circle border border-dark border-3" style="width: 100px; cursor: pointer" @click="openFilePicker">
  
                </div>
  
  
  
  
                <div style="margin-top: 5%;"><svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-camera-fill" viewBox="0 0 16 16">
  
                  <path d="M10.5 8.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>
  
                  <path d="M2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4H2zm.5 2a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1zm9 2.5a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0z"/></svg>
  
                </div>
  
  
  
  
      <div style="text-align: left; margin-top: 10%;">
  
          <p style="color: black; margin-left: 3%; font-weight: bold;">닉네임</p>
  
          <div class="input-group mb-3">
  
            <input type="text" name="nickname" class="form-control" placeholder="닉네임"  style="border:none;" v-model="닉네임">
  
          </div>
  
          <hr>
  
      </div>
  
      <div style="text-align: left; margin-top: 10%;">
  
          <p style="color: black; margin-left: 3%; font-weight: bold;">생년월일</p>
  
          <div class="input-group mb-3">
  
              <input type="text" name="birthday" class="form-control" placeholder="YYYY-MM-DD" style="border:none;" v-model="생년월일">
  
                    
  
          </div>
  
          <hr>
  
      </div>
  
  
  
  
      <div style="text-align: left; margin-top: 10%;">
  
          <p style="color: black; margin-left: 3%; font-weight: bold;">키</p>
  
          <div class="input-group mb-3">
  
              <input type="text" name="height" class="form-control" placeholder="cm" style="border:none;" v-model="키">
  
                  
  
          </div>
  
          <hr>
  
      </div>
  
  
  
  
      <div style="text-align: left; margin-top: 10%;">
  
          <p style="color: black; margin-left: 3%; font-weight: bold;">몸무게</p>
  
          <div class="input-group mb-3">
  
              <input type="text" name="weight" class="form-control" placeholder="kg" style="border:none;" v-model="몸무게">
  
          </div>
  
          <hr>
  
      </div>
  
  
  
  
      <div style="text-align: left; margin-top: 10%;">
  
          <p style="color: black; margin-left: 3%; font-weight: bold;">성별</p>
  
          <div class="input-group mb-3">
  
              <input type="text" name="gender" class="form-control" placeholder="남녀" style="border:none;" v-model="성별">
  
          </div>
  
      </div>
  
      <button type="submit">
  
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
  
              <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
  
              <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
  
          </svg>
  
          <span>저장</span>
  
      </button>
  
  
  
  
            </div>
  
          </div>
  
        </div>
  
  
  
  
  
  
      </div>
  
  </template>
  
  
  
  
  <script>
  
  import { useUserInfo } from '../../stores';
  
  import axios from 'axios'
  
  import {ref} from 'vue'
  
  import Cookies from 'js-cookie';
  
  
  
  
    export default {
  
      data () {
  
        const 닉네임 = ref('')
  
        const 생년월일 = ref('')
  
        const 키 = ref('')
  
        const 몸무게 = ref('')
  
        const 성별 = ref('')
  
        const userInfo = useUserInfo()
  
        const csrf_token = Cookies.get('csrftoken');
  
  
  
  
      const myupdate_post = () => {
  
        axios
  
        .post(`/api/account/myupdate/${userInfo.memberId}`, {
  
          nickname: 닉네임.value,
  
          birthday: 생년월일.value,
  
          height: 키.value,
  
          weight: 몸무게.value,
  
          gender: 성별.value,
  
  
        },
  
        {
  
        headers: {
  
          "X-CSRFToken": csrf_token, // 토큰 추가
  
          "Content-Type": "application/json", // Content-Type 추가
  
        },
  
      })
  
      return {
  
        myupdate_post,
  
        csrf_token
  
      }
  
      }
  
      }
  
    }
  
  </script>
  
  
  
  
  <style>
  
  .container {
  
      width: 100%; /* 화면 너비에 꽉 차도록 설정 */
  
      height: 100%; /* 화면 높이에 꽉 차도록 설정 */
  
      display: block;
  
      margin-bottom: 10%;
  
    }
  
  
  
  
    .card-container {
  
      margin-top: 2%;
  
    }
  
  
  
  
    .name {
  
      width: 100%;
  
      height: 100%;
  
      margin-top: 50%;
  
      
  
    }
  
  
  
  
  </style> myupdatePage.vue 