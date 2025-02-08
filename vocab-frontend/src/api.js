import axios from 'axios';


const getCSRFToken = () => {
    const cookieValue = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];
    return cookieValue;
  };

// Korrekte Axios-Konfiguration
const api = axios.create({
    baseURL: "http://localhost:8000/",
    withCredentials: true,  // Sendet Cookies
    headers: {
      "X-CSRFToken": getCSRFToken(),
      "Content-Type": "application/json"
    }
  });

// Funktionen exportieren
export const addWord = (wordData) => api.post('/vocabulary/words/', wordData);
export const generateMetadata = (word) => api.post('/vocabulary/generate-metadata/', { word });
export const getWords = () => api.get('/vocabulary/words/');
export const generateExercise = (exerciseTypeId) => api.post('/exercises/generate-exercise/', { exercise_type_id: exerciseTypeId });
export const submitAnswer = (exerciseItemId, userAnswer) => api.post(`/exercises/items/${exerciseItemId}/submit-answer/`, { user_answer: userAnswer });
export const generateCombinationExercise = (exerciseTypeId) => api.post('/exercises/generate-combination-exercise/', { exercise_type_id: exerciseTypeId });