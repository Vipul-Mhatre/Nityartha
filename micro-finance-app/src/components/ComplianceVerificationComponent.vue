<template>
  <div class="compliance-verification">
    <h2>Compliance Verification</h2>

    <div class="compliance-grid">
      <!-- KYC Verification -->
      <div class="compliance-card">
        <h3>KYC Verification</h3>
        <div class="document-upload">
          <div 
            class="upload-zone"
            @dragover.prevent
            @drop.prevent="handleDocumentDrop"
          >
            <i class="upload-icon">📄</i>
            <p>Drag and drop documents here or</p>
            <input 
              type="file" 
              @change="handleDocumentSelect" 
              multiple 
              accept=".pdf,.jpg,.png"
              ref="fileInput"
            >
            <button @click="$refs.fileInput.click()">
              Select Files
            </button>
          </div>

          <div v-if="documents.length" class="document-list">
            <div 
              v-for="(doc, index) in documents" 
              :key="index"
              class="document-item"
            >
              <span>{{ doc.name }}</span>
              <button @click="removeDocument(index)" class="remove-btn">
                ×
              </button>
            </div>
          </div>
        </div>

        <button 
          @click="verifyDocuments" 
          :disabled="!documents.length || loading"
          class="verify-btn"
        >
          {{ loading ? 'Verifying...' : 'Verify Documents' }}
        </button>
      </div>

      <!-- Biometric Verification -->
      <div class="compliance-card">
        <h3>Biometric Verification</h3>
        <div class="biometric-section">
          <div class="biometric-type" v-for="type in biometricTypes" :key="type.id">
            <h4>{{ type.name }}</h4>
            <p>{{ type.description }}</p>
            <button 
              @click="enrollBiometric(type.id)"
              :disabled="loading"
              class="enroll-btn"
            >
              Enroll {{ type.name }}
            </button>
          </div>
        </div>
      </div>

      <!-- Compliance Status -->
      <div class="compliance-card">
        <h3>Compliance Status</h3>
        <div class="status-grid">
          <div 
            v-for="status in complianceStatus" 
            :key="status.id"
            class="status-item"
            :class="status.status"
          >
            <div class="status-icon">
              {{ status.icon }}
            </div>
            <div class="status-info">
              <h4>{{ status.name }}</h4>
              <p>{{ status.message }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ComplianceVerificationComponent',
  data() {
    return {
      loading: false,
      documents: [],
      biometricTypes: [
        {
          id: 'fingerprint',
          name: 'Fingerprint',
          description: 'Scan your fingerprint for secure verification'
        },
        {
          id: 'facial',
          name: 'Facial Recognition',
          description: 'Use your camera for facial verification'
        }
      ],
      complianceStatus: [
        {
          id: 'kyc',
          name: 'KYC Verification',
          status: 'pending',
          icon: '⏳',
          message: 'Awaiting document verification'
        },
        {
          id: 'aml',
          name: 'AML Check',
          status: 'pending',
          icon: '⏳',
          message: 'Pending verification'
        },
        {
          id: 'biometric',
          name: 'Biometric Verification',
          status: 'pending',
          icon: '⏳',
          message: 'Not enrolled'
        }
      ]
    }
  },
  methods: {
    handleDocumentDrop(event) {
      const files = event.dataTransfer.files
      this.addDocuments(files)
    },
    handleDocumentSelect(event) {
      const files = event.target.files
      this.addDocuments(files)
    },
    addDocuments(files) {
      for (let file of files) {
        if (this.isValidDocument(file)) {
          this.documents.push(file)
        }
      }
    },
    isValidDocument(file) {
      const validTypes = ['application/pdf', 'image/jpeg', 'image/png']
      return validTypes.includes(file.type)
    },
    removeDocument(index) {
      this.documents.splice(index, 1)
    },
    async verifyDocuments() {
      try {
        this.loading = true
        const formData = new FormData()
        this.documents.forEach(doc => {
          formData.append('documents', doc)
        })

        const response = await this.axios.post('/verify_compliance', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })

        this.updateComplianceStatus('kyc', response.data.verified)
      } catch (error) {
        console.error('Error verifying documents:', error)
      } finally {
        this.loading = false
      }
    },
    async enrollBiometric(type) {
      try {
        this.loading = true
        // In a real implementation, this would integrate with device biometric APIs
        const response = await this.axios.post('/enroll_biometric', {
          user_id: 'current_user',
          bio_type: type,
          bio_data: 'sample_data'
        })

        if (response.data.enrolled) {
          this.updateComplianceStatus('biometric', true)
        }
      } catch (error) {
        console.error('Error enrolling biometric:', error)
      } finally {
        this.loading = false
      }
    },
    updateComplianceStatus(id, verified) {
      const status = this.complianceStatus.find(s => s.id === id)
      if (status) {
        status.status = verified ? 'verified' : 'failed'
        status.icon = verified ? '✓' : '✗'
        status.message = verified ? 
          'Successfully verified' : 
          'Verification failed'
      }
    }
  }
}
</script>

<style scoped>
.compliance-verification {
  padding: 2rem;
}

h2 {
  color: var(--primary-color);
  margin-bottom: 2rem;
}

.compliance-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.compliance-card {
  background: var(--background-color);
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 12px var(--shadow-color);
}

.compliance-card h3 {
  color: var(--primary-color);
  margin-bottom: 1.5rem;
}

.upload-zone {
  border: 2px dashed var(--border-color);
  border-radius: 8px;
  padding: 2rem;
  text-align: center;
  margin-bottom: 1rem;
}

.upload-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.upload-zone input[type="file"] {
  display: none;
}

.document-list {
  margin-top: 1rem;
}

.document-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 4px;
  margin-bottom: 0.5rem;
}

.remove-btn {
  background: none;
  border: none;
  color: var(--text-color);
  font-size: 1.25rem;
  cursor: pointer;
  padding: 0 0.5rem;
}

.verify-btn {
  width: 100%;
  margin-top: 1rem;
}

.biometric-section {
  display: grid;
  gap: 1.5rem;
}

.biometric-type {
  padding: 1rem;
  border: 1px solid var(--border-color);
  border-radius: 4px;
}

.biometric-type h4 {
  margin-bottom: 0.5rem;
}

.biometric-type p {
  margin-bottom: 1rem;
  color: var(--text-color);
  opacity: 0.8;
}

.status-grid {
  display: grid;
  gap: 1rem;
}

.status-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border-radius: 4px;
  background: var(--background-color);
  border: 1px solid var(--border-color);
}

.status-icon {
  font-size: 1.5rem;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: var(--border-color);
}

.status-info h4 {
  margin-bottom: 0.25rem;
}

.status-info p {
  font-size: 0.875rem;
  color: var(--text-color);
  opacity: 0.8;
}

.status-item.verified .status-icon {
  background: #2ecc71;
  color: white;
}

.status-item.failed .status-icon {
  background: #e74c3c;
  color: white;
}

button {
  background-color: var(--primary-color);
  color: white;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: var(--secondary-color);
}

button:disabled {
  background-color: var(--border-color);
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .compliance-verification {
    padding: 1rem;
  }
  
  .compliance-grid {
    grid-template-columns: 1fr;
  }
}
</style>
