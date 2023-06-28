<template>
    <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
            <span class="navbar-brand" @click="$router.back()" style="margin-left: 2vh;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left"
                    viewBox="0 0 16 16">
                    <path fill-rule="evenodd"
                        d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />
                </svg>
            </span>
            <div style="margin-right: 2vh;">{{ rank_title }} 제품 순위</div>
            <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill"
                    viewBox="0 0 16 16">
                    <path
                        d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
                </svg>
            </div>
        </div>
    </nav>

    <div class="bg-white" style="position: fixed; top: 50px; left: 0; width: 100%; height: 144px; z-index: 1030;">
        <div>
            <button class="roundbox bg-theme" style="width: 40%; margin: 10px 3%" @click="open_popup('personalize')">관심
                항목</button>
            <button class="roundbox bg-theme" style="width: 40%; margin: 10px 3%"
                @click="open_popup('ingredient')">영양소</button>
        </div>
        <select class="roundbox bg-theme" style="width: 86%; height: 35px; border-radius: 4px;" v-model="age_group">
            <option disabled value="">연령대를 선택해 주세요</option>
            <option>total</option>
            <option>age1</option>
            <option>age2</option>
        </select>
        <div v-if="selected_items.length > 0"
            style="margin-top: 1vh; font-weight: bold; text-align: center; font-size: small;">선택항목: {{
                selected_items.join(',') }}</div>
        <hr>
    </div>
    <div class="background bg-whitesmoke" style="padding-top: 190px; min-height: 100%; padding-bottom: 60px;">
        <router-link class="rank_box bg-white"
            v-for="(product,index) in totalRanking" :key="index"
            :to="`/product/${product.업체별_제품코드}`">
            <div class="rank_order">{{ index + 1 }}위</div>
            <div class="rank_image"><img class="rank_image" :src='`/media/product_images/${product.업체별_제품코드}`' alt="상품이미지"
                    style="height: min(25vh, 25vw); width: min(25vh, 25vw);" /></div>
            <div class="rank_manufacturer">{{ product.업소명 }}</div>
            <div class="rank_name">{{ product.nutraceuticals_name }}</div>
            <div class="rank_mount">온라인 평점:{{ product.review.average_rating }}({{ product.review.total_reviews }}) </div>
            <div class="rank_price">온라인 최저가 :{{ product.review.lowest }} 원</div>
            <div class="">바름 평점:{{ product.bareum_review.average_rating }}({{ product.bareum_review.total_reviews }}) </div>

        </router-link>
    </div>
    <div v-show="popup" class="background bg-white" style="position: fixed; margin-top: 220px; min-height: calc(100vh - 220px); z-index: 1200;">
        <customSearch :selected_option="selected_option" :popup="popup" @close_popup="(close_popup) => popup = close_popup" @selected_items="(option, item) => getOptions(option, item)"></customSearch>
    </div>
</template>

<script>
import { ref, computed,onMounted, onUnmounted } from 'vue';
import { useRouter } from "vue-router";
import searchBar from '../../../components/Navbar/SearchBar.vue';
import customSearch from '../../../components/CustomSearch.vue';
import axios from "axios";

export default {
    components: { searchBar, customSearch },
    setup() {
        const router = useRouter();
        const popup = ref(false);
        const selected_option = ref(null);
        const selected_items = ref([]);
        const dataset = ref(null);
        const page = ref(1);
        const per_page = 10;
        const postTotalPages = ref(1);
        const loader = ref(null);

        const totalRanking = ref([]);
        const rank_title = computed(() => {
            if (selected_items.value.length == 0) {
                return '종합'
            }
            if (selected_option.value == 'personalize') {
                return '부위별'
            }
            if (selected_option.value == 'ingredient') {
                return '성분별'
            }
        });


        const filtered_dataset = computed(() => {
            if (selected_items.value.length == 0 || selected_option.value == null) {
                return dataset.value
            }
            if (selected_option.value == 'personalize') {
                return dataset.value.filter((f) => selected_items.value.includes(f.personalize))
            }
            if (selected_option.value == 'ingredient') {
                return dataset.value.filter((f) => selected_items.value.includes(f.ingredient))
            }
        });
        const age_group = ref('total');

        const open_popup = (params) => {
            if (popup.value == true & selected_option.value == params) {
                popup.value = false;
            }

            else {
                selected_option.value = params;
                popup.value = true;
            }
        };
        const fetchRanking = async() => {
            if(page.value <= postTotalPages.value){
                try{
                const response = await axios.get(`/api/product/total-ranking/?page=${page.value}`);
                totalRanking.value.push(...response.data.results);
                postTotalPages.value = Math.ceil(response.data.count/ per_page);
                page.value+=1;
                }catch(err){
                    console.error(err);
                }
            }
        }
        const fetchDetailRanking = (detail) =>{

        }
        
        const getOptions = (option, items) => {
            console.log(option, items, items.length);

            selected_option.value = option;
            selected_items.value = items;
        };

        
        let observer;
        
        onMounted(async () => {
          await fetchRanking();

          observer = new IntersectionObserver(async (entries, observer) => {
            if (entries[0].isIntersecting) {
              await fetchRanking();
            }
          });

          if (loader.value) {   
            observer.observe(loader.value);
          }
        });

        onUnmounted(() => {
          if (loader.value) {
            observer.unobserve(loader.value);
          }
        });


        return {
            router,
            popup,
            selected_option,
            selected_items,
            dataset,
            filtered_dataset,
            rank_title,
            age_group,
            open_popup,
            getOptions,

            totalRanking,
            fetchDetailRanking,
            fetchRanking,
            loader,
        };
    }
}
</script>

<style>
.rank_box {
    align-self: center;
    justify-self: center;
    display: grid;
    width: 100vw;
    grid-template-columns: 10vw min(27vh, 27vw) 50vw;
    grid-template-rows: 2vh 3vh 3vh 3vh;
    align-content: center;
    margin-bottom: 2vh;
    padding: 5vw;
    font-weight: bold;
    box-shadow: 2px 2px 2px 2px #eeeeee;
}

.rank_order {
    grid-column: 1 / 2;
    grid-row: 1 / 5;
    align-self: center;
}

.rank_image {
    grid-column: 2 / 3;
    grid-row: 1 / 5;
    align-self: center;
    justify-self: center;
    padding: 2vw;
}

.rank_manufacturer {
    grid-column: 3 / 4;
    grid-row: 1 / 2;
    align-self: center;
    justify-self: start;
    padding: 0 5vw;
    font-size: small;
    color: gray;
}

.rank_name {
    grid-column: 3 / 4;
    grid-row: 2 / 3;
    align-self: center;
    justify-self: start;
    padding: 0 5vw;
}

.rank_mount {
    grid-column: 3 / 4;
    grid-row: 3 / 4;
    align-self: center;
    justify-self: start;
    padding: 0 5vw;
}

.rank_price {
    grid-column: 3 / 4;
    grid-row: 4 / 5;
    align-self: center;
    justify-self: start;
    padding: 0 5vw;
}
</style>