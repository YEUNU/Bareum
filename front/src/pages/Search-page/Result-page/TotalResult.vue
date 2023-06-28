<template>
    <div class="background bg-whitesmoke" style="margin-top: 59px; min-height: calc(100vh - 59px);">
      <div style="position: relative;">
        <div
          class="result_box bg-white"
          v-for="(product, i) in products"
          :key="i"
          @click="goToProductDetail(product.id)"
        >
          <div class="result_image">
            <img
              class="result_image"
              :src="product.img"
              alt="상품이미지"
              style="height: min(25vh, 25vw); width: min(25vh, 25vw);"
            />
          </div>
          <div class="result_manufacturer">{{ product["company_name"] }}</div>
          <div class="result_name"> {{ product["name"] }}</div>
          <div class="result_mount">별점: {{ product["star"] }}</div>
          <div class="result_price">최저가: {{ product["lowest_value"] }}</div>
        </div>
        <div
          style="
            bottom: 0;
            display: flex;
            flex-direction: column;
            text-align: start;
            background-color: white;
            margin-bottom: 1vh;
            padding: 5vw;
            color: gray;
          "
        >
          <span>찾으시는 제품이 없나요?</span>
          <span style="font-size: 0.9em;">제품 등록을 요청하시면, 금방 추가해드리겠습니다.</span>
          <router-link :to="{ name: 'mynewaddPage' }"
            >제품등록 요청하러 가기</router-link
          >
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed, onMounted } from "vue";
  import { useRouter } from "vue-router";
  import axios from "axios";
  
  export default {
    name: "TotalResult",
    props: ["query"],
    setup(props) {
      const searchQuery = ref(props.query);
      const products = ref([]);
      const router = useRouter();
  
      const fetchData = async () => {
        try {
          const response = await axios.post("/api/product/search/", {
            searchQuery: searchQuery.value,
          });
          products.value = response.data.search_res;
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      };
  
      onMounted(fetchData);
  
      const goToProductDetail = (productId) => {
        router.push(`/product/${productId}`);
      };
  
      const filteredProducts = computed(() => {
        return products.value.filter((product) =>
          product.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        );
      });
  
      return {
        filteredProducts,
        products,
        goToProductDetail,
      };
    },
  };
  </script>
  


<style>

.search_detail_option_box {
    width: 100%;
    display: flex;
    flex-direction: column;
    font-size: 0.8em;
    font-weight: bold;
}

#option_button_container {
    width: 100%;
    display: flex;
    justify-content: space-around;

    position: sticky;
}

.search_detail_option_box button {
    flex-grow: 1;
    border-radius: 10px;
    margin: 2vh 2vw;
    font-size: 0.9em;
    color: #333;
    background-color: white;
}

.result_box {
    align-self: center;
    justify-self: center;
    display: grid;
    width: 100vw;
	grid-template-columns: min(30vh, 30vw) 60vw;
	grid-template-rows: 3vh 4vh 5vh 5vh;
    align-content: center;
    margin-bottom: 2vh;
    padding: 5vw;
    font-weight: bold;
    box-shadow: 2px 2px 2px 2px #eeeeee
}


.result_image {
    grid-column: 1 / 2;
	grid-row: 1 / 5;
    align-self: center;
    justify-self: center;
}

.result_manufacturer {
    grid-column: 2 / 3;
    grid-row: 1 / 2;
    align-self: center;
    justify-self: start;
    padding: 0 5vw;
    font-size: small;
    color: gray;
}

.result_name {
    grid-column: 2 / 3;
	grid-row: 2 / 3;
    align-self: center;
    justify-self: start;
    padding: 0 5vw;
    font-size: large;
}

.result_mount {
    grid-column: 2 / 3;
	grid-row: 3 / 4;
    align-self: center;
    justify-self: start;
    padding: 0 5vw;
    font-size: medium;
}

</style>