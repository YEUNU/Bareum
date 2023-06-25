<template>

<div class="pushcontainer">
    <nav class="navbar fixed-top bg-white" style="padding: 10px 0;">
        <div class="container-fluid">
            <span class="navbar-brand" @click="() => {$router.back(); searchbarClear();}" style="margin-right: 0px">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"></path>
                </svg>
            </span>
        </div>
    </nav>

<!--
    <div class="date_selector">
        <input type="date" name="date" id="date" :min="currentDate" :value="currentDate">
    </div>
-->
    <div class="background" style="margin-top: 60px; min-height: calc(100vh - 60px);">
        <div class="card" v-for="(alarm, i) in settingAlarm" :key="i" 
        style="width: 80%; display:flex; padding: 0; margin: 1vh auto; box-shadow: 2px 2px 2px 2px #eeeeee">
            <div class="card-body">

                <svg style="position: absolute; width: 17px; right: 17px; margin: 0; z-index: 1;" @click="delete_alarm(alarm)" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
                </svg>

                <div class="product_image">
                    <img :src="alarm.img" :alt="alarm.name" style="width: min(33vw, 33vh);">
                </div>

                <div class="product_name">
                    <span>{{ alarm.name }}</span>
                </div>

                <div class="day_selector">
                    <input type="checkbox" name="sunday" :id="'sunday'+alarm.id" v-model="alarm.days.sunday">
                    <label :for="'sunday'+alarm.id">일</label>

                    <input type="checkbox" name="monday" :id="'monday'+alarm.id" v-model="alarm.days.monday">
                    <label :for="'monday'+alarm.id">월</label>

                    <input type="checkbox" name="tuesday" :id="'tuesday'+alarm.id" v-model="alarm.days.tuesday">
                    <label :for="'tuesday'+alarm.id">화</label>

                    <input type="checkbox" name="wednesday" :id="'wednesday'+alarm.id" v-model="alarm.days.wednesday">
                    <label :for="'wednesday'+alarm.id">수</label>

                    <input type="checkbox" name="thursday" :id="'thursday'+alarm.id" v-model="alarm.days.thursday">
                    <label :for="'thursday'+alarm.id">목</label>

                    <input type="checkbox" name="friday" :id="'friday'+alarm.id" v-model="alarm.days.friday">
                    <label :for="'friday'+alarm.id">금</label>

                    <input type="checkbox" name="saturday" :id="'saturday'+alarm.id" v-model="alarm.days.saturday">
                    <label :for="'saturday'+alarm.id">토</label>
                </div>

                <div class="time_selector">
                    <input type="time" name="time" :id="'time'+alarm.id" v-model="alarm.time">
                    <label :for="'time'+alarm.id"></label>
                </div>
                <div class="save_buttons">
                    <button class="roundbox" @click="save_alarm(alarm)">저장</button>
                </div>
            </div>
        </div>

        <div v-if="new_alarm == null" class="add_new_alarm">
            <button class="roundbox" style="width: 80%;" @click="add_new_alarm()">추가</button>
        </div>
        <div v-else class="card" style="width: 80%; display:flex; padding: 0; margin: 1vh auto; box-shadow: 2px 2px 2px 2px #eeeeee">
            <div v-if="new_alarm.name == null" class="card-body">
                <div class="select_nutraceutical_box" v-for="(nutraceutical, i) in my_nutraceuticals" :key="i">
                    <input type="radio" v-model="checked_nutraceutical" :value="nutraceutical" :name="nutraceutical.name" :id="i">
                    <label class="nutraceutical_img" :for="i"><img :src="nutraceutical.img" :alt="nutraceutical.name"></label>
                    <label class="nutraceutical_name" :for="i">{{nutraceutical.name}}</label>
                </div>
                <button class="roundbox" @click="check_nutraceutical(checked_nutraceutical);">선택</button>
            </div>
            <div v-else class="card-body">
                <svg style="position: absolute; width: 17px; right: 17px; margin: 0; z-index: 1;" @click="delete_new_alarm()" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
                </svg>
                <div class="product_image">
                    <img @click="() => {new_alarm.name = null; new_alarm.img = null;}" :src="new_alarm.img" :alt="new_alarm.name" style="width: min(33vw, 33vh);">
                </div>

                <div class="product_name">
                    <span>{{ new_alarm.name }}</span>
                </div>

                <div class="day_selector">
                    <input type="checkbox" name="sunday" id="sunday" v-model="new_alarm.days.sunday">
                    <label for="sunday">일</label>

                    <input type="checkbox" name="monday" id="monday" v-model="new_alarm.days.monday">
                    <label for="monday">월</label>

                    <input type="checkbox" name="tuesday" id="tuesday" v-model="new_alarm.days.tuesday">
                    <label for="tuesday">화</label>

                    <input type="checkbox" name="wednesday" id="wednesday" v-model="new_alarm.days.wednesday">
                    <label for="wednesday">수</label>

                    <input type="checkbox" name="thursday" id="thursday" v-model="new_alarm.days.thursday">
                    <label for="thursday">목</label>

                    <input type="checkbox" name="friday" id="friday" v-model="new_alarm.days.friday">
                    <label for="friday">금</label>

                    <input type="checkbox" name="saturday" id="saturday" v-model="new_alarm.days.saturday">
                    <label for="saturday">토</label>
                </div>

                <div class="time_selector">
                    <input type="time" name="time" id="time" v-model="new_alarm.time">
                    <label for="time"></label>
                </div>

                <div class="save_buttons">
                    <button class="roundbox" @click="save_new_alarm(new_alarm)">추가</button>
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

        const my_nutraceuticals = ref(null);
        const checked_nutraceutical = ref(null);

        const getCurrentTime = () => {
            var curr = new Date();
            var KR_TIME_DIFF = curr.getTimezoneOffset() * 60000
            var kr_curr = new Date(curr.getTime() - KR_TIME_DIFF);
            
            var currentDate = ref(kr_curr.toISOString().slice(0, 10));
            var currentTime = ref(kr_curr.toISOString().slice(11, 16));

            return {'date': currentDate, 'time': currentTime}
        }

        const settingAlarm = ref([
            {
            id: 0,
            name: '닥터린 덴마크 락토지지 유산균',
            img: 'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcR3h8B7MrzEI3wg-A8_FArF5oQlBGzRrtr8F-PN-MI41_LsiInYYB7_JkFxbrY1XTGGcbbI-W8Or2ymn4cXLM2wS3xW_Y3Ii0EJ4lPnniZSeHyZ2OahUqGrBCix8Ki3IoQw_A&usqp=CAc',
            days: { sunday : false,
                    monday : false,
                    tuesday : false,
                    wednesday : true,
                    thursday : false,
                    friday : false,
                    saturday : false,
                },
            time: '15:55',
            },
            {
            id: 1,
            name: '얼라이브 원스데일리 멀티비타민',
            img: '//thumbnail9.coupangcdn.com/thumbnails/remote/492x492ex/image/retail/images/1743393023473072-96246b1b-737e-4b28-808a-eeb5f36b1add.jpg',
            days: { sunday: false,
                    monday : true,
                    tuesday : false,
                    wednesday : true,
                    thursday : false,
                    friday : false,
                    saturday : false,
                },
                time: '07:00',
            },
        ]);
        
        const delete_alarm = (params) => {
            console.log(settingAlarm)
            if(confirm('정말 삭제하시겠습니까?')){
                settingAlarm.value = settingAlarm.value.filter((element) => element !== params);
            }
            console.log(settingAlarm)

        };
        
        const save_alarm = (params) => {
            // 알람 저장하는 함수
            if(confirm('저장하시겠습니까?')){
                console.log(settingAlarm);
            }
        }
        
        const new_alarm = ref(null);
        
        const add_new_alarm = () => {
            new_alarm.value = {
                id: settingAlarm.value.length,
                name: null,
                img: null,
                days: { 'sunday': false,
                        'monday' : false,
                        'tuesday' : false,
                        'wednesday' : false,
                        'thursday' : false,
                        'friday' : false,
                        'saturday' : false,
                    },
                time: null,
            };
            if(my_nutraceuticals.value == null) { get_my_nutraceuticals(); }
        };

        const get_my_nutraceuticals = (userID) => {
            my_nutraceuticals.value = [
                {
                id: 0,
                name: '닥터린 덴마크 락토지지 유산균',
                img: 'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcR3h8B7MrzEI3wg-A8_FArF5oQlBGzRrtr8F-PN-MI41_LsiInYYB7_JkFxbrY1XTGGcbbI-W8Or2ymn4cXLM2wS3xW_Y3Ii0EJ4lPnniZSeHyZ2OahUqGrBCix8Ki3IoQw_A&usqp=CAc',
                },
                {
                id: 1,
                name: '얼라이브 원스데일리 멀티비타민',
                img: '//thumbnail9.coupangcdn.com/thumbnails/remote/492x492ex/image/retail/images/1743393023473072-96246b1b-737e-4b28-808a-eeb5f36b1add.jpg',
                },
                {
                id: 2,
                name: '활력UP 멀티비타민',
                img: '//healthhelper.kr/web/product/big/202208/974f37ad198063c0bc83685c2c28d6c9.png',
                },

            ]
        }

        const check_nutraceutical = (checked_nutraceutical) => {
            new_alarm.value.name = checked_nutraceutical.name;
            new_alarm.value.img = checked_nutraceutical.img;
            new_alarm.value.time = getCurrentTime().time;
            console.log(checked_nutraceutical, new_alarm.value);
        }

        const delete_new_alarm = () => {
            new_alarm.value = null;
        }

        const save_new_alarm = (params) => {
            // 알람 저장하는 함수 추가
            new_alarm.value = null;
        }

        return {
            settingAlarm,
            my_nutraceuticals,
            checked_nutraceutical,
            new_alarm,
            save_alarm,
            delete_alarm,
            add_new_alarm,
            check_nutraceutical,
            save_new_alarm,
            delete_new_alarm,
        };
    },
};
</script>

