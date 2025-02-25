import axios from 'axios';

const API_URL = 'http://localhost:5000';  // Flask backend URL

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const loanService = {
  // Loan Recommendations
  async getRecommendations(userId, score, risk) {
    const response = await api.post('/recommend-loans', { user_id: userId, score, risk });
    return response.data;
  },

  async submitLoanApplication(applicationData) {
    const response = await api.post('/submit-loan', applicationData);
    return response.data;
  },

  // Compliance Verification
  async verifyCompliance(userData, documentText, transactionData, bioData = null) {
    const response = await api.post('/verify-compliance', {
      user_data: userData,
      document_text: documentText,
      transaction_data: transactionData,
      bio_data: bioData
    });
    return response.data;
  },

  async enrollBiometric(userId, bioData) {
    const response = await api.post('/enroll-biometric', {
      user_id: userId,
      bio_data: bioData
    });
    return response.data;
  },

  // Credit Assessment
  async assessCreditworthiness(data, socialData = null) {
    const response = await api.post('/assess-credit', {
      data,
      social_data: socialData
    });
    return response.data;
  },

  // ESG Tracking
  async trackESG(sourceData, factors, impactData, risk = null) {
    const response = await api.post('/track-esg', {
      source_data: sourceData,
      factors,
      impact_data: impactData,
      risk
    });
    return response.data;
  }
};

export default api;