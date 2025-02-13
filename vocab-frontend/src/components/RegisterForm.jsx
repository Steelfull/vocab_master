import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function RegisterForm() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [csrfToken, setCsrfToken] = useState('');
  const navigate = useNavigate();

  // CSRF-Token beim Laden der Komponente abrufen
  useEffect(() => {
    const fetchCsrfToken = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/csrf_token/', {
          withCredentials: true,  // Cookies werden mitgesendet
        });
        setCsrfToken(response.data.csrfToken);  // CSRF-Token speichern
      } catch (err) {
        console.error('Fehler beim Abrufen des CSRF-Tokens:', err);
        setError('Fehler beim Laden der Registrierungsseite. Bitte versuche es später erneut.');
      }
    };

    fetchCsrfToken();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Überprüfe, ob alle Felder ausgefüllt sind
    if (!username || !email || !password) {
      setError('Bitte fülle alle Felder aus.');
      return;
    }

    try {
      const response = await axios.post(
        'http://localhost:8000/api/register/',
        { username, email, password },
        {
          withCredentials: true,  // Cookies werden mitgesendet
          headers: {
            'X-CSRFToken': csrfToken,  // CSRF-Token in den Headern senden
          },
        }
      );

      if (response.status === 201) {
        navigate('/login');  // Weiterleitung zur Login-Seite
      }
    } catch (err) {
      if (err.response) {
        // Fehler vom Server (z. B. 400 oder 403)
        setError(err.response.data.detail || 'Registrierung fehlgeschlagen. Bitte überprüfe deine Eingaben.');
      } else {
        // Netzwerkfehler oder anderer Fehler
        setError('Ein Netzwerkfehler ist aufgetreten. Bitte überprüfe deine Internetverbindung.');
      }
      console.error('Fehler bei der Registrierung:', err);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Registrierung</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Benutzername:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Benutzername"
            required
          />
        </div>
        <div>
          <label htmlFor="email">E-Mail:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="E-Mail"
            required
          />
        </div>
        <div>
          <label htmlFor="password">Passwort:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Passwort"
            required
          />
        </div>
        <button type="submit">Registrieren</button>
      </form>
    </div>
  );
}