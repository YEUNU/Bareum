<template lang="">
    <nav class="bottom-nav-bar">

        <ul>
            <li :class="{active: homepage}" style="align-self: flex-end;">
                <router-link to="/">
                    <span class="nav-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" v-if="homepage" width="30" height="30" fill="#2dce89" class="bi bi-house-door-fill" viewBox="0 0 16 16">
                            <path d="M6.5 14.5v-3.505c0-.245.25-.495.5-.495h2c.25 0 .5.25.5.5v3.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5Z"/>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" v-else width="30" height="30" fill="currentColor" class="bi bi-house-door" viewBox="0 0 16 16">
                            <path d="M8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.50000000000000000000000000000000 7.5v7a.5.5 0 0 0 .5.5h4.5a.5.5 0 0 0 .5-.5v-4h2v4a.5.5 0 0 0 .5.5H14a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146ZM2.5 14V7.707l5.5-5.5 5.5 5.5V14H10v-4a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5v4H2.5Z"/>
                        </svg>
                    </span>
                    <span :class="{'nav-text-active' : homepage, 'nav-text-inactive': !homepage }"></span>
                </router-link>
            </li>
            <li :class="{active: shop}" style="align-self: flex-end;">
                <router-link to="/shop">
                    <span class="nav-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" v-if="shop" width="30" height="30" fill="#2dce89" class="bi bi-cart-fill" viewBox="0 0 16 16">
                            <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" v-else width="30" height="30" fill="currentColor" class="bi bi-cart" viewBox="0 0 16 16" >
                            <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l1.313 7h8.17l1.313-7H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                        </svg>
                    </span>
                    <span :class="{'nav-text-active' : shop, 'nav-text-inactive': !shop }"></span>
                </router-link>
            </li>
            <li>
                <span class="nav-icon" data-bs-toggle="modal" data-bs-target="#cameraModal">
                    <img height="70" src="../../assets/camera.png" alt="">
                </span>
            </li>
            <li :class="{ active: community}" style="align-self: flex-end;">
                <router-link to="/community">
                    <span class="nav-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" v-if="community" width="30" height="30" fill="#2dce89" class="bi bi-chat-left-fill" viewBox="0 0 16 16">
                            <path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H4.414a1 1 0 0 0-.707.293L.854 15.146A.5.5 0 0 1 0 14.793V2zm3.5 1a.5.5 0 0 0 0 1h9a.5.5 0 0 0 0-1h-9zm0 2.5a.5.5 0 0 0 0 1h9a.5.5 0 0 0 0-1h-9zm0 2.5a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5z"/>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" v-else width="30" height="30" fill="currentColor" class="bi bi-chat-left" viewBox="0 0 16 16">
                            <path d="M14 1a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H4.414A2 2 0 0 0 3 11.586l-2 2V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12.793a.5.5 0 0 0 .854.353l2.853-2.853A1 1 0 0 1 4.414 12H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
                            <path d="M3 3.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 6a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 6zm0 2.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z"/>
                        </svg>
                    </span>
                    <span :class="{'nav-text-active' : community, 'nav-text-inactive': !community }"></span>
                </router-link>
            </li>
            <li :class="{ active: mypage}" style="align-self: flex-end;">
                <router-link to="/mypage">
                    <span class="nav-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" v-if="mypage" width="30" height="30" fill="#2dce89" class="bi bi-person-fill" viewBox="0 0 16 16">
                            <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3Zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"/>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" v-else width="30" height="30" fill="currentColor" class="bi bi-person" viewBox="0 0 16 16">
                            <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z"/>
                        </svg>
                    </span>
                    <span :class="{'nav-text-active' : mypage, 'nav-text-inactive': !mypage }"></span>
                </router-link>
            </li>
        </ul>
    </nav>


    <div class="modal fade" id="cameraModal" tabindex="-1" aria-labelledby="cameraModalLabel" aria-hidden="true">
        <video ref="cameraPreview" width="100%" height="100%" autoplay playsinline></video>
        <input
        type="file"
        accept="image/*"
        @change="onFileSelected"
        style="display: none"
        ref="fileInput"
        />
        <div v-if="firstTime" @close="disableModal">
        <div class="modal-dialog" style="position: fixed; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 90%; margin: 0;">
            <div class="modal-content" style="width: 80%; margin-left: 10%; margin-right: 2%;">            
                <div class="modal-header">
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>

                <div class="modal-body">
                    <h5 style="text-align: center;">촬영 가이드 확인</h5>
                    <router-link to="/cameraguide">
                        <button class="yesbutton" data-bs-dismiss="modal" aria-label="Close" style="width: 100%; margin-top: 10%;" @click="closeModal()">네</button>
                    </router-link>
                    <button style="width: 100%;"  @click="disableModal">그만 보겠습니다.</button>
                </div>
            </div>
        </div>   
    </div>
   

    <div class="modal-dialog" style="position: fixed; left: 50%; bottom: 0; transform: translate(-50%, 0); width: 90%; margin: 0;">

        <div class="modal-content" style="width:105%; margin-left: -2%; margin-right: 2%;">

            <div class="modal-body" style="text-align: right;"><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button></div>
            <div class="modal-body">
                <router-link to="/ocr/camera" class="router-link" >
                    <button class="addcamera" data-bs-dismiss="modal" aria-label="Close">
                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-camera" viewBox="0 0 16 16">
                            <path d="M15 12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1.172a3 3 0 0 0 2.12-.879l.83-.828A1 1 0 0 1 6.827 3h2.344a1 1 0 0 1 .707.293l.828.828A3 3 0 0 0 12.828 5H14a1 1 0 0 1 1 1v6zM2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4H2z"/>
                            <path d="M8 11a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5zm0 1a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM3 6.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0z"/>
                        </svg>
                        카메라 촬영
                    </button>
                </router-link>
            </div>
            <div class="modal-body">
                <button class="addcamera" @click="openGallery">
                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-images" viewBox="0 0 16 16">
                        <path d="M4.502 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/>
                        <path d="M14.002 13a2 2 0 0 1-2 2h-10a2 2 0 0 1-2-2V5A2 2 0 0 1 2 3a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-1.998 2zM14 2H4a1 1 0 0 0-1 1h9.002a2 2 0 0 1 2 2v7A1 1 0 0 0 15 11V3a1 1 0 0 0-1-1zM2.002 4a1 1 0 0 0-1 1v8l2.646-2.354a.5.5 0 0 1 .63-.062l2.66 1.773 3.71-3.71a.5.5 0 0 1 .577-.094l1.777 1.947V5a1 1 0 0 0-1-1h-10z"/>
                    </svg>
                    사진 앨범에서 선택
                </button>
            </div>

        </div>
    </div>
