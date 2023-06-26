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
app.use(router);
app.use(csrf);
app.use(InfiniteScroll);

const userInfo = useUserInfo();
async function fetchUserSession() {
    try {
      const response = await axios.get('/api/account/session/');
        userInfo.userLogin();
        userInfo.userAddInfo();
      return response.data;
    } catch (error) {
      console.error(error);
      return null;
    }
  }



app.mount('#app');
