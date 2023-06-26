<template>
  <div class="mynutrientscontainer">
    <nav class="navbar fixed-top bg-white">
      <div class="container-fluid">
        <router-link to="/mypage" @click="goBack" class="navbar-brand">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16" style="margin-left: 2vh;">
            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
          </svg>
        </router-link>
      </div>
    </nav>
    <div class="chart-container" style="text-align:center;">
      <canvas id="myChart"></canvas>
    </div>
      <div class="add-nutrient-btn" style="text-align:center; margin-top:1rem;">
        <router-link to="/taking/regist" >
          <button class="btn btn-primary" style="border: none; background-color: #2dce89; color: white; border-radius: 5px;" @click="openRegistration">내 영양식품 관리</button>
        </router-link>
      </div>
  </div>
</template>


<script>
// Chart.js를 가져옵니다.
import Chart from "chart.js/auto";

export default {
  methods: {
        goBack() {
            this.$router.go(-1); // 이전 페이지로 이동
        },
    },
  mounted() {
    // 차트를 렌더링할 캔버스를 선택합니다.
    const ctx = document.getElementById("myChart").getContext("2d");

    // 새 차트 인스턴스를 생성합니다.
      const myChart = new Chart(ctx, {
      type: "polarArea",
      data: {
        labels: ["비타민C", "비타민D", "비타민A", "칼슘", "마그네슘", "아연"],
        datasets: [
          {
            label: "Sample Dataset",
            data: [11, 16, 7, 3, 14, 20],
            backgroundColor: [
              "rgba(255, 99, 132, 0.5)",
              "rgba(75, 192, 192, 0.5)",
              "rgba(255, 205, 86, 0.5)",
              "rgba(201, 203, 207, 0.5)",
              "rgba(54, 162, 235, 0.5)",
              "rgba(139, 0, 255, 0.5)",
            ],
            borderColor: [
              "rgb(255, 99, 132)",
              "rgb(75, 192, 192)",
              "rgb(255, 205, 86)",
              "rgb(201, 203, 207)",
              "rgb(54, 162, 235)",
              "rgba(139, 0, 255)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        plugins:{
          legend: {
            display: false,
          }
        },
        scales: {
      r: {
        min: 0,
        max: 100,
        pointLabels: {
          display: true,
          centerPointLabels: true,
          font: {
            size: 18
          }
        }
      }
      },
    },
    });
  },
};
</script>

<style>
.mynutrientscontainer {
    width: 100%; /* 화면 너비에 꽉 차도록 설정 */
    height: 100%; /* 화면 높이에 꽉 차도록 설정 */
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