<template lang="">
    <div class="navbar fixed-top bg-theme" style="padding: 10px 5vw;">
        <div class="box_search">
            <router-link to="/search"><SearchBar background-color="#FFFFFF" :placeholder="searchPlaceholder"></SearchBar></router-link>
        </div>
        
        <button class="box_alarm" @click="router.push({path: '/receivealarm'});">
            <img class="alarm_icon" src="../../assets/received_alarm.png" alt="">
        </button>
    </div>
    <div class="background bg-theme" style="padding-top: 63px; padding-bottom: 60px;">
        <div class="bg-whitesmoke"
        style="border-top-left-radius: 10px; border-top-right-radius: 10px; min-height: calc(100vh - 123px);">
        <div class="menu_container">
            <router-link to="/taking" class="item menus" style="grid-row: 1 / 2; grid-column: 1 / 3">
                <div id="menu_comment">현재 나의</div>
                <div id="menu_name">영양소 균형점수</div>
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <div id="home_chart">
                        <div style="width: min(75vw, 75vh); height: min(75vw, 75vh);"><canvas id="homeChart"></canvas></div>
                    </div>
                    <div style="display: flex; flex-direction: column; justify-content: space-around; align-items: start; flex-grow: 1; margin: 0 5vw">
                        <div style="font-size: 1.5rem; padding-bottom: 1rem;">
                            <span style="font-size: 1rem; font-weight: normal;">나의 종합 점수: </span> {{100 - Math.round(nutrientsArray.map((arr) => Math.abs(100 - arr.reduce((sum, item) => sum + item.value, 0))).reduce((a, b) => a + b, 0) / 6)}}점
                        </div>
                    </div>
                </div>
                <!--<div id="menu_icon"><img src="../../assets/taking.png" alt=""></div>-->
            </router-link>
            <router-link to="/ranking" class="item menus">
                <div id="menu_comment">많은 사람들이 구매한</div>
                <div id="menu_name">바름랭킹</div>
                <div id="menu_icon"><img height="" src="../../assets/product.png" alt=""></div>
            </router-link>
            <router-link to="/recommend" class="item menus">
                <div id="menu_comment">당신을 위한 맞춤</div>
                <div id="menu_name">추천</div>
                <div id="menu_icon"><img src="../../assets/recommand.png" alt=""></div>
            </router-link>
            <router-link to="/alarm" class="item menus">
                <div id="menu_comment">규칙적인 나만의 비서</div>
                <div id="menu_name">알림설정</div>
                <div id="menu_icon"><img src="../../assets/alarm.png" alt=""></div>
            </router-link>
            <router-link to="/regulardelivery" class="item menus">
                <div id="menu_comment">내가 까먹어도 기사님은 안까먹는</div>
                <div id="menu_name">정기배송신청</div>
                <div id="menu_icon"><img src="../../assets/delivery.png" alt=""></div>
            </router-link>
            <div data-bs-toggle="modal" data-bs-target="#cameraModal" class="item menus" style="grid-column: 1 / 3">
                <div id="menu_comment">성능이 상당한</div>
                <div id="menu_name">건강기능식품 글자 인식</div>
                <div id="menu_icon"><img src="../../assets/camera.png" alt=""></div>
            </div>
        </div>
    </div>
