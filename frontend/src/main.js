import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'
import Registro from './components/Registro.vue'
import Verificar from './components/Verificar.vue'

const routes = [
    { path: '/', component: Registro },
    { path: '/verificar/:token', component: Verificar }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

createApp(App).use(router).mount('#app')