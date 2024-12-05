import React, { useState } from 'react';
import api from '../api';

function BeerEdit() {
  const [id, setId] = useState('');
  const [nome, setNome] = useState('');
  const [estoque, setEstoque] = useState('');
  const [valor, setValor] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.put(`/cervejas/${id}`, { nome, estoque: parseInt(estoque), valor: parseFloat(valor) });
      alert('Cerveja atualizada com sucesso!');
      setId('');
      setNome('');
      setEstoque('');
      setValor('');
    } catch (error) {
      console.error('Erro ao atualizar cerveja:', error);
    }
  };

  return (
    <div>
      <h1>Editar Cerveja</h1>
      <form onSubmit={handleSubmit}>
        <input placeholder="ID" value={id} onChange={(e) => setId(e.target.value)} required />
        <input placeholder="Nome" value={nome} onChange={(e) => setNome(e.target.value)} />
        <input placeholder="Estoque" value={estoque} onChange={(e) => setEstoque(e.target.value)} />
        <input placeholder="Valor" value={valor} onChange={(e) => setValor(e.target.value)} />
        <button type="submit">Atualizar</button>
      </form>
    </div>
  );
}

export default BeerEdit;
