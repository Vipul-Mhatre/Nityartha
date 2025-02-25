<template>
  <div class="train-models">
    <div class="page-header">
      <h1>Train Models</h1>
      <button class="btn btn-primary">
        <i class="fas fa-play"></i>
        Start Training
      </button>
    </div>

    <div class="grid grid-cols-4 metrics">
      <div class="card">
        <h3>Model Accuracy</h3>
        <div class="accuracy">95.75%</div>
        <div class="trend positive">
          <i class="fas fa-arrow-up"></i>
          2.5%
        </div>
      </div>
      
      <div class="card">
        <h3>Training Time</h3>
        <div class="time">1.5 hrs</div>
        <div class="trend neutral">
          <i class="fas fa-minus"></i>
          No change
        </div>
      </div>

      <div class="card">
        <h3>Data Points</h3>
        <div class="data-points">25,000</div>
        <div class="trend positive">
          <i class="fas fa-arrow-up"></i>
          5,000
        </div>
      </div>

      <div class="card">
        <h3>Last Trained</h3>
        <div class="last-trained">2 days ago</div>
        <p>25 Feb 2025, 10:30 AM</p>
      </div>
    </div>

    <div class="grid grid-cols-2 main-content">
      <div class="card">
        <h2>Model Performance</h2>
        <div class="model-list">
          <div class="model-item">
            <div class="model-header">
              <h3>Credit Risk Model</h3>
              <span class="status active">Active</span>
            </div>
            <div class="model-metrics">
              <div class="metric">
                <span>Accuracy</span>
                <div class="progress">
                  <div class="progress-bar" style="width: 95%"></div>
                  <span>95.75%</span>
                </div>
              </div>
              <div class="metric">
                <span>Precision</span>
                <div class="progress">
                  <div class="progress-bar" style="width: 92%"></div>
                  <span>92.50%</span>
                </div>
              </div>
              <div class="metric">
                <span>Recall</span>
                <div class="progress">
                  <div class="progress-bar" style="width: 88%"></div>
                  <span>88.25%</span>
                </div>
              </div>
            </div>
          </div>

          <div class="model-item">
            <div class="model-header">
              <h3>Fraud Detection</h3>
              <span class="status training">Training</span>
            </div>
            <div class="model-metrics">
              <div class="metric">
                <span>Accuracy</span>
                <div class="progress">
                  <div class="progress-bar" style="width: 88%"></div>
                  <span>88.50%</span>
                </div>
              </div>
              <div class="metric">
                <span>Precision</span>
                <div class="progress">
                  <div class="progress-bar" style="width: 85%"></div>
                  <span>85.75%</span>
                </div>
              </div>
              <div class="metric">
                <span>Recall</span>
                <div class="progress">
                  <div class="progress-bar" style="width: 82%"></div>
                  <span>82.25%</span>
                </div>
              </div>
            </div>
          </div>

          <div class="model-item">
            <div class="model-header">
              <h3>ESG Assessment</h3>
              <span class="status inactive">Inactive</span>
            </div>
            <div class="model-metrics">
              <div class="metric">
                <span>Accuracy</span>
                <div class="progress">
                  <div class="progress-bar" style="width: 90%"></div>
                  <span>90.25%</span>
                </div>
              </div>
              <div class="metric">
                <span>Precision</span>
                <div class="progress">
                  <div class="progress-bar" style="width: 87%"></div>
                  <span>87.50%</span>
                </div>
              </div>
              <div class="metric">
                <span>Recall</span>
                <div class="progress">
                  <div class="progress-bar" style="width: 85%"></div>
                  <span>85.75%</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="card">
        <h2>Training Configuration</h2>
        <div class="config-form">
          <div class="form-group">
            <label>Select Model</label>
            <select class="form-control">
              <option>Credit Risk Model</option>
              <option>Fraud Detection</option>
              <option>ESG Assessment</option>
            </select>
          </div>

          <div class="form-group">
            <label>Training Data</label>
            <div class="data-selection">
              <div class="data-option selected">
                <input type="checkbox" checked />
                <span>Historical Data</span>
                <small>15,000 records</small>
              </div>
              <div class="data-option">
                <input type="checkbox" checked />
                <span>Recent Transactions</span>
                <small>5,000 records</small>
              </div>
              <div class="data-option">
                <input type="checkbox" checked />
                <span>External Data</span>
                <small>5,000 records</small>
              </div>
            </div>
          </div>

          <div class="form-group">
            <label>Hyperparameters</label>
            <div class="hyperparameters">
              <div class="param-group">
                <label>Learning Rate</label>
                <input type="number" class="form-control" value="0.001" step="0.001" />
              </div>
              <div class="param-group">
                <label>Epochs</label>
                <input type="number" class="form-control" value="100" />
              </div>
              <div class="param-group">
                <label>Batch Size</label>
                <input type="number" class="form-control" value="32" />
              </div>
            </div>
          </div>

          <div class="actions">
            <button class="btn btn-secondary">
              <i class="fas fa-save"></i>
              Save Configuration
            </button>
            <button class="btn btn-primary">
              <i class="fas fa-play"></i>
              Start Training
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TrainModelsView'
}
</script>

<style scoped>
.train-models {
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

.accuracy, .time, .data-points, .last-trained {
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

.trend.neutral {
  color: #95a5a6;
}

.main-content {
  gap: 30px;
}

.model-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.model-item {
  padding: 20px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background: #f8fafc;
}

.model-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.status {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.status.active {
  background: #f0fdf4;
  color: #166534;
}

.status.training {
  background: #fff7ed;
  color: #c2410c;
}

.status.inactive {
  background: #f1f5f9;
  color: #64748b;
}

.model-metrics {
  display: flex;
  flex-direction: column;
  gap: 15px;
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

.progress {
  height: 8px;
  background: #e2e8f0;
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}

.progress-bar {
  height: 100%;
  background: #3498db;
  border-radius: 4px;
}

.progress span {
  position: absolute;
  right: 0;
  top: -20px;
  font-size: 12px;
  color: #64748b;
}

.config-form {
  margin-top: 20px;
}

.data-selection {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.data-option {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
  background: #f8fafc;
}

.data-option.selected {
  border-color: #3498db;
  background: #eff6ff;
}

.data-option small {
  margin-left: auto;
  color: #64748b;
}

.hyperparameters {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
}

.param-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.param-group label {
  font-size: 12px;
  color: #64748b;
}

.actions {
  margin-top: 30px;
  display: flex;
  justify-content: flex-end;
  gap: 15px;
}
</style>
