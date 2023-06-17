import { createApp } from 'vue';
import { createPinia } from 'pinia';
import './style.css';
import App from './App.vue';
import router from './router.js';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import checkSession from './checkSession';
import InfiniteScroll from 'vue-infinite-scroll';

const pinia = createPinia();
const app = createApp(App);

app.use(pinia);
app.use(router);
app.mixin(checkSession);
app.use(InfiniteScroll);



axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.withCredentials = true;

// main.js

app.mount('#app');

