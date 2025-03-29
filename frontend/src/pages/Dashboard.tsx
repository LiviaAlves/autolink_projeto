import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const [data, setData] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/admin/", {
          headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
        });
        setData(response.data.message);
      } catch (error: unknown) {
        if (axios.isAxiosError(error)) {
          alert(error.response?.data?.detail || "Erro na requisição.");
        } else {
          alert("Erro desconhecido.");
        }
      }
    };

    fetchData();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <div>
      <h1>Dashboard</h1>
      <p>{data}</p>
      <button onClick={handleLogout}>Sair</button>
    </div>
  );
};

export default Dashboard;
