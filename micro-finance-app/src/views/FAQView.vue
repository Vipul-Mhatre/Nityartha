<template>
  <div class="faq">
    <div class="page-header">
      <h1>Frequently Asked Questions</h1>
      <div class="search-box">
        <i class="fas fa-search"></i>
        <input type="text" placeholder="Search FAQs..." />
      </div>
    </div>

    <div class="grid grid-cols-4 metrics">
      <div class="metric-card">
        <div class="icon">
          <i class="fas fa-book"></i>
        </div>
        <div class="value">200+</div>
        <div class="label">Articles</div>
      </div>

      <div class="metric-card">
        <div class="icon">
          <i class="fas fa-users"></i>
        </div>
        <div class="value">98%</div>
        <div class="label">Resolution Rate</div>
      </div>

      <div class="metric-card">
        <div class="icon">
          <i class="fas fa-clock"></i>
        </div>
        <div class="value">&lt; 2 hours</div>
        <div class="label">Response Time</div>
      </div>

      <div class="metric-card">
        <div class="icon">
          <i class="fas fa-language"></i>
        </div>
        <div class="value">5</div>
        <div class="label">Languages</div>
      </div>
    </div>

    <div class="grid grid-cols-4 gap-6 main-content">
      <div class="col-span-1">
        <div class="categories-sidebar">
          <h3>Categories</h3>
          <ul class="category-list">
            <li class="active">
              <i class="fas fa-home"></i>
              Getting Started
            </li>
            <li>
              <i class="fas fa-money-bill-wave"></i>
              Loans & Financing
            </li>
            <li>
              <i class="fas fa-user-shield"></i>
              Account Security
            </li>
            <li>
              <i class="fas fa-file-alt"></i>
              Documentation
            </li>
            <li>
              <i class="fas fa-chart-line"></i>
              ESG & Compliance
            </li>
            <li>
              <i class="fas fa-mobile-alt"></i>
              Mobile App
            </li>
            <li>
              <i class="fas fa-wallet"></i>
              Payments
            </li>
            <li>
              <i class="fas fa-headset"></i>
              Support
            </li>
          </ul>
        </div>

        <div class="help-card">
          <h3>Need More Help?</h3>
          <p>Can't find what you're looking for?</p>
          <button class="btn btn-primary">
            <i class="fas fa-comments"></i>
            Contact Support
          </button>
        </div>
      </div>

      <div class="col-span-3">
        <div class="faq-section">
          <h2>Getting Started</h2>
          
          <div class="faq-list">
            <div class="faq-item" v-for="(faq, index) in faqs" :key="index">
              <div class="faq-header" @click="toggleFaq(index)">
                <h3>{{ faq.question }}</h3>
                <i class="fas fa-chevron-down" :class="{ 'rotated': faq.isOpen }"></i>
              </div>
              <div class="faq-content" v-show="faq.isOpen">
                <p v-html="faq.answer"></p>
              </div>
            </div>
          </div>
        </div>

        <div class="popular-articles">
          <h2>Popular Articles</h2>
          <div class="articles-grid">
            <div class="article-card">
              <div class="article-icon">
                <i class="fas fa-shield-alt"></i>
              </div>
              <h3>Security Best Practices</h3>
              <p>Learn how to keep your account secure</p>
              <a href="#" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
            </div>

            <div class="article-card">
              <div class="article-icon">
                <i class="fas fa-mobile-alt"></i>
              </div>
              <h3>Mobile App Guide</h3>
              <p>Getting started with our mobile app</p>
              <a href="#" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
            </div>

            <div class="article-card">
              <div class="article-icon">
                <i class="fas fa-chart-pie"></i>
              </div>
              <h3>Understanding ESG Scores</h3>
              <p>How we calculate ESG ratings</p>
              <a href="#" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FAQView',
  data() {
    return {
      faqs: [
        {
          question: 'How do I create an account?',
          answer: 'Creating an account is simple:<br>1. Click on "Sign Up" button<br>2. Enter your personal details<br>3. Verify your email address<br>4. Complete KYC verification',
          isOpen: false
        },
        {
          question: 'What documents do I need for KYC?',
          answer: 'Required documents include:<br>- Government-issued ID (Aadhaar/PAN)<br>- Recent passport-size photograph<br>- Proof of address<br>- Bank statements (last 6 months)',
          isOpen: false
        },
        {
          question: 'How long does the approval process take?',
          answer: 'Our AI-powered system typically processes applications within:<br>- Initial assessment: 5-10 minutes<br>- Document verification: 1-2 hours<br>- Final approval: 24-48 hours',
          isOpen: false
        },
        {
          question: 'What are the eligibility criteria?',
          answer: 'Basic eligibility criteria include:<br>- Age: 21-60 years<br>- Monthly income: ₹25,000+<br>- Credit score: 700+<br>- Employment: 2+ years experience',
          isOpen: false
        }
      ]
    }
  },
  methods: {
    toggleFaq(index) {
      this.faqs[index].isOpen = !this.faqs[index].isOpen;
    }
  }
}
</script>

