import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import BeerList from './components/BeerList';
import BeerCreate from './components/BeerCreate';
import BeerEdit from './components/BeerEdit';
import BeerDelete from './components/BeerDelete';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<BeerList />} />
        <Route path="/create" element={<BeerCreate />} />
        <Route path="/edit" element={<BeerEdit />} />
        <Route path="/delete" element={<BeerDelete />} />
      </Routes>
    </Router>
  );
}

export default App;
