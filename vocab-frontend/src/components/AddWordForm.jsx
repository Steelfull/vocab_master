import React, { useState } from 'react';
import api from '../api';  // Verwende die API-Instanz
import { useAuth } from '../context/AuthContext';  // Importiere den Auth-Context
import { useNavigate } from 'react-router-dom';

export default function AddWordForm() {
  const { isAuthenticated } = useAuth();  // Auth-Status abrufen
  const navigate = useNavigate();

  const [word, setWord] = useState('');
  const [metadata, setMetadata] = useState(null);
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!isAuthenticated) {
      alert('Bitte melde dich zuerst an!');
      navigate('/login');
      return;
    }

    setIsLoading(true);
    setError('');

    try {
      // 1. Metadaten generieren
      const metadataResponse = await api.post('/api/vocabulary/generate-metadata/', { word });
      const parsedMetadata = metadataResponse.data.metadata;
      setMetadata(parsedMetadata); // Metadaten speichern


      // 2. Wort mit Metadaten zur Datenbank hinzufügen
      const wordData = {
        base_form: word,
        word_class: parsedMetadata.word_class,
        gender: parsedMetadata.gender || null,
        metadata: parsedMetadata,
      };

      const response = await api.post('/api/vocabulary/words/', wordData);

      if (response.status === 201) {
        alert('Wort erfolgreich hinzugefügt!');
        setWord('');
      }
    } catch (err) {
      setError('Fehler beim Hinzufügen des Wortes: ' + (err.response?.data?.error || err.message));
    } finally {
      setIsLoading(false);
    }
  };

  if (!isAuthenticated) {
    return <p>Melde dich zuerst an.</p>;
  }

  return (
    <div style={{ padding: 20 }}>
      <h2>Neues Wort hinzufügen</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={word}
          onChange={(e) => setWord(e.target.value)}
          placeholder="Wort eingeben"
          required
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Lädt...' : 'Hinzufügen'}
        </button>
      </form>

      {metadata && (
        <div>
          <h3>Metadaten:</h3>
          <pre>{JSON.stringify(metadata, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
