import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Vuesax from 'vuesax-alpha'
import 'vuesax-alpha/dist/index.css'

const app = createApp(App)
app.use(router)
app.use(Vuesax)
app.mount('#app')
