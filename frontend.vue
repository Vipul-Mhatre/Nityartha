<template>
  <div class="app">
    <header>
      <h1>AI-Powered Micro-Finance Platform</h1>
    </header>
    <main>
      <section v-if="currentPage === 'compliance'">
        <h2>Compliance Verification</h2>
        <form @submit.prevent="submitCompliance">
          <input type="text" v-model="complianceData" placeholder="Enter compliance details" required />
          <button type="submit">Verify</button>
        </form>
      </section>
      <section v-if="currentPage === 'loan'">
        <h2>Loan Recommendations</h2>
        <form @submit.prevent="submitLoan">
          <input type="text" v-model="loanData" placeholder="Enter loan details" required />
          <button type="submit">Get Recommendations</button>
        </form>
      </section>
      <section v-if="currentPage === 'biometric'">
        <h2>Enroll Biometric Data</h2>
        <form @submit.prevent="submitBiometric">
          <input type="text" v-model="biometricData" placeholder="Enter biometric data" required />
          <button type="submit">Enroll</button>
        </form>
      </section>
    </main>
    <footer>
      <p>© {{ currentYear }} AI Micro-Finance Platform. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentPage: 'compliance',
      complianceData: '',
      loanData: '',
      biometricData: '',
      currentYear: new Date().getFullYear(),
    };
  },
  methods: {
    submitCompliance() {
      // Handle compliance submission
    },
    submitLoan() {
      // Handle loan submission
    },
    submitBiometric() {
      // Handle biometric enrollment
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
}
h1 {
  color: #2c3e50;
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
