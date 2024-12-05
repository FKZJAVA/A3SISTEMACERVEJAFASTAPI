import React, { useState } from 'react';
import api from '../api';

function BeerDelete() {
  const [id, setId] = useState('');

  const handleDelete = async () => {
    try {
      await api.delete(`/cervejas/${id}`);
      alert('Cerveja deletada com sucesso!');
      setId('');
    } catch (error) {
      console.error('Erro ao deletar cerveja:', error);
    }
  };

  return (
    <div>
      <h1>Deletar Cerveja</h1>
      <input placeholder="ID" value={id} onChange={(e) => setId(e.target.value)} />
      <button onClick={handleDelete}>Deletar</button>
    </div>
  );
}

export default BeerDelete;