<style scoped>
.faq {
  padding: 40px 20px;
}

.page-header {
  text-align: center;
  margin-bottom: 60px;
}

.page-header h1 {
  font-size: 36px;
  color: #2c3e50;
  margin-bottom: 20px;
}

.search-box {
  max-width: 600px;
  margin: 0 auto;
  position: relative;
}

.search-box i {
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  color: #64748b;
}

.search-box input {
  width: 100%;
  padding: 15px 20px 15px 50px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 16px;
}

.metrics {
  max-width: 1200px;
  margin: 0 auto 60px;
  gap: 30px;
}

.metric-card {
  background: white;
  border-radius: 8px;
  padding: 30px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.icon {
  width: 50px;
  height: 50px;
  background: #eff6ff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 15px;
}

.icon i {
  font-size: 20px;
  color: #3498db;
}

.value {
  font-size: 28px;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 5px;
}

.label {
  color: #64748b;
}

.main-content {
  max-width: 1200px;
  margin: 0 auto;
}

.categories-sidebar {
  background: white;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 30px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.categories-sidebar h3 {
  color: #2c3e50;
  margin-bottom: 20px;
}

.category-list {
  list-style: none;
  padding: 0;
}

.category-list li {
  padding: 12px 15px;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 12px;
  color: #64748b;
  transition: all 0.3s;
}

.category-list li:hover {
  background: #f8fafc;
  color: #2c3e50;
}

.category-list li.active {
  background: #eff6ff;
  color: #3498db;
  font-weight: 500;
}

.category-list li i {
  width: 20px;
}

.help-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.help-card h3 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.help-card p {
  color: #64748b;
  margin-bottom: 20px;
}

.faq-section {
  background: white;
  border-radius: 8px;
  padding: 30px;
  margin-bottom: 40px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.faq-section h2 {
  color: #2c3e50;
  margin-bottom: 30px;
}

.faq-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.faq-item {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  overflow: hidden;
}

.faq-header {
  padding: 20px;
  background: #f8fafc;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
}

.faq-header h3 {
  color: #2c3e50;
  font-size: 16px;
  margin: 0;
}

.faq-content {
  padding: 20px;
  border-top: 1px solid #e2e8f0;
}

.faq-content p {
  color: #64748b;
  margin-bottom: 15px;
}

.faq-content ul, .faq-content ol {
  padding-left: 20px;
  color: #64748b;
}

.popular-articles h2 {
  color: #2c3e50;
  margin-bottom: 30px;
}

.articles-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

.article-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.article-icon {
  width: 50px;
  height: 50px;
  background: #eff6ff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 15px;
}

.article-icon i {
  font-size: 20px;
  color: #3498db;
}

.article-card h3 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.article-card p {
  color: #64748b;
  margin-bottom: 15px;
}

.read-more {
  color: #3498db;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
}
</style>
