import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/DashboardView.vue')
  },
  {
    path: '/creditworthiness',
    name: 'CreditworthinessAssessment',
    component: () => import('@/views/CreditworthinessView.vue')
  },
  {
    path: '/compliance',
    name: 'ComplianceVerification',
    component: () => import('@/views/ComplianceView.vue')
  },
  {
    path: '/behavioral',
    name: 'BehavioralAnalysis',
    component: () => import('@/views/BehavioralView.vue')
  },
  {
    path: '/esg',
    name: 'ESGTracking',
    component: () => import('@/views/ESGView.vue')
  },
  {
    path: '/loans',
    name: 'LoanRecommendations',
    component: () => import('@/views/LoanRecommendationsView.vue')
  },
  {
    path: '/train',
    name: 'TrainModels',
    component: () => import('@/views/TrainModelsView.vue')
  },
  {
    path: '/compliance-rules',
    name: 'SetComplianceRule',
    component: () => import('@/views/ComplianceRulesView.vue')
  },
  {
    path: '/biometric',
    name: 'EnrollBiometric',
    component: () => import('@/views/BiometricView.vue')
  },
  {
    path: '/guide',
    name: 'UserGuide',
    component: () => import('@/views/UserGuideView.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/AboutView.vue')
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('@/views/ContactView.vue')
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: () => import('@/views/FAQView.vue')
  },
  {
    path: '/privacy',
    name: 'Privacy',
    component: () => import('@/views/PrivacyView.vue')
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
