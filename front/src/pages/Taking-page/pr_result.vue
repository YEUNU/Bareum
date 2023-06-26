<template>
  <div>
    <button class="save-button" @click="handleSave">저장</button>
    <ul>
      <li v-for="(item, index) in searchResults" :key="index">
        <div class="result-card">
          <div
            class="label-content"
            :class="{ 'result-card-active': activeItem === item }"
            @click="handleItemClick(item)"
          >
            <p><strong>제품명:</strong> {{ item.nutraceuticals_name }}</p>
            <p><strong>업소명:</strong> {{ item.업소명 }}</p>
          </div>
          <input
            type="checkbox"
            class="checkbox"
            :id="`checkbox-${index}`"
            :value="item"
            v-model="checkedItems"
          />
        </div>
      </li>
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
    const router = useRouter();
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
        const response = await axios.post("/api/taking/save", {
          checkedItems: checkedItems.value.map((item) => ({
            nutraceuticals_name: item.nutraceuticals_name,
            loginId: loginId.value,
          })),
        });

        if (response.data.message === "success") {
          alert("저장에 성공하였습니다.");
          router.back();
        } else if (response.data.message === "fail") {
          alert("이미 등록되어있는 제품을 제외하고 저장되었습니다.");
          router.back();
        }
      } catch (error) {
        console.error("저장에 실패하였습니다:", error);
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
.result-card {
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 4px;
  background-color: #f8f8f8;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: space-between;
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
