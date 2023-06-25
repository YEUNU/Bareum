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
</style>