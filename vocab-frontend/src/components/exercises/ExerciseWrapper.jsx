const ExerciseWrapper = ({ exercise }) => {
    const renderExercise = () => {
      switch(exercise.exercise_type.structure) {
        case 'ARTICLE_NOUN':
          return <ArticleNounExercise items={exercise.items} />;
        case 'PRONOUN_NOUN':
          return <PronounNounExercise items={exercise.items} />;
        // ... andere Übungstypen
      }
    }
  
    return (
      <div className="exercise-container">
        <h2>{exercise.exercise_type.name}</h2>
        {renderExercise()}
      </div>
    );
  };