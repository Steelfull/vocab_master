// src/components/DeclensionGrid.jsx
import { useState } from 'react';

export default function DeclensionGrid({ item, onAnswer }) {
  const [answers, setAnswers] = useState({
    nominativ: '',
    akkusativ: '',
    dativ: '',
    genitiv: ''
  });

  const handleSubmit = () => {
    onAnswer(item.id, answers);
  };

  return (
    <div className="bg-gray-50 p-6 rounded-lg">
      <h4 className="text-lg font-semibold mb-4">{item.question}</h4>
      
      <div className="grid grid-cols-4 gap-4 mb-4">
        {Object.entries(answers).map(([caseName]) => (
          <input
            key={caseName}
            placeholder={caseName.toUpperCase()}
            value={answers[caseName]}
            onChange={(e) => setAnswers({...answers, [caseName]: e.target.value})}
            className="p-2 border rounded focus:ring-2 focus:ring-blue-500"
          />
        ))}
      </div>
      
      <button
        onClick={handleSubmit}
        className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
      >
        Antwort überprüfen
      </button>
    </div>
  );
}