import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import LoginPage from '../pages/Login.vue'
import HomeLayout from '../pages/Home.vue'
import HomeOverview from '../pages/overview-safe.vue'
import PromptPage from '../pages/knowledge-safe.vue'
import TestCasesPage from '../pages/cases-safe.vue'
import BugsPage from '../pages/diff-safe.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    redirect: '/login',
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
  },
  {
    path: '/home',
    component: HomeLayout,
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        name: 'Home',
        component: HomeOverview,
      },
      {
        path: 'prompts',
        name: 'Prompts',
        component: PromptPage,
      },
      {
        path: 'testcases',
        name: 'TestCases',
        component: TestCasesPage,
      },
      {
        path: 'bugs',
        name: 'Bugs',
        component: BugsPage,
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, _from, next) => {
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true'

  if (to.meta.requiresAuth && !isLoggedIn) {
    next({
      name: 'Login',
      query: { redirect: to.fullPath },
    })
    return
  }

  if (to.name === 'Login' && isLoggedIn) {
    const redirect = typeof to.query.redirect === 'string' ? to.query.redirect : '/home'
    next(redirect)
    return
  }

  next()
})

export default router
