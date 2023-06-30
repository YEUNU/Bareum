<template>
  <div class="mycontainer">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <router-link to="/mypage" class="navbar-brand" style="margin-left: 2vh;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left"
            viewBox="0 0 16 16">
            <path fill-rule="evenodd"
              d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
          </svg>
        </router-link>
        <div style="margin-right: 2vh;">개인 정보 수정</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill"
            viewBox="0 0 16 16">
            <path
              d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
          </svg>
        </div>
      </div>
    </nav>

    <div class="mycard-container">
      <div class="card" style="width: 100%; padding:0; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
        <div class="card-body">

          <form @submit.prevent="updateProfile">
            <div style="display: flex; flex-direction: column; align-items: center;">
              <div>
                <img :src="profileImg" alt="Profile image" class="img-fluid rounded-circle border border-dark border-3"
                  style="width: 100px;">
              </div>
              <div style="margin-top: 5%;">
                <input id="images" ref="imageInput" type="file" accept="image/*" @change="previewImages"
                  style="display: none;" />
                <label for="images" style="cursor: pointer;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor"
                    class="bi bi-camera-fill" viewBox="0 0 16 16">
                    <path d="M10.5 8.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z" />
                    <path
                      d="M2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4H2zm.5 2a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1zm9 2.5a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0z" />
                  </svg>
                </label>
              </div>
            </div>

            <div style="text-align: left; margin-top: 10%;">
              <p style="color: black; margin-left: 3%; font-weight: bold;">닉네임</p>
              <div class="input-group mb-3">
                <input type="text" name="nickname" class="form-control" placeholder="닉네임" style="border:none;"
                  v-model="닉네임">
              </div>
              <hr>
            </div>
            <div style="text-align: left; margin-top: 10%;">
              <p style="color: black; margin-left: 3%; font-weight: bold;">생년월일</p>
              <div class="input-group mb-3">
                <input type="date" name="birthday" class="form-control" style="border:none;" v-model="생년월일">

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
              <div class="input-group mb-3" style="margin-left: 3%;">
                <label for="male">남자</label>
                <input type="radio" id="male" name="gender" value="male" v-model="성별" style="margin-left: 3%;">
                <label for="female" style="margin-left: 3%;">여자</label>
                <input type="radio" id="female" name="gender" value="female" v-model="성별" style="margin-left: 3%;">
              </div>
              <hr>
            </div>
            <button type="submit"
              style="width:100%; margin-bottom: 50%; background-color: #2dce89; border-radius: 5px; color:white; box-shadow: 2px 2px 2px 2px #eeeeee">
              저장
            </button>

          </form>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { ref } from 'vue';
import { useUserInfo } from '../../stores';
import { onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import Cookies from 'js-cookie';
export default {
  setup() {
    const imageInput = ref(null);
    const userInfo = useUserInfo();
    const profileImg = ref("")
    const router = useRouter();
    const csrf_token = Cookies.get('csrftoken');
    const 닉네임 = ref('')
    const 생년월일 = ref('')
    const 키 = ref('')
    const 몸무게 = ref('')
    const 성별 = ref('')

    const previewImages = async () => {
      console.log(imageInput.value.files[0]);
      const file = imageInput.value.files[0];
      profileImg.value = URL.createObjectURL(file);
    }

    const getUserAddInfo = (member_id) => {
      axios.get(`/api/account/addInfo/${member_id}/`)
        .then(response => {
          // 서버로부터 받은 데이터 처리
          const data = response.data;
          userInfo.userAddInfo(data.birthday, data.gender, data.nickname, data.weight, data.height);
        })
        .catch(error => {
          // 서버와의 통신 오류 처리
          console.error('Error:', error);
        });
    }

    const updateProfile = async () => {
      try {
        if (profileImg.value != userInfo.profileImgUrl) {
          const formData = new FormData();
          const newProfileImg = imageInput.value.files[0]
          formData.append("image", newProfileImg);
          userInfo.profileImgUrl = URL.createObjectURL(newProfileImg);
          await axios.post(`api/account/profile/img/${userInfo.memberId}`, formData, {
            headers: {
              "Content-Type": "multipart/form-data", // 폼 데이터 전송을 위해 수정
              "X-CSRFToken": csrf_token,
            }
          });
        }


        await axios.put(`/api/account/addInfo/${userInfo.memberId}/`, {
          nickname: 닉네임.value,
          birthday: 생년월일.value,
          height: 키.value,
          weight: 몸무게.value,
          gender: 성별.value
        }, {
          headers: {
            "X-CSRFToken": csrf_token,
            "Content-Type": "application/json",
          }
        })
        getUserAddInfo(userInfo.memberId);
        window.alert("수정되었습니다.");
        router.push('/mypage');
      } catch (error) {
        console.error(error);
      }


    }

    onMounted(() => {
      profileImg.value = userInfo.profileImgUrl;
      닉네임.value = userInfo.nickname;
      생년월일.value = userInfo.birthDay;
      키.value = userInfo.height;
      몸무게.value = userInfo.weight;
      성별.value = userInfo.gender;
    })

    return {
      profileImg,
      imageInput,
      userInfo,
      updateProfile,
      previewImages,
      닉네임,
      생년월일,
      키,
      몸무게,
      성별

    };
  },
  components: {}
}
</script>

<style>
.container {
  width: 100%;
  /* 화면 너비에 꽉 차도록 설정 */
  height: 100%;
  /* 화면 높이에 꽉 차도록 설정 */
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
</style>