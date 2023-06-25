<template>
    <div>
        <input type="text" v-model="searchInput" @input="fetchNutraceuticals" placeholder="Search Nutraceuticals">
        <div v-for="nutraceutical in filteredNutraceuticals" :key="nutraceutical.id">
            {{ nutraceutical.nutraceuticals_name }}
        </div>
    </div>
</template>

<script>
import { ref, computed } from 'vue'
import axios from 'axios'

export default {
    setup() {
        const searchInput = ref('')
        const nutraceuticals = ref([])

        const fetchNutraceuticals = async () => {
            const response = await axios.get('/api/taking/search', {
                params: { search: searchInput.value }
            });
            nutraceuticals.value = response.data;
        }

        const filteredNutraceuticals = computed(() => {
            return nutraceuticals.value;
        })

        return {
            searchInput,
            filteredNutraceuticals,
            fetchNutraceuticals
        }
    }
}
</script>

<style scoped>
    
</style>