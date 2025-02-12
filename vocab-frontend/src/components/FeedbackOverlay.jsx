// src/components/FeedbackOverlay.jsx
import { motion } from 'framer-motion';

export default function FeedbackOverlay({ isCorrect, feedback }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className={`fixed bottom-4 right-4 p-4 rounded-lg shadow-lg ${
        isCorrect ? 'bg-green-100' : 'bg-red-100'
      }`}
    >
      <h3 className={`font-semibold ${isCorrect ? 'text-green-700' : 'text-red-700'}`}>
        {isCorrect ? '✓ Richtig!' : '✗ Leider falsch'}
      </h3>
      {!isCorrect && (
        <div className="mt-2">
          <p className="text-sm">{feedback.explanation}</p>
          <p className="mt-2 text-sm font-medium">
            Richtige Antwort: {feedback.correct_answer}
          </p>
        </div>
      )}
    </motion.div>
  );
}