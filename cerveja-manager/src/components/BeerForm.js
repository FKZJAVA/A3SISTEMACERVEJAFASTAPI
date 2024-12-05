import React, { useState } from 'react';
import api from '../api';

function BeerForm() {
  const [nome, setNome] = useState('');
  const [valor, setValor] = useState('');
  const [estoque, setEstoque] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post('/cervejas/', { nome, valor, estoque })
      .then(() => {
        setNome('');
        setValor('');
        setEstoque(0);
        alert('Cerveja adicionada com sucesso!');
      })
      .catch(error => console.error('Erro ao adicionar cerveja:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Adicionar Nova Cerveja</h2>
      <input type="text" placeholder="Nome" value={nome} onChange={(e) => setNome(e.target.value)} required />
      <input type="number" placeholder="Valor" value={valor} onChange={(e) => setValor(e.target.value)} required />
      <input type="number" placeholder="Estoque" value={estoque} onChange={(e) => setEstoque(e.target.value)} />
      <button type="submit">Adicionar</button>
    </form>
  );
}

export default BeerForm;
