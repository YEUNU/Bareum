<template>

    <div class="bg-white" style="display: flex; flex-direction: column;">
        <!--
            <div class="select_option_box">
                <h2 style="font-weight: bold;">항목선택</h2>
                <div>
                    <label class="option_kind">
                        <input  type="radio" name="options" value="personalize" v-model="selected_option">
                        <span style="border-top-left-radius: 10px; border-bottom-left-radius: 10px;">관심 항목</span>
                    </label>
                
                    <label class="option_kind">
                        <input type="radio" name="options" value="ingredient" v-model="selected_option">
                        <span style="border-top-right-radius: 10px; border-bottom-right-radius: 10px;">영양소</span>
                    </label>
                </div>
            </div>
        -->
        <div class="search_option_items">
            <div class="search_option_item" v-for="part in parts" :key="part.id">
                <input type="checkbox" :id="part.id" :value="part.text" v-model="part.checked">
                <label :for="part.id">{{part.text}}</label>
            </div>
        </div>          
        <button class="roundbox" style="margin-top: 3vh;" @click='sendCheckedItems()'>{{ searchList.length > 0 ? '확인' : '닫기' }}</button>
    </div>
</template>
  
<script>
import { ref, computed } from "vue"
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
            if(props.selected_option == 'ingredient'){
                return ingredient_parts.value
            }
            else{
                return personalize_parts.value
            }
        });

        const searchList = computed(() => {
            return parts.value.filter((f) => f.checked).map(x => x.text);
        });
        
        const sendCheckedItems = () => {

            context.emit("close_popup", false);
            context.emit("selected_items", props.selected_option, searchList.value);
            console.log(searchList.value);

        };

        const closePopup = () => {
            context.emit("close_popup", false);
        };

        return {
            router,
            selected_option,
            searchList,
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

.select_option_box {
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.search_option_items {
    align-self: center;
    display: grid;
    grid-template-columns: min(24vw, 22vh) min(24vw, 22vh) min(24vw, 22vh);
    grid-template-rows: min(24vw, 22vh) min(24vw, 22vh) min(24vw, 22vh);
}

.search_option_item {
    position: relative;
    align-self: center;
    justify-self: center;
    width: min(23vw, 20vh);
    height: min(23vw, 20vh);
}

.option_kind input[type="radio"] {
    display: none;
}

.option_kind input[type="radio"] + span {
    display: inline-block;
    padding: 15px 10px;
    border: 2px solid #2dce89;
    background-color: white;
    text-align: center;
    cursor: pointer;
    color: #6e6e6e;
    font-size: 1.1em;
    text-decoration: none;
    font-weight: 750;
}

.option_kind input[type="radio"]:checked + span {
    background-color: #2dce89;
    color: white;
}

.search_option_item input[type="checkbox"] {
    display: none;
}

.search_option_item input[type="checkbox"] + label{
    display: flex;
    width: min(22vw, 20vh);
    height: min(22vw, 20vh);
    position: relative;
    box-sizing: content-box;
    border-radius: 5pt;
    border: 2px solid #2dce89;
    background-color: white;
    text-align: center;
    justify-content: center;
    align-items: center;
    color: #6e6e6e;
    font-size: 1.1em;
    text-decoration: none;
    font-weight: 750;
}

.search_option_item input[type="checkbox"]:checked + label{
    background-color: #2dce89;
    color: white;
}

</style>