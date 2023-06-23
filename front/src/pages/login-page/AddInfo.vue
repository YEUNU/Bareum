<template>
    <div>
      로그인 이후 추가정보입력받기
    </div>
    <form @submit.prevent="submintAddInfo">
      <div>
        <label for="nickName">Nickname:</label>
        <input type="text" id="nickName" name="nickName" v-model="nickName" required/>
      </div>
      <div>
        <label for="birthDay">Birthday:</label>
        <input type="date" id="birthDay" name="birthDay" v-model="birthDay" required/>
      </div>
      <div>
        <label for="height">Height:</label>
        <input type="number" id="height" name="height" v-model="height" required/>
      </div>
      <div>
        <label for="weight">Weight:</label>
        <input type="number" id="weight" name="weight" pattern="\d*" v-model="weight" required/>
      </div>
      <div>
        <label for="gender">Gender:</label>
        <input type="radio" id="male" name="gender" value="male" v-model="gender" required/>
        <label for="male">남자</label>
        <input type="radio" id="female" name="gender" value="female" v-model="gender" required/>
        <label for="female">여자</label>
      </div>
      <button>저장</button>
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
  