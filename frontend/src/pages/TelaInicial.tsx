import "../styles/Telainicial.css";
import { useNavigate } from "react-router-dom";

const TelaInicial = () => {
  const navigate = useNavigate();

  const handleProximasOficinas = () => {
    navigate("/dashboard");
  };

  return (
    <div className="min-h-screen bg-cover bg-center relative">
      {/* Overlay escura */}
      <div className="absolute inset-0 bg-black bg-opacity-70"></div>

      {/* Conteúdo principal */}
      <div className="relative z-10 flex flex-col min-h-screen">
        {/* Header */}
        <header className="header text-white">
          <div className="header-content">
            <div className="logo">
              <img src="/autolink2.png" alt="AutoLink" className="h-10" />
            </div>
            <nav className="nav-links">
              <a href="#">REGISTRAR EMPRESA</a>
              <a href="#">MECÂNICAS</a>
              <div className="user-info">
                <span className="font-bold">LÍVIA</span>
                <img src="/perfil.jpeg" alt="Avatar do usuário" className="avatar" />
              </div>
            </nav>
          </div>
        </header>

        {/* Texto Central */}
        <main className="relative flex-1 flex flex-col justify-center items-start text-white px-8">
          <div className="ofc max-w-3xl">
            <h1 className="text-3xl md:text-4xl lg:text-5xl font-bold mb-4">
              Serviço automotivo fácil e rápido no Auto Link
            </h1>
            <p className="text-base md:text-lg lg:text-xl mb-8 max-w-2xl">
              Serviço de mecânica onde e quando precisar! Agende e resolvemos na sua porta.
            </p>
          </div>

          {/* Botão posicionado manualmente na direita */}
          <button
            onClick={handleProximasOficinas}
            className="btn3 bg-yellow-600 hover:bg-yellow-500 text-white font-bold py-3 px-6 rounded"
          >
            OFICINAS PRÓXIMAS
          </button>
        </main>
      </div>
    </div>
  );
};

export default TelaInicial;
