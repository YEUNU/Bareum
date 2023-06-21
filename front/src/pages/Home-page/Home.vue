<template lang="">

    <div class="navbar fixed-top bg-theme" style="padding: 10px 5vw;">
        <div class="box_search">
            <router-link to="/search"><SearchBar background-color="#FFFFFF" :placeholder="searchPlaceholder"></SearchBar></router-link>
        </div>
        
        <button class="box_alerts" @click="router.push({path: '/alerts'});">
            <img class="alerts_icon" src="../../assets/received_alarm.png" alt="">
        </button>
    </div>
    <div class="background bg-theme" style="padding-top: 63px; padding-bottom: 60px;">
        <div class="bg-whitesmoke"
             style="border-top-left-radius: 10px; border-top-right-radius: 10px; min-height: 100%">
            <div class="menu_container">
                <router-link to="/ranking" class="item menus">
                <div id="menu_comment">많은 사람들이 구매한</div>
                <div id="menu_name">제품</div>
                <div id="menu_icon"><img height="" src="../../assets/product.png" alt=""></div>
            </router-link>
            <router-link to="/recommend" class="item menus">
                <div id="menu_comment">당신을 위한 맞춤</div>
                <div id="menu_name">추천</div>
                <div id="menu_icon"><img src="../../assets/recommand.png" alt=""></div>
            </router-link>
            <router-link to="/set_alarm" class="item menus">
                <div id="menu_comment">규칙적인 나만의 비서</div>
                <div id="menu_name">알림설정</div>
                <div id="menu_icon"><img src="../../assets/alarm.png" alt=""></div>
            </router-link>
            <router-link to="/regular_delivery" class="item menus">
                <div id="menu_comment">내가 까먹어도 기사님은 안까먹는</div>
                <div id="menu_name">정기배송신청</div>
                <div id="menu_icon"><img src="../../assets/delivery.png" alt=""></div>
            </router-link>
        </div>
    </div>
</div>

</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "../../stores";
import SearchBar from "../../components/Navbar/SearchBar.vue";

export default {
  name: "HomePage",
  components: {
    SearchBar,
  },
  setup() {
    const store = useStore();
    const router = useRouter();
    const searchPlaceholder = ref("건강기능식품을 검색해보세요");
    const fileInput = ref(null);
    const showMenu = ref(false);

    const openGallery = () => {
      showMenu.value = false;
      fileInput.value.removeAttribute("capture");
      fileInput.value.click();
    };

    const onFileSelected = (event) => {
      const selectedFile = event.target.files[0];

      // 선택한 파일에 대한 로직
      const reader = new FileReader();

      reader.onload = (e) => {
        const img = new Image();
        img.src = e.target.result;
      };

      reader.readAsDataURL(selectedFile);
    };

    return {
      store,
      router,
      searchPlaceholder,
      fileInput,
      openGallery,
      onFileSelected,
    };
  },
};

</script>
<style>

video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.background {
    position: absolute;
    left: 0;
    top: 0;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    /*
    display: flex;
    flex-direction: column;
    justify-content: center;
    */
}

.bg-theme {
    background-color: #2dce89;
}

.bg-whitesmoke {
    background-color: whitesmoke;
}

.box_search {
    margin-right: 10px;
    flex-grow: 1;
}

.box_alerts {
    border: 0;
    padding: 0;
    margin: 5px;
    background-color: rgba(255,255,255,0);
    z-index: 1;
}

.alerts_icon {
    border: 0;
    padding: 0;
    width: 30px;
    height: 30px;
}

.menu_container {

    position: static;
    display: grid;
    grid-template-columns: 45vw 45vw;
    grid-template-rows: 50% 50%;
    padding: 4% 5%;
    justify-content: center;
    align-items: center;

}

.menus {
    position: relative;
    background-color: white;

    color: #6e6e6e;
    font-size: 1.2em;
    text-decoration: none;
    font-weight: 750;
    transition: 0.25s;

    border: 2px solid #2dce89;
    border-radius: 8px;
    box-shadow: 0 0 2px 2px #EAEAEA;

    flex-direction: column;
    display: flex;
    justify-content: space-evenly;
    margin: 1vw;
}

#menu_comment {
    align-self: start;
    padding: 2.5% 0 0 2.5%;
    color: gray;
    font-size: min(1.7vw, 1.7vh);
}

#menu_name {
    align-self: start;
    padding: 0.5% 0 0 2.5%;
    color: black;
    font-size: min(5vw, 5vh);
}

#menu_icon {
    margin: 0 5% 5% 0;
    align-self: end;
}

#menu_icon img {
    height: min(15vw, 15vh);
}

.roundbox {
    width: 100%;
    border-radius: 10px;
    border: none;
    background-color: #2dce89;
    color: white;
    font-size: 1.1em;
    text-decoration: none;
    font-weight: 750;
}
.modal-container {
  position: relative;
  height: 100vh;
}

.modal {
  position: absolute;
  bottom: 0;
}
.modal-body {
    width:100%;
    text-align:left;
    border-bottom: 1px solid #CCCCCC;
}

.yesbutton {
    border-radius: 10px;
    border: none;
    background-color: #2dce89;
    color: white;
    font-size: 15px;
}
/* .alret-box{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
    border-radius: 8px;
    height: 80px;
    padding: 20px;
    box-sizing: border-box;
}
.alret-box p {
    margin: 0;
    font-size: 20px;
    color: #fff;
} */
</style>
