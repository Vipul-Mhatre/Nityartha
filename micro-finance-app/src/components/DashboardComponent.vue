<template>
  <div class="dashboard">
    <div class="dashboard-grid">
      <!-- Creditworthiness Section -->
      <div class="dashboard-card">
        <h2>Creditworthiness Assessment</h2>
        <form @submit.prevent="assessCreditworthiness" class="assessment-form">
          <div class="form-group">
            <label>Monthly Income</label>
            <input type="number" v-model="creditData.monthlyIncome" required>
          </div>
          <div class="form-group">
            <label>Employment Status</label>
            <select v-model="creditData.employmentStatus" required>
              <option value="employed">Employed</option>
              <option value="self-employed">Self Employed</option>
              <option value="business">Business Owner</option>
            </select>
          </div>
          <div class="form-group">
            <label>Social Score</label>
            <input type="number" v-model="creditData.socialScore" min="0" max="100">
          </div>
          <button type="submit" :disabled="loading">
            {{ loading ? 'Processing...' : 'Assess Creditworthiness' }}
          </button>
        </form>
      </div>

      <!-- ESG Tracking Section -->
      <div class="dashboard-card">
        <h2>ESG Impact Tracking</h2>
        <div class="esg-metrics" v-if="esgData">
          <div class="metric">
            <h4>Environmental Score</h4>
            <div class="score">{{ esgData.environmental }}</div>
          </div>
          <div class="metric">
            <h4>Social Score</h4>
            <div class="score">{{ esgData.social }}</div>
          </div>
          <div class="metric">
            <h4>Governance Score</h4>
            <div class="score">{{ esgData.governance }}</div>
          </div>
        </div>
        <button @click="trackESG" :disabled="loading">
          Update ESG Metrics
        </button>
      </div>

      <!-- Behavioral Analysis Section -->
      <div class="dashboard-card">
        <h2>Behavioral Analysis</h2>
        <div class="behavior-metrics" v-if="behaviorData">
          <div class="metric">
            <h4>Stability Score</h4>
            <div class="score">{{ behaviorData.stability }}</div>
          </div>
          <div class="metric">
            <h4>Risk Level</h4>
            <div class="score">{{ behaviorData.risk }}</div>
          </div>
        </div>
        <button @click="analyzeBehavior" :disabled="loading">
          Analyze Behavior
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DashboardComponent',
  data() {
    return {
      loading: false,
      creditData: {
        monthlyIncome: null,
        employmentStatus: '',
        socialScore: 50
      },
      esgData: {
        environmental: 85,
        social: 75,
        governance: 90
      },
      behaviorData: {
        stability: 'High',
        risk: 'Low'
      }
    }
  },
  methods: {
    async assessCreditworthiness() {
      try {
        this.loading = true
        // Simulate API call with timeout
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        // Mock response
        const score = Math.floor((this.creditData.monthlyIncome / 5000) * 50 + 
                               this.creditData.socialScore * 0.5)
        
        this.$emit('assessment-complete', {
          score: score,
          risk: score > 70 ? 'Low' : score > 40 ? 'Medium' : 'High',
          recommendation: score > 70 ? 'Approved' : 'Review Required'
        })
      } catch (error) {
        console.error('Error assessing creditworthiness:', error)
      } finally {
        this.loading = false
      }
    },
    async trackESG() {
      try {
        this.loading = true
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        // Random fluctuation in ESG scores
        this.esgData = {
          environmental: Math.min(100, this.esgData.environmental + (Math.random() * 10 - 5)),
          social: Math.min(100, this.esgData.social + (Math.random() * 10 - 5)),
          governance: Math.min(100, this.esgData.governance + (Math.random() * 10 - 5))
        }
      } catch (error) {
        console.error('Error tracking ESG:', error)
      } finally {
        this.loading = false
      }
    },
    async analyzeBehavior() {
      try {
        this.loading = true
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        // Update behavior metrics based on credit data
        const stabilityScore = this.creditData.monthlyIncome > 3000 ? 'High' : 'Medium'
        this.behaviorData = {
          stability: stabilityScore,
          risk: stabilityScore === 'High' ? 'Low' : 'Medium'
        }
      } catch (error) {
        console.error('Error analyzing behavior:', error)
      } finally {
        this.loading = false
      }
    }
  },
  mounted() {
    // Initial data load
    this.trackESG()
    this.analyzeBehavior()
  }
}
</script>

<style scoped>
.dashboard {
  padding: 2rem;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.dashboard-card {
  background: var(--background-color);
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 12px var(--shadow-color);
}

.dashboard-card h2 {
  color: var(--primary-color);
  margin-bottom: 1.5rem;
}

.assessment-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-weight: 600;
}

input, select {
  padding: 0.75rem;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  background: var(--background-color);
  color: var(--text-color);
}

button {
  background-color: var(--primary-color);
  color: white;
  padding: 0.75rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: var(--secondary-color);
}

button:disabled {
  background-color: var(--border-color);
  cursor: not-allowed;
}

.esg-metrics,
.behavior-metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.metric {
  text-align: center;
}

.metric h4 {
  margin-bottom: 0.5rem;
  color: var(--text-color);
}

.score {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-color);
}

@media (max-width: 768px) {
  .dashboard {
    padding: 1rem;
  }
  
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
}
</style>
