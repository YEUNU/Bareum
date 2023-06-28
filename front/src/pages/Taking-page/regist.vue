<template>
  <div class="mycontainer">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <router-link to="/taking" >
        <a class="navbar-brand" style="margin-left: 2vh;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left"
            viewBox="0 0 16 16">
            <path fill-rule="evenodd"
              d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
          </svg>
        </a>
      </router-link>
        <div class="navbar-title" style="margin-right: 2vh;">섭취 관리</div>
        <router-link to="/mysetting" class="navbar-right" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill"
            viewBox="0 0 16 16">
            <path
              d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
          </svg>
        </router-link>
      </div>
    </nav>
    <div class="d-flex align-items-center justify-content-between w-100 header-content" style="white-space: normal;">
      <h1 style="text-align: left; word-break: break-word;">
        {{ nickname }}님의<br />섭취중인 영양제
      </h1>
      <router-link to="/taking/search">
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="#2dce89" class="bi bi-plus-square-fill"
          viewBox="0 0 16 16">
          <path
            d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3a.5.5 0 0 1 1 0z" />
        </svg>
      </router-link>
    </div>
    
    <div v-for="(r, index) in nutraceuticals" :key="index">
  <div class="item-box" style="display: flex; align-items: center; position: relative; height: 15vh;" @click="goToProduct(r.제품코드)">
    <img :src="`../../../media/product_images/${r.제품코드}.png`" width="100" alt="제품 이미지" class="item-img" />
      <div style="flex-grow: 1;">
        <h5 style="text-align: center; margin-bottom: 0.5rem;">{{ r.제품명 }}</h5>
        <h6 style="text-align: center;">{{ r.업소명 }}</h6>
      </div>
        <button class="btn btn-danger" style="position: absolute; top: 0; right: 0;" @click.stop="() => removeItem(r.제품명, r.checking_number)">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash"
            viewBox="0 0 16 16">
            <path
              d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5.5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6zM9.5 5.5a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5z" />
            <path fill-rule="evenodd"
              d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v1zm-1 10V4h1v9a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V4h1v9h10zm-1-11H3v1h10V2z" />
          </svg>
        </button>
        </div>
    </div>
    
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import axios from "axios";
import { useUserInfo } from "../../stores.js";
import Cookies from 'js-cookie';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const userInfo = useUserInfo();
    const loginId = computed(() => userInfo.loginId);
    const nutraceuticals = ref([]);
    const nickname = computed(() => userInfo.nickname);
    const csrf_token = Cookies.get("csrftoken");
    
    const router = useRouter(); 
    const goToProduct = (productCode) => {
      router.push(`/product/${productCode}`);
    };

    async function take_nutrace() {
      try {
        const response = await axios.post("/api/taking/regist", {
          headers: { "Content-Type": "application/json",
                      "X-CSRFToken": csrf_token,},
          loginId: loginId.value,
        });
        nutraceuticals.value = response.data.take;
      } catch (error) {
        console.log("Error fetching user nutraceuticals:", error);
      }
    }

    async function removeItem(nutraceuticals_name, checking_number) {
      try {
        await axios.delete("/api/taking/remove", {
          headers: {
                      "Content-Type": "application/json",
                      "X-CSRFToken": csrf_token,
                  },
          data: {
            loginId: loginId.value,
            nutraceuticals_name: nutraceuticals_name,
            checking_number: checking_number,
          },
        });
        take_nutrace();
      } catch (error) {
        console.log("Error deleting item:", error);
      }
    }
    onMounted(() => {
      take_nutrace();
    });

    return {
      nickname,
      nutraceuticals,
      removeItem,
      goToProduct,
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

.header-content {
  padding-top: 2rem;
}

.item-box {
  min-height: 200px;
}
</style>