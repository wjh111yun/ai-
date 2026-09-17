import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '../views/LoginView.vue'
import DashboardView from '../views/DashboardView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', component: LoginView, meta: { public: true } },
    { path: '/dashboard', component: DashboardView },
  ],
})

router.beforeEach((to) => {
  const has_token = Boolean(localStorage.getItem('access_token'))
  if (!to.meta.public && !has_token) return '/login'
  if (to.path === '/login' && has_token) return '/dashboard'
})

export default router
