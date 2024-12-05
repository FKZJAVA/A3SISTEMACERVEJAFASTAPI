import React, { useEffect, useState } from 'react';
import api from '../api';

function BeerList() {
  const [beers, setBeers] = useState([]);

  useEffect(() => {
    api.get('/cervejas/')
      .then(response => setBeers(response.data))
      .catch(error => console.error('Erro ao buscar cervejas:', error));
  }, []);

  const handleDelete = (id) => {
    api.delete(`/cervejas/${id}`)
      .then(() => setBeers(beers.filter(beer => beer.id_cerveja !== id)))
      .catch(error => console.error('Erro ao deletar cerveja:', error));
  };

  return (
    <div>
      <h1>Lista de Cervejas</h1>
      <ul>
        {beers.map(beer => (
          <li key={beer.id_cerveja}>
            {beer.nome} - {beer.valor} - Estoque: {beer.estoque}
            <button onClick={() => handleDelete(beer.id_cerveja)}>Deletar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BeerList;
