import { Link } from "react-router-dom";

function Dashboard() {
  return (
    <div>
      <h1>Bem-vindo ao Dashboard</h1>
      <Link to="/register-company">
        <button>Registrar nova empresa</button>
      </Link>
    </div>
  );
}

export default Dashboard;
