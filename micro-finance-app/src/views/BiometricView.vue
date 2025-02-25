<template>
  <div class="biometric">
    <div class="page-header">
      <h1>Biometric Verification</h1>
      <button class="btn btn-primary">
        <i class="fas fa-plus"></i>
        New Verification
      </button>
    </div>

    <div class="grid grid-cols-4 metrics">
      <div class="card">
        <h3>Success Rate</h3>
        <div class="rate">97.5%</div>
        <div class="trend positive">
          <i class="fas fa-arrow-up"></i>
          2.5%
        </div>
      </div>
      
      <div class="card">
        <h3>Verifications Today</h3>
        <div class="count">125</div>
        <div class="trend positive">
          <i class="fas fa-arrow-up"></i>
          15 more
        </div>
      </div>

      <div class="card">
        <h3>Failed Attempts</h3>
        <div class="failures">8</div>
        <div class="trend negative">
          <i class="fas fa-arrow-up"></i>
          2 more
        </div>
      </div>

      <div class="card">
        <h3>Average Time</h3>
        <div class="time">45s</div>
        <div class="trend positive">
          <i class="fas fa-arrow-down"></i>
          10s faster
        </div>
      </div>
    </div>

    <div class="grid grid-cols-2 main-content">
      <div class="card verification-section">
        <h2>Verification Methods</h2>
        <div class="methods-grid">
          <div class="method-card">
            <div class="method-icon">
              <i class="fas fa-fingerprint"></i>
            </div>
            <h3>Fingerprint</h3>
            <p>NIST Level 2 Verification</p>
            <div class="method-stats">
              <div class="stat">
                <span>Success Rate</span>
                <strong>98.5%</strong>
              </div>
              <div class="stat">
                <span>Average Time</span>
                <strong>30s</strong>
              </div>
            </div>
            <button class="btn btn-primary">Start Scan</button>
          </div>

          <div class="method-card">
            <div class="method-icon">
              <i class="fas fa-eye"></i>
            </div>
            <h3>Iris Scan</h3>
            <p>ISO/IEC 19794-6</p>
            <div class="method-stats">
              <div class="stat">
                <span>Success Rate</span>
                <strong>99.2%</strong>
              </div>
              <div class="stat">
                <span>Average Time</span>
                <strong>45s</strong>
              </div>
            </div>
            <button class="btn btn-primary">Start Scan</button>
          </div>

          <div class="method-card">
            <div class="method-icon">
              <i class="fas fa-camera"></i>
            </div>
            <h3>Face Recognition</h3>
            <p>3D Liveness Detection</p>
            <div class="method-stats">
              <div class="stat">
                <span>Success Rate</span>
                <strong>96.8%</strong>
              </div>
              <div class="stat">
                <span>Average Time</span>
                <strong>35s</strong>
              </div>
            </div>
            <button class="btn btn-primary">Start Scan</button>
          </div>

          <div class="method-card">
            <div class="method-icon">
              <i class="fas fa-signature"></i>
            </div>
            <h3>Digital Signature</h3>
            <p>eSign with Aadhaar</p>
            <div class="method-stats">
              <div class="stat">
                <span>Success Rate</span>
                <strong>99.5%</strong>
              </div>
              <div class="stat">
                <span>Average Time</span>
                <strong>60s</strong>
              </div>
            </div>
            <button class="btn btn-primary">Start Process</button>
          </div>
        </div>
      </div>

      <div class="card">
        <h2>Recent Verifications</h2>
        <div class="verifications-list">
          <div class="verification-item success">
            <div class="user-info">
              <div class="user-avatar">
                <i class="fas fa-user"></i>
              </div>
              <div class="user-details">
                <h4>Rahul Sharma</h4>
                <p>Fingerprint Verification</p>
              </div>
            </div>
            <div class="verification-status">
              <span class="status-badge success">Success</span>
              <small>2 mins ago</small>
            </div>
          </div>

          <div class="verification-item failed">
            <div class="user-info">
              <div class="user-avatar">
                <i class="fas fa-user"></i>
              </div>
              <div class="user-details">
                <h4>Priya Patel</h4>
                <p>Face Recognition</p>
              </div>
            </div>
            <div class="verification-status">
              <span class="status-badge failed">Failed</span>
              <small>5 mins ago</small>
            </div>
          </div>

          <div class="verification-item success">
            <div class="user-info">
              <div class="user-avatar">
                <i class="fas fa-user"></i>
              </div>
              <div class="user-details">
                <h4>Amit Kumar</h4>
                <p>Digital Signature</p>
              </div>
            </div>
            <div class="verification-status">
              <span class="status-badge success">Success</span>
              <small>10 mins ago</small>
            </div>
          </div>
        </div>

        <div class="security-metrics">
          <h3>Security Metrics</h3>
          <div class="metrics-grid">
            <div class="metric-item">
              <span>False Accept Rate</span>
              <strong>0.001%</strong>
            </div>
            <div class="metric-item">
              <span>False Reject Rate</span>
              <strong>0.1%</strong>
            </div>
            <div class="metric-item">
              <span>Spoof Detection</span>
              <strong>99.99%</strong>
            </div>
            <div class="metric-item">
              <span>Data Encryption</span>
              <strong>256-bit</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BiometricView'
}
</script>

<style scoped>
.biometric {
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

.rate, .count, .failures, .time {
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

.methods-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 20px;
}

.method-card {
  padding: 20px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background: #f8fafc;
  text-align: center;
}

.method-icon {
  width: 60px;
  height: 60px;
  margin: 0 auto 15px;
  background: #eff6ff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.method-icon i {
  font-size: 24px;
  color: #3498db;
}

.method-stats {
  display: flex;
  justify-content: space-around;
  margin: 15px 0;
}

.stat {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.stat span {
  font-size: 12px;
  color: #64748b;
}

.stat strong {
  font-size: 16px;
  color: #2c3e50;
}

.verifications-list {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.verification-item {
  padding: 15px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 15px;
}

.user-avatar {
  width: 40px;
  height: 40px;
  background: #f1f5f9;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.user-avatar i {
  color: #64748b;
}

.user-details h4 {
  margin: 0;
  color: #2c3e50;
}

.user-details p {
  margin: 0;
  font-size: 14px;
  color: #64748b;
}

.verification-status {
  text-align: right;
}

.status-badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
  margin-bottom: 5px;
}

.status-badge.success {
  background: #f0fdf4;
  color: #166534;
}

.status-badge.failed {
  background: #fef2f2;
  color: #991b1b;
}

.verification-status small {
  display: block;
  color: #64748b;
}

.security-metrics {
  margin-top: 30px;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 15px;
}

.metric-item {
  padding: 15px;
  background: #f8fafc;
  border-radius: 8px;
  text-align: center;
}

.metric-item span {
  display: block;
  font-size: 14px;
  color: #64748b;
  margin-bottom: 5px;
}

.metric-item strong {
  font-size: 18px;
  color: #2c3e50;
}
</style>
