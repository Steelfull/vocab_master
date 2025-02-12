import api from './api'; // Basis-API-Instanz

export const generateExercise = async (exerciseTypeId) => {
  try {
    const response = await api.post('/exercises/generate/', {
      exercise_type: exerciseTypeId
    });
    return response.data;
  } catch (error) {
    throw new Error('Übung konnte nicht generiert werden: ' + error.message);
  }
};

export const checkAnswer = async (itemId, userAnswer) => {
  try {
    const response = await api.post(`/exercises/items/${itemId}/check/`, {
      answer: userAnswer
    });
    return response.data;
  } catch (error) {
    throw new Error('Antwort konnte nicht überprüft werden: ' + error.message);
  }
};