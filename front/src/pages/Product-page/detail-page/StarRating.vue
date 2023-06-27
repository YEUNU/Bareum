<template>
    <div class="star-rating">
      <span v-for="(star, index) in stars" :key="index" @click="setRating(index)">
        {{ star }}
      </span>
    </div>
  </template>
  
  <script>
  import { ref, computed } from "vue";
  
  export default {
    setup(_, { emit }) {
      const rating = ref(0);
      const stars = computed(() => { 
        return Array.from({ length: 5 }, (_, index) => {
          return index < rating.value ? "★" : "☆";
        });
      });
  
      function setRating(index) {
          rating.value = index + 1;
          emit("update-rating", rating.value);
        }

  
      return { stars, setRating };
    },
  };
  </script>
  
  <style scoped>
  .star-rating {
    display: flex;
    cursor: pointer;
    justify-content: center;
  }
  
  .star-rating span {
    margin-right: 0.5rem;
    font-size: 1.5rem;
  }
  
  .star-rating span:last-child {
    margin-right: 0;
  }
  </style>
  