<template>
  <div class="frontend">
    <div class="hero-section">
      <h1>Welcome to Nityartha</h1>
      <p>Empowering financial inclusion through AI-driven solutions</p>
    </div>

    <div class="features-grid">
      <div class="feature-card" v-for="(feature, index) in features" :key="index">
        <h3>{{ feature.title }}</h3>
        <p>{{ feature.description }}</p>
        <router-link :to="feature.route" class="feature-link">
          Learn More
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FrontendComponent',
  data() {
    return {
      features: [
        {
          title: 'Creditworthiness Assessment',
          description: 'Advanced AI-driven credit scoring using alternative data and federated learning',
          route: '/dashboard'
        },
        {
          title: 'Compliance Automation',
          description: 'Automated KYC, document verification, and AML detection',
          route: '/compliance-verification'
        },
        {
          title: 'Loan Recommendations',
          description: 'Personalized loan products based on your profile',
          route: '/loan-recommendations'
        },
        {
          title: 'ESG Impact Tracking',
          description: 'Monitor and optimize your environmental and social impact',
          route: '/dashboard'
        }
      ]
    }
  }
}
</script>

<style scoped>
.frontend {
  padding: 2rem;
}

.hero-section {
  text-align: center;
  margin-bottom: 3rem;
  padding: 4rem 2rem;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
  color: white;
  border-radius: 8px;
}

.hero-section h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.feature-card {
  background: var(--background-color);
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 12px var(--shadow-color);
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-card h3 {
  color: var(--primary-color);
  margin-bottom: 1rem;
}

.feature-link {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background-color: var(--primary-color);
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.feature-link:hover {
  background-color: var(--secondary-color);
}

@media (max-width: 768px) {
  .hero-section {
    padding: 2rem 1rem;
  }

  .hero-section h1 {
    font-size: 2rem;
  }
}
</style>
