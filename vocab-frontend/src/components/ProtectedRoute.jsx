// src/components/ProtectedRoute.jsx
import { useEffect } from 'react';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import api from '../api/axios';
import { useAuth } from '../context/AuthContext';

const ProtectedRoute = ({ children }) => {
  const { isAuthenticated, loginUser, logoutUser } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const checkAuth = async () => {
      try {
        // 1. Server-Session prüfen
        const response = await api.get('/api/check-session/');
        
        // 2. Auth Context synchronisieren
        if (response.data.status === 'authenticated' && !isAuthenticated) {
          loginUser();
        }
        
        // 3. Bei Fehler zur Login-Seite
      } catch (error) {
        logoutUser();
        navigate('/login', {
          state: { from: location },
          replace: true
        });
      }
    };

    // Nur prüfen wenn nicht bereits authentifiziert
    if (!isAuthenticated) {
      checkAuth();
    }

    // Browser-Navigation Events abfangen
    const handlePopState = () => {
      if (!isAuthenticated) checkAuth();
    };
    
    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, [navigate, location, isAuthenticated, loginUser, logoutUser]);

  // Combined rendering logic
  return isAuthenticated ? (
    children ? children : <Outlet /> // Unterstützt sowohl Route-Element als auch Children
  ) : null; // Vermeidet kurzzeitiges Anzeigen von geschützten Inhalten
};

export default ProtectedRoute;