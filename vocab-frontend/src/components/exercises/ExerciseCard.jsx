// src/components/ExerciseCard.jsx
import { ProgressCircle } from '@tremor/react';

export default function ExerciseCard({ type, title, difficulty, progress, onStart }) {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
      <div className="flex items-center gap-4">
        <ProgressCircle value={progress} size="md" color="blue">
          <span className="text-sm font-medium">{difficulty}</span>
        </ProgressCircle>
        <div>
          <h3 className="text-xl font-semibold">{title}</h3>
          <p className="text-gray-600">Schwierigkeitsgrad: {difficulty}/5</p>
        </div>
      </div>
      <button 
        onClick={onStart}
        className="mt-4 w-full bg-blue-500 hover:bg-blue-600 text-white py-2 rounded-md transition-colors"
      >
        Übung starten
      </button>
    </div>
  );
}