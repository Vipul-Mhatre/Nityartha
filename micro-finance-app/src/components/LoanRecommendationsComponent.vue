<template>
  <div class="loan-recommendations">
    <h2>Loan Recommendations</h2>
    
    <!-- Loan Search Section -->
    <div class="search-section">
      <div class="search-box">
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Search for specific loan types..."
          @input="searchLoans"
        >
      </div>
      
      <div class="filters">
        <select v-model="selectedRisk">
          <option value="">All Risk Levels</option>
          <option value="low">Low Risk</option>
          <option value="medium">Medium Risk</option>
          <option value="high">High Risk</option>
        </select>
        
        <select v-model="sortBy">
          <option value="amount">Amount</option>
          <option value="interest">Interest Rate</option>
          <option value="duration">Duration</option>
        </select>
      </div>
    </div>

    <!-- Loan Cards -->
    <div class="loans-grid" v-if="loans.length">
      <div 
        v-for="loan in filteredLoans" 
        :key="loan.id" 
        class="loan-card"
        :class="loan.risk"
      >
        <div class="loan-header">
          <h3>{{ loan.name }}</h3>
          <span class="risk-badge">{{ loan.risk }}</span>
        </div>
        
        <div class="loan-details">
          <div class="detail">
            <span class="label">Amount:</span>
            <span class="value">${{ loan.amount }}</span>
          </div>
          <div class="detail">
            <span class="label">Interest Rate:</span>
            <span class="value">{{ loan.interestRate }}%</span>
          </div>
          <div class="detail">
            <span class="label">Duration:</span>
            <span class="value">{{ loan.duration }} months</span>
          </div>
        </div>

        <div class="loan-features">
          <h4>Features:</h4>
          <ul>
            <li v-for="(feature, index) in loan.features" :key="index">
              {{ feature }}
            </li>
          </ul>
        </div>

        <button @click="applyForLoan(loan)" :disabled="loading">
          {{ loading ? 'Processing...' : 'Apply Now' }}
        </button>
      </div>
    </div>

    <div v-else class="no-loans">
      <p>No loan recommendations available at the moment.</p>
    </div>

    <!-- Loan Application Modal -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h3>Apply for {{ selectedLoan?.name }}</h3>
        <form @submit.prevent="submitApplication">
          <div class="form-group">
            <label>Full Name</label>
            <input type="text" v-model="application.fullName" required>
          </div>
          <div class="form-group">
            <label>Email</label>
            <input type="email" v-model="application.email" required>
          </div>
          <div class="form-group">
            <label>Phone</label>
            <input type="tel" v-model="application.phone" required>
          </div>
          <div class="form-actions">
            <button type="button" @click="showModal = false">Cancel</button>
            <button type="submit" :disabled="loading">Submit Application</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoanRecommendationsComponent',
  data() {
    return {
      loans: [
        {
          id: 1,
          name: 'Business Startup Loan',
          amount: 25000,
          interestRate: 8.5,
          duration: 24,
          risk: 'medium',
          features: [
            'No collateral required',
            'Flexible repayment options',
            'Business mentorship included'
          ]
        },
        {
          id: 2,
          name: 'Personal Development Loan',
          amount: 10000,
          interestRate: 7.5,
          duration: 12,
          risk: 'low',
          features: [
            'Low interest rate',
            'Quick approval',
            'No prepayment penalties'
          ]
        },
        {
          id: 3,
          name: 'Agriculture Investment Loan',
          amount: 50000,
          interestRate: 6.5,
          duration: 36,
          risk: 'medium',
          features: [
            'Seasonal repayment structure',
            'Technical assistance included',
            'Weather insurance included'
          ]
        }
      ],
      searchQuery: '',
      selectedRisk: '',
      sortBy: 'amount',
      loading: false,
      showModal: false,
      selectedLoan: null,
      application: {
        fullName: '',
        email: '',
        phone: ''
      }
    }
  },
  computed: {
    filteredLoans() {
      let filtered = [...this.loans]
      
      if (this.searchQuery) {
        filtered = filtered.filter(loan => 
          loan.name.toLowerCase().includes(this.searchQuery.toLowerCase())
        )
      }
      
      if (this.selectedRisk) {
        filtered = filtered.filter(loan => 
          loan.risk === this.selectedRisk
        )
      }
      
      filtered.sort((a, b) => {
        if (this.sortBy === 'amount') {
          return b.amount - a.amount
        } else if (this.sortBy === 'interest') {
          return a.interestRate - b.interestRate
        } else {
          return a.duration - b.duration
        }
      })
      
      return filtered
    }
  },
  methods: {
    async fetchRecommendations() {
      try {
        this.loading = true
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1000))
        // Using the mock data already in the loans array
      } catch (error) {
        console.error('Error fetching loan recommendations:', error)
      } finally {
        this.loading = false
      }
    },
    applyForLoan(loan) {
      this.selectedLoan = loan
      this.showModal = true
    },
    async submitApplication() {
      try {
        this.loading = true
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        this.showModal = false
        this.$emit('application-submitted', {
          loan: this.selectedLoan,
          application: this.application
        })
        
        // Reset form
        this.application = {
          fullName: '',
          email: '',
          phone: ''
        }
      } catch (error) {
        console.error('Error submitting loan application:', error)
      } finally {
        this.loading = false
      }
    }
  },
  mounted() {
    this.fetchRecommendations()
  }
}
</script>

<style scoped>
.loan-recommendations {
  padding: 2rem;
}

h2 {
  color: var(--primary-color);
  margin-bottom: 2rem;
}

.search-section {
  margin-bottom: 2rem;
}

.search-box input {
  width: 100%;
  padding: 1rem;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  margin-bottom: 1rem;
}

.filters {
  display: flex;
  gap: 1rem;
}

.filters select {
  padding: 0.5rem;
  border: 1px solid var(--border-color);
  border-radius: 4px;
}

.loans-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.loan-card {
  background: var(--background-color);
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 12px var(--shadow-color);
}

.loan-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.risk-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
}

.loan-card.low .risk-badge {
  background-color: #2ecc71;
  color: white;
}

.loan-card.medium .risk-badge {
  background-color: #f1c40f;
  color: black;
}

.loan-card.high .risk-badge {
  background-color: #e74c3c;
  color: white;
}

.loan-details {
  margin-bottom: 1.5rem;
}

.detail {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.label {
  color: var(--text-color);
  opacity: 0.8;
}

.value {
  font-weight: 600;
}

.loan-features {
  margin-bottom: 1.5rem;
}

.loan-features ul {
  list-style-type: none;
  padding-left: 0;
}

.loan-features li {
  margin-bottom: 0.5rem;
  padding-left: 1.5rem;
  position: relative;
}

.loan-features li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: var(--primary-color);
}

button {
  width: 100%;
  padding: 0.75rem;
  background-color: var(--primary-color);
  color: white;
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

.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: var(--background-color);
  padding: 2rem;
  border-radius: 8px;
  width: 100%;
  max-width: 500px;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--border-color);
  border-radius: 4px;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 1.5rem;
}

.no-loans {
  text-align: center;
  padding: 2rem;
  background: var(--background-color);
  border-radius: 8px;
  box-shadow: 0 2px 12px var(--shadow-color);
}

@media (max-width: 768px) {
  .loan-recommendations {
    padding: 1rem;
  }
  
  .filters {
    flex-direction: column;
  }
  
  .modal-content {
    margin: 1rem;
  }
}
</style>
