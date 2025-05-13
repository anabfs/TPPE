import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [clientes, setClientes] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/clientes")
      .then((response) => setClientes(response.data))
      .catch((error) => console.error("Erro ao buscar clientes:", error));
  }, []);

  return (
    <div>
      <h1>Clientes</h1>
      <ul>
        {clientes.map((cliente) => (
          <li key={cliente.cpf}>{cliente.nome}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
