<template>
  <div class="app-layout">
    <!-- Sidebar -->
    <nav class="sidebar" :class="{ 'sidebar-collapsed': isSidebarCollapsed }">
      <div class="sidebar-header">
        <i class="fas fa-landmark fa-2x"></i>
        <h1 v-if="!isSidebarCollapsed">Micro Finance</h1>
        <button @click="toggleSidebar" class="collapse-btn">
          <i :class="isSidebarCollapsed ? 'fas fa-chevron-right' : 'fas fa-chevron-left'"></i>
        </button>
      </div>

      <!-- Main Navigation -->
      <div class="nav-section">
        <h2 v-if="!isSidebarCollapsed">Main Features</h2>
        <router-link to="/creditworthiness" class="nav-item" :title="isSidebarCollapsed ? 'Creditworthiness Assessment' : ''">
          <i class="fas fa-chart-line"></i>
          <span v-if="!isSidebarCollapsed">Creditworthiness Assessment</span>
        </router-link>
        <router-link to="/compliance" class="nav-item" :title="isSidebarCollapsed ? 'Compliance Verification' : ''">
          <i class="fas fa-shield-alt"></i>
          <span v-if="!isSidebarCollapsed">Compliance Verification</span>
        </router-link>
        <router-link to="/behavioral" class="nav-item" :title="isSidebarCollapsed ? 'Behavioral Analysis' : ''">
          <i class="fas fa-brain"></i>
          <span v-if="!isSidebarCollapsed">Behavioral Analysis</span>
        </router-link>
        <router-link to="/esg" class="nav-item" :title="isSidebarCollapsed ? 'ESG Tracking' : ''">
          <i class="fas fa-leaf"></i>
          <span v-if="!isSidebarCollapsed">ESG Tracking</span>
        </router-link>
        <router-link to="/loans" class="nav-item" :title="isSidebarCollapsed ? 'Loan Recommendations' : ''">
          <i class="fas fa-hand-holding-usd"></i>
          <span v-if="!isSidebarCollapsed">Loan Recommendations</span>
        </router-link>
        <router-link to="/" class="nav-item" :title="isSidebarCollapsed ? 'Dashboard' : ''">
          <i class="fas fa-tachometer-alt"></i>
          <span v-if="!isSidebarCollapsed">Dashboard</span>
        </router-link>
      </div>

      <!-- Administrative Tools -->
      <div class="nav-section">
        <h2 v-if="!isSidebarCollapsed">Admin Tools</h2>
        <router-link to="/train" class="nav-item" :title="isSidebarCollapsed ? 'Train Models' : ''">
          <i class="fas fa-cogs"></i>
          <span v-if="!isSidebarCollapsed">Train Models</span>
        </router-link>
        <router-link to="/compliance-rules" class="nav-item" :title="isSidebarCollapsed ? 'Set Compliance Rule' : ''">
          <i class="fas fa-gavel"></i>
          <span v-if="!isSidebarCollapsed">Set Compliance Rule</span>
        </router-link>
        <router-link to="/biometric" class="nav-item" :title="isSidebarCollapsed ? 'Enroll Biometric' : ''">
          <i class="fas fa-fingerprint"></i>
          <span v-if="!isSidebarCollapsed">Enroll Biometric</span>
        </router-link>
      </div>

      <!-- Help & Support -->
      <div class="nav-section">
        <h2 v-if="!isSidebarCollapsed">Help & Support</h2>
        <router-link to="/guide" class="nav-item" :title="isSidebarCollapsed ? 'User Guide' : ''">
          <i class="fas fa-book"></i>
          <span v-if="!isSidebarCollapsed">User Guide</span>
        </router-link>
        <router-link to="/about" class="nav-item" :title="isSidebarCollapsed ? 'About Us' : ''">
          <i class="fas fa-info-circle"></i>
          <span v-if="!isSidebarCollapsed">About Us</span>
        </router-link>
        <router-link to="/contact" class="nav-item" :title="isSidebarCollapsed ? 'Contact Us' : ''">
          <i class="fas fa-envelope"></i>
          <span v-if="!isSidebarCollapsed">Contact Us</span>
        </router-link>
        <router-link to="/faq" class="nav-item" :title="isSidebarCollapsed ? 'FAQ' : ''">
          <i class="fas fa-question-circle"></i>
          <span v-if="!isSidebarCollapsed">FAQ</span>
        </router-link>
        <router-link to="/privacy" class="nav-item" :title="isSidebarCollapsed ? 'Privacy Policy' : ''">
          <i class="fas fa-lock"></i>
          <span v-if="!isSidebarCollapsed">Privacy Policy</span>
        </router-link>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="main-content" :class="{ 'main-content-expanded': isSidebarCollapsed }">
      <header class="top-bar">
        <div class="search-bar">
          <i class="fas fa-search"></i>
          <input type="text" placeholder="Search..." />
        </div>
        <div class="user-menu">
          <div class="notifications">
            <i class="fas fa-bell"></i>
            <span class="badge">3</span>
          </div>
          <div class="user-profile">
            <i class="fas fa-user-circle fa-2x"></i>
            <span v-if="!isSidebarCollapsed">John Doe</span>
          </div>
        </div>
      </header>

      <div class="content">
        <slot></slot>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'AppLayout',
  data() {
    return {
      isSidebarCollapsed: false
    }
  },
  methods: {
    toggleSidebar() {
      this.isSidebarCollapsed = !this.isSidebarCollapsed
    }
  }
}
</script>

<style scoped>
.app-layout {
  display: flex;
  min-height: 100vh;
  background-color: #f8f9fa;
}

.sidebar {
  width: 280px;
  background: #2c3e50;
  color: white;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.sidebar-collapsed {
  width: 70px;
}

.sidebar-header {
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.collapse-btn {
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px;
}

.nav-section {
  padding: 20px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.nav-section h2 {
  padding: 0 20px;
  font-size: 0.8em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.5);
  margin-bottom: 10px;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 12px 20px;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: all 0.3s ease;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.nav-item.router-link-active {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border-left: 3px solid #3498db;
}

.nav-item i {
  width: 24px;
  margin-right: 10px;
  text-align: center;
}

.main-content {
  flex: 1;
  transition: all 0.3s ease;
  margin-left: 280px;
}

.main-content-expanded {
  margin-left: 70px;
}

.top-bar {
  background: white;
  padding: 15px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.search-bar {
  display: flex;
  align-items: center;
  background: #f8f9fa;
  padding: 8px 15px;
  border-radius: 20px;
}

.search-bar input {
  border: none;
  background: none;
  margin-left: 10px;
  outline: none;
  width: 200px;
}

.user-menu {
  display: flex;
  align-items: center;
  gap: 20px;
}

.notifications {
  position: relative;
}

.badge {
  position: absolute;
  top: -8px;
  right: -8px;
  background: #e74c3c;
  color: white;
  border-radius: 50%;
  padding: 4px 8px;
  font-size: 0.7em;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 10px;
}

.content {
  padding: 30px;
}

@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    z-index: 1000;
    transform: translateX(-100%);
  }

  .sidebar.active {
    transform: translateX(0);
  }

  .main-content {
    margin-left: 0;
  }
}
</style>
