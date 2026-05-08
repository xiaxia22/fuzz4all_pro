import { createRouter, createWebHashHistory } from 'vue-router'
import IntroPage from '../views/IntroPage.vue'
import EvidencePage from '../views/EvidencePage.vue'
import ResultsPage from '../views/ResultsPage.vue'
import ClassificationPage from '../views/ClassificationPage.vue'
import CategoryPage from '../views/CategoryPage.vue'

const routes = [
  { path: '/', name: 'intro', component: IntroPage },
  { path: '/evidence', name: 'evidence', component: EvidencePage },
  { path: '/results', name: 'results', component: ResultsPage },
  { path: '/classification', name: 'classification', component: ClassificationPage },
  { path: '/category/:id', name: 'category', component: CategoryPage, props: true },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior () {
    return { top: 0 }
  }
})

export default router
