<template>
  <div class="mycontainer">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand" style="margin-left: 2vh;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left"
            viewBox="0 0 16 16">
            <path fill-rule="evenodd"
              d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
          </svg>
        </router-link>
        <div style="margin-right: 2vh;">정기 배송 신청</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill"
            viewBox="0 0 16 16">
            <path
              d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
          </svg>
        </div>
      </div>
    </nav>

    <div class="calendar" style="margin-top: 10%; width: 100%;">
      <h2>
        <a href="#" v-on:click="onClickPrev(currentMonth)" style="color: #2dce89;">◀</a>
        {{ currentYear }}년 {{ currentMonth }}월
        <a href="#" v-on:click="onClickNext(currentMonth)" style="color: #2dce89;">▶</a>
      </h2>
      <table class="table table-hover" style="table-layout: fixed;">
        <colgroup>
          <col style="width: 15%;">
          <col style="width: 15%;">
          <col style="width: 15%;">
          <col style="width: 15%;">
          <col style="width: 15%;">
          <col style="width: 15%;">
          <col style="width: 15%;">
        </colgroup>
        <thead>
          <tr>
            <td v-for="(weekName, index) in weekNames" :key="index">
              {{ weekName.slice(0, 1) }} <!-- 요일 텍스트를 첫 글자로 줄여 표시 -->
            </td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, rowIndex) in currentCalendarMatrix" :key="rowIndex">
            <td v-for="(day, dayIndex) in row" :key="dayIndex" style="padding: 20px;">
              <span v-if="isSelected(currentYear, currentMonth, day)" class="rounded"
                v-on:click="selectDate(currentYear, currentMonth, day)">
                {{ day }}
              </span>
              <span v-else v-on:click="selectDate(currentYear, currentMonth, day)">
                {{ day }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="mycard-container">
      <div class="card"
        style="width: 100%; padding:0;  display:block; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">

        <div class="card-body">

          <h5 style="text-align: left; font-weight: bold;">정기 배송 품목</h5>
          
        </div>
      </div>
    </div>
    <div class="mycard-container">
      <div
        class="card"
        style="
          width: 100%;
          padding: 0;
          display: block;
          margin-bottom: -5%;
          box-shadow: 2px 2px 2px 2px #eeeeee;
        "
      >
        <div class="card-body">
          <h5 style="text-align: left; font-weight: bold;">내 건강기능식품 정기 배송 신청</h5>
          <div class="item-container">
            <div
              v-for="(r, index) in nutraceuticals"
              :key="index"
              class="item-box"
              style="
                display: flex;
                flex-direction: column;
                align-items: center;
                position: relative;
                width: calc(25% - 1rem);
                margin-bottom: 1rem;
                border: 1px solid #eeeeee;
                padding: 1rem;
                box-shadow: 2px 2px 2px 2px #eeeeee;
                background-color: #fff;
              "
              @click="goToProduct(r.제품코드)"
            >
              <img
                :src="`../../../media/product_images/${r.제품코드}.png`"
                width="100"
                alt="제품 이미지"
                class="item-img"
              />
              <h5 style="text-align: center; margin-bottom: 0.5rem;">{{ r.제품명 }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="mycard-container">
      <div class="card" style="width: 100%; padding:0; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">
        <div class="card-body">

          <div style="text-align: left;">
            <h5 style="color: black; font-weight: bold; margin-bottom: 5%;">배송지</h5>
            <div class="input-group mb-3" style="border-bottom: 2px solid #eeeeee;">
              <router-link to="/address" style="color: black; text-decoration: none;">
                <input type="text" name="gender" class="form-control" v-model=address placeholder="주소"
                  aria-label="Recipient's username" aria-describedby="button-addon2" style="border:none;">
              </router-link>
            </div>
          </div>




        </div>
      </div>
    </div>
    <router-link to="/"><button
        style="width:100%; margin-top: 5%; margin-bottom: 10%; background-color: #2dce89; border-radius: 5px; color:white; box-shadow: 2px 2px 2px 2px #eeeeee">완
        료</button></router-link>
  </div>
</template>
  
<script>
import { ref, computed } from 'vue';
import axios from 'axios';
import { useUserInfo } from "../../stores.js";
import Cookies from 'js-cookie';
export default {
  name: 'Calendar',
  setup() {
    const weekNames = ref(["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]);
    const rootYear = 1904;
    const rootDayOfWeekIndex = 4; // 2000년 1월 1일은 토요일
    const currentYear = ref(new Date().getFullYear());
    const currentMonth = ref(new Date().getMonth() + 1);
    const currentDay = ref(new Date().getDate());
    const currentMonthStartWeekIndex = ref(null);
    const currentCalendarMatrix = ref([]);
    const endOfDay = ref(null);
    const memoDatas = ref([]);
    const selectedDate = ref(null);
    const address = ref("");
    const nutraceuticals = ref([]);
    const userInfo = useUserInfo();
    const loginId = computed(() => userInfo.loginId);
    const csrf_token = Cookies.get("csrftoken");
    const images = ref([
      {
        src: 'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcR3h8B7MrzEI3wg-A8_FArF5oQlBGzRrtr8F-PN-MI41_LsiInYYB7_JkFxbrY1XTGGcbbI-W8Or2ymn4cXLM2wS3xW_Y3Ii0EJ4lPnniZSeHyZ2OahUqGrBCix8Ki3IoQw_A&usqp=CAc',
        alt: 'Image 1',
        isChecked: false,
      },
      {
        src: 'https://img.danawa.com/prod_img/500000/591/160/img/6160591_1.jpg?_v=20220804162302',
        alt: 'Image 2',
        isChecked: false,
      },
      {
        src: "../../assets/product.png",
        alt: 'Image 3',
        isChecked: false,
      },
    ]);

    const imageSize = computed(() => {
      return `min(20vh, 20vw)`;
    });
    const fetchData = async () => {
      try {
        const userInfo = useUserInfo()
        const response = await axios.get('/api/account/address/' + userInfo.memberId + '/');
        address.value = response.data.address;

        return address
      } catch (error) {
        console.error(error);
      }
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
    const init = () => {
      currentMonthStartWeekIndex.value = getStartWeek(currentYear.value, currentMonth.value);
      endOfDay.value = getEndOfDay(currentYear.value, currentMonth.value);
      initCalendar();
      fetchData();
      take_nutrace();
    };

    const toggleCheck = (index) => {
      images.value[index].isChecked = !images.value[index].isChecked;
    };

    const initCalendar = () => {
      currentCalendarMatrix.value = [];
      let day = 1;
      for (let i = 0; i < 6; i++) {
        let calendarRow = [];
        for (let j = 0; j < 7; j++) {
          if (i == 0 && j < currentMonthStartWeekIndex.value) {
            calendarRow.push("");
          } else if (day <= endOfDay.value) {
            calendarRow.push(day);
            day++;
          } else {
            calendarRow.push("");
          }
        }
        currentCalendarMatrix.value.push(calendarRow);
      }
    };

    const getEndOfDay = (year, month) => {
      switch (month) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
          return 31;
        case 4:
        case 6:
        case 9:
        case 11:
          return 30;
        case 2:
          if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            return 29;
          } else {
            return 28;
          }
        default:
          console.log("unknown month " + month);
          return 0;
      }
    };

    const getStartWeek = (targetYear, targetMonth) => {
      let year = rootYear;
      let month = 1;
      let sumOfDay = rootDayOfWeekIndex;
      while (true) {
        if (targetYear > year) {
          for (let i = 0; i < 12; i++) {
            sumOfDay += getEndOfDay(year, month + i);
          }
          year++;
        } else if (targetYear == year) {
          if (targetMonth > month) {
            sumOfDay += getEndOfDay(year, month);
            month++;
          } else if (targetMonth == month) {
            return (sumOfDay) % 7;
          }
        }
      }
    };

    const onClickPrev = (month) => {
      month--;
      if (month <= 0) {
        currentMonth.value = 12;
        currentYear.value -= 1;
      } else {
        currentMonth.value -= 1;
      }
      init();
    };

    const onClickNext = (month) => {
      month++;
      if (month > 12) {
        currentMonth.value = 1;
        currentYear.value += 1;
      } else {
        currentMonth.value += 1;
      }
      init();
    };
    
    const isToday = (year, month, day) => {
      let date = new Date();
      return year == date.getFullYear() && month == date.getMonth() + 1 && day == date.getDate();
    };

    const isSelected = (year, month, day) => {
      return selectedDate.value && year === selectedDate.value.year && month === selectedDate.value.month && day === selectedDate.value.day;
    };

    const selectDate = (year, month, day) => {
      selectedDate.value = { year, month, day };
    };

    init();

    return {
      weekNames,
      currentYear,
      currentMonth,
      currentDay,
      currentMonthStartWeekIndex,
      currentCalendarMatrix,
      endOfDay,
      memoDatas,
      selectedDate,
      images,
      imageSize,
      address,
      nutraceuticals,

      toggleCheck,
      onClickPrev,
      onClickNext,
      isToday,
      isSelected,
      selectDate,
      take_nutrace,
    }
  }
};
</script>

  
<style>
.mycontainer {
  width: 100%;
  /* 화면 너비에 꽉 차도록 설정 */
  height: 100%;
  /* 화면 높이에 꽉 차도록 설정 */
  display: block;
  margin-bottom: 10%;
  border-radius: 10px;
}

.rounded {
  -moz-border-radius: 20px 20px 20px 20px;
  border-radius: 20px 20px 20px 20px;
  border: solid 1px #ffffff;
  background-color: #2dce89;
  padding: 10px;
  color: #ffffff;
}
.item-container {
  display: flex;
  flex-wrap: nowrap;
  gap: 1rem;
  overflow-x: auto;
  padding-bottom: 1rem;
}

.item-box::-webkit-scrollbar {
  height: 8px;
}

.item-box::-webkit-scrollbar-thumb {
  background-color: #cccccc;
  border-radius: 4px;
}
</style>