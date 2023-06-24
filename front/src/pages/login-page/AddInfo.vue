<template>
    <div style="width: 100%; font-weight: bold; font-size:38px;">
      개인 정보 추가 입력
    </div>
    <form @submit.prevent="submintAddInfo">
      <div style="text-align: left; margin-top: 20%;">
        <p style="color: black; font-weight: bold;" >닉네임</p>
        <input type="text" id="nickName" name="nickName" placeholder="닉네임" v-model="nickName" required style="width:100%; border-radius: 6px; border: 2px solid #eeeeee;"/>
      </div>

      <div style="text-align: left; margin-top: 10%;">
        <p style="color: black; font-weight: bold;" >생년월일</p>
        <input type="date" id="birthDay" name="birthDay" v-model="birthDay" required style="width:100%; border-radius: 6px; border: 2px solid #eeeeee;"/>
      </div>

      <div style="text-align: left; margin-top: 10%;">
        <p style="color: black; font-weight: bold;" >키 (cm)</p>
        <input type="number" id="height" name="height" placeholder="cm"  v-model="height" required style="width:100%; border-radius: 6px; border: 2px solid #eeeeee;"/>
      </div>

      <div style="text-align: left; margin-top: 10%;">
        <p style="color: black; font-weight: bold;" >체중 (kg)</p>
        <input type="number" id="weight" name="weight" placeholder="kg"  pattern="\d*" v-model="weight" required style="width:100%; border-radius: 6px; border: 2px solid #eeeeee;"/>
      </div>

      <div style="text-align: left; margin-top: 10%;">
        <p style="color: black; font-weight: bold;" >성별</p>
        <input type="radio" id="male" name="gender" value="male" v-model="gender" required style="border-radius: 6px; border: 2px solid #eeeeee; margin-right: 2%;"/>
        <label for="male" style="margin-right: 5%;">남자</label>
        <input type="radio" id="female" name="gender" value="female" v-model="gender" required style="border-radius: 6px; border: 2px solid #eeeeee; margin-right: 2%;"/>
        <label for="female">여자</label>
      </div>

      <button style="width:50%; margin-top: 15%; background-color: #2dce89; border-radius: 5px; color:white; box-shadow: 2px 2px 2px 2px #eeeeee">저장</button>
    </form>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useUserInfo } from '../../stores';
import { useRouter } from "vue-router";
  import axios from 'axios';
  import Cookies from 'js-cookie';
  export default {
    setup() {
      const userInfo = useUserInfo();
      const csrf_token = Cookies.get('csrftoken');
        const router = useRouter();

        const nickName = ref('');
        const birthDay = ref('');
        const height = ref('');
        const weight = ref('');
        const gender = ref('');

      
      const submintAddInfo = async () => {
          try {
            if (!birthDay.value) {
                console.log(birthDay.value);
                window.alert("날짜형식이 잘못됨");
                return;
            }
        

          await axios.put(`/api/account/addInfo/${userInfo.memberId}/`, {
            nickname: nickName.value,
            birthday: birthDay.value,
            height: height.value,
            weight: weight.value,
            gender: gender.value
          },{
            headers:{
              "X-CSRFToken": csrf_token,
              "Content-Type": "application/json",
            }
          });
  
          userInfo.userAddInfo(birthDay.value, gender.value,nickName.value, weight.value, height.value);
          router.push("/");
        } catch (err) {
          console.error(err);
        }
      };
  
      return {
        nickName,
        birthDay,
        height,
        weight,
        gender,
        submintAddInfo,
        userInfo
      };
    },
  };
  </script>
  