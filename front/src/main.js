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

axios.defaults.withCredentials = true;

const pinia = createPinia();
const app = createApp(App);

app.use(pinia);
app.use(router);
app.use(csrf);
app.use(InfiniteScroll);



app.mount('#app');
