<template>
  <div class="privacy">
    <div class="page-header">
      <h1>Privacy Policy</h1>
      <p>Last updated: February 26, 2025</p>
    </div>

    <div class="privacy-content">
      <div class="content-nav">
        <div class="nav-header">
          <h3>Quick Navigation</h3>
        </div>
        <ul class="nav-links">
          <li v-for="section in sections" :key="section.id" :class="{ active: activeSection === section.id }">
            <a @click="scrollToSection(section.id)">
              <i :class="section.icon"></i>
              {{ section.title }}
            </a>
          </li>
        </ul>
      </div>

      <div class="main-content">
        <section id="introduction" class="content-section">
          <h2>Introduction</h2>
          <div class="section-content">
            <p>
              At Micro Finance App, we take your privacy seriously. This Privacy Policy explains how we collect,
              use, disclose, and safeguard your information when you use our platform.
            </p>
            <div class="info-box">
              <i class="fas fa-info-circle"></i>
              <p>
                Please read this privacy policy carefully. If you do not agree with the terms of this privacy policy,
                please do not access the application.
              </p>
            </div>
          </div>
        </section>

        <section id="information-collection" class="content-section">
          <h2>Information We Collect</h2>
          <div class="section-content">
            <div class="data-category">
              <h3>Personal Information</h3>
              <ul>
                <li>Name and contact details</li>
                <li>Date of birth and gender</li>
                <li>Government-issued identification</li>
                <li>Employment and income information</li>
                <li>Bank account details</li>
              </ul>
            </div>

            <div class="data-category">
              <h3>Technical Information</h3>
              <ul>
                <li>Device information</li>
                <li>IP address and location data</li>
                <li>Browser type and version</li>
                <li>Operating system</li>
                <li>Usage patterns and preferences</li>
              </ul>
            </div>
          </div>
        </section>

        <section id="data-usage" class="content-section">
          <h2>How We Use Your Information</h2>
          <div class="section-content">
            <div class="usage-grid">
              <div class="usage-card">
                <i class="fas fa-user-check"></i>
                <h3>Account Management</h3>
                <p>Creating and maintaining your account, verifying your identity</p>
              </div>

              <div class="usage-card">
                <i class="fas fa-chart-line"></i>
                <h3>Service Improvement</h3>
                <p>Analyzing usage patterns to enhance our platform</p>
              </div>

              <div class="usage-card">
                <i class="fas fa-shield-alt"></i>
                <h3>Security</h3>
                <p>Protecting against fraud and unauthorized access</p>
              </div>

              <div class="usage-card">
                <i class="fas fa-bullhorn"></i>
                <h3>Communication</h3>
                <p>Sending important updates and promotional content</p>
              </div>
            </div>
          </div>
        </section>

        <section id="data-sharing" class="content-section">
          <h2>Information Sharing and Disclosure</h2>
          <div class="section-content">
            <div class="sharing-info">
              <h3>We Share Data With:</h3>
              <ul>
                <li>
                  <i class="fas fa-building"></i>
                  <span>Banking partners for loan processing</span>
                </li>
                <li>
                  <i class="fas fa-gavel"></i>
                  <span>Regulatory authorities as required by law</span>
                </li>
                <li>
                  <i class="fas fa-user-shield"></i>
                  <span>Security service providers for fraud prevention</span>
                </li>
                <li>
                  <i class="fas fa-chart-bar"></i>
                  <span>Analytics partners to improve our services</span>
                </li>
              </ul>
            </div>

            <div class="warning-box">
              <i class="fas fa-exclamation-triangle"></i>
              <div class="warning-content">
                <h4>Important Notice</h4>
                <p>
                  We never sell your personal information to third parties for marketing purposes.
                  Data sharing is strictly limited to necessary business operations and legal requirements.
                </p>
              </div>
            </div>
          </div>
        </section>

        <section id="data-security" class="content-section">
          <h2>Data Security</h2>
          <div class="section-content">
            <div class="security-measures">
              <div class="security-card">
                <i class="fas fa-lock"></i>
                <h3>Encryption</h3>
                <p>256-bit encryption for all data transmission</p>
              </div>

              <div class="security-card">
                <i class="fas fa-server"></i>
                <h3>Secure Storage</h3>
                <p>Data stored in secure, certified facilities</p>
              </div>

              <div class="security-card">
                <i class="fas fa-user-lock"></i>
                <h3>Access Control</h3>
                <p>Strict access controls and authentication</p>
              </div>

              <div class="security-card">
                <i class="fas fa-shield-virus"></i>
                <h3>Regular Audits</h3>
                <p>Periodic security assessments and updates</p>
              </div>
            </div>
          </div>
        </section>

        <section id="user-rights" class="content-section">
          <h2>Your Rights and Choices</h2>
          <div class="section-content">
            <div class="rights-grid">
              <div class="right-card">
                <i class="fas fa-eye"></i>
                <h3>Access</h3>
                <p>View your personal data</p>
              </div>

              <div class="right-card">
                <i class="fas fa-edit"></i>
                <h3>Correction</h3>
                <p>Update incorrect information</p>
              </div>

              <div class="right-card">
                <i class="fas fa-trash-alt"></i>
                <h3>Deletion</h3>
                <p>Request data deletion</p>
              </div>

              <div class="right-card">
                <i class="fas fa-download"></i>
                <h3>Export</h3>
                <p>Download your data</p>
              </div>
            </div>

            <div class="action-box">
              <h3>Exercise Your Rights</h3>
              <p>
                To exercise any of these rights, please contact our Privacy Team at:
                <a href="mailto:privacy@microfinance.com">privacy@microfinance.com</a>
              </p>
              <button class="btn btn-primary">
                <i class="fas fa-envelope"></i>
                Contact Privacy Team
              </button>
            </div>
          </div>
        </section>

        <section id="updates" class="content-section">
          <h2>Policy Updates</h2>
          <div class="section-content">
            <div class="update-info">
              <p>
                We may update this privacy policy from time to time. The updated version will be indicated by an
                updated "Last updated" date and the updated version will be effective as soon as it is accessible.
              </p>
              <div class="notification-box">
                <i class="fas fa-bell"></i>
                <p>
                  Enable notifications to stay informed about privacy policy updates.
                </p>
                <button class="btn btn-secondary">
                  <i class="fas fa-bell"></i>
                  Enable Notifications
                </button>
              </div>
            </div>
          </div>
        </section>

        <section id="contact" class="content-section">
          <h2>Contact Us</h2>
          <div class="section-content">
            <div class="contact-info">
              <p>
                If you have any questions or suggestions about our Privacy Policy, do not hesitate to contact us.
              </p>
              <div class="contact-methods">
                <div class="contact-method">
                  <i class="fas fa-envelope"></i>
                  <h3>Email</h3>
                  <p>privacy@microfinance.com</p>
                </div>
                <div class="contact-method">
                  <i class="fas fa-phone"></i>
                  <h3>Phone</h3>
                  <p>+91-XXX-XXX-XXXX</p>
                </div>
                <div class="contact-method">
                  <i class="fas fa-map-marker-alt"></i>
                  <h3>Address</h3>
                  <p>123 Financial District, Mumbai</p>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PrivacyView',
  data() {
    return {
      activeSection: 'introduction',
      sections: [
        { id: 'introduction', title: 'Introduction', icon: 'fas fa-info-circle' },
        { id: 'information-collection', title: 'Information Collection', icon: 'fas fa-database' },
        { id: 'data-usage', title: 'Data Usage', icon: 'fas fa-tasks' },
        { id: 'data-sharing', title: 'Data Sharing', icon: 'fas fa-share-alt' },
        { id: 'data-security', title: 'Data Security', icon: 'fas fa-shield-alt' },
        { id: 'user-rights', title: 'Your Rights', icon: 'fas fa-user-shield' },
        { id: 'updates', title: 'Updates', icon: 'fas fa-sync' },
        { id: 'contact', title: 'Contact', icon: 'fas fa-envelope' }
      ]
    }
  },
  methods: {
    scrollToSection(sectionId) {
      const element = document.getElementById(sectionId)
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
        this.activeSection = sectionId
      }
    }
  }
}
</script>

