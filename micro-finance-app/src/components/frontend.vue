<template>
  <div>
    <h1>Welcome to the Micro-Finance App</h1>
    <router-link to="/dashboard">Go to Dashboard</router-link>
    <router-link to="/loan-recommendations">View Loan Recommendations</router-link>
    <router-link to="/compliance-verification">Verify Compliance</router-link>
  </div>
</template>

<script>
export default {
  name: 'FrontendComponent',
  data() {
    return {
      currentPage: 'creditworthiness',
      creditData: '',
      complianceData: '',
      biometricData: '',
      behaviorData: '',
      loanData: '',
      currentYear: new Date().getFullYear(),
    };
  },
  methods: {
    submitCreditworthiness() {
      this.$http.post('/assess_creditworthiness', { data: this.creditData })
        .then(response => {
          console.log('Creditworthiness assessed:', response.data);
        });
    },
    submitCompliance() {
      this.$http.post('/verify_compliance', { user_data: this.complianceData })
        .then(response => {
          console.log('Compliance verified:', response.data);
        });
    },
    submitBiometric() {
      this.$http.post('/enroll_biometric', { user_id: 'user123', bio_data: this.biometricData })
        .then(response => {
          console.log('Biometric enrolled:', response.data);
        });
    },
    submitBehavior() {
      this.$http.post('/analyze_behavior', { features: this.behaviorData })
        .then(response => {
          console.log('Behavior analyzed:', response.data);
        });
    },
    submitLoan() {
      this.$http.post('/recommend_loans', { user_id: 'user123', score: 750, risk: 'low' })
        .then(response => {
          console.log('Loan recommendations:', response.data);
        });
    }
  }
};
</script>

<style scoped>
.app {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  background-color: #f8f9fa;
  padding: 20px;
}
header {
  text-align: center;
  margin-bottom: 20px;
}
h1 {
  color: #2c3e50;
}
nav ul {
  list-style-type: none;
  padding: 0;
}
nav ul li {
  display: inline;
  margin: 0 15px;
  cursor: pointer;
  color: #007bff;
}
nav ul li:hover {
  text-decoration: underline;
}
main {
  margin: 20px 0;
}
form {
  margin: 10px 0;
}
input {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ced4da;
  width: 100%;
  margin-bottom: 10px;
}
button {
  padding: 10px;
  background-color: #003366;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
footer {
  text-align: center;
  margin-top: 20px;
}
</style>
