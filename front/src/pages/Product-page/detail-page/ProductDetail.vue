<template>
<div class="background" style="display: flex; flex-direction: column; align-items: center;">
    <nav class="navbar fixed-top bg-white" style="box-shadow: 0 0 1px 1px #EAEAEA;">
        <div class="container-fluid">
            <span class="navbar-brand" @click="$router.back()" style="margin-left: 2vh;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                </svg>
            </span>
            <div style="margin-right: 2vh; font-size: larger; font-weight: bold;">  </div>
            <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
                    <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
                </svg>
            </div>
        </div>
    </nav>
    
    <div class="background bg-whitesmoke" style="display: flex; flex-direction: column; align-items: center; margin-top:56px; min-height: calc(100vh - 56px);">

        <div class="product_card product_head">
            <div class="product_iamge bg-white">
                <img src="https://product.hstatic.net/1000343598/product/381fc8e899a54b16853cfd35117bd052_85c1af13783d419c8dbf90bd51742397_master.png" alt="(상품 이미지)"/>
            </div>
            <div class="manufacturer">
                <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAI6UlEQVR4AZ2XA3RsyRpG91910N3pdIxr+z7btm3btm3bto2xbc+1JjeZdLqT5kHV/8aTTN4a7bW+pYPa5SpRVQCm3/tgUEEMmCgFvw/xV2L6N2F6lyFhoYQNHwP6QM3Tu2q3sdLP7urX5iE0WjWLjO73eXyOb3OCn03+5WaajfycGXRPGzDclFVaBSDgZlFAlyPmrRKEzyMMRxFBwgi1Ifgcl1Qhn64QDawQE91PjHk9xlQR+QXKF4F93Azm5guXd2GiHRIW30IUj0qQIHYOApAgRqIyEvaCJohmIIAVsDJEIG/Eyg7gfbdHoAj6b5BPi7EFREAE8IADFARArguLEcAQAh8HjgIqLGZeFxgBBaCiuZ6mmdksSQL2IARDGB+hUT8YQchQ14WronkLNIAwJAgtFCxODHkC4nM8OWAf6pFzPOaeQPX/C6SKb2YQmFPCsWBzMLISE4+oFIqYogU7C+rQPMC3iuJn5/DN3QSFOezYKrJWROdgrt2DHZKJLvl0ip8oABZLLhHZ2ojuqWA3eyK3SCC5rEYwVv5D6c6lrcGwxZSHMMUBweagdWAS8TtQd0A1HcaVVpMfqJNMVqgfV2HuwrmrBDKcOlEABCXCmBJ2NCIaCynZbH3p0sN/M+3mYxcJ2HL4rMqjVj7Vltv4doomKd7XIQAxDkwE0gemLqbHEy6PJ9Khe3/qsqfud/VW590RuiLASIhF8ShKuKpItLmXcKyIlAL0qiR3HX5MfNTOFwM/XiBQecKGX5hCiKvlYN21haqCCmBBC6iOA5Udoei3KJW/HY8OdpYnU4Sk3+tiX+3hNYrfQiDEd+mntL2fsGQwrTayZwqZ7uBji1/e88NFAmLtIdfIVoqJQVPUp1hiQhNCXIBy8Sh6Kz8gaPyKVo36wTYnnFhnp72SO+dRtpnoaw3yr02Kf8bQfYZe3nfHvkeSdPGXT8OlVcgdFCw2MGDM4UVdoJm7pxr5oPhgU3GgZOkPqhBcRG7P7nbyE/bum5u5YO8kk/U6fz/pSs68uEm13oUABqOYh/gS78iHubv0/G5iqPC7VPOR/l1T9+o7d+puZuvgau40MkolLky1sx3ZxNzHuY4blmL93XORwRL0Bxy8cB8/OmInZ+/tMjmXc7jWZd/hJj7PBVBAQBATYALB4RRxrHBFHisVTu1NaBhHfztnHKFvVZn+coFnbR/nQRuG4OIp+NmZCwX4+4vYMdnkx0fv4Ot/vZy5ZvIt4LlAGVAw2MA2RWSNEX4GPHrektMS5NeJ5K9BnSPlWcBHwKzHiuKcA34G8ooPP2gdLxwqseYP5y0UuPvmcc7fPUOWZQBfjqL4TaAA6bzlrgmsA74BPBJQgOskC8DbgB8CNQDgCkABuYo/Jkn+BnAU4ohON1koICKAEEUhwCFgKbAa2Mctc2fgHOAfwFeA/wJfAz4ICGCADtD2quS5R32+cBBGUcQ8UoCbKfwYYMu8lokAgB/Pq/3rgDdwI98FXmVEiEI7fym+WQRQFlMEygCAzvuPuy4ALWAOkOsyA5ClDsUtFkjTFDBEUTC/RsuAgyzmPgDz5O4CnA28EvgcAPAJ4DMu9zjv5r1qGFjSu1hgZMsAs7ta14nIH+IoeoOiB4DmvKauAluB7wH340YqAMAfgC6AiPSmSYbiieKIqGDZ9vAV3PEpqymMR4sFHvDt7fRMWXb8e4Jzf7P3jd1mUgSeB5QBLGCDMEUEhBXAypuMmR+nafZ9MA8C3Q1+AuA577ov93zSWmabGf3ryjTSLrWZ5mKBrJMzum6A9R8YY+PjlnLmX3e9orqj8QrTCOnM5LQON9A8CwzkwEMB0SDEea5K5gAXhhFZlp0MrFu7bYSnv/Hu3PcZm6jXu9BIqB5s0EwSMnIWC6TpyMRE7f2HDs1sNGMm2PaWlVdKGl80kI6embcqJ11wRd48+5LJPDtcxZxzIDP7Z9B6GwdUBkvc95GreMZr70h1sp2Z0LJq69hoaaD4kH0763ftpm5Nih8wKs4auTz1+glgcsE68IwjHriv0/ErMUJAQMn2XJU+xPbQDnr8JVHPfy7w8oN8tv4HZhsw1SLcXeV1G0Lude9Rlq7vJ0kcIjzF5fryuXr6qE47t14MqYfEKR3naGQ5Lep7v/jgf61ZIPDiY1+shTglrUUYY/FEtAmZ8JbdGUwkGa7Vhm77Iqz5Fjb8fnEpyW/uVaQ4p9F0vfsyo+61ofXbDYoCTi2ZWlJv6DqhlSm2UGO2pfqBB/zFLOiCf3554/Pv8caJn9sVGa2piNmOZdrBVOavXTY7LcgTMH4bQffraOc9bs/yj+3t83q/FQc/YMuyPMks4hUAxZBriPExSkAU5CwfrHFZrYcjjnnCyz7wAG6yFC/9EqxO/9b3pNrjs00NusUE7xPodKHTgTQHHxC4gtrukKRza9CJu1Aphzzxzhfx0NUXs3pgp/bHB6VgZ0AiUh0g9RWaeYXJ9iDH7V7Lb064139q02OP1p/cfeEglGUpOmmfNPv10UtZ07uBZS2l3CaOnIwWi1oOe6nIAB03zM7OuGq3T+hJaRHy13Mex8V7H6Lrhg8zXtmvQ6W9FMIEkZJ0sl6dmBvlgsmlcvLesT247uODJQ0WL8UeZMB5vLuPTsans7e0FhXWDJXYsnRQyoMVGr0FTg4NbZ9Bb53hSsyGkqE3qpFLLDsbGzizfme6PgLxFCSj5L0EPiOS5r71I/V7zzqXhxIvFgBAAaEqZXdnLWZ/KUXBQwZGPPlwylylzeWRZ8pZMJZyT8zaYkBvHKCBpSFQC5rUXIOuBxBKBrAwZvT4vjx/8mxda96BGr35m5FCA3hoJbQf7ClGuYkCOtYyoQa8IHHA8kJAb2TBGqrGsNsJezOYxUAUYCNLQ4w/6PhIS3kQqjVVAFC4GYF5iPAxa81GCe3X68bWZr2AMVRiy2BoCAJLwxgOOaHqoFwIuMtAgQcOFur3GIi/1VewG3PlwzdXSMDNoAqK7hGRN3RF3q/KY7HmgZXQ3KkYmKXemMoMwnROoxAFV9yxEp2/OrbHBSL/rGa+Lsot8j+zDSbLNGGVdgAAAABJRU5ErkJggg==" alt="(제조사 로고)" class="manufacturer_logo"/>
                <span class="manufacturer_name"> {{ product.업소명 }} </span>
            </div>
            <div class="product_name"> {{ product.nutraceuticals_name }} </div>
        </div>
        



        <ul class="commu-menu bg-theme" style="position: sticky; top: 56px;">
            <li class="commu-item">
            <router-link class="commu-link" :to="{name:'productInfoPage', params:{productCode}}" >제품 정보</router-link>

            </li>
            <li class="commu-item" >
            <router-link class="commu-link" :to="{name:'productReviewPage', params:{productCode}}">제품 리뷰</router-link>
            </li>
        </ul>
        
        <router-view></router-view>        
    </div>
