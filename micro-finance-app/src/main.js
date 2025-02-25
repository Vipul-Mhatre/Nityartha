import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'

const app = createApp(App)

// Configure axios
axios.defaults.baseURL = process.env.VUE_APP_API_URL || 'http://localhost:5000'

// Register plugins
app.use(router)
app.use(VueAxios, axios)

// Global error handler
app.config.errorHandler = (err) => {
  console.error('Global error:', err)
  // You can add error reporting service here
}

app.mount('#app')
