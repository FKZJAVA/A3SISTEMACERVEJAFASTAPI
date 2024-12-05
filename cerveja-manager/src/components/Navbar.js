import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav style={{ padding: '10px', backgroundColor: '#f0f0f0' }}>
      <Link to="/" style={{ margin: '10px' }}>Lista de Cervejas</Link>
      <Link to="/create" style={{ margin: '10px' }}>Adicionar Cerveja</Link>
      <Link to="/edit" style={{ margin: '10px' }}>Editar Cerveja</Link>
      <Link to="/delete" style={{ margin: '10px' }}>Deletar Cerveja</Link>
    </nav>
  );
}

export default Navbar;
