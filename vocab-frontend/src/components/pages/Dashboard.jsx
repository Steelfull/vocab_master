// src/components/pages/Dashboard.jsx
import { useEffect, useState } from 'react';  // useState import hinzufügen
import { useNavigate } from 'react-router-dom';
import api from '../../api/axios';
import ExerciseCard from '../ExerciseCard';  // Pfad anpassen

export default function Dashboard() {
  const navigate = useNavigate();
  // State mit Default-Werten initialisieren
  const [progress, setProgress] = useState({
    streak: 0,
    totalWords: 0,
    accuracy: 0
  });

  useEffect(() => {
    const checkAuth = async () => {
      try {
        await api.get('/api/check-session/');
      } catch (error) {
        navigate('/login');
      }
    };
    checkAuth();
  }, [navigate]);

  // Temporäre Testdaten bis Backend implementiert ist
  useEffect(() => {
    setProgress({
      streak: 5,
      totalWords: 42,
      accuracy: 87
    });
  }, []);

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-8">Dein Lernfortschritt</h1>
      
      <div className="grid grid-cols-3 gap-6 mb-8">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-2">Aktuelle Serie</h3>
          <div className="text-4xl font-bold text-blue-600">
            {progress?.streak || 0} 🔥  {/* Safe Navigation hinzufügen */}
          </div>
        </div>
      </div>

      <div className="space-y-6">
        <h2 className="text-2xl font-semibold">Empfohlene Übungen</h2>
        <ExerciseCard
          type="declension"
          title="Deklinationsmeister"
          difficulty={3}
          progress={65}
          onStart={() => navigate('/exercise/declension/')}  // navigate verwenden
        />
      </div>
    </div>
  );
}