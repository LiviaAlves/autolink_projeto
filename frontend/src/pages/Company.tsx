import { useEffect, useState } from "react";
import axios from "axios";
import "../styles/viewCompany.css";

interface Empresa {
  id: number;
  nome_fantasia: string;
  endereco: string;
  logo: string | null;
}

const Empresas = () => {
  const [empresas, setEmpresas] = useState<Empresa[]>([]);

  useEffect(() => {
    const fetchEmpresas = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/empresas/");
        setEmpresas(response.data);
      } catch (error) {
        console.error("Erro ao buscar empresas:", error);
      }
    };

    fetchEmpresas();
  }, []);

  return (
    <div className="container">
      <h1 className="titulo">Empresas Disponíveis</h1>
      <div className="grid">
        {empresas.map((empresa) => (
          <div key={empresa.id} className="card">
            <div className="logo-empresa">
              {empresa.logo ? (
                // Concatene corretamente a URL da imagem
                <img
                  src={`http://localhost:8000${empresa.logo}`} // Certifique-se que a logo está retornando um caminho válido
                  className="logo-empresa"
                />
              ) : (
                <span>{empresa.nome_fantasia[0]}</span> // Caso não tenha logo, exibe a inicial
              )}
            </div>
            <div className="empresa-info">
              <h2>{empresa.nome_fantasia}</h2>
              <p>{empresa.endereco}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Empresas;
