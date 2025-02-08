import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      const response = await axios.post(
        'http://localhost:8000/api/logout/',
        {},
        { withCredentials: true }
      );
      
      if (response.status === 200) {
        navigate('/login');  // Weiterleitung zur Login-Seite
      }
    } catch (err) {
      console.error('Logout fehlgeschlagen', err);
    }
  };

  return (
    <button onClick={handleLogout}>Logout</button>
  );
};

export default Logout;