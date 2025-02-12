// src/components/ExerciseSession.jsx
import { useState, useEffect } from 'react';
import api from '../api';
import DeclensionGrid from './DeclensionGrid';
import FeedbackOverlay from './FeedbackOverlay';
import ProgressIndicator from './ProgressIndicator';

export default function ExerciseSession({ exerciseType }) {
  const [exercise, setExercise] = useState(null);
  const [currentItem, setCurrentItem] = useState(0);
  const [feedback, setFeedback] = useState(null);


  // Übung initial laden
  useEffect(() => {
    const loadExercise = async () => {
      const response = await api.post('/exercises/generate/', {
        exercise_type: exerciseType.id
      });
      setExercise(response.data);
    };
    loadExercise();
  }, [exerciseType]);

  // Antwort verarbeiten
  const handleAnswer = async (answer) => {
    const itemId = exercise.items[currentItem].id;
    const response = await api.post(`/exercises/items/${itemId}/check/`, {
      answer
    });
    
    setFeedback(response.data);
    
    if (response.data.is_correct) {
      setTimeout(() => {
        setCurrentItem(prev => prev + 1);
        setFeedback(null);
      }, 2000);
    }
  };

  // Render-Logik
  if (!exercise) return <div>Lade Übung...</div>;

  return (
    <div className="max-w-2xl mx-auto p-6">
      <ProgressIndicator 
        total={exercise.items.length}
        current={currentItem + 1}
      />
      
      {feedback && <FeedbackOverlay {...feedback} />}

      <DeclensionGrid
        item={exercise.items[currentItem]}
        onSubmit={handleAnswer}
      />
    </div>
  );
}