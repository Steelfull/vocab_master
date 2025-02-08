import React, { useState } from 'react';
import { generateExercise, submitAnswer } from '../api';

export default function Exercise() {
  const [exercise, setExercise] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [userAnswers, setUserAnswers] = useState({});

  const handleGenerateExercise = async () => {
    setIsLoading(true);
    try {
      const response = await generateExercise(1);  // Beispiel: Übungstyp-ID 1
      setExercise(response.data);
    } catch (error) {
      console.error('Fehler beim Generieren der Übung:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSubmitAnswer = async (exerciseItemId) => {
    const userAnswer = userAnswers[exerciseItemId];
    if (!userAnswer) return;

    try {
      const response = await submitAnswer(exerciseItemId, userAnswer);
      alert(response.data.is_correct ? 'Richtig!' : 'Falsch!');
    } catch (error) {
      console.error('Fehler:', error);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Übung generieren</h2>
      <button onClick={handleGenerateExercise} disabled={isLoading}>
        {isLoading ? 'Lädt...' : 'Übung starten'}
      </button>

      {exercise && (
        <div>
          <h3>{exercise.exercise_type.name}</h3>
          <ul>
            {exercise.items.map((item) => (
              <li key={item.id}>
                <p>{item.question}</p>
                <input
                  type="text"
                  value={userAnswers[item.id] || ''}
                  onChange={(e) => setUserAnswers({ ...userAnswers, [item.id]: e.target.value })}
                  placeholder="Deine Antwort"
                />
                <button onClick={() => handleSubmitAnswer(item.id)}>Antwort überprüfen</button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}