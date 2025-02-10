import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AddWordForm from './components/AddWordForm';
import Exercise from './components/Exercise';
import LoginForm from './components/LoginForm';
import WordList from './components/WordList';
import CombinationExercise from './components/CombinationExercise';
import ProtectedRoute from './components/ProtectedRoute';
import RegisterForm from './components/RegisterForm';
import { AuthProvider } from './context/AuthContext';
import Logout from './components/Logout'; 




function App() {
  return (
    <AuthProvider>
    <Router>
      <div>
        <h1>VocabMaster</h1>
        <nav>
          <a href="/">Home</a>
          <a href="/register">Registrieren</a>
          <a href="/add-word">Wort hinzufügen</a>
          <a href="/exercises">Übungen</a>
          <a href="/word-list">Wortliste</a>
          <Logout />  {}


        </nav>
        <Routes>
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/login" element={<LoginForm />} />
          <Route element={<ProtectedRoute />}>
            <Route path="/" element={<AddWordForm />} />
            <Route path="/add-word" element={<AddWordForm />} />
            <Route path="/exercises" element={<Exercise />} />
            <Route path="/word-list" element={<WordList />} />
            <Route path="/combination-exercise" element={<CombinationExercise />} />
          </Route>
        </Routes>
      </div>
    </Router>
    </AuthProvider>
  );
}

export default App;