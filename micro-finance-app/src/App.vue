<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import { createRouter, createWebHistory } from 'vue-router';
import FrontendComponent from './components/frontend.vue';
import DashboardComponent from './components/DashboardComponent.vue';
import LoanRecommendations from './components/LoanRecommendationsComponent.vue';
import ComplianceVerification from './components/ComplianceVerificationComponent.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: FrontendComponent,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardComponent,
  },
  {
    path: '/loan-recommendations',
    name: 'LoanRecommendations',
    component: LoanRecommendations,
  },
  {
    path: '/compliance-verification',
    name: 'ComplianceVerification',
    component: ComplianceVerification,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default {
  name: 'App',
  router,
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