<style lang="css">

.day_selector {
    display: flex;
    justify-content: center;
    margin: 2vh;
}

.day_selector input[type="checkbox"] {
    display: none;
}

.day_selector input[type="checkbox"] + label{
    display: flex;
    width: min(10vw, 10vh);
    height: min(10vw, 10vh);
    position: relative;
    box-sizing: content-box;
    border: 1px solid white;
    background-color: white;
    text-align: center;
    justify-content: center;
    align-items: center;
    color: #333;
    font-size: 1.1em;
    text-decoration: none;
    font-weight: 750;
}

.day_selector input[type="checkbox"]:checked + label{
    border: 1px solid #2dce89;
    background-color: rgba(235, 242, 233, 1);
    color: #333;
}

.time_selector {
    margin: 2vh;
}

.add_new_alarm {
    margin: 1vh auto;
}

.select_nutraceutical_box {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 1vh 1vw;
}

.select_nutraceutical_box input[type="radio"] {
    display: none;
}

.select_nutraceutical_box input[type="radio"] ~ label.nutraceutical_img {
    display: flex;
    justify-self: center;
    border: 1px solid #2dce89;
    background-color: white;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    color: #6e6e6e;
    font-size: 1.1em;
    text-decoration: none;
    font-weight: 750;
    width: min(21vw, 21vh);
    height: min(21vw, 21vh);
}

.select_nutraceutical_box input[type="radio"]:checked ~ label.nutraceutical_img {
    background-color: #2dce89;
    color: white;
}

.select_nutraceutical_box input[type="radio"] ~ label.nutraceutical_img img {
    width: min(21vw, 21vh);
    height: min(21vw, 21vh);
}

.select_nutraceutical_box input[type="radio"]:checked ~ label.nutraceutical_img img {
    width: min(18vw, 18vh);
    height: min(18vw, 18vh);
}

.select_nutraceutical_box input[type="radio"] ~ label.nutraceutical_name {
    display: inline-block;
    color: #333;
}

.select_nutraceutical_box input[type="radio"]:checked ~ label.nutraceutical_name {
    display: inline-block;
    color: #2dce89;
}
</style>
