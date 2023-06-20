<template lang="">

    <div class="navbar fixed-top bg-theme">
        <div class="box_search">
            <router-link to="/search"><SearchBar class="box_search_input" background-color="#FFFFFF" :placeholder="searchPlaceholder"></SearchBar></router-link>
        </div>
        
        <button class="box_alerts" @click="router.push({path: '/alerts'});">
            <img class="alerts_icon" src="\src\assets\bell.png"/>
        </button>
    </div>

    <div class="menu_container">
        <router-link to="/ranking" class="item menus" style="box-shadow: 4px 4px 4px 4px #eeeeee">제품</router-link>
        <router-link to="/recommend" class="item menus" style="box-shadow: 4px 4px 4px 4px #eeeeee">추천</router-link>
        <router-link to="/set_alarm" class="item menus" style="box-shadow: 4px 4px 4px 4px #eeeeee">알람설정</router-link>
        <router-link to="/regular_delivery" class="item menus" style="box-shadow: 4px 4px 4px 4px #eeeeee">정기배송신청</router-link>
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
    return {
      store,
      router,
      searchPlaceholder,
    };
  },
  methods: {
    openCamera() {
      this.showMenu = false;
      this.$refs.fileInput.setAttribute("capture", "camera");
      this.$refs.fileInput.click();
    },
    openGallery() {
      this.showMenu = false;
      this.$refs.fileInput.removeAttribute("capture");
      this.$refs.fileInput.click();
    },
    onFileSelected(event) {
      const selectedFile = event.target.files[0];

      // 선택한 파일에 대한 로직
      const reader = new FileReader();

      reader.onload = (e) => {
        const img = new Image();
        img.src = e.target.result;
      };

      reader.readAsDataURL(selectedFile);
    },
  },
};

</script>
<style>
.bg-theme {
    background-color: #2dce89;
}

.box_search {
    margin: 20px;
    flex-grow: 1;
}

.box_search_input {
    height: 8vh;
}

.box_alerts {
    border: 0;
    padding: 0;
    max-width: 85px;
    max-height: 85px;
    width: 12vw;
    height: 12vw;
    background-color: rgba(255,255,255,0);
    z-index: 1;
}

.alerts_icon {
    border: 0;
    padding: 0;
    width: 100%;
    height: 100%;
}

.menu_container {
    margin-top: 10vh;
    margin-bottom: 62px;
    position: static;
    display: grid;
    grid-template-columns: 40vw 40vw;
    grid-template-rows: 21vh 21vh 21vh;

    justify-content: center;
    align-items: center;

}

.item:nth-child(5) {
	grid-column: 1 / 3;
	grid-row: 3 / 4;
}

.menus {
    margin: 2vw;
    position: relative;
    
    justify-content: center;
    align-items: center;
    
    line-height: min(25vw, 15vh);
    font-family: "paybooc-Light", sans-serif;
    color: #6e6e6e;
    font-size: 1.2em;
    text-decoration: none;
    font-weight: 750;
    transition: 0.25s;

    border: 2px solid #2dce89;
    border-radius: 5px;
}
.menus:hover {
    background-color: #2dce89;
    color: #d4dfe6;
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
