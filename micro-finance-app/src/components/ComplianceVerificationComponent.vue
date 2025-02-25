<template>
  <div class="compliance-verification">
    <h2>Compliance Verification</h2>
    
    <div v-if="error" class="error-message">
      {{ error }}
    </div>

    <form @submit.prevent="verifyCompliance" class="verification-form">
      <div class="form-group">
        <label for="fullName">Full Name</label>
        <input 
          id="fullName"
          v-model="formData.fullName"
          type="text"
          required
        >
      </div>

      <div class="form-group">
        <label for="idNumber">ID Number</label>
        <input 
          id="idNumber"
          v-model="formData.idNumber"
          type="text"
          required
        >
      </div>

      <div class="form-group">
        <label for="document">Upload Document</label>
        <input 
          id="document"
          type="file"
          @change="handleFileUpload"
          accept=".txt,.pdf,.doc,.docx"
        >
      </div>

      <div class="form-group">
        <label for="transactions">Transaction History</label>
        <textarea 
          id="transactions"
          v-model="formData.transactionHistory"
          placeholder="Enter transaction amounts, one per line"
          rows="5"
          required
        ></textarea>
      </div>

      <div class="form-group">
        <button 
          type="button" 
          @click="handleBiometricCapture"
          :disabled="loading"
        >
          Capture Biometric Data
        </button>
        <span v-if="formData.biometricData" class="success-text">
          ✓ Biometric data captured
        </span>
      </div>

      <button 
        type="submit"
        :disabled="loading"
        class="verify-button"
      >
        {{ loading ? 'Verifying...' : 'Verify Compliance' }}
      </button>
    </form>

    <div v-if="verificationResult" class="verification-result">
      <h3>Verification Result</h3>
      <pre>{{ JSON.stringify(verificationResult, null, 2) }}</pre>
    </div>
  </div>
</template>

<script>
import { loanService } from '@/services/api'

export default {
  name: 'ComplianceVerification',
  data() {
    return {
      loading: false,
      formData: {
        fullName: '',
        idNumber: '',
        documentText: '',
        transactionHistory: '',
        biometricData: null
      },
      verificationResult: null,
      error: null
    }
  },
  methods: {
    async handleFileUpload(event) {
      const file = event.target.files[0]
      if (file) {
        try {
          // In a real app, you'd use proper file handling
          const reader = new FileReader()
          reader.onload = (e) => {
            this.formData.documentText = e.target.result
          }
          reader.readAsText(file)
        } catch (error) {
          console.error('Error reading file:', error)
          this.error = 'Error reading file. Please try again.'
        }
      }
    },

    async handleBiometricCapture() {
      try {
        // In a real app, this would interface with a biometric capture device
        this.formData.biometricData = [0.5, 0.7, 0.3, 0.9, 0.4]
        await loanService.enrollBiometric(1, this.formData.biometricData)
      } catch (error) {
        console.error('Error capturing biometric data:', error)
        this.error = 'Error capturing biometric data. Please try again.'
      }
    },

    async verifyCompliance() {
      try {
        this.loading = true
        this.error = null
        
        const userData = {
          fullName: this.formData.fullName,
          idNumber: this.formData.idNumber
        }
        
        const transactionData = this.formData.transactionHistory
          .split('\n')
          .map(line => parseFloat(line.trim()))
          .filter(num => !isNaN(num))

        const response = await loanService.verifyCompliance(
          userData,
          this.formData.documentText,
          transactionData,
          this.formData.biometricData
        )

        this.verificationResult = response
      } catch (error) {
        console.error('Error verifying compliance:', error)
        this.error = 'Error verifying compliance. Please check your inputs and try again.'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.compliance-verification {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.verification-form {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

input[type="text"],
input[type="file"],
textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.verify-button {
  background: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.verify-button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.error-message {
  color: #dc3545;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #dc3545;
  border-radius: 4px;
  background: #f8d7da;
}

.verification-result {
  margin-top: 20px;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 4px;
}

.success-text {
  color: #28a745;
  margin-left: 10px;
}

pre {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 4px;
  overflow-x: auto;
}
</style>
