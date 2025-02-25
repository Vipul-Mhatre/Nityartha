<template>
  <div id="app">
    <nav class="main-nav">
      <div class="nav-brand">
        <img src="@/assets/logo.png" alt="Logo" class="nav-logo" v-if="false">
        <span class="brand-text">Nityartha</span>
      </div>
      <div class="nav-links">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/dashboard" class="nav-link">Dashboard</router-link>
        <router-link to="/loan-recommendations" class="nav-link">Loans</router-link>
        <router-link to="/compliance-verification" class="nav-link">Compliance</router-link>
      </div>
      <div class="nav-actions">
        <button class="theme-toggle" @click="toggleTheme">
          🌙
        </button>
      </div>
    </nav>
    
    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <footer class="main-footer">
      <p>&copy; {{ currentYear }} Nityartha. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
import { createRouter, createWebHistory } from 'vue-router';
import FrontendComponent from './components/frontend.vue';
import DashboardComponent from './components/Dashboard.vue';
import LoanRecommendations from './components/LoanRecommendations.vue';
import ComplianceVerification from './components/ComplianceVerification.vue';

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
  data() {
    return {
      darkMode: false,
      currentYear: new Date().getFullYear()
    }
  },
  methods: {
    toggleTheme() {
      this.darkMode = !this.darkMode;
      document.body.classList.toggle('dark-theme');
    }
  },
  mounted() {
    // Check system preference for dark mode
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      this.darkMode = true;
      document.body.classList.add('dark-theme');
    }
  },
  router,
};
</script>

<style>
:root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --background-color: #ffffff;
  --text-color: #2c3e50;
  --border-color: #e0e0e0;
  --shadow-color: rgba(0, 0, 0, 0.1);
}

.dark-theme {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --background-color: #1a1a1a;
  --text-color: #ffffff;
  --border-color: #333333;
  --shadow-color: rgba(0, 0, 0, 0.3);
}

body {
  margin: 0;
  padding: 0;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  background-color: var(--background-color);
  color: var(--text-color);
  transition: background-color 0.3s ease, color 0.3s ease;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-nav {
  background-color: var(--background-color);
  box-shadow: 0 2px 10px var(--shadow-color);
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-logo {
  height: 2rem;
}

.brand-text {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-color);
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-link {
  text-decoration: none;
  color: var(--text-color);
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.nav-link:hover,
.nav-link.router-link-active {
  color: var(--primary-color);
  background-color: var(--shadow-color);
}

.theme-toggle {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 50%;
  transition: transform 0.3s ease;
}

.theme-toggle:hover {
  transform: scale(1.1);
}

.main-content {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
  box-sizing: border-box;
}

.main-footer {
  background-color: var(--background-color);
  border-top: 1px solid var(--border-color);
  padding: 1rem;
  text-align: center;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
  }
  
  .main-nav {
    padding: 1rem;
  }
  
  .main-content {
    padding: 1rem;
  }
}
</style>
