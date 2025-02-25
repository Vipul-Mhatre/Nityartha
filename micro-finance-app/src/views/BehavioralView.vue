<template>
  <div class="behavioral">
    <div class="page-header">
      <h1>Behavioral Analysis</h1>
      <button class="btn btn-primary">
        <i class="fas fa-sync"></i>
        Update Analysis
      </button>
    </div>

    <div class="grid grid-cols-3 metrics">
      <div class="card">
        <h3>Transaction Score</h3>
        <div class="score">8.5</div>
        <div class="score-label good">Excellent</div>
      </div>
      
      <div class="card">
        <h3>Repayment Pattern</h3>
        <div class="pattern positive">
          <i class="fas fa-check-circle"></i>
          Consistent
        </div>
      </div>

      <div class="card">
        <h3>Risk Assessment</h3>
        <div class="risk low">Low Risk</div>
        <p>Based on behavioral patterns</p>
      </div>
    </div>

    <div class="grid grid-cols-2 analysis">
      <div class="card">
        <h2>Transaction History</h2>
        <div class="chart-container">
          <canvas id="transactionChart"></canvas>
        </div>
      </div>

      <div class="card">
        <h2>Payment Timeline</h2>
        <div class="timeline">
          <div class="timeline-item on-time">
            <div class="timeline-icon">
              <i class="fas fa-check"></i>
            </div>
            <div class="timeline-content">
              <h4>EMI Payment - ₹15,000</h4>
              <p>Paid 2 days before due date</p>
              <span>25 Feb 2025</span>
            </div>
          </div>

          <div class="timeline-item on-time">
            <div class="timeline-icon">
              <i class="fas fa-check"></i>
            </div>
            <div class="timeline-content">
              <h4>EMI Payment - ₹15,000</h4>
              <p>Paid on due date</p>
              <span>25 Jan 2025</span>
            </div>
          </div>

          <div class="timeline-item delayed">
            <div class="timeline-icon">
              <i class="fas fa-clock"></i>
            </div>
            <div class="timeline-content">
              <h4>EMI Payment - ₹15,000</h4>
              <p>Paid 3 days after due date</p>
              <span>28 Dec 2024</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="card insights">
      <h2>Behavioral Insights</h2>
      <div class="grid grid-cols-3 insight-cards">
        <div class="insight-card positive">
          <i class="fas fa-calendar-check"></i>
          <h4>Payment Consistency</h4>
          <p>90% payments made on time</p>
        </div>

        <div class="insight-card neutral">
          <i class="fas fa-exchange-alt"></i>
          <h4>Transaction Frequency</h4>
          <p>Average 25 transactions/month</p>
        </div>

        <div class="insight-card positive">
          <i class="fas fa-piggy-bank"></i>
          <h4>Savings Pattern</h4>
          <p>Consistent monthly savings</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BehavioralView'
}
</script>

<style scoped>
.behavioral {
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

.pattern {
  font-size: 24px;
  font-weight: 600;
  margin: 10px 0;
  display: flex;
  align-items: center;
  gap: 10px;
}

.pattern.positive {
  color: #2ecc71;
}

.risk {
  font-size: 24px;
  font-weight: 600;
  margin: 10px 0;
}

.risk.low {
  color: #2ecc71;
}

.analysis {
  margin-bottom: 30px;
}

.chart-container {
  height: 300px;
}

.timeline {
  padding: 20px 0;
}

.timeline-item {
  display: flex;
  gap: 15px;
  padding: 15px 0;
  position: relative;
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: 20px;
  top: 50px;
  bottom: -15px;
  width: 2px;
  background: #e2e8f0;
}

.timeline-item:last-child::before {
  display: none;
}

.timeline-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f8fafc;
  border: 2px solid;
  z-index: 1;
}

.timeline-item.on-time .timeline-icon {
  color: #2ecc71;
  border-color: #2ecc71;
}

.timeline-item.delayed .timeline-icon {
  color: #f1c40f;
  border-color: #f1c40f;
}

.timeline-content {
  flex: 1;
}

.timeline-content h4 {
  margin-bottom: 5px;
}

.timeline-content p {
  color: #64748b;
  margin-bottom: 5px;
}

.timeline-content span {
  font-size: 12px;
  color: #94a3b8;
}

.insights {
  margin-top: 30px;
}

.insight-cards {
  margin-top: 20px;
}

.insight-card {
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

.insight-card i {
  font-size: 24px;
  margin-bottom: 10px;
}

.insight-card.positive {
  background: #f0fdf4;
  color: #166534;
}

.insight-card.neutral {
  background: #f8fafc;
  color: #475569;
}

.insight-card h4 {
  margin-bottom: 10px;
}
</style>