</div>

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
import { ref, computed, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import { useStore, useUserInfo } from "../../stores";
import SearchBar from "../../components/Navbar/SearchBar.vue";
import axios from 'axios';
import Chart from 'chart.js/auto';
import Cookies from 'js-cookie';

export default {
    name: "HomePage",
    components: {
        SearchBar,
    },
    setup(_, { root }) {
        const store = useStore();
        const router = useRouter();
        const searchPlaceholder = ref("건강기능식품을 검색해보세요");
        const fileInput = ref(null);
        const showMenu = ref(false);
        const userInfo = useUserInfo();
        const loginId = computed(() => userInfo.loginId);
        const nutraceuticals = ref([]);
        const csrf_token = Cookies.get("csrftoken");
        const nutrientsArray = ref([]);
        const displayGuideModal = ref(false);
        const guideModalSeen = ref(false);
        const firstTime = ref(true);

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

        const take_nutrace = async () => {
            try {
                const response = await axios.post("/api/taking/regist", {
                    headers: { "Content-Type": "application/json", "X-CSRFToken": csrf_token },
                    loginId: loginId.value,
                });
                nutraceuticals.value = response.data.take;
            } catch (error) {
                console.log("Error fetching user nutraceuticals:", error);
            }
        };

        async function getUserProductsData() {
            try {
                const response = await axios.get("/api/taking/", {
                    params: {
                        user_id: loginId.value,
                    },
                });
                const user_products_data = response.data.a;
                return user_products_data;
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        }

        onMounted(async () => {
            take_nutrace();
            const productsData = await getUserProductsData();
            const maxValues = [100, 100, 100, 100, 100, 100];

            nutrientsArray.value = productsData.reduce(
                (result, product) => {
                const nutrients = Object.keys(product)
                    .slice(1)
                    .map((nutrient, index) => {
                        return [
                            ...result[index],
                            {
                                product: product.제품명,
                                value: product[nutrient] / maxValues[index] * 100,
                            },
                        ];
                    });

                return nutrients;
                },
                Array.from({ length: 6 }, () => [])
            );

            const ctx = document.getElementById('homeChart').getContext('2d');
            var ns = nutrientsArray.value.map((arr) => arr.reduce((sum, item) => sum + item.value, 0));
            const overlow = [];
            const upper_limit = [2000 / 1, 100 / 0.2, 3000 / 7, 2500 / 7, 350 / 3.15, 35 / 0.085];
            const lower_limit = [75 / 1, 0, 500 / 7, 600 / 7, 250 / 3.15, 7 / 0.085];

            for (let index = 0; index < ns.length; index++) {
                if(upper_limit[index] < ns[index]) {
                    overlow[index] = 'over'
                }
                else if(lower_limit[index] > ns[index]) {
                    overlow[index] = 'low'
                }
                else {
                    overlow[index] = 'good'
                }
            };
            const OLcolorMapping = {
                'good': ['rgba(45, 206, 137, 0.5)', 'rgba(45, 206, 137, 0.25)'],
                'over': ['rgba(245, 5, 0, 0.5)', 'rgba(245, 5, 0, 0.25)'],
                'low': ['rgba(255, 204, 33, 0.5)', 'rgba(255, 204, 33, 0.25)'],
            }

            const homeChart = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['비타민C', '비타민D', '비타민A', '칼슘', '마그네슘', '아연'],
                    datasets: [
                    {
                            label: ['my nutrients'],
                            data: nutrientsArray.value.map((arr) => Math.min(150, arr.reduce((sum, item) => sum + item.value, 0))),
                            backgroundColor: overlow.map((ol) => OLcolorMapping[ol][1]),
                            borderColor: overlow.map((ol) => OLcolorMapping[ol][0]),
                            borderWidth: 1,
                        },
                        {
                            label: ['recommend nutrients'],
                            data: maxValues,
                            backgroundColor: 'rgba(150, 150, 150, 0.1)',
                            borderColor: 'rgba(150, 150, 150, 0)',
                            borderWidth: 1,
                        },
                    ],
                },
                options: {
                    responsive: true,
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function (context) {
                                const productData = nutrientsArray.value[context.dataIndex];
                                return productData
                                    .map((product) => product.value > 0? product.product + ": " + product.value.toFixed(1) + "%" : "")
                                    .filter((element) => element !== "");
                                },
                            },
                        },
                        legend: {
                            display: false,
                        },
                    },
                    scales: {
                        r: {
                            startAngle: 30,
                            min: 0,
                            max: 150,
                            grid: {
                                circular: true,
                            },
                            pointLabels: {
                                display: true,
                            },
                            ticks: {
                                display: false,
                                stepSize: 50,
                            }
                        },
                    },
                },
            });
        });
        
        return {
            store,
            router,
            searchPlaceholder,
            fileInput,
            nutraceuticals,
            nutrientsArray,
            openGallery,
            onFileSelected,
            disableModal,
            displayGuideModal,
            guideModalSeen,
            firstTime,
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
    width: 100%;
    min-height: 100vh;
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

.box_alarm {
    border: 0;
    padding: 0;
    margin: 5px;
    background-color: rgba(255,255,255,0);
    z-index: 1;
}

.alarm_icon {
    border: 0;
    padding: 0;
    width: 30px;
    height: 30px;
}

.menu_container {
    display: grid;
    grid-template-columns: 48vw 48vw;
    padding: 2vh 0;
    justify-content: center;
    align-items: center;

}

.menus {
    position: relative;
    background-color: white;

    color: #6e6e6e;
    text-decoration: none;
    font-weight: 750;
    transition: 0.25s;

    border-radius: 8px;
    box-shadow: 0 0 3px 3px #eeeeee;

    flex-direction: column;
    display: flex;
    justify-content: space-evenly;
    margin: min(2vw, 2vh);
}

#menu_comment {
    align-self: start;
    padding: 0.5vh 0 0 0.5vh;
    color: gray;
    font-size: 0.6em;
}

#menu_name {
    align-self: start;
    padding: 0.2vh 0 0 0.5vh;
    color: black;
    font-size: 1.2em;
}

#home_chart {
    margin: 0 5vw;
}

#menu_icon {
    margin: 0 1vh 1vh 0;
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