</div>
</template>

<script>
import { ref, computed, onMounted, reactive } from "vue";
import { useRouter } from "vue-router";

export default {
  setup() {
    const showMenu = ref(true);
    const displayGuideModal = ref(false);
    const guideModalSeen = ref(false);
    const firstTime = ref(true);
    const route = useRouter();
    const capturedImage = ref(null);

    const homepage = computed(() => route.currentRoute.value.path === "/");
    const shop = computed(() => route.currentRoute.value.path === "/shop");
    const community = computed(() => route.currentRoute.value.path === "/community");
    const mypage = computed(() => route.currentRoute.value.path === "/mypage");

    onMounted(() => {
      const savedValue = localStorage.getItem("guideModalSeen");
      if (savedValue !== null) {
        guideModalSeen.value = JSON.parse(savedValue);
      } else {
        guideModalSeen.value = false;
      }
      firstTime.value = !guideModalSeen.value;
    });

    const disableModal = () => {
      displayGuideModal.value = false;
      guideModalSeen.value = true;
      localStorage.setItem("guideModalSeen", JSON.stringify(guideModalSeen.value));
      firstTime.value = false;
    }

    const openCamera = () => {
      showMenu.value = false;
      getImage(true);
    }

    const openGallery = () => {
      showMenu.value = false;
      getImage(false);

    };

    const getImage = (camera) => {
        const input = document.createElement("input");
        input.type = "file";
        input.accept = "image/*";
        if (camera) {
            input.capture = "camera";
        }
        input.onchange = (e) => {
            const file = e.target.files[0];
            const reader = new FileReader();
            reader.onloadstart = () => {
            const cameraModalElement = document.getElementById("cameraModal");
            const cameraModal = bootstrap.Modal.getInstance(cameraModalElement);
            cameraModal.hide();
            };
            reader.onload = (e) => {
            capturedImage.value = e.target.result;

            // 이미지가 로드된 후에 이미지 데이터를 경로의 파라미터로 전달
            if (capturedImage.value) {
                route.push("/ocr/result/" + encodeURIComponent(capturedImage.value));
            }
            };
            reader.readAsDataURL(file);
        };
        input.click();
    };

    return {
      showMenu,
      displayGuideModal,
      guideModalSeen,
      firstTime,
      homepage,
      shop,
      community,
      mypage,
      disableModal,
      openCamera,
      openGallery,
    };
  },
};
</script>

<style scoped>
.bottom-nav-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-around;
  background-color: white;
  padding: 10px;
  box-sizing: border-box;
}
.bottom-nav-bar ul {
  display: flex;
  list-style: none;
  padding: 0;
  margin: -35px 0 5px 0;
  width: 100%;
}
.bottom-nav-bar li {
  flex: 1;
  text-align: center;
}
.bottom-nav-bar router-link {
  display: block;
  padding: 10px;
  text-decoration: none;
  color: #333;
}
@media (max-width: 600px) {
  .bottom-nav-bar li {
    font-size: 12px;
  }
}
.nav-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  color: gray
}
.nav-text {
  margin-top: 4px; /* 아이콘 위로 약간의 간격 추가 */
  color: gray;
}
.active-icon {
  fill: black; /* 활성화된 상태의 아이콘 색상 */
}
.active-text {
  color: black; /* 활성화된 텍스트 색상 */
}
.nav-text-active {
  color: rgb(000, 204, 051);
  font-weight: 10px;/* 활성화된 메뉴의 글자 색상을 변경 */
}
.nav-text-inactive {
  color: gray; /* 비활성화된 메뉴의 글자 색상 */
}
</style>