</div>
</template>

<script>
import axios from 'axios';
import {ref, onMounted} from 'vue';
export default {
    props:{
        productCode:{
            type:String,
            required:true
        }
    },

    setup(props){
        const product = ref({})
        const fetchProductDetail = async () =>{
            try{
                const response = await axios.get(`/api/product/detail/${props.productCode}/`);
                product.value = response.data;


            }catch(error){
                console.error(error);
            }
        }

        onMounted(() => {
          fetchProductDetail();  
        })

        return{
            fetchProductDetail,
            product
        }
    }
}

</script>

<style>

.product_card {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    background-color: white;
    margin: 1vh 0;
}

.product_head {
    display: flex;
    flex-direction: column;
    align-items: start;
    margin-top: 0;
    padding: 3vh 5vw;
}

.product_iamge {
    align-self: center;
    width: min(100vw, calc(100vh - 56px));
    height: min(100vw, calc(100vh - 56px));
}

.product_iamge img {
    width: min(100vw, calc(100vh - 56px));
    height: min(100vw, calc(100vh - 56px));
}

.manufacturer_logo {
    width: 1.5em;
    height: 1.5em;
    margin: 0.2em;
}

.manufacturer_name {
    font-size: 1em;
}

.product_head .product_name {
    font-size: 2em;
}

</style>