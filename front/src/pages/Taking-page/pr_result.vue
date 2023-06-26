<template>
    <div class="prresult">
      <ul style="width: 100%; padding-left: 0;">
        <div v-for="(item, index) in searchResults" :key="index">
          <div class="result-card" style="width: 100%;">
            <p style="text-align: left;"><strong>제품명 : </strong> {{ item.nutraceuticals_name }}</p>
            <p style="text-align: left;"><strong>업소명 : </strong> {{ item.업소명 }}</p>
          </div>
        </div>
      </ul>
    </div>
  </template>

<script>
import axios from "axios";
import { ref, reactive, computed } from "vue";
import { useRouter } from "vue-router";
import {useUserInfo} from "../../stores.js"
import Cookies from 'js-cookie';
// CSRF 토큰이 저장된 DOM 요소를 찾은 후
const csrfTokenMeta = document.querySelector('meta[name="csrf-token"]');
// content 속성 값을 CSRF 토큰으로 설정
const csrfToken = csrfTokenMeta ? csrfTokenMeta.getAttribute('content') : '';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;
axios.defaults.headers.common['X-CSRFToken'] = csrfToken; // Axios에 CSRF 토큰 설정

export default {
  props: {
    searchResults: {
      type: Array,
      default: () => [],
    },
  },
  setup(props) {
    const activeItem = ref(null);
    const checkedItems = ref([]);
    const userInfo = useUserInfo();
    const loginId = computed(() => userInfo.loginId);
    function handleItemClick(item) {
      activeItem.value = item;
      console.log("클릭한 제품: ", item);
    }

    async function handleSave() {
      console.log("저장된 항목들: ", checkedItems.value);
      
      try {
        await axios.post("/api/taking/save", {
          checkedItems: checkedItems.value.map(item => ({
            nutraceuticals_name: item.nutraceuticals_name,
            loginId: loginId.value,
          })),
        });
        console.log("저장 성공");
      } catch (error) {
        console.log("저장에 실패하였습니다:", error);
      }
    }

    return {
      activeItem,
      handleItemClick,
      checkedItems,
      handleSave,
    };
  },
};

</script>


<style scoped>
.prresult {
  width: 100%; /* 화면 너비에 꽉 차도록 설정 */
  height: 100%; /* 화면 높이에 꽉 차도록 설정 */
  display: block;
  margin-bottom: 10%;
  border-radius: 10px;
  padding-top: 10%;
  padding-bottom: 10%;
}
.result-card {
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 4px;
  background-color: white;
  box-shadow: 2px 2px 2px 2px #eeeeee
}
.result-card-active {
  background-color: #e0e0e0;
}
.label-content {
  display: block;
  flex-grow: 1;
}
.checkbox {
  margin-left: 1rem;
  height: 20px;
  width: 20px;
}
.save-button {
  border: none;
  background-color: #0062cc;
  color: white;
  padding: 10px 20px;
  font-size: 14px;
  cursor: pointer;
  border-radius: 3px;
  margin-bottom: 1rem;
}
</style>
