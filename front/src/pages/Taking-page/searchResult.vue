<template>
    <div class="search-results">
      <ul>
        <li v-for="result in filteredResults" :key="result.nutraceuticals_name">
          {{ result.nutraceuticals_name }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: ['nutraceuticals', 'searchQuery'],
    computed: {
      filteredResults() {
        return this.nutraceuticals.filter((item) =>
          item.nutraceuticals_name
            .toLowerCase()
            .includes(this.searchQuery.toLowerCase())
        );
      },
    },
  };
  </script>
  
  <style scoped>
  .search-results {
    padding: 0;
    list-style-type: none;
  }
  .search-results ul li {
    margin: 10px;
    border-bottom: 1px solid #ccc;
    padding: 10px 0;
  }
  </style>