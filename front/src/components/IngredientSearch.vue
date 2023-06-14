<template lang="">
  <div>
      <div v-for="ingredient in ingredients" :key="id">
          <a class="tile" title="ingredient.text" href="/">
              <button id="actio nMenuButton" class="icon-more-vert" tabindex="0" title="추가 작업" role="button"></button>
              <div class="tile-icon">
                  <img draggable="false" alt="" src="">
                  <div class="query-tile-icon" draggable="false"></div>
              </div>
              <div class="tile-title title-ltr">
                  <span>{{ingredient.text}}</span>
              </div>
          </a>
      </div>
  </div>
</template>

<script>
import { ref } from "vue"
export default {
  name:"test",
  setup() {
    let id = 0;
    const ingredients = ref([
      { id: id++, text: '탄수화물' },
      { id: id++, text: '단백질' },
      { id: id++, text: '지방' },
      { id: id++, text: '비타민' },
      { id: id++, text: '무기질' },
      { id: id++, text: '물' }
    ])
        return {
          ingredients,
        };
    },
}
</script>
<style lang="">
    
</style>