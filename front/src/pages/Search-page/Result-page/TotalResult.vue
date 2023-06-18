<template>
    <div class="background">
        <div style="position: relative;">
            <div class="result_box" v-for="(product, i) in dataset" :key="i">
                <div class="result_image"><img class="result_image" :src=product.img alt="상품이미지"/></div>
                <div class="result_manufacturer">{{product['manufacturer']}}</div>
                <div class="result_name">{{product['name']}}</div>
                <div class="result_mount">별점: {{product['star']}}</div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    name:"select_item_popup",
    props: {
        selected_option: String,
        query: Array,
    },

    setup(props, context) {
        const selected_option = ref(props.selected_option);
        const searchList = ref(props.query);
        const dataset = ref(null);

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

        dataset.value = example_data.value;

        return {
            searchList,
            selected_option,
            dataset,
            };
    },
}
</script>


<style>

.background {
    position: absolute;
    left: 0;
    top: 60px;
    width: 100vw;
    background-color: whitesmoke;
}

.result_box {
    align-self: center;
    justify-self: center;
    display: grid;
    width: 100vw;
    background-color: white;
	grid-template-columns: min(30vh, 30vw) 60vw;
	grid-template-rows: 2vh 3vh 3vh 4vh;
    align-content: center;
    margin-bottom: 1vh;
    padding: 5vw;
    font-weight: bold;
}


.result_image {
    grid-column: 1 / 2;
	grid-row: 1 / 5;
    height: min(25vh, 25vw);
    width: min(25vh, 25vw);
    align-self: center;
    justify-self: center;
}

.result_manufacturer {
    grid-column: 2 / 3;
    grid-row: 1 / 2;
    align-self: center;
    justify-self: start;
    padding: 0 5vw;
    font-size: small;
    color: gray;
}

.result_name {
    grid-column: 2 / 3;
	grid-row: 2 / 3;
    align-self: center;
    justify-self: start;
    padding: 0 5vw;
    font-size: large;
}

.result_mount {
    grid-column: 2 / 3;
	grid-row: 3 / 4;
    align-self: center;
    justify-self: start;
    padding: 0 5vw;
    font-size: medium;
}

</style>