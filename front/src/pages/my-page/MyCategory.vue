<template >
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
        <div style="margin-right: 2vh;">건강 관심항목 관리</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill"
            viewBox="0 0 16 16">
            <path
              d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
          </svg>
        </div>
      </div>
    </nav>
    <div class="bg-white" style="display: flex;  padding-top: 50px; flex-direction: column;">
        <h2>건강 관심항목 수정</h2>
        <p>최대 3개</p>
        <div class="search_option_items"
            style="overflow-y: auto; max-height: 50%; margin-top: 5%; display: flex; flex-direction: row; flex-wrap: wrap; justify-content:center; align-items:center;">
            <div class="search_option_item_container" style="margin-bottom: 10px; margin-right: 10px;" v-for="part in parts"
                :key="part.id">
                <div class="search_option_item">
                    <input type="checkbox" :id="part.id" :value="part.text" v-model="part.checked"  :disabled="part.disabled">
                    <label :for="part.id">{{ part.text }}</label>
                </div>
            </div>
        </div>

        <button class="roundbox" style="margin-top: 3vh;" @click="sendCheckedItems()"
    :class="{disabled: selectList.length==0}" :disabled="selectList.length==0">저장</button>

    </div>

    </div>
</template>
<script>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { ref, computed,watchEffect,onMounted  } from 'vue';
import Cookies from 'js-cookie';
export default {
    setup(){
        const csrf_token = Cookies.get('csrftoken');
        const router = useRouter();

        const personalize_parts = ref([
            { id: 1, text: '혈중 콜레스테롤', checked: false },
            { id: 2, text: '눈 건강', checked: false },
            { id: 3, text: '피로감', checked: false },
            { id: 4, text: '장 건강', checked: false },
            { id: 5, text: '간 건강', checked: false },
            { id: 6, text: '피부 건강', checked: false },
            { id: 7, text: '빈혈', checked: false },
            { id: 8, text: '노화 & 항산화', checked: false },
            { id: 9, text: '혈관 & 혈액순환', checked: false },
            { id: 10, text: '혈압', checked: false },
            { id: 11, text: '혈당', checked: false },
            { id: 12, text: '뼈 건강', checked: false },
            { id: 13, text: '두뇌활동', checked: false },
            { id: 14, text: '체지방', checked: false },
            { id: 15, text: '탈모 & 손톱건강', checked: false },
            { id: 16, text: '면역 기능', checked: false },
            { id: 17, text: '관절 건강', checked: false },
            { id: 18, text: '남성 건강', checked: false },
            { id: 19, text: '여성 갱년기', checked: false },
            { id: 20, text: '혈중 중성지방', checked: false },
            { id: 21, text: '임산부 & 태아건강', checked: false },
            { id: 22, text: '호흡기 건강', checked: false },
            { id: 23, text: '스트레스 & 수면', checked: false },
            { id: 24, text: '소화 & 위식도 건강', checked: false },
            { id: 25, text: '운동 능력 & 근육량', checked: false },
            { id: 26, text: '갑산성 건강', checked: false },
            { id: 27, text: '치아 & 잇몸', checked: false },
            { id: 28, text: '여성 건강', checked: false }
        ]);
        const parts = computed(() => {
            return personalize_parts.value
        });


        const selectList = computed(() => {
            return parts.value.filter((f) => f.checked).map(x => x.text);
        });

        const sendCheckedItems = async() => {
            try{
                await axios.put('/api/account/interest/',{
                    interest:selectList.value
                },{
                    headers:{
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrf_token,
                    }
                })
                window.alert('수정되었습니다.');
                router.push('/mypage');

            }catch(err){
                console.error(err);
            }

        };

        const getUserInterest = async() => {
          try{
            const response = await axios.get('/api/account/interest/');
            const tempList = response.data.interest;

            personalize_parts.value.forEach((part) => {
              part.checked = tempList.includes(part.text);
            });
          }catch(err){
            console.error(err);
          }
        }

        onMounted(() => {
          getUserInterest()
        })
        
        watchEffect(() => {
            const maxSelections = 3;

            if (selectList.value.length >= maxSelections) {
                parts.value.forEach((part) => {
                    if (!part.checked) {
                        part.disabled = true;
                    }
                });
            } else {
                parts.value.forEach((part) => {
                    part.disabled = false;
                });
            }
        });

        return{
            selectList,
            parts,
            personalize_parts,
            sendCheckedItems,
            getUserInterest
        }
    }
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

.select_option_box {
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.search_option_items {
    align-self: center;
    display: grid;
    grid-template-columns: min(24vw, 22vh) min(24vw, 22vh) min(24vw, 22vh);
    grid-template-rows: min(24vw, 22vh) min(24vw, 22vh) min(24vw, 22vh);
}

.search_option_item {
    position: relative;
    align-self: center;
    justify-self: center;
    width: min(23vw, 20vh);
    height: min(23vw, 20vh);
}

.option_kind input[type="radio"] {
    display: none;
}

.option_kind input[type="radio"]+span {
    display: inline-block;
    padding: 15px 10px;
    border: 2px solid #2dce89;
    background-color: white;
    text-align: center;
    cursor: pointer;
    color: #6e6e6e;
    font-size: 1.1em;
    text-decoration: none;
    font-weight: 750;
}

.option_kind input[type="radio"]:checked+span {
    background-color: #2dce89;
    color: white;
}

.search_option_item input[type="checkbox"] {
    display: none;
}

.search_option_item input[type="checkbox"]+label {
    display: flex;
    width: min(22vw, 20vh);
    height: min(22vw, 20vh);
    position: relative;
    box-sizing: content-box;
    border-radius: 5pt;
    border: 2px solid #2dce89;
    background-color: white;
    text-align: center;
    justify-content: center;
    align-items: center;
    color: #6e6e6e;
    font-size: 1.1em;
    text-decoration: none;
    font-weight: 750;
}

.roundbox.disabled {
        background-color: #A9A9A9;
        color: #fff;
    }


.search_option_item input[type="checkbox"]:checked+label {
    background-color: #2dce89;
    color: white;
}
</style>