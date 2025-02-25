<template>
  <div class="dashboard">
    <div class="dashboard-header">
      <h1>Dashboard</h1>
      <div class="date-filter">
        <button class="btn btn-outline">
          <i class="fas fa-calendar"></i>
          Last 30 Days
          <i class="fas fa-chevron-down"></i>
        </button>
      </div>
    </div>

    <!-- Key Metrics -->
    <div class="grid grid-cols-4 metrics">
      <div class="metric-card">
        <div class="metric-icon" style="background: rgba(52, 152, 219, 0.1); color: #3498db;">
          <i class="fas fa-chart-line"></i>
        </div>
        <div class="metric-content">
          <h3>Total Loans</h3>
          <p class="metric-value">$2.4M</p>
          <p class="metric-change positive">
            <i class="fas fa-arrow-up"></i>
            12.5% from last month
          </p>
        </div>
      </div>

      <div class="metric-card">
        <div class="metric-icon" style="background: rgba(46, 204, 113, 0.1); color: #2ecc71;">
          <i class="fas fa-check-circle"></i>
        </div>
        <div class="metric-content">
          <h3>Approval Rate</h3>
          <p class="metric-value">85%</p>
          <p class="metric-change positive">
            <i class="fas fa-arrow-up"></i>
            5.2% from last month
          </p>
        </div>
      </div>

      <div class="metric-card">
        <div class="metric-icon" style="background: rgba(241, 196, 15, 0.1); color: #f1c40f;">
          <i class="fas fa-clock"></i>
        </div>
        <div class="metric-content">
          <h3>Processing Time</h3>
          <p class="metric-value">2.3 days</p>
          <p class="metric-change negative">
            <i class="fas fa-arrow-down"></i>
            0.5 days improvement
          </p>
        </div>
      </div>

      <div class="metric-card">
        <div class="metric-icon" style="background: rgba(231, 76, 60, 0.1); color: #e74c3c;">
          <i class="fas fa-exclamation-triangle"></i>
        </div>
        <div class="metric-content">
          <h3>Risk Score</h3>
          <p class="metric-value">Low</p>
          <p class="metric-change neutral">
            <i class="fas fa-minus"></i>
            No change
          </p>
        </div>
      </div>
    </div>

    <!-- Charts Section -->
    <div class="grid grid-cols-2 charts">
      <div class="card">
        <div class="card-header">
          <h2>Loan Distribution</h2>
          <div class="card-actions">
            <button class="btn btn-outline">
              <i class="fas fa-download"></i>
              Export
            </button>
          </div>
        </div>
        <div class="chart">
          <!-- Add Chart.js chart here -->
        </div>
      </div>

      <div class="card">
        <div class="card-header">
          <h2>Risk Analysis</h2>
          <div class="card-actions">
            <button class="btn btn-outline">
              <i class="fas fa-download"></i>
              Export
            </button>
          </div>
        </div>
        <div class="chart">
          <!-- Add Chart.js chart here -->
        </div>
      </div>
    </div>

    <!-- Recent Activities -->
    <div class="card activities">
      <div class="card-header">
        <h2>Recent Activities</h2>
        <div class="card-actions">
          <button class="btn btn-outline">View All</button>
        </div>
      </div>
      <div class="activity-list">
        <div class="activity-item">
          <div class="activity-icon" style="background: rgba(52, 152, 219, 0.1); color: #3498db;">
            <i class="fas fa-file-signature"></i>
          </div>
          <div class="activity-content">
            <h4>New Loan Application</h4>
            <p>John Doe submitted a loan application for $50,000</p>
            <span class="activity-time">2 hours ago</span>
          </div>
          <div class="activity-status pending">Pending</div>
        </div>

        <div class="activity-item">
          <div class="activity-icon" style="background: rgba(46, 204, 113, 0.1); color: #2ecc71;">
            <i class="fas fa-check-circle"></i>
          </div>
          <div class="activity-content">
            <h4>Loan Approved</h4>
            <p>Sarah Smith's loan application was approved</p>
            <span class="activity-time">5 hours ago</span>
          </div>
          <div class="activity-status approved">Approved</div>
        </div>

        <div class="activity-item">
          <div class="activity-icon" style="background: rgba(231, 76, 60, 0.1); color: #e74c3c;">
            <i class="fas fa-times-circle"></i>
          </div>
          <div class="activity-content">
            <h4>Compliance Alert</h4>
            <p>Unusual transaction pattern detected</p>
            <span class="activity-time">1 day ago</span>
          </div>
          <div class="activity-status alert">Alert</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DashboardView'
}
</script>

<style scoped>
.dashboard {
  padding: 20px;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.date-filter {
  display: flex;
  gap: 10px;
}

.metrics {
  margin-bottom: 30px;
}

.metric-card {
  background: white;
  border-radius: 12px;
  padding: 20px;
  display: flex;
  align-items: flex-start;
  gap: 15px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.metric-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
}

.metric-content h3 {
  font-size: 14px;
  color: #64748b;
  margin-bottom: 5px;
}

.metric-value {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 5px;
}

.metric-change {
  font-size: 12px;
  display: flex;
  align-items: center;
  gap: 5px;
}

.metric-change.positive {
  color: #2ecc71;
}

.metric-change.negative {
  color: #e74c3c;
}

.metric-change.neutral {
  color: #95a5a6;
}

.charts {
  margin-bottom: 30px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.card-header h2 {
  font-size: 18px;
  font-weight: 600;
}

.chart {
  height: 300px;
}

.activities {
  margin-bottom: 30px;
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.activity-item {
  display: flex;
  align-items: flex-start;
  gap: 15px;
  padding: 15px;
  border-radius: 8px;
  background: white;
  transition: all 0.3s ease;
}

.activity-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.activity-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
}

.activity-content {
  flex: 1;
}

.activity-content h4 {
  font-size: 16px;
  margin-bottom: 5px;
}

.activity-content p {
  color: #64748b;
  margin-bottom: 5px;
}

.activity-time {
  font-size: 12px;
  color: #94a3b8;
}

.activity-status {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.activity-status.pending {
  background: #fff7ed;
  color: #c2410c;
}

.activity-status.approved {
  background: #f0fdf4;
  color: #166534;
}

.activity-status.alert {
  background: #fef2f2;
  color: #991b1b;
}

.btn-outline {
  border: 1px solid #e2e8f0;
  background: white;
  color: #64748b;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 14px;
  transition: all 0.3s ease;
}

.btn-outline:hover {
  border-color: #cbd5e1;
  background: #f8fafc;
}
</style>
