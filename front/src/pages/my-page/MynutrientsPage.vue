<template>
  <div class="mynutrientscontainer">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <div @click="goBack" class="navbar-brand">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left"
            viewBox="0 0 16 16" style="margin-left: 2vh;">
            <path fill-rule="evenodd"
              d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
          </svg>
        </div>
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
    <div class="chart-container" style="text-align:center;">
      <canvas id="myChart"></canvas>
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
import { useUserInfo } from "../../stores.js";

export default {
  setup(_, { root }) {
    const userInfo = useUserInfo();
    const loginId = computed(() => userInfo.loginId);
    const goBack = () => {
      window.history.back(); // 이전 페이지로 이동
    };

    async function getUserNutrientsData() {
      try {
        const response = await axios.get("/api/taking/", {
          params: {
            user_id: loginId.value,
          },
        });
        const user_nutrients_data = response.data;
        return user_nutrients_data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }

    onMounted(async () => {
      const nutrientsData = await getUserNutrientsData();
      const maxValues = [100, 20, 700, 700, 315, 8.5];
      const nutrientsArray = ['비타민C', '비타민D', '비타민A', '칼슘', '마그네슘', '아연'].map((label, index) => {
        const value = nutrientsData[label] / maxValues[index] * 100;
        return value;
      });
      // 차트를 렌더링할 캔버스를 선택합니다.
      const ctx = document.getElementById('myChart').getContext('2d');
      // 새 차트 인스턴스를 생성합니다.
      const myChart = new Chart(ctx, {
        type: 'polarArea',
        data: {
          labels: ['비타민C', '비타민D', '비타민A', '칼슘', '마그네슘', '아연'],
          datasets: [
            {
              label: 'Sample Dataset',
              data: nutrientsArray,
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

    return { goBack };
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
  margin-top: 10%;
  border: 1px solid #d3d3d3;
  border-radius: 10px;
  box-shadow: 2px 2px 2px 2px #eeeeee;
}
</style>