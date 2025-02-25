<template>
  <div class="compliance-rules">
    <div class="page-header">
      <h1>Compliance Rules</h1>
      <button class="btn btn-primary">
        <i class="fas fa-plus"></i>
        Add New Rule
      </button>
    </div>

    <div class="grid grid-cols-4 metrics">
      <div class="card">
        <h3>Active Rules</h3>
        <div class="count">25</div>
        <div class="trend positive">
          <i class="fas fa-arrow-up"></i>
          3 new
        </div>
      </div>
      
      <div class="card">
        <h3>Compliance Rate</h3>
        <div class="rate">98.5%</div>
        <div class="trend positive">
          <i class="fas fa-arrow-up"></i>
          1.5%
        </div>
      </div>

      <div class="card">
        <h3>Violations</h3>
        <div class="violations">12</div>
        <div class="trend negative">
          <i class="fas fa-arrow-down"></i>
          5 less
        </div>
      </div>

      <div class="card">
        <h3>Last Updated</h3>
        <div class="last-updated">1 day ago</div>
        <p>25 Feb 2025, 15:45 PM</p>
      </div>
    </div>

    <div class="grid grid-cols-3 main-content">
      <div class="card col-span-2">
        <div class="rules-header">
          <h2>Active Rules</h2>
          <div class="filters">
            <select class="form-control">
              <option>All Categories</option>
              <option>KYC</option>
              <option>AML</option>
              <option>Risk Assessment</option>
            </select>
            <input type="text" class="form-control" placeholder="Search rules..." />
          </div>
        </div>

        <div class="rules-list">
          <div class="rule-item">
            <div class="rule-header">
              <h3>KYC Verification</h3>
              <span class="category kyc">KYC</span>
            </div>
            <p>Mandatory verification of customer identity through approved government ID</p>
            <div class="rule-metrics">
              <div class="metric">
                <span>Compliance</span>
                <strong>99.5%</strong>
              </div>
              <div class="metric">
                <span>Violations</span>
                <strong>2</strong>
              </div>
              <div class="metric">
                <span>Priority</span>
                <strong class="high">High</strong>
              </div>
            </div>
            <div class="rule-actions">
              <button class="btn btn-outline">Edit</button>
              <button class="btn btn-outline">View Details</button>
            </div>
          </div>

          <div class="rule-item">
            <div class="rule-header">
              <h3>Transaction Monitoring</h3>
              <span class="category aml">AML</span>
            </div>
            <p>Monitor transactions above ₹50,000 for suspicious activity</p>
            <div class="rule-metrics">
              <div class="metric">
                <span>Compliance</span>
                <strong>98.75%</strong>
              </div>
              <div class="metric">
                <span>Violations</span>
                <strong>5</strong>
              </div>
              <div class="metric">
                <span>Priority</span>
                <strong class="high">High</strong>
              </div>
            </div>
            <div class="rule-actions">
              <button class="btn btn-outline">Edit</button>
              <button class="btn btn-outline">View Details</button>
            </div>
          </div>

          <div class="rule-item">
            <div class="rule-header">
              <h3>Risk Assessment</h3>
              <span class="category risk">Risk</span>
            </div>
            <p>Regular assessment of borrower's credit risk profile</p>
            <div class="rule-metrics">
              <div class="metric">
                <span>Compliance</span>
                <strong>97.25%</strong>
              </div>
              <div class="metric">
                <span>Violations</span>
                <strong>3</strong>
              </div>
              <div class="metric">
                <span>Priority</span>
                <strong class="medium">Medium</strong>
              </div>
            </div>
            <div class="rule-actions">
              <button class="btn btn-outline">Edit</button>
              <button class="btn btn-outline">View Details</button>
            </div>
          </div>
        </div>
      </div>

      <div class="card">
        <h2>Rule Summary</h2>
        <div class="summary-stats">
          <div class="stat-item">
            <h4>By Category</h4>
            <div class="stat-chart">
              <div class="chart-bar">
                <span>KYC</span>
                <div class="bar">
                  <div class="fill" style="width: 40%"></div>
                  <span>10</span>
                </div>
              </div>
              <div class="chart-bar">
                <span>AML</span>
                <div class="bar">
                  <div class="fill" style="width: 32%"></div>
                  <span>8</span>
                </div>
              </div>
              <div class="chart-bar">
                <span>Risk</span>
                <div class="bar">
                  <div class="fill" style="width: 28%"></div>
                  <span>7</span>
                </div>
              </div>
            </div>
          </div>

          <div class="stat-item">
            <h4>By Priority</h4>
            <div class="stat-chart">
              <div class="chart-bar">
                <span>High</span>
                <div class="bar">
                  <div class="fill high" style="width: 48%"></div>
                  <span>12</span>
                </div>
              </div>
              <div class="chart-bar">
                <span>Medium</span>
                <div class="bar">
                  <div class="fill medium" style="width: 36%"></div>
                  <span>9</span>
                </div>
              </div>
              <div class="chart-bar">
                <span>Low</span>
                <div class="bar">
                  <div class="fill low" style="width: 16%"></div>
                  <span>4</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="recent-updates">
          <h4>Recent Updates</h4>
          <div class="updates-list">
            <div class="update-item">
              <i class="fas fa-plus-circle"></i>
              <div class="update-content">
                <p>New KYC rule added</p>
                <small>2 days ago</small>
              </div>
            </div>
            <div class="update-item">
              <i class="fas fa-edit"></i>
              <div class="update-content">
                <p>Modified AML threshold</p>
                <small>3 days ago</small>
              </div>
            </div>
            <div class="update-item">
              <i class="fas fa-trash"></i>
              <div class="update-content">
                <p>Removed duplicate rule</p>
                <small>5 days ago</small>
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
  name: 'ComplianceRulesView'
}
</script>

