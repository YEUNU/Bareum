<template lang="">
    <div class="container">
        <nav class="navbar fixed-top bg-white">
            <div class="container-fluid">
                <span class="navbar-brand" @click="closePopup">
                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"></path>
                    </svg>
                </span>
            </div>
        </nav>
    </div>
    
    <div class="select_option">
        <h3>항목선택</h3>
        <div>
            <label class="option_kind">
                <input type="radio" name="options" value="personalize" v-model="selected_option">
                <span>맞춤</span>
            </label>
            
            <label class="option_kind">
                <input type="radio" name="options" value="ingredient" v-model="selected_option  ">
                <span>영양소</span>
            </label>
        </div>
    </div>
    <div class="container">

        <div class="search_option_items">
        <div class="search_option_item" v-for="part in parts" :key="part.id">
                <input type="checkbox" :id="part.id" :value="part.text" v-model="part.checked">
                <label :for="part.id">{{part.text}}</label>
            </div>
        </div>
        <button @click='sendCheckedItems()'>check</button>
    </div>
</template>
  
<script>
import { ref, computed, defineEmits } from "vue"
import { useRouter } from "vue-router";

export default {
    name:"select_item_popup",
    props: {
        selected_option: String,
        popup: Boolean,
    },
    emits: ['close_popup', 'selected_items'],

    setup(props, context) {
        const router = useRouter();
        const selected_option = ref(props.selected_option);
        const popup = ref(props.popup);
        const searchList = ref('');


        const personalize_parts = ref([
            { id: 1, text: '눈 건강', checked: false },
            { id: 2, text: '피로감', checked: false },
            { id: 3, text: '혈중 콜레스테롤', checked: false },
            { id: 4, text: '간 건강', checked: false },
            { id: 5, text: '빈혈', checked: false },
            { id: 6, text: '혈압', checked: false },
            { id: 7, text: '혈당', checked: false },
            { id: 8, text: '뼈 건강', checked: false },
            { id: 9, text: '체지방', checked: false },
        ]);

        const ingredient_parts = ref([
            { id: 1, text: '오메가3', checked: false },
            { id: 2, text: '비타민c', checked: false },
            { id: 3, text: '칼슘', checked: false },
            { id: 4, text: '레시틴', checked: false },
            { id: 5, text: '쏘팔메토', checked: false },
            { id: 6, text: '글루코사민', checked: false },
            { id: 7, text: '엽산', checked: false },
            { id: 8, text: '아연', checked: false },
            { id: 9, text: '마그네슘', checked: false },
        ]);

        const parts = computed(() => {
            if(selected_option.value == 'ingredient'){
                return ingredient_parts.value
            }
            else{
                return personalize_parts.value
            }
        });
        
        const sendCheckedItems = () => {

            searchList.value = parts.value.filter((f) => f.checked).map(x => x.text);

            context.emit("close_popup", false);
            context.emit("selected_items", selected_option.value, searchList.value);
            console.log(searchList.value);

        };

        const closePopup = () => {
            context.emit("close_popup", false);
        };

        return {
            router,
            selected_option,
            popup,
            parts,
            sendCheckedItems,
            closePopup,
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

.select_option {
    display: flex;
    justify-content: space-between;
    align-items: center;

}

.search_option_items {
    position: static;

    display: grid;
    align-content: center;
    justify-content: center;
    
    grid-template-columns: min(22vw, 22vh) min(22vw, 22vh) min(22vw, 22vh);
    grid-template-rows: min(22vw, 22vh) min(22vw, 22vh) min(22vw, 22vh);
}

.search_option_item {
    position: relative;
    align-self: center;
    justify-self: center;
    height: 100%;
    width: 100%;
}

.option_kind input[type="radio"] {
    display: none;
}

.option_kind input[type="radio"] + span {
    display: inline-block;
    padding: 15px 10px;
    border: 1px solid #dfdfdf;
    background-color: #ffffff;
    text-align: center;
    cursor: pointer;
}

.option_kind input[type="radio"]:checked + span {
    background-color: #113a6b;
    color: #ffffff;
}



input[type="checkbox"]{
    display: none;
}

input[type="checkbox"] + label{
    width: min(20vw, 20vh);
    height: min(20vw, 20vh);
    margin: min(1vw, 1vh);
    position: relative;
    box-sizing: content-box;
    background-color: aquamarine;
    justify-self: center;
}

input[type="checkbox"]:checked + label{
    width: min(20vw, 20vh);
    height: min(20vw, 20vh);
    margin: min(1vw, 1vh);
    position: relative;
    box-sizing: content-box;
    background-color: #2dce89;

}

</style>