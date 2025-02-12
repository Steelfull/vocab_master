import React, { createContext, useContext, useState, useEffect } from 'react';
import api from '../api';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Beim Laden den aktuellen Authentifizierungsstatus vom Server prüfen
  useEffect(() => {
    const checkAuthStatus = async () => {
      try {
        // Ersetze '/api/check_session/' durch den tatsächlichen Endpunkt, der den Sessionstatus prüft
        await api.get('/api/check-session/');
        setIsAuthenticated(true);
      } catch (error) {
        setIsAuthenticated(false);
      }
    };
    checkAuthStatus();
  }, []);

  // src/context/AuthContext.jsx
const loginUser = async () => {
  try {
    const response = await api.get('/api/check-session/');
    if (response.data.status === 'authenticated') {
      setIsAuthenticated(true);
    }
  } catch (error) {
    setIsAuthenticated(false);
  }
};

  const logoutUser = () => {
    setIsAuthenticated(false);
    // Optional: Führe einen Server-Logout aus, falls benötigt
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, loginUser, logoutUser }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
