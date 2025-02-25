<template>
  <div class="compliance">
    <div class="page-header">
      <h1>Compliance Verification</h1>
      <button class="btn btn-primary">
        <i class="fas fa-plus"></i>
        New Verification
      </button>
    </div>

    <div class="grid grid-cols-3 metrics">
      <div class="card">
        <h3>KYC Status</h3>
        <div class="status verified">
          <i class="fas fa-check-circle"></i>
          Verified
        </div>
      </div>
      
      <div class="card">
        <h3>AML Check</h3>
        <div class="status verified">
          <i class="fas fa-check-circle"></i>
          Passed
        </div>
      </div>

      <div class="card">
        <h3>Document Verification</h3>
        <div class="status pending">
          <i class="fas fa-clock"></i>
          In Progress
        </div>
      </div>
    </div>

    <div class="card verification-form">
      <h2>Verification Details</h2>
      <div class="form-grid">
        <div class="form-group">
          <label>Aadhaar Number</label>
          <input type="text" class="form-control" placeholder="Enter Aadhaar number" />
        </div>
        
        <div class="form-group">
          <label>PAN Number</label>
          <input type="text" class="form-control" placeholder="Enter PAN number" />
        </div>

        <div class="form-group">
          <label>Document Type</label>
          <select class="form-control">
            <option>Aadhaar Card</option>
            <option>PAN Card</option>
            <option>Passport</option>
            <option>Driving License</option>
          </select>
        </div>

        <div class="form-group">
          <label>Document Upload</label>
          <input type="file" class="form-control" />
        </div>
      </div>

      <div class="actions">
        <button class="btn btn-secondary">
          <i class="fas fa-shield-alt"></i>
          Verify Documents
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ComplianceView'
}
</script>

<style scoped>
.compliance {
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

.status {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 18px;
  font-weight: 600;
  margin: 10px 0;
  padding: 10px;
  border-radius: 8px;
}

.status.verified {
  background: #f0fdf4;
  color: #166534;
}

.status.pending {
  background: #fff7ed;
  color: #c2410c;
}

.verification-form {
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
