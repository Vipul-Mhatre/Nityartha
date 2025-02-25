import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Frontend',
    component: () => import('@/components/FrontendComponent.vue')
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('@/components/DashboardComponent.vue')
  },
  {
    path: '/loan-recommendations',
    name: 'LoanRecommendations',
    component: () => import('@/components/LoanRecommendationsComponent.vue')
  },
  {
    path: '/compliance-verification',
    name: 'ComplianceVerification',
    component: () => import('@/components/ComplianceVerificationComponent.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router
