import React, { useState } from 'react';
import { addWord, generateMetadata } from '../api';
import Spinner from './Spinner';
import { useNavigate } from 'react-router-dom';

export default function AddWordForm() {
  const navigate = useNavigate();
  const [word, setWord] = useState('');
  const [metadata, setMetadata] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!localStorage.getItem('isAuthenticated')) {  // Beispiel: Checke Login-Status
        alert('Bitte melde dich zuerst an!');
        navigate('/login');
        return;
      }

  
    try {
      const metadataResponse = await generateMetadata({ word });
      const parsedMetadata = metadataResponse.data.metadata;
      setMetadata(parsedMetadata);
  
      const wordData = {
        base_form: word,
        word_class: parsedMetadata.word_class,
        gender: parsedMetadata.gender,
        metadata: parsedMetadata,
      };
      await addWord(wordData);
  
      alert('Wort erfolgreich hinzugefügt!');
    } catch (error) {
      console.error('Fehler:', error.response?.data || error.message);
      alert(`Ein Fehler ist aufgetreten: ${error.response?.data?.error || error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Neues Wort hinzufügen</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={word}
          onChange={(e) => setWord(e.target.value)}
          placeholder="Wort eingeben"
          required
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Lädt...' : 'Wort hinzufügen'}
        </button>
      </form>

      {metadata && (
        <div>
          <h3>Metadaten:</h3>
          <pre>{JSON.stringify(metadata, null, 2)}</pre>
        </div>
      )}

      {isLoading && <Spinner />}
    </div>
  );
}