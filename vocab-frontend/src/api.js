import axios from 'axios';

  
// api.js
const getCSRFToken = () => {
  const cookies = document.cookie.split('; ');
  // Nehme das letzte CSRF-Token-Cookie
  const csrfCookie = cookies.reverse().find(c => c.startsWith('csrftoken='));
  return csrfCookie ? csrfCookie.split('=')[1] : null;
};
  
  const api = axios.create({
    baseURL: "http://localhost:8000/",
    withCredentials: true,
    headers: {
      "Content-Type": "application/json"
    }
  });
  
  api.interceptors.request.use(config => {
    if (['post', 'put', 'patch', 'delete'].includes(config.method.toLowerCase())) {
      config.headers['X-CSRFToken'] = getCSRFToken();
    }
    return config;
  });

export default api;

// Funktionen exportieren
export const addWord = (wordData) => api.post('/vocabulary/words/', wordData);
export const generateMetadata = (word) => api.post('/vocabulary/generate-metadata/', { word });
export const getWords = () => api.get('/vocabulary/words/');
export const generateExercise = (exerciseTypeId) => api.post('/exercises/generate-exercise/', { exercise_type_id: exerciseTypeId });
export const submitAnswer = (exerciseItemId, userAnswer) => api.post(`/exercises/items/${exerciseItemId}/submit-answer/`, { user_answer: userAnswer });
export const generateCombinationExercise = (exerciseTypeId) => api.post('/exercises/generate-combination-exercise/', { exercise_type_id: exerciseTypeId });