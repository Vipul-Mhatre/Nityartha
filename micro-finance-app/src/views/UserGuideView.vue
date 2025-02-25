<template>
  <div class="user-guide">
    <div class="page-header">
      <h1>User Guide</h1>
      <div class="header-actions">
        <button class="btn btn-outline">
          <i class="fas fa-download"></i>
          Download PDF
        </button>
        <button class="btn btn-primary">
          <i class="fas fa-video"></i>
          Video Tutorials
        </button>
      </div>
    </div>

    <div class="grid grid-cols-4 gap-6">
      <div class="col-span-1">
        <div class="sidebar-nav">
          <div class="search-box">
            <i class="fas fa-search"></i>
            <input type="text" placeholder="Search guides..." />
          </div>
          
          <div class="nav-sections">
            <div class="nav-section">
              <h3>Getting Started</h3>
              <ul>
                <li class="active">Overview</li>
                <li>Quick Start Guide</li>
                <li>System Requirements</li>
              </ul>
            </div>

            <div class="nav-section">
              <h3>Features</h3>
              <ul>
                <li>Loan Management</li>
                <li>Creditworthiness</li>
                <li>ESG Tracking</li>
                <li>Compliance</li>
              </ul>
            </div>

            <div class="nav-section">
              <h3>Security</h3>
              <ul>
                <li>Biometric Verification</li>
                <li>Data Protection</li>
                <li>Privacy Settings</li>
              </ul>
            </div>

            <div class="nav-section">
              <h3>Support</h3>
              <ul>
                <li>FAQs</li>
                <li>Troubleshooting</li>
                <li>Contact Support</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <div class="col-span-3">
        <div class="content-section">
          <div class="breadcrumb">
            Getting Started > Overview
          </div>

          <div class="guide-content">
            <h2>Overview</h2>
            <p class="intro">
              Welcome to the Micro-Finance Application! This comprehensive guide will help you understand
              and utilize all features of our platform effectively.
            </p>

            <div class="feature-cards">
              <div class="feature-card">
                <div class="icon">
                  <i class="fas fa-money-bill-wave"></i>
                </div>
                <h3>Loan Management</h3>
                <p>Process and track loans efficiently</p>
                <a href="#" class="learn-more">Learn More <i class="fas fa-arrow-right"></i></a>
              </div>

              <div class="feature-card">
                <div class="icon">
                  <i class="fas fa-chart-line"></i>
                </div>
                <h3>Credit Assessment</h3>
                <p>Evaluate creditworthiness instantly</p>
                <a href="#" class="learn-more">Learn More <i class="fas fa-arrow-right"></i></a>
              </div>

              <div class="feature-card">
                <div class="icon">
                  <i class="fas fa-shield-alt"></i>
                </div>
                <h3>Compliance</h3>
                <p>Stay compliant with regulations</p>
                <a href="#" class="learn-more">Learn More <i class="fas fa-arrow-right"></i></a>
              </div>
            </div>

            <div class="quick-start">
              <h3>Quick Start Steps</h3>
              <div class="steps">
                <div class="step">
                  <div class="step-number">1</div>
                  <div class="step-content">
                    <h4>Account Setup</h4>
                    <p>Create and verify your account with basic information</p>
                  </div>
                </div>

                <div class="step">
                  <div class="step-number">2</div>
                  <div class="step-content">
                    <h4>KYC Verification</h4>
                    <p>Complete the KYC process with required documents</p>
                  </div>
                </div>

                <div class="step">
                  <div class="step-number">3</div>
                  <div class="step-content">
                    <h4>Explore Features</h4>
                    <p>Navigate through different modules and features</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="video-tutorials">
              <h3>Video Tutorials</h3>
              <div class="video-grid">
                <div class="video-card">
                  <div class="video-thumbnail">
                    <i class="fas fa-play-circle"></i>
                  </div>
                  <h4>Getting Started</h4>
                  <span>5:30 mins</span>
                </div>

                <div class="video-card">
                  <div class="video-thumbnail">
                    <i class="fas fa-play-circle"></i>
                  </div>
                  <h4>Loan Application</h4>
                  <span>8:45 mins</span>
                </div>

                <div class="video-card">
                  <div class="video-thumbnail">
                    <i class="fas fa-play-circle"></i>
                  </div>
                  <h4>ESG Tracking</h4>
                  <span>6:15 mins</span>
                </div>
              </div>
            </div>

            <div class="help-section">
              <h3>Need More Help?</h3>
              <div class="help-options">
                <button class="btn btn-outline">
                  <i class="fas fa-comments"></i>
                  Live Chat
                </button>
                <button class="btn btn-outline">
                  <i class="fas fa-envelope"></i>
                  Email Support
                </button>
                <button class="btn btn-outline">
                  <i class="fas fa-phone"></i>
                  Call Us
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserGuideView'
}
</script>

<style scoped>
.user-guide {
  padding: 20px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.header-actions {
  display: flex;
  gap: 15px;
}

.sidebar-nav {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.search-box {
  position: relative;
  margin-bottom: 20px;
}

.search-box i {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #64748b;
}

.search-box input {
  width: 100%;
  padding: 8px 12px 8px 35px;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
  font-size: 14px;
}

.nav-sections {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.nav-section h3 {
  color: #2c3e50;
  font-size: 16px;
  margin-bottom: 10px;
}

.nav-section ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-section li {
  padding: 8px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  color: #64748b;
}

.nav-section li:hover {
  background: #f8fafc;
  color: #2c3e50;
}

.nav-section li.active {
  background: #eff6ff;
  color: #3498db;
  font-weight: 500;
}

.content-section {
  background: white;
  border-radius: 8px;
  padding: 30px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.breadcrumb {
  color: #64748b;
  font-size: 14px;
  margin-bottom: 20px;
}

.guide-content h2 {
  margin-bottom: 20px;
  color: #2c3e50;
}

.intro {
  font-size: 16px;
  color: #475569;
  margin-bottom: 30px;
}

.feature-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-bottom: 40px;
}

.feature-card {
  padding: 20px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  text-align: center;
}

.feature-card .icon {
  width: 50px;
  height: 50px;
  margin: 0 auto 15px;
  background: #eff6ff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.feature-card .icon i {
  font-size: 20px;
  color: #3498db;
}

.feature-card h3 {
  margin-bottom: 10px;
  color: #2c3e50;
}

.feature-card p {
  color: #64748b;
  margin-bottom: 15px;
}

.learn-more {
  color: #3498db;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
}

.quick-start {
  margin-bottom: 40px;
}

.steps {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 20px;
}

.step {
  display: flex;
  gap: 20px;
  align-items: flex-start;
}

.step-number {
  width: 30px;
  height: 30px;
  background: #eff6ff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3498db;
  font-weight: 600;
}

.step-content h4 {
  margin-bottom: 5px;
  color: #2c3e50;
}

.step-content p {
  color: #64748b;
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 20px;
}

.video-card {
  text-align: center;
}

.video-thumbnail {
  height: 120px;
  background: #f8fafc;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 10px;
}

.video-thumbnail i {
  font-size: 40px;
  color: #3498db;
}

.video-card h4 {
  margin-bottom: 5px;
  color: #2c3e50;
}

.video-card span {
  color: #64748b;
  font-size: 14px;
}

.help-section {
  margin-top: 40px;
  text-align: center;
}

.help-options {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}
</style>
