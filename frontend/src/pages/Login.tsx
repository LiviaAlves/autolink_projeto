import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { FiEye, FiEyeOff } from "react-icons/fi";
import '../styles/login.css';

const Login = () => {
  const [form, setForm] = useState({ username: "", password: "" });
  const [passwordVisible, setPasswordVisible] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleForgotPasswordRedirect = () => {
    navigate("/forgot-password");
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccessMessage(null);

  

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/token/", form);
      localStorage.setItem("token", response.data.access);
      setSuccessMessage("Login realizado com sucesso!");
      setTimeout(() => {
        navigate("/dashboard"); 
      }, 2000);
    } catch (error: unknown) {
      if (axios.isAxiosError(error)) {
        setError(error.response?.data?.detail || "Usuário ou senha incorretos.");
      } else {
        setError("Erro desconhecido.");
      }
    }
  };

  const handleRegisterRedirect = () => {
    navigate("/register");
  };

  return (
    <div className="container">
      <div className="logo">
        <img src="../../public/autolink2.png" alt="Logo" />
      </div>

      <div className="form-container">
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-container">
            <input
              type="text"
              name="username"
              placeholder=" "
              onChange={handleChange}
              required
              value={form.username}
            />
            <label htmlFor="username">Nome</label>
          </div>

          <div className="input-container password-container">
            <input
              type={passwordVisible ? "text" : "password"}
              name="password"
              placeholder=" "
              onChange={handleChange}
              required
              value={form.password}
            />
            <label htmlFor="password">Senha</label>
            <span
              className="eye-icon"
              onClick={() => setPasswordVisible(!passwordVisible)}
            >
              {passwordVisible ? <FiEyeOff /> : <FiEye />}
            </span>
          </div>

          {error && <div className="error">{error}</div>}

          <button className="esqueci-senha" onClick={handleForgotPasswordRedirect}>
            Esqueceu a senha?
          </button>

          <button type="submit">Entrar</button>
        </form>

        <button className="ja-temo-conta" onClick={handleRegisterRedirect}>
          Não tenho conta
        </button>

        {successMessage && <div className="success-message">{successMessage}</div>}
      </div>
    </div>
  );
};

export default Login;
