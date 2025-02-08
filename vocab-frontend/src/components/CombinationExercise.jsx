import React, { useState } from 'react';
import { generateCombinationExercise } from '../api';

export default function CombinationExercise() {
  const [exercise, setExercise] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleGenerateExercise = async () => {
    setIsLoading(true);
    try {
      const response = await generateCombinationExercise(2);  // Beispiel: Übungstyp-ID 2
      setExercise(response.data);
    } catch (error) {
      console.error('Fehler beim Generieren der Übung:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Kombinationsübung generieren</h2>
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
                <p>Korrekte Antwort: {item.correct_answer}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}