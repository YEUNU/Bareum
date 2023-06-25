<template>
    <div>
      <ul>
        <li v-for="(item, index) in searchResults" :key="index">
          <div class="result-card">
            <p><strong>제품명:</strong> {{ item.nutraceuticals_name }}</p>
            <p><strong>업소명:</strong> {{ item.업소명 }}</p>
          </div>
        </li>
      </ul>
    </div>
  </template>

<script>
export default {
  props: {
    searchResults: {
      type: Array,
      default: () => [],
    },
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
</style>