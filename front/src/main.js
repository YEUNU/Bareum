import { createApp } from 'vue';
import { createPinia } from 'pinia';
import './style.css';
import App from './App.vue';
import router from './router.js';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import InfiniteScroll from 'vue-infinite-scroll';
import csrf from './csrf';
import Cookies from 'js-cookie';
import { useUserInfo } from './stores';
axios.defaults.withCredentials = true;

const pinia = createPinia();
const app = createApp(App);

app.use(pinia);

const userInfo = useUserInfo();
const fetchUserInfo = async () =>{
  try {
    const response = await axios.get('/api/account/check_session/');
    if (response.data.logged_in) {
      userInfo.userLogin(response.data.member_id,response.data.login_id,response.data.user_name,response.data.profile_img_url);
      userInfo.userAddInfo(response.data.birthday,response.data.gender,response.data.nickname,response.data.weight, response.data.height);

    }
  } catch (error) {
    console.error(error);
    return null;
  }
}

await fetchUserInfo();

app.use(router);
app.use(csrf);
app.use(InfiniteScroll);

app.mount('#app');
