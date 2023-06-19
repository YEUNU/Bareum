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
        <router-link to="/ranking" class="item menus">제품</router-link>
        <router-link to="/recommend" class="item menus">추천</router-link>
        <router-link to="/set_alarm" class="item menus">알람설정</router-link>
        <router-link to="/regular_delivery" class="item menus">정기배송신청</router-link>
        <button type="button" class="item menus" style="margin-top: 10%;" data-bs-toggle="modal" data-bs-target="#homeModal">영양제 촬영하기</button>
    </div>


    <div class="modal fade" id="homeModal" tabindex="-1" aria-labelledby="homeModalLabel" aria-hidden="true">

            <div class="modal-dialog" style="margin-top: 95%; margin-bottom: 20%;">

                <div class="modal-content" style="width:80%; margin-left: 10%; margin-right: 2%;">            
                    <div class="modal-header">
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>

                    <div class="modal-body">
                    <h5 style="text-align: center;">촬영 가이드 확인</h5>
                    <router-link to="/cameraguide"><button class="yesbutton" data-bs-dismiss="modal" aria-label="Close" style="width: 100%; margin-top: 10%;" @click="closeModal()">네</button></router-link>
                    <button style="width: 100%;">그만 보겠습니다.</button>
                    </div>

                </div>
            </div>
        
            <div class="modal-dialog">
            
                <div class="modal-content" style="width:105%; margin-left: -2%; margin-right: 2%;">

                            <div class="modal-body">
                            <button class="addcamera" @click="openCamera">
                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-camera" viewBox="0 0 16 16">
                            <path d="M15 12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1.172a3 3 0 0 0 2.12-.879l.83-.828A1 1 0 0 1 6.827 3h2.344a1 1 0 0 1 .707.293l.828.828A3 3 0 0 0 12.828 5H14a1 1 0 0 1 1 1v6zM2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4H2z"/>
                            <path d="M8 11a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5zm0 1a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM3 6.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0z"/>
                            </svg>
                            카메라 촬영</button>
                            </div>

                            <div class="modal-body">
                            <button class="addcamera" @click="openGallery">
                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-images" viewBox="0 0 16 16">
                            <path d="M4.502 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/>
                            <path d="M14.002 13a2 2 0 0 1-2 2h-10a2 2 0 0 1-2-2V5A2 2 0 0 1 2 3a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-1.998 2zM14 2H4a1 1 0 0 0-1 1h9.002a2 2 0 0 1 2 2v7A1 1 0 0 0 15 11V3a1 1 0 0 0-1-1zM2.002 4a1 1 0 0 0-1 1v8l2.646-2.354a.5.5 0 0 1 .63-.062l2.66 1.773 3.71-3.71a.5.5 0 0 1 .577-.094l1.777 1.947V5a1 1 0 0 0-1-1h-10z"/>
                            </svg>
                            사진 앨범에서 선택</button>
                            </div>

                </div>
            </div>

    </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from "vue-router";
import { useStore } from '../../stores';
import SearchBar from '../../components/Navbar/SearchBar.vue';

export default {
    name:"HomePage",
    components: {
        SearchBar
    },
    setup() {
        const store = useStore();
        const router = useRouter();
        const searchPlaceholder = ref('건강기능식품을 검색해보세요');
        return {
            store,
            router,
            searchPlaceholder,
        };
    },
    methods: {
        openCamera() {
        this.showMenu = false;
        this.getImage(true);
        },
        openGallery() {
        this.showMenu = false;
        this.getImage(false);
        },
        getImage(camera) {
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = 'image/*';
        if (camera) {
        input.capture = 'camera';
        }

        input.onchange = (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();

        reader.onload = (e) => {
            const img = new Image();
            img.src = e.target.result;
        };

        reader.readAsDataURL(file);
        };

        input.click();
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
