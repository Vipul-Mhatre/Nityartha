<template>
  <div class="esg">
    <div class="page-header">
      <h1>ESG Tracking</h1>
      <button class="btn btn-primary">
        <i class="fas fa-plus"></i>
        New Assessment
      </button>
    </div>

    <div class="grid grid-cols-3 metrics">
      <div class="card">
        <h3>Overall ESG Score</h3>
        <div class="score">85.5</div>
        <div class="score-label excellent">Excellent</div>
      </div>
      
      <div class="card">
        <h3>Carbon Footprint</h3>
        <div class="footprint low">
          <i class="fas fa-leaf"></i>
          12.5 tCO2e
        </div>
        <p>Annual emissions</p>
      </div>

      <div class="card">
        <h3>Social Impact</h3>
        <div class="impact positive">
          <i class="fas fa-users"></i>
          High Impact
        </div>
        <p>Community engagement score</p>
      </div>
    </div>

    <div class="grid grid-cols-3 categories">
      <div class="card">
        <div class="category-header">
          <h2>Environmental</h2>
          <div class="category-score">90.25</div>
        </div>
        <div class="category-metrics">
          <div class="metric">
            <span>Energy Usage</span>
            <div class="progress">
              <div class="progress-bar" style="width: 85%"></div>
            </div>
          </div>
          <div class="metric">
            <span>Waste Management</span>
            <div class="progress">
              <div class="progress-bar" style="width: 92%"></div>
            </div>
          </div>
          <div class="metric">
            <span>Resource Efficiency</span>
            <div class="progress">
              <div class="progress-bar" style="width: 78%"></div>
            </div>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="category-header">
          <h2>Social</h2>
          <div class="category-score">88.75</div>
        </div>
        <div class="category-metrics">
          <div class="metric">
            <span>Employee Welfare</span>
            <div class="progress">
              <div class="progress-bar" style="width: 89%"></div>
            </div>
          </div>
          <div class="metric">
            <span>Community Impact</span>
            <div class="progress">
              <div class="progress-bar" style="width: 95%"></div>
            </div>
          </div>
          <div class="metric">
            <span>Supply Chain</span>
            <div class="progress">
              <div class="progress-bar" style="width: 82%"></div>
            </div>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="category-header">
          <h2>Governance</h2>
          <div class="category-score">82.50</div>
        </div>
        <div class="category-metrics">
          <div class="metric">
            <span>Board Diversity</span>
            <div class="progress">
              <div class="progress-bar" style="width: 75%"></div>
            </div>
          </div>
          <div class="metric">
            <span>Ethics & Compliance</span>
            <div class="progress">
              <div class="progress-bar" style="width: 88%"></div>
            </div>
          </div>
          <div class="metric">
            <span>Risk Management</span>
            <div class="progress">
              <div class="progress-bar" style="width: 85%"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="card initiatives">
      <h2>Sustainability Initiatives</h2>
      <div class="grid grid-cols-4 initiative-cards">
        <div class="initiative-card">
          <i class="fas fa-solar-panel"></i>
          <h4>Solar Power</h4>
          <p>40% energy from renewable sources</p>
        </div>

        <div class="initiative-card">
          <i class="fas fa-recycle"></i>
          <h4>Waste Reduction</h4>
          <p>85% waste recycled</p>
        </div>

        <div class="initiative-card">
          <i class="fas fa-hand-holding-heart"></i>
          <h4>Community Programs</h4>
          <p>25 active programs</p>
        </div>

        <div class="initiative-card">
          <i class="fas fa-building"></i>
          <h4>Green Buildings</h4>
          <p>LEED Platinum certified</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ESGView'
}
</script>

<style scoped>
.esg {
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

.score-label.excellent {
  background: #f0fdf4;
  color: #166534;
}

.footprint, .impact {
  font-size: 24px;
  font-weight: 600;
  margin: 10px 0;
  display: flex;
  align-items: center;
  gap: 10px;
}

.footprint.low {
  color: #2ecc71;
}

.impact.positive {
  color: #3498db;
}

.categories {
  margin-bottom: 30px;
}

.category-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.category-score {
  font-size: 24px;
  font-weight: 700;
  color: #2c3e50;
}

.category-metrics {
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
}

.progress-bar {
  height: 100%;
  background: #3498db;
  border-radius: 4px;
}

.initiatives {
  margin-top: 30px;
}

.initiative-cards {
  margin-top: 20px;
}

.initiative-card {
  padding: 20px;
  border-radius: 8px;
  background: #f8fafc;
  text-align: center;
}

.initiative-card i {
  font-size: 24px;
  color: #3498db;
  margin-bottom: 10px;
}

.initiative-card h4 {
  margin-bottom: 10px;
  color: #2c3e50;
}

.initiative-card p {
  color: #64748b;
  font-size: 14px;
}
</style>
