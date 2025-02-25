<template>
  <div class="creditworthiness">
    <div class="page-header">
      <h1>Creditworthiness Assessment</h1>
      <button class="btn btn-primary">
        <i class="fas fa-plus"></i>
        New Assessment
      </button>
    </div>

    <div class="grid grid-cols-3 metrics">
      <div class="card">
        <h3>Credit Score</h3>
        <div class="score">750</div>
        <div class="score-label good">Good</div>
      </div>
      
      <div class="card">
        <h3>Risk Level</h3>
        <div class="risk low">Low Risk</div>
        <p>Based on historical data and behavior</p>
      </div>

      <div class="card">
        <h3>Eligibility</h3>
        <div class="eligibility-amount">₹5,00,000</div>
        <p>Maximum eligible amount</p>
      </div>
    </div>

    <div class="card assessment-form">
      <h2>Assessment Details</h2>
      <div class="form-grid">
        <div class="form-group">
          <label>Full Name</label>
          <input type="text" class="form-control" placeholder="Enter full name" />
        </div>
        
        <div class="form-group">
          <label>PAN Number</label>
          <input type="text" class="form-control" placeholder="Enter PAN number" />
        </div>

        <div class="form-group">
          <label>Annual Income</label>
          <input type="number" class="form-control" placeholder="Enter annual income" />
        </div>

        <div class="form-group">
          <label>Employment Type</label>
          <select class="form-control">
            <option>Salaried</option>
            <option>Self-employed</option>
            <option>Business Owner</option>
          </select>
        </div>
      </div>

      <div class="actions">
        <button class="btn btn-secondary">
          <i class="fas fa-calculator"></i>
          Calculate Score
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CreditworthinessView'
}
</script>

<style scoped>
.creditworthiness {
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

.score {
  font-size: 48px;
  font-weight: 700;
  color: #2c3e50;
  margin: 10px 0;
}

.score-label {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 20px;
  font-weight: 500;
}

.score-label.good {
  background: #f0fdf4;
  color: #166534;
}

.risk {
  font-size: 24px;
  font-weight: 600;
  margin: 10px 0;
}

.risk.low {
  color: #2ecc71;
}

.eligibility-amount {
  font-size: 32px;
  font-weight: 700;
  color: #3498db;
  margin: 10px 0;
}

.assessment-form {
  margin-top: 30px;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin: 20px 0;
}

.actions {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
}
</style>
