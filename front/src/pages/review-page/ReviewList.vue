<!-- ProductReview.vue -->
<template>
  <div>
    <!-- <input type="text" v-model="nutraceuticals_name" placeholder="제품명 입력" /> -->
    <h1>리뷰보기</h1>
    <!-- <button @click="fetchReviews">검색</button> -->
    <!-- <button @click="showNutraceuticalsName">보기</button> -->
    <ul v-if="reviews.length > 0">
      <li v-for="(review, index) in reviews" :key="index">
        <h4>제품명 : {{ review.nutraceuticals_name }}</h4>
        <p>{{ review.reviews }}</p>
      </li>

    </ul>
    <div v-else>
      <h4>{{ nutraceuticals_name }}</h4>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProductReview',
  data() {
    return {
      nutraceuticals_name: '킹맨',
      reviews: []
    }
  },
  created() {
    this.fetchReviews() // 컴포넌트가 생성될 때 리뷰를 가져옵니다.
  },
  methods: {
    async fetchReviews() {
      try {
        const response = await axios.get(`api/reviews/`, {
          params: { nutraceuticals_name: this.nutraceuticals_name },
        })
        this.reviews = response.data
      } catch (error) {
        console.error('Error fetching reviews:', error)
      }
    },
    showNutraceuticalsName() {
      this.reviews = []
    },
  },
}
</script>

