<template>
<div class="mywishcontainer">
    <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
            <router-link to="/mypage" class="navbar-brand" style="margin-left: 2vh;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                </svg>
            </router-link>
            <div style="margin-right: 2vh;">찜 목록</div>
            <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
                    <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
                </svg>
            </div>
        </div>
    </nav>

    <div v-show="tmp1" class="mycard-container">
        <div class="card" style="width: 100%; padding:0; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
            <div class="card-body">
                <div class="d-flex align-items-center mb-4">
                    <div @click="foo(1)" style="position: absolute; top: 0; right: 10px; font-size: 1.5em; color: #FFCC21;">★</div>
                    <div class="flex-shrink-0">
                        <img src="https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcR3h8B7MrzEI3wg-A8_FArF5oQlBGzRrtr8F-PN-MI41_LsiInYYB7_JkFxbrY1XTGGcbbI-W8Or2ymn4cXLM2wS3xW_Y3Ii0EJ4lPnniZSeHyZ2OahUqGrBCix8Ki3IoQw_A&usqp=CAc"
                            alt=""
                            style="height: min(25vh, 25vw); width: min(25vh, 25vw);">
                    </div>
                    <div class="flex-grow-1 ms-3">
                        <div class="d-flex flex-row align-items-center mb-2">
                            <h4 class="mb-0 me-2" style="text-align: left; font-weight: bold;">닥터린 덴마크 락토지지 유산균</h4>
                        </div>
                        <div>
                            <p class="mb-0 me-2" style="text-align: left; margin-top: 10%;">58000원</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div v-show="tmp2" class="mycard-container">
        <div class="card" style="width: 100%; padding:0; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
            <div class="card-body">
                <div class="d-flex align-items-center mb-4">
                    <div @click="foo(2)" style="position: absolute; top: 0; right: 10px; font-size: 1.5em; color: #FFCC21;">★</div>

                    <div class="flex-shrink-0">
                        <img src="https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSdLUrGJYVpSCoxC9SENnc6gk3vtdt1ppZD-2Wt4fIM24LCmmlJwTAoCcC7csepDE6qnzrEShb_Ipbd_EimvyvPfWz9K0FlIDlY-dNvjw5mMkZ7rRySeHtdnKtvzs6QeTccag&usqp=CAc"
                            alt=""
                            style="height: min(25vh, 25vw); width: min(25vh, 25vw);">
                    </div>
                    <div class="flex-grow-1 ms-3">
                        <div class="d-flex flex-row align-items-center mb-2">
                            <h4 class="mb-0 me-2" style="text-align: left; font-weight: bold;">닥터린 비타민C</h4>
                        </div>
                        <div>
                            <p class="mb-0 me-2" style="text-align: left; margin-top: 10%;">48000원</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>
</template>
  
<script>
import {ref} from 'vue'

export default {
    setup() {
        var tmp1 = ref(true);
        var tmp2 = ref(true);

        const foo = (tmp) => {

            if(confirm('찜 목록에서 삭제하시겠습니까?')) {
                
                if(tmp == 1){
                    tmp1.value = !tmp1.value;
                }
                else if(tmp == 2) {
                    tmp2.value = !tmp2.value
                }
            }
        }

        return {
            tmp1,
            tmp2,
            foo,
        }
    }
}
</script>

<style>

.mywishcontainer {
    width: 100%; /* 화면 너비에 꽉 차도록 설정 */
    height: 100%; /* 화면 높이에 꽉 차도록 설정 */
    display: block;
    margin-bottom: 10%;
    padding-bottom: 80%;
}

.card {
    margin-top: 10%;
}

</style>