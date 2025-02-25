<template>
  <div class="contact">
    <div class="page-header">
      <h1>Contact Us</h1>
      <p>We're here to help and answer any questions you might have</p>
    </div>

    <div class="grid grid-cols-3 contact-methods">
      <div class="contact-card">
        <div class="icon">
          <i class="fas fa-headset"></i>
        </div>
        <h3>Customer Support</h3>
        <p>24/7 support for all your queries</p>
        <div class="contact-info">
          <div class="info-item">
            <i class="fas fa-phone"></i>
            <span>+91-XXX-XXX-XXXX</span>
          </div>
          <div class="info-item">
            <i class="fas fa-envelope"></i>
            <span>support@microfinance.com</span>
          </div>
        </div>
        <button class="btn btn-primary">
          <i class="fas fa-comments"></i>
          Start Live Chat
        </button>
      </div>

      <div class="contact-card">
        <div class="icon">
          <i class="fas fa-building"></i>
        </div>
        <h3>Business Inquiries</h3>
        <p>Partner with us for business growth</p>
        <div class="contact-info">
          <div class="info-item">
            <i class="fas fa-phone"></i>
            <span>+91-XXX-XXX-XXXX</span>
          </div>
          <div class="info-item">
            <i class="fas fa-envelope"></i>
            <span>business@microfinance.com</span>
          </div>
        </div>
        <button class="btn btn-primary">
          <i class="fas fa-handshake"></i>
          Partner With Us
        </button>
      </div>

      <div class="contact-card">
        <div class="icon">
          <i class="fas fa-newspaper"></i>
        </div>
        <h3>Media Relations</h3>
        <p>Press and media inquiries</p>
        <div class="contact-info">
          <div class="info-item">
            <i class="fas fa-phone"></i>
            <span>+91-XXX-XXX-XXXX</span>
          </div>
          <div class="info-item">
            <i class="fas fa-envelope"></i>
            <span>press@microfinance.com</span>
          </div>
        </div>
        <button class="btn btn-primary">
          <i class="fas fa-newspaper"></i>
          Press Kit
        </button>
      </div>
    </div>

    <div class="grid grid-cols-2 main-content">
      <div class="contact-form-section">
        <h2>Send us a Message</h2>
        <form class="contact-form">
          <div class="form-group">
            <label>Full Name</label>
            <input type="text" class="form-control" placeholder="Enter your name" />
          </div>

          <div class="form-group">
            <label>Email Address</label>
            <input type="email" class="form-control" placeholder="Enter your email" />
          </div>

          <div class="form-group">
            <label>Phone Number</label>
            <input type="tel" class="form-control" placeholder="Enter your phone number" />
          </div>

          <div class="form-group">
            <label>Subject</label>
            <select class="form-control">
              <option>General Inquiry</option>
              <option>Technical Support</option>
              <option>Business Partnership</option>
              <option>Media Inquiry</option>
              <option>Other</option>
            </select>
          </div>

          <div class="form-group">
            <label>Message</label>
            <textarea class="form-control" rows="5" placeholder="Type your message here"></textarea>
          </div>

          <button type="submit" class="btn btn-primary">
            <i class="fas fa-paper-plane"></i>
            Send Message
          </button>
        </form>
      </div>

      <div class="location-section">
        <h2>Visit Our Office</h2>
        <div class="office-details">
          <div class="office-card">
            <div class="office-header">
              <h3>Mumbai Headquarters</h3>
              <span class="badge">Main Office</span>
            </div>
            <div class="office-info">
              <div class="info-row">
                <i class="fas fa-map-marker-alt"></i>
                <p>123 Financial District, Mumbai, Maharashtra 400001</p>
              </div>
              <div class="info-row">
                <i class="fas fa-clock"></i>
                <p>Monday - Friday: 9:00 AM - 6:00 PM</p>
              </div>
              <div class="info-row">
                <i class="fas fa-phone"></i>
                <p>+91-XXX-XXX-XXXX</p>
              </div>
            </div>
          </div>

          <div class="map-container">
            <div class="map-placeholder">
              <i class="fas fa-map"></i>
              <p>Interactive Map</p>
            </div>
          </div>

          <div class="directions">
            <h4>Getting Here</h4>
            <div class="transport-options">
              <div class="transport-option">
                <i class="fas fa-train"></i>
                <span>Nearest Metro: Financial District Station (500m)</span>
              </div>
              <div class="transport-option">
                <i class="fas fa-bus"></i>
                <span>Bus Stop: Central Business Hub (200m)</span>
              </div>
              <div class="transport-option">
                <i class="fas fa-car"></i>
                <span>Parking available in building</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="social-section">
      <h2>Connect With Us</h2>
      <div class="social-links">
        <a href="#" class="social-link">
          <i class="fab fa-linkedin"></i>
          <span>LinkedIn</span>
        </a>
        <a href="#" class="social-link">
          <i class="fab fa-twitter"></i>
          <span>Twitter</span>
        </a>
        <a href="#" class="social-link">
          <i class="fab fa-facebook"></i>
          <span>Facebook</span>
        </a>
        <a href="#" class="social-link">
          <i class="fab fa-instagram"></i>
          <span>Instagram</span>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactView'
}
</script>

<style scoped>
.contact {
  padding: 40px 20px;
}

.page-header {
  text-align: center;
  margin-bottom: 60px;
}

.page-header h1 {
  font-size: 36px;
  color: #2c3e50;
  margin-bottom: 15px;
}

.page-header p {
  color: #64748b;
  font-size: 18px;
}

.contact-methods {
  max-width: 1200px;
  margin: 0 auto 60px;
  gap: 30px;
}

.contact-card {
  background: white;
  border-radius: 8px;
  padding: 30px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.icon {
  width: 60px;
  height: 60px;
  background: #eff6ff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
}

.icon i {
  font-size: 24px;
  color: #3498db;
}

.contact-card h3 {
  margin-bottom: 10px;
  color: #2c3e50;
}

.contact-card p {
  color: #64748b;
  margin-bottom: 20px;
}

.contact-info {
  margin: 20px 0;
}

.info-item {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-bottom: 10px;
}

.info-item i {
  color: #3498db;
}

.main-content {
  max-width: 1200px;
  margin: 0 auto;
  gap: 40px;
}

.contact-form-section, .location-section {
  background: white;
  border-radius: 8px;
  padding: 30px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #2c3e50;
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: #2c3e50;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
  font-size: 14px;
}

textarea.form-control {
  resize: vertical;
}

.office-card {
  background: #f8fafc;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 30px;
}

.office-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.badge {
  background: #eff6ff;
  color: #3498db;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
}

.office-info {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.info-row {
  display: flex;
  gap: 15px;
  color: #64748b;
}

.info-row i {
  color: #3498db;
}

.map-container {
  height: 300px;
  background: #f8fafc;
  border-radius: 8px;
  margin-bottom: 30px;
}

.map-placeholder {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #64748b;
}

.map-placeholder i {
  font-size: 48px;
  margin-bottom: 15px;
}

.directions {
  background: #f8fafc;
  border-radius: 8px;
  padding: 20px;
}

.transport-options {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 15px;
}

.transport-option {
  display: flex;
  align-items: center;
  gap: 15px;
  color: #64748b;
}

.transport-option i {
  color: #3498db;
}

.social-section {
  max-width: 1200px;
  margin: 60px auto 0;
  text-align: center;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-top: 30px;
}

.social-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  color: #64748b;
  text-decoration: none;
  transition: color 0.3s;
}

.social-link:hover {
  color: #3498db;
}

.social-link i {
  font-size: 24px;
}
</style>
