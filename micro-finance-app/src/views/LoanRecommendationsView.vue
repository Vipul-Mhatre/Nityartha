<template>
  <div class="loan-recommendations">
    <div class="page-header">
      <h1>Loan Recommendations</h1>
      <button class="btn btn-primary">
        <i class="fas fa-plus"></i>
        New Application
      </button>
    </div>

    <div class="grid grid-cols-3 metrics">
      <div class="card">
        <h3>Eligible Amount</h3>
        <div class="amount">₹5,00,000</div>
        <p>Based on credit score</p>
      </div>
      
      <div class="card">
        <h3>Interest Rate</h3>
        <div class="rate">10.5%</div>
        <p>Personalized rate</p>
      </div>

      <div class="card">
        <h3>Tenure Options</h3>
        <div class="tenure">12-60</div>
        <p>Months</p>
      </div>
    </div>

    <div class="grid grid-cols-2 recommendations">
      <div class="card">
        <h2>Recommended Loans</h2>
        <div class="loan-options">
          <div class="loan-option">
            <div class="loan-header">
              <h3>Personal Loan</h3>
              <span class="badge best">Best Match</span>
            </div>
            <div class="loan-details">
              <div class="detail">
                <span>Amount</span>
                <strong>₹3,00,000</strong>
              </div>
              <div class="detail">
                <span>Interest</span>
                <strong>10.5%</strong>
              </div>
              <div class="detail">
                <span>Tenure</span>
                <strong>36 months</strong>
              </div>
              <div class="detail">
                <span>EMI</span>
                <strong>₹9,725</strong>
              </div>
            </div>
            <button class="btn btn-primary">Apply Now</button>
          </div>

          <div class="loan-option">
            <div class="loan-header">
              <h3>Business Loan</h3>
              <span class="badge alternative">Alternative</span>
            </div>
            <div class="loan-details">
              <div class="detail">
                <span>Amount</span>
                <strong>₹5,00,000</strong>
              </div>
              <div class="detail">
                <span>Interest</span>
                <strong>12.75%</strong>
              </div>
              <div class="detail">
                <span>Tenure</span>
                <strong>48 months</strong>
              </div>
              <div class="detail">
                <span>EMI</span>
                <strong>₹13,250</strong>
              </div>
            </div>
            <button class="btn btn-outline">Apply Now</button>
          </div>
        </div>
      </div>

      <div class="card">
        <h2>EMI Calculator</h2>
        <div class="calculator">
          <div class="form-group">
            <label>Loan Amount</label>
            <div class="input-group">
              <span class="input-group-text">₹</span>
              <input type="number" class="form-control" v-model="amount" />
            </div>
          </div>

          <div class="form-group">
            <label>Interest Rate (%)</label>
            <input type="number" class="form-control" v-model="interest" step="0.1" />
          </div>

          <div class="form-group">
            <label>Tenure (months)</label>
            <input type="number" class="form-control" v-model="tenure" />
          </div>

          <div class="emi-details">
            <div class="emi-item">
              <span>Monthly EMI</span>
              <strong>₹9,725</strong>
            </div>
            <div class="emi-item">
              <span>Total Interest</span>
              <strong>₹50,100</strong>
            </div>
            <div class="emi-item">
              <span>Total Amount</span>
              <strong>₹3,50,100</strong>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="card requirements">
      <h2>Eligibility & Documents</h2>
      <div class="grid grid-cols-2">
        <div class="eligibility">
          <h3>Eligibility Criteria</h3>
          <ul>
            <li>
              <i class="fas fa-check"></i>
              Age: 21-60 years
            </li>
            <li>
              <i class="fas fa-check"></i>
              Minimum income: ₹25,000 per month
            </li>
            <li>
              <i class="fas fa-check"></i>
              Credit score: 700+
            </li>
            <li>
              <i class="fas fa-check"></i>
              Employment: 2+ years experience
            </li>
          </ul>
        </div>

        <div class="documents">
          <h3>Required Documents</h3>
          <ul>
            <li>
              <i class="fas fa-file-alt"></i>
              Identity Proof (Aadhaar/PAN)
            </li>
            <li>
              <i class="fas fa-file-alt"></i>
              Address Proof
            </li>
            <li>
              <i class="fas fa-file-alt"></i>
              Income Proof
            </li>
            <li>
              <i class="fas fa-file-alt"></i>
              Bank Statements (6 months)
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoanRecommendationsView',
  data() {
    return {
      amount: 300000,
      interest: 10.5,
      tenure: 36
    }
  }
}
</script>

<style scoped>
.loan-recommendations {
  padding: 20px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.metrics {
  margin-bottom: 30px;
}

.amount, .rate, .tenure {
  font-size: 32px;
  font-weight: 700;
  color: #2c3e50;
  margin: 10px 0;
}

.recommendations {
  margin-bottom: 30px;
}

.loan-options {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 20px;
}

.loan-option {
  padding: 20px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background: #f8fafc;
}

.loan-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.badge {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.badge.best {
  background: #f0fdf4;
  color: #166534;
}

.badge.alternative {
  background: #eff6ff;
  color: #1e40af;
}

.loan-details {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
  margin-bottom: 20px;
}

.detail {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.detail span {
  font-size: 14px;
  color: #64748b;
}

.calculator {
  margin-top: 20px;
}

.input-group {
  display: flex;
  align-items: center;
}

.input-group-text {
  padding: 8px 12px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-right: none;
  border-radius: 4px 0 0 4px;
  color: #64748b;
}

.input-group .form-control {
  border-radius: 0 4px 4px 0;
}

.emi-details {
  margin-top: 20px;
  padding: 20px;
  background: #f8fafc;
  border-radius: 8px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.emi-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
  text-align: center;
}

.emi-item span {
  font-size: 14px;
  color: #64748b;
}

.emi-item strong {
  font-size: 18px;
  color: #2c3e50;
}

.requirements {
  margin-top: 30px;
}

.requirements ul {
  list-style: none;
  padding: 0;
  margin: 20px 0;
}

.requirements li {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 15px;
  color: #475569;
}

.requirements li i {
  color: #2ecc71;
}

.documents li i {
  color: #3498db;
}
</style>
