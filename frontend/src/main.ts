import './assets/main.css'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import { useApiService } from './services/apiService';
import bootstrap from 'bootstrap/dist/js/bootstrap.js';

const app = createApp(App);
const pinia = createPinia();

app.use(bootstrap);
app.use(pinia);
app.use(router);


// Inicializa o serviço apiService
useApiService();

app.mount('#app');
