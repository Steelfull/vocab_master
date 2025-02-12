import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000',
  withCredentials: true,
  headers: {
    'X-Requested-With': 'XMLHttpRequest'
  }
});

api.interceptors.request.use(async (config) => {
  if (!document.cookie.includes('csrftoken')) {
    await api.get('/api/csrf_token/');
  }
  
  const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)[1];
  config.headers['X-CSRFToken'] = csrfToken;
  
  // Für GET-Requests benötigen wir das Cookie-Header
  if (config.method === 'get') {
    config.headers['Cookie'] = document.cookie;
  }
  
  return config;
});

export default api;
