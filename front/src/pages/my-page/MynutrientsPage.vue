<template>
  <div class="mynutrientscontainer">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <router-link to="/" >
        <div class="navbar-brand">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left"
            viewBox="0 0 16 16" style="margin-left: 2vh;">
            <path fill-rule="evenodd"
              d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
          </svg>
        </div>
      </router-link>
        <div style="margin-right: 2vh;">섭취 관리</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill"
            viewBox="0 0 16 16">
            <path
              d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
          </svg>
        </div>
      </div>
    </nav>
    <h5 style="text-align: left; font-weight: bold; margin-top:10%">섭취중인 영양소</h5>
    <div class="chart-container" style="text-align:center;">
      <canvas id="myChart"></canvas>
    </div>
    <div class="mycard-container">
      <div class="card"
        style="width: 100%; padding:0;  display:block; margin-bottom: -5%; box-shadow: 2px 2px 2px 2px #eeeeee">

        <div class="card-body">

          <h5 style="text-align: left; font-weight: bold;">내 영양제</h5>
          <div v-for="(r, index) in nutraceuticals" :key="index">
          <div class="item-box" style="display: flex; align-items: center; position: relative; height: 15vh;" @click="goToProduct(r.제품코드)">
            <img :src="`../../../media/product_images/${r.제품코드}.png`" width="100" alt="제품 이미지" class="item-img" />
              <div style="flex-grow: 1;">
                <h5 style="text-align: center; margin-bottom: 0.5rem;">{{ r.제품명 }}</h5>
                <h6 style="text-align: center;">{{ r.업소명 }}</h6>
              </div>
                </div>
            </div>
        </div>
      </div>
    </div>

    <div class="add-nutrient-btn" style="text-align:center; margin-top:1rem;">
      <router-link to="/taking/regist">
        <button class="btn btn-primary" style="border: none; background-color: #2dce89; color: white; border-radius: 5px;"
          @click="openRegistration">내 영양식품 관리</button>
      </router-link>
    </div>
  </div>
</template>


<script>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import Chart from 'chart.js/auto';
import Cookies from 'js-cookie';
import { useUserInfo } from "../../stores.js";

export default {
  setup(_, { root }) {
    const userInfo = useUserInfo();
    const loginId = computed(() => userInfo.loginId);
    const nutraceuticals = ref([]);
    const csrf_token = Cookies.get("csrftoken");
    const goBack = () => {
      window.history.back(); // 이전 페이지로 이동
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
        const user_products_data = response.data;
        return user_products_data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }

    onMounted(async () => {
      take_nutrace();
      const productsData = await getUserProductsData();
      const maxValues = [100, 100, 100, 100, 100, 100];

      const nutrientsArray = productsData.reduce(
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

      // 차트를 렌더링할 캔버스를 선택합니다.
      const ctx = document.getElementById('myChart').getContext('2d');
      // 새 차트 인스턴스를 생성합니다.
      const myChart = new Chart(ctx, {
        type: 'polarArea',
        data: {
          labels: ['비타민C', '비타민D', '비타민A', '칼슘', '마그네슘', '아연'],
          datasets: [
            {
              label: ['Sample Dataset'],
              data: nutrientsArray.map((arr) => arr.reduce((sum, item) => sum + item.value, 0)),
              backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(255, 205, 86, 0.5)',
                'rgba(201, 203, 207, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(139, 0, 255, 0.5)',
              ],
              borderColor: [
                'rgb(255, 99, 132)',
                'rgb(75, 192, 192)',
                'rgb(255, 205, 86)',
                'rgb(201, 203, 207)',
                'rgb(54, 162, 235)',
                'rgba(139, 0, 255)',
              ],
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
                  const productData = nutrientsArray[context.dataIndex];
                  return productData
                    .map((product) => product.product + ": " + product.value.toFixed(1) + "%")
                    .join(", ");
                },
              },
            },
            legend: {
              display: false,
            },
          },
          scales: {
            r: {
              min: 0,
              max: 100,
              pointLabels: {
                display: true,
                centerPointLabels: true,
                font: {
                  size: 18,
                },
              },
            },
          },
        },
      });
    });

    return { goBack,
      nutraceuticals, };
  },
};
</script>


<style>
.mynutrientscontainer {
  width: 100%;
  /* 화면 너비에 꽉 차도록 설정 */
  height: 100%;
  /* 화면 높이에 꽉 차도록 설정 */
  margin-bottom: 10%;
  padding-bottom: 100%;

}

.chart-container {
  width: 100%;
  height: 100%;
  margin-bottom: -5%;
  border: 1px solid #d3d3d3;
  border-radius: 10px;
  box-shadow: 2px 2px 2px 2px #eeeeee;
}
</style>