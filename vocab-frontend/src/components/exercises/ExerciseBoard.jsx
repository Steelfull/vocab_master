// components/ExerciseBoard.jsx

const ExerciseBoard = () => {
    const [currentExercise, setCurrentExercise] = useState(null);
    const [feedback, setFeedback] = useState({});
    const [streak, setStreak] = useState(0);
  
    const loadExercise = async (type) => {
      const response = await api.post('/exercises/generate/', { type });
      setCurrentExercise(response.data);
    };
  
    const handleSubmit = async (answer) => {
      const result = await api.post(`/items/${currentExercise.id}/check/`, answer);
      
      setFeedback({
        correct: result.is_correct,
        correctAnswer: result.correct_answer,
        explanation: result.explanation
      });
  
      if (result.is_correct) {
        setStreak(s => s + 1);
        if (streak % 3 === 0) {
          unlockAchievement('3er-Serie');
        }
      } else {
        setStreak(0);
      }
    };
  
    return (
      <div className="exercise-board">
        <StreakCounter count={streak} />
        
        {currentExercise?.items.map((item, index) => (
          <ExerciseItem
            key={item.id}
            data={item}
            onSubmit={handleSubmit}
            feedback={feedback[index]}
          />
        ))}
        
        <ExerciseProgress 
          total={currentExercise?.items.length} 
          completed={Object.keys(feedback).length}
        />
      </div>
    );
  };