<style scoped>
.privacy {
  padding: 40px 20px;
}

.page-header {
  text-align: center;
  margin-bottom: 60px;
}

.page-header h1 {
  font-size: 36px;
  color: #2c3e50;
  margin-bottom: 10px;
}

.page-header p {
  color: #64748b;
}

.privacy-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 40px;
}

.content-nav {
  position: sticky;
  top: 20px;
  height: fit-content;
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.nav-header h3 {
  color: #2c3e50;
  margin-bottom: 20px;
}

.nav-links {
  list-style: none;
  padding: 0;
}

.nav-links li {
  margin-bottom: 10px;
}

.nav-links a {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px;
  color: #64748b;
  text-decoration: none;
  border-radius: 6px;
  transition: all 0.3s;
  cursor: pointer;
}

.nav-links a:hover {
  background: #f8fafc;
  color: #2c3e50;
}

.nav-links li.active a {
  background: #eff6ff;
  color: #3498db;
  font-weight: 500;
}

.content-section {
  background: white;
  border-radius: 8px;
  padding: 30px;
  margin-bottom: 30px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.content-section h2 {
  color: #2c3e50;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 2px solid #e2e8f0;
}

.info-box {
  background: #eff6ff;
  border-radius: 8px;
  padding: 20px;
  display: flex;
  gap: 15px;
  align-items: flex-start;
  margin-top: 20px;
}

.info-box i {
  color: #3498db;
  font-size: 20px;
}

.data-category {
  margin-bottom: 30px;
}

.data-category h3 {
  color: #2c3e50;
  margin-bottom: 15px;
}

.data-category ul {
  list-style: none;
  padding: 0;
}

.data-category ul li {
  padding: 10px 0;
  color: #64748b;
  border-bottom: 1px solid #e2e8f0;
}

.data-category ul li:last-child {
  border-bottom: none;
}

.usage-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.usage-card {
  background: #f8fafc;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
}

.usage-card i {
  font-size: 24px;
  color: #3498db;
  margin-bottom: 15px;
}

.usage-card h3 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.usage-card p {
  color: #64748b;
}

.sharing-info ul {
  list-style: none;
  padding: 0;
}

.sharing-info ul li {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 15px 0;
  border-bottom: 1px solid #e2e8f0;
}

.sharing-info ul li:last-child {
  border-bottom: none;
}

.sharing-info ul li i {
  color: #3498db;
}

.warning-box {
  background: #fff5f5;
  border-radius: 8px;
  padding: 20px;
  display: flex;
  gap: 15px;
  align-items: flex-start;
  margin-top: 30px;
}

.warning-box i {
  color: #e53e3e;
  font-size: 20px;
}

.warning-box h4 {
  color: #e53e3e;
  margin-bottom: 5px;
}

.security-measures {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.security-card {
  background: #f8fafc;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
}

.security-card i {
  font-size: 24px;
  color: #3498db;
  margin-bottom: 15px;
}

.security-card h3 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.security-card p {
  color: #64748b;
}

.rights-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 30px;
}

.right-card {
  background: #f8fafc;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
}

.right-card i {
  font-size: 24px;
  color: #3498db;
  margin-bottom: 15px;
}

.right-card h3 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.right-card p {
  color: #64748b;
}

.action-box {
  background: #eff6ff;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
}

.action-box h3 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.action-box p {
  color: #64748b;
  margin-bottom: 20px;
}

.notification-box {
  background: #f8fafc;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  margin-top: 20px;
}

.notification-box i {
  font-size: 24px;
  color: #3498db;
  margin-bottom: 15px;
}

.contact-methods {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 30px;
}

.contact-method {
  text-align: center;
}

.contact-method i {
  font-size: 24px;
  color: #3498db;
  margin-bottom: 15px;
}

.contact-method h3 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.contact-method p {
  color: #64748b;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-primary {
  background: #3498db;
  color: white;
  border: none;
}

.btn-primary:hover {
  background: #2980b9;
}

.btn-secondary {
  background: #f8fafc;
  color: #3498db;
  border: 1px solid #3498db;
}

.btn-secondary:hover {
  background: #eff6ff;
}
</style>
