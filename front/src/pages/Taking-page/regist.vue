<template>
    <div>
        <div class="d-flex justify-content-between align-items-center">
            <h1>내가 먹는 영양제 관리</h1>
            <router-link to="/taking/search" >
                <button class="btn btn-primary" >영양제 등록</button>
            </router-link>
        </div>
        <li v-for="(r, index) in nutraceuticals" :key="index">
          <div class="item-box" >
                <!-- 여기에 경로/제품코드.png하면 나올거임 -->
            <img :src="`assets/${r.제품코드}.png`" alt="제품 이미지" class="item-img"/>
            <div>
              <h3>{{ r.제품명 }}</h3>
              <p>업소명: {{ r.업소명 }}</p>
            </div>
          </div>
        </li>
    </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import axios from "axios";
import { useUserInfo } from "../../stores.js";

export default {
  setup() {
    const userInfo = useUserInfo();
    const loginId = computed(() => userInfo.loginId);
    const nutraceuticals = ref([]);

    async function take_nutrace() {
        try {
          const response = await axios.post("/api/taking/regist", {
            loginId: loginId.value, 
          });
          nutraceuticals.value = response.data.take;
        } catch (error) {
          console.log("Error fetching user nutraceuticals:", error);
        }
      }
    onMounted(() => {
        take_nutrace();
    });

    return {
      nutraceuticals,
    };
  },
};
</script>

<style scoped>
.nutraceutical-list {
    padding: 0;
    list-style-type: none;
}
.nutraceutical-list ul li {
    margin: 10px;
    border-bottom: 1px solid #ccc;
    padding: 10px 0;
}
</style>
