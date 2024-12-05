import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import BeerList from './components/BeerList';
import BeerForm from './components/BeerForm';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<BeerList />} />
        <Route path="/add" element={<BeerForm />} />
      </Routes>
    </Router>
  );
}

export default App;
