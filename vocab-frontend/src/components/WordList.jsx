import React, { useEffect, useState } from 'react';
import { getWords } from '../api';
import Spinner from './Spinner';  // Spinner importieren

export default function WordList() {
  const [words, setWords] = useState([]);  // words definieren
  const [isLoading, setIsLoading] = useState(true);  // isLoading definieren

  useEffect(() => {
    const fetchWords = async () => {
      try {
        const response = await getWords();
        setWords(response.data);
      } catch (error) {
        console.error('Fehler beim Laden der Wörter:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchWords();
  }, []);

  if (isLoading) {
    return <Spinner />;  // Spinner anzeigen
  }

  return (
    <div style={{ padding: 20 }}>
      <h2>Deine Wörter</h2>
      <ul>
        {words.map((word) => (
          <li key={word.id}>
            <strong>{word.base_form}</strong> ({word.word_class})
            <pre>{JSON.stringify(word.metadata, null, 2)}</pre>
          </li>
        ))}
      </ul>
    </div>
  );
}