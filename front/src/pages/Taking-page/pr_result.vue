<template>
    <div>
      <ul>
        <li v-for="(item, index) in searchResults" :key="index">
          <div
            class="result-card"
            :class="{ 'result-card-active': activeItem === item }"
            @click="handleItemClick(item)"
          >
            <p><strong>제품 명:</strong> {{ item.nutraceuticals_name }}</p>
            <p><strong>업소 명:</strong> {{ item.업소명 }}</p>
          </div>
        </li>
      </ul>
    </div>
  </template>

<script>
import { ref } from "vue";

export default {
  props: {
    searchResults: {
      type: Array,
      default: () => [],
    },
  },
  setup(props) {
    const activeItem = ref(null);

    function handleItemClick(item) {
      activeItem.value = item;
      console.log("클릭한 제품: ", item);
    }

    return {
      activeItem,
      handleItemClick,
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
}
.result-card-active {
  /* 원하는 클릭한 후의 스타일을 여기에 추가하세요 */
  background-color: #e0e0e0;
}
</style>