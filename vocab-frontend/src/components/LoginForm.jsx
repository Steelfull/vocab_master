import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';  
import { useAuth } from '../context/AuthContext';  

export default function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { loginUser } = useAuth(); 

  useEffect(() => {
    // CSRF-Token mit Credentials holen
    api.get('/api/csrf_token/', { withCredentials: true })
      .then(() => console.log('CSRF-Token gesetzt:', document.cookie))
      .catch(console.error);
  }, []);
  

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Explizite Cookie-Prüfung
    if (!document.cookie.includes('csrftoken')) {
      alert('CSRF-Token fehlt!');
      return;
    }
  
    try {
      const response = await api.post('/api/login/', 
        { username, password },
        {
          headers: {
            'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)[1],
            'Content-Type': 'application/json'
          },
          withCredentials: true
        }
      );
      if (response.status === 200) {
        loginUser();  // Setzt den Authentifizierungszustand
        navigate('/dashboard');  // Weiterleitung zur geschützten Route
      }
    } catch (err) {
      setError('Ungültige Anmeldedaten');
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Login</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Benutzername"
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Passwort"
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}
