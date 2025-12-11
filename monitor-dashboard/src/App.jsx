import { useEffect, useState } from "react";
import "./App.css";
import Card from "./Card";

function App() {
  const [dolar, setDolar] = useState("...");
  const [euro, setEuro] = useState("...");

  async function buscarDados() {
    try {
      const respDolar = await fetch("http://localhost:8000/dolar");
      const dadosDolar = await respDolar.json();
      setDolar(dadosDolar.valor);

      const respEuro = await fetch("http://localhost:8000/euro");
      const dadosEuro = await respEuro.json();
      setEuro(dadosEuro.valor);
    } catch (e) {
      console.error("Erro ao buscar dados: ", e);
      setDolar("Erro");
      setEuro("Erro");
    }
  }

  useEffect(() => {
    buscarDados();
  }, []);

  return (
    <>
      <div className="painel">
        <h1>Monitor Fiscal Dashboard</h1>
        <div className="status-bar">
          <button onClick={buscarDados}>Atualizar Agora</button>
        </div>

        <div className="cards-container">
          <Card titulo="Dólar comercial" valor={dolar} />
          <Card titulo="Euro" valor={euro} />
        </div>
      </div>
    </>
  );
}

export default App;
