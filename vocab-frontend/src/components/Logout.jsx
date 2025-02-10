// src/components/Logout.jsx
import React from 'react';
import api from '../api';  // Verwende die API-Instanz
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';  // Importiere den Auth-Context

const Logout = () => {
  const navigate = useNavigate();
  const { logoutUser } = useAuth();  // Destrukturierung des logoutUser-Handlers

  const handleLogout = async () => {
    try {
      const response = await api.post('/api/logout/');
      
      if (response.status === 200) {
        logoutUser();  // Setzt den globalen Authentifizierungsstatus als "ausgeloggt"
        navigate('/login');  // Weiterleitung zur Login-Seite
      }
    } catch (err) {
      console.error('Fehler beim Logout:', err);
    }
  };

  return (
    <button onClick={handleLogout}>Logout</button>
  );
};

export default Logout;