import React, { useState } from 'react';
import api from '../api';

function BeerCreate() {
  const [nome, setNome] = useState('');
  const [estoque, setEstoque] = useState('');
  const [valor, setValor] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/cervejas/', { nome, estoque: parseInt(estoque), valor: parseFloat(valor) });
      alert('Cerveja adicionada com sucesso!');
      setNome('');
      setEstoque('');
      setValor('');
    } catch (error) {
      console.error('Erro ao adicionar cerveja:', error);
    }
  };

  return (
    <div>
      <h1>Adicionar Cerveja</h1>
      <form onSubmit={handleSubmit}>
        <input placeholder="Nome" value={nome} onChange={(e) => setNome(e.target.value)} required />
        <input placeholder="Estoque" value={estoque} onChange={(e) => setEstoque(e.target.value)} required />
        <input placeholder="Valor" value={valor} onChange={(e) => setValor(e.target.value)} required />
        <button type="submit">Adicionar</button>
      </form>
    </div>
  );
}

export default BeerCreate;
