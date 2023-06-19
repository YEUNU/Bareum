<template lang="">
    <div v-if="popup">
        <customSearch :selected_option="selected_option" :popup="popup" @close_popup="(close_popup) => popup = close_popup" @selected_items="(option, item) => getOptions(option, item)"></customSearch>
    </div>
    <div v-else>
        <nav class="navbar fixed-top bg-white">
            <div class="container-fluid">
                <span class="navbar-brand" @click="$router.back()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"></path>
                    </svg>
                </span>
            </div>
        </nav>
        <div class="bg-white" style="position: fixed; top: 50px; left: 0; width: 100%; z-index: 1030;">
            <h3>{{rank_title}} 제품 순위</h3>
            <div>
                <button class="roundbox bg-theme" style="width: 40%; margin: 3%" @click="open_popup('personalize')">부위별</button>
                <button class="roundbox bg-theme" style="width: 40%; margin: 3%" @click="open_popup('ingredient')">성분별</button>
            </div>
            <select class="roundbox bg-theme" style="width: 86%; border-radius: 4px;" v-model="age_group">
                <option disabled value="">연령대를 선택해 주세요</option>
                <option>total</option>
                <option>age1</option>
                <option>age2</option>
            </select>
            <div v-if="selected_items.length > 0" style="font-weight: bold; text-align: center; font-size: small;">선택항목: {{selected_items.join(', ')}}</div>
            <hr>
        </div>
        <div class="background bg-whitesmoke" style="top: 210px; padding-bottom: 55px; min-height: 70%">
            <div class="rank_box bg-white" v-for="(product, i) in filtered_dataset.sort(function(a, b) { return b[age_group] - a[age_group];})" :key="i">
                <div class="rank_order">{{i+1}}위</div>
                <div class="rank_image"><img class="rank_image" :src=product.img alt="상품이미지" style="height: min(25vh, 25vw); width: min(25vh, 25vw);"/></div>
                <div class="rank_manufacturer">{{product['manufacturer']}}</div>
                <div class="rank_name">{{product['name']}}</div>
                <div class="rank_mount">판매량: {{product[age_group]}}</div>
                <div class="rank_price">가격: {{product['price']}}원</div>
            </div>
        </div>
    </div>

</template>

<script>
import { ref, computed } from 'vue';
import { useRouter } from "vue-router";
import searchBar from '../../../components/Navbar/SearchBar.vue';
import customSearch from '../../../components/CustomSearch.vue';
import axios from "axios";

export default {
    components:{searchBar, customSearch},
    setup() {
        const router = useRouter();
        const popup = ref(false);
        const selected_option = ref(null);
        const selected_items = ref([]);
        const dataset = ref(null);
        const rank_title = computed(() => {
            if(selected_items.value.length == 0) {
                return '종합'
            }

            if(selected_option.value == 'personalize') {
                return '부위별'
            }
            if(selected_option.value == 'ingredient') {
                return '성분별'
            }
        });
        
        
        const filtered_dataset = computed(() => {
            if(selected_items.value.length == 0) {
                return dataset.value
            }
            if(selected_option.value == 'personalize') {
                return dataset.value.filter((f) => selected_items.value.includes(f.personalize))
            }
            if(selected_option.value == 'ingredient') {
                return dataset.value.filter((f) => selected_items.value.includes(f.ingredient))
            }
        });
        const age_group = ref('total');

        const open_popup = (params) => {
            selected_option.value = params;
            popup.value = true;
        }

        const example_data = ref([
            { id: 1, name: '제품1', manufacturer: '제조업체1', personalize: '눈 건강',    ingredient: '오메가3',     price: 3413,     total: 43291,    age1: 5427,     age2: 64,       star: 3.5,
            img: "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcT_CJ0XcjPMVECLcSyUE0r2ruUzKisTcxY8aQaAbekjGHUyJlQnOzsJSeeFdG-QlaW032Pk4oqJl0g02tx4pBlzk7fZV9O0Z8rFrQ7CQQRFo6B0CxagDGBCuYi5vDDXH-ZM1kw&usqp=CAc" },
            { id: 2, name: '제품2', manufacturer: '제조업체2', personalize: '혈당',       ingredient: '비타민c',     price: 888454,   total: 64354,    age1: 7574,     age2: 6458,     star: 4.2,
            img: "https://src.hidoc.co.kr/image/lib/2017/11/27/20171127123357561_0.jpg" },
            { id: 3, name: '제품3', manufacturer: '제조업체3', personalize: '체지방',     ingredient: '칼슘',        price: 68521,    total: 354,      age1: 225,      age2: 8654,     star: 3.1,
            img: "https://mikookvitamin.com/wp-content/uploads/2022/08/1-44.jpg" },
            { id: 4, name: '제품4', manufacturer: '제조업체4', personalize: '혈압',       ingredient: '레시틴',      price: 35488,    total: 6783456,  age1: 58574,    age2: 5648,     star: 2.4,
            img: "https://www.mindpharm.co.kr/shopimages/hsbchong7/010000000558.jpg?1665123386" },
            { id: 5, name: '제품5', manufacturer: '제조업체5', personalize: '간 건강',    ingredient: '쏘팔메토',    price: 676417,   total: 543453,   age1: 547,      age2: 468,      star: 3.9,
            img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuz3Nvk3gHgGE8ty_xDNv1N8IyG1tlI_MgQg&usqp=CAU" },
            { id: 6, name: '제품6', manufacturer: '제조업체6', personalize: '빈혈',       ingredient: '글루코사민',  price: 111,       total: 7545852,  age1: 274,      age2: 84563,   star: 4.0,
            img: "https://blog.kakaocdn.net/dn/ccSTa7/btq2iVJYeeO/MnhO8BM97mX9AKcKVujXrk/img.png" },
            { id: 7, name: '제품7', manufacturer: '제조업체7', personalize: '피로감',     ingredient: '엽산',        price: 564354,   total: 42524,    age1: 23,       age2: 4,        star: 4.6,
            img: "https://wiselycompany.com/web/product/medium/202304/e64cb84719683d853ef26b0a2807274f.png" },
            { id: 8, name: '제품8', manufacturer: '제조업체8', personalize: '피로감',     ingredient: '아연',        price: 54386841, total: 7423,     age1: 78,       age2: 5574,     star: 5.0,
            img: "https://gdimg.gmarket.co.kr/2506504936/still/280?ver=1666777374" },
            { id: 9, name: '제품9', manufacturer: '제조업체9', personalize: '체지방',     ingredient: '마그네슘',    price: 121111,   total: 4755,     age1: 527527,   age2: 15,       star: 3.2,
            img: "https://m.fromvet.com/web/product/big/202012/51436f8621129cdd29f47c2b94fa1b76.png" },
        ]);

        const getRankings = () => {
            return example_data.value
            /*
            axios.get('/data', {
            params: {
                option: selected_option,
                detail: selected_items.join(","), // 체크한 항목들 걍 ','로 붙임
            }
            })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
            */
        };
        
        const getOptions = (option, items) => {
            console.log(option, items, items.length);

            selected_option.value = option;
            selected_items.value = items;
        };

        dataset.value = getRankings();


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
    box-shadow: 0 3px 3px -3px black;
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