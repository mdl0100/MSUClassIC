import './assets/main.css'

import { createApp } from 'vue';
import App from './App.vue';
import store from './store';  // Ensure the path is correct

import router from './router'

const app = createApp(App)

app.use(router)
app.use(store);
app.mount('#app')
