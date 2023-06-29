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
    position: relative;
    font-size: 2.5rem;
    font-weight: normal;
    color: #FFCC21;
    z-index: 1;
}

.star-rating span::before {
    position: absolute;
    top: 0;
    left: 0;
    content: "★";
    color: whitesmoke;
    z-index: -1;
}

</style>
  