<style scoped>
.compliance-rules {
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

.count, .rate, .violations, .last-updated {
  font-size: 32px;
  font-weight: 700;
  color: #2c3e50;
  margin: 10px 0;
}

.trend {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 14px;
  font-weight: 500;
}

.trend.positive {
  color: #2ecc71;
}

.trend.negative {
  color: #e74c3c;
}

.main-content {
  gap: 30px;
}

.rules-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.filters {
  display: flex;
  gap: 15px;
}

.rules-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.rule-item {
  padding: 20px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background: #f8fafc;
}

.rule-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.category {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.category.kyc {
  background: #f0fdf4;
  color: #166534;
}

.category.aml {
  background: #eff6ff;
  color: #1e40af;
}

.category.risk {
  background: #fff7ed;
  color: #c2410c;
}

.rule-metrics {
  display: flex;
  gap: 30px;
  margin: 15px 0;
}

.metric {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.metric span {
  font-size: 14px;
  color: #64748b;
}

.metric strong {
  font-size: 16px;
  color: #2c3e50;
}

.metric strong.high {
  color: #e74c3c;
}

.metric strong.medium {
  color: #f39c12;
}

.rule-actions {
  display: flex;
  gap: 15px;
  margin-top: 15px;
}

.summary-stats {
  display: flex;
  flex-direction: column;
  gap: 30px;
  margin-top: 20px;
}

.stat-item h4 {
  margin-bottom: 15px;
  color: #2c3e50;
}

.stat-chart {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.chart-bar {
  display: flex;
  align-items: center;
  gap: 10px;
}

.chart-bar span {
  width: 60px;
  font-size: 14px;
  color: #64748b;
}

.bar {
  flex: 1;
  height: 8px;
  background: #e2e8f0;
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}

.fill {
  height: 100%;
  background: #3498db;
  border-radius: 4px;
}

.fill.high {
  background: #e74c3c;
}

.fill.medium {
  background: #f39c12;
}

.fill.low {
  background: #2ecc71;
}

.bar span {
  position: absolute;
  right: -25px;
  top: -4px;
  font-size: 12px;
  color: #64748b;
}

.recent-updates {
  margin-top: 30px;
}

.updates-list {
  margin-top: 15px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.update-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.update-item i {
  font-size: 16px;
  color: #3498db;
}

.update-content p {
  margin: 0;
  font-size: 14px;
  color: #2c3e50;
}

.update-content small {
  color: #64748b;
}
</style>
