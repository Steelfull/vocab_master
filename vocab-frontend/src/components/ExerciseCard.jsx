const ExerciseCard = ({ type, title, difficulty, progress, onStart }) => {
    return (
      <div className="bg-white p-6 rounded-lg shadow-md">
        <h3 className="text-xl font-semibold mb-4">{title}</h3>
        <div className="flex justify-between items-center mb-4">
          <span className="text-gray-600">Schwierigkeit: {difficulty}/5</span>
          <span className="text-blue-600">{progress}% abgeschlossen</span>
        </div>
        <button 
          onClick={onStart}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Übung starten
        </button>
      </div>
    );
  };
  
  export default ExerciseCard;