<template lang="">
    <div>
        <nav class="navbar fixed-top bg-white">
            <div class="container-fluid">
                <span @click="$router.back()"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"></path>
                    </svg>
                </span>
            </div>
        </nav>
    </div>

    <div class="search_option_items">
        <div class="search_option_item" v-for="part in parts" :key="id">
            <input type="checkbox" :id="part.id" :value="part.text" v-model="part.checked">
            <label :for="part.id">{{part.text}}</label>
        </div>
    </div>
    <button @click='checkArr()'>check</button>
</template>

<script>
import { ref } from "vue"
import { useRouter } from "vue-router";

export default {
    name:"test2",
    setup() {
        let id = 0;
        const router = useRouter();
        const checkedNames = ref([]);
        const parts = ref([
          { id: id++, text: '오메가3', checked: false },
          { id: id++, text: '비타민c', checked: false },
          { id: id++, text: '칼슘', checked: false },
          { id: id++, text: '레시틴', checked: false },
          { id: id++, text: '쏘팔메토', checked: false },
          { id: id++, text: '글루코사민', checked: false },
          { id: id++, text: '엽산', checked: false },
          { id: id++, text: '아연', checked: false },
          { id: id++, text: '마그네슘', checked: false },
        ])
        const checkArr = () => {

            console.log(parts.value.filter((f) => f.checked).map(x => x.text));
            alert(parts.value.filter((f) => f.checked).map(x => x.text));
        }

        return {
            router,
            checkedNames,
            parts,
            checkArr,
        };
    },
}
</script>
<style>

.container {
    width: 100%; /* 화면 너비에 꽉 차도록 설정 */
    height: 100%; /* 화면 높이에 꽉 차도록 설정 */
    display: block;
    margin-bottom: 10%;
}

.search_option_items {
    position: static;

    display: grid;
    align-content: center;
    justify-content: center;
    
    grid-template-columns: 27vw 27vw 27vw;
    grid-template-rows: 27vw 27vw 27vw;
}

.search_option_item {
    position: relative;
    align-content: center;
    justify-content: center;
    
    height: 100%;
    width: 100%;
}

input[type="checkbox"]{
    display: none;
}

input[type="checkbox"] + label{
    display: block;
    width: 24vw;
    height: 24vw;
    margin: 2vw;
    position: relative;
    place-content: center center;
    box-sizing: content-box;
    background-color: aquamarine;
}

input[type="checkbox"]:checked + label{
    display: block;
    width: 24vw;
    height: 24vw;
    margin: 2vw;
    position: relative;
    place-content: center center;
    box-sizing: content-box;
    background-color: #2dce89;

}

</style>