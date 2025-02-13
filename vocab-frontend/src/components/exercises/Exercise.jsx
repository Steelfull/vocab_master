import React, { useState, useEffect } from 'react';
import axios from 'axios';  // Verwende deine angepasste Axios-Instanz

const Exercise = () => {
    const [exercise, setExercise] = useState(null);
    const [userAnswer, setUserAnswer] = useState('');
    const [feedback, setFeedback] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    // Hole eine neue Übung vom Backend
    const fetchExercise = async () => {
        setIsLoading(true);
        try {
            const response = await axios.get('/api/vocabulary/generate-exercise/');
            console.log('API-Antwort:', response.data);  // Debugging
            if (!response.data) {
                throw new Error('Keine Daten erhalten');
            }
            setExercise(response.data);
            setFeedback('');
        } catch (error) {
            console.error('Fehler beim Laden der Übung:', error);
            setFeedback('Fehler beim Laden der Übung. Bitte versuche es später erneut.');
        } finally {
            setIsLoading(false);
        }
    };

    // Lade eine Übung, wenn die Komponente geladen wird
    useEffect(() => {
        fetchExercise();
    }, []);

    // Überprüfe die Antwort des Benutzers
    const checkAnswer = () => {
        if (!exercise) return;

        // Beispiel: Überprüfe, ob der Benutzer den richtigen Fall verwendet hat
        const correctAnswer = `${exercise.article} ${exercise.adjective} ${exercise.noun}`;
        if (userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {
            setFeedback('Richtig! 🎉');
        } else {
            setFeedback(`Falsch. Die richtige Antwort ist: ${correctAnswer}`);
        }
    };

    return (
        <div className="exercise">
            <h2>Deklinationsübung</h2>
            {isLoading ? (
                <div className="spinner">⏳</div>
            ) : exercise ? (
                <>
                    <p>
                        Kombiniere: {exercise.conjunction} {exercise.pronoun} {exercise.adjective} {exercise.noun} ({exercise.case})
                    </p>
                    <input
                        type="text"
                        value={userAnswer}
                        onChange={(e) => setUserAnswer(e.target.value)}
                        placeholder="Gib deine Antwort ein"
                    />
                    <button onClick={checkAnswer}>Antwort überprüfen</button>
                    {feedback && <p>{feedback}</p>}
                </>
            ) : (
                <p>Lade Übung...</p>
            )}
            <button onClick={fetchExercise}>Neue Übung</button>
        </div>
    );
};

export default Exercise;