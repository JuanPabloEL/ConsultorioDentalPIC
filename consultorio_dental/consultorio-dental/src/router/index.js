import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import PacientesView from '@/views/PacientesView.vue';
import CitasView from '@/views/CitasView.vue';

const routes = [
  { path: '/', component: HomeView },
  { path: '/login', component: LoginView },
  { path: '/pacientes', component: PacientesView },
  { path: '/citas', component: CitasView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
 // const token = localStorage.getItem('token');
  const rol = localStorage.getItem('rol');

  if (to.meta.role && to.meta.role !== rol) {
    return next('/dashboard');
  }

  next();

});

export default router