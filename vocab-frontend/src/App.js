import React from 'react';

import { Provider } from 'react-redux';
import { AuthProvider } from './context/AuthContext';
import store from './store/store';
import AddWordForm from './components/AddWordForm';

import LoginForm from './components/LoginForm';
import WordList from './components/WordList';
import CombinationExercise from './components/CombinationExercise';
import ProtectedRoute from './components/ProtectedRoute';
import RegisterForm from './components/RegisterForm';
import Logout from './components/Logout';
import ExerciseSession from './components/ExerciseSession';
import Dashboard from './components/pages/Dashboard';
// Am Anfang der Imports
import { 
  BrowserRouter as Router, 
  Route, 
  Routes, 
  Navigate // Dieser Import fehlte
} from 'react-router-dom';

function App() {
  return (
    <Provider store={store}>
      <AuthProvider>
        <Router>
          <div className="App">
            <h1>VocabMaster</h1>
            <nav>
              <a href="/">Home</a>
              <a href="/register">Registrieren</a>
              <a href="/add-word">Wort hinzufügen</a>
              <a href="/exercises">Übungen</a>
              <a href="/word-list">Wortliste</a>
              <Logout />
            </nav>
            <Routes>
              <Route path="/register" element={<RegisterForm />} />
              <Route path="/login" element={<LoginForm />} />
              <Route element={<ProtectedRoute />}>
                <Route path="/" element={<AddWordForm />} />
                <Route path="/add-word" element={<AddWordForm />} />
                <Route path="/exercises" element={<ExerciseSession />} />
                <Route path="/word-list" element={<WordList />} />
                <Route path="/combination-exercise" element={<CombinationExercise />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/" element={<Navigate to="/dashboard" replace />} />
                <Route path="/dashboard" element={<Dashboard />} />

              </Route>
            </Routes>
          </div>
        </Router>
      </AuthProvider>
    </Provider>
  );
}

export default App;


