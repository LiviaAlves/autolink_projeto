import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { FiEye, FiEyeOff } from "react-icons/fi";
import "../styles/register.css";

const Register = () => {
  const [form, setForm] = useState({ username: "", email: "", password: "", confirmPassword: "" });
  const [error, setError] = useState<string | null>(null); 
  const [successMessage, setSuccessMessage] = useState<string | null>(null);
  const [passwordVisible, setPasswordVisible] = useState(false);
  const [confirmPasswordVisible, setConfirmPasswordVisible] = useState(false);
  const [passwordError, setPasswordError] = useState<string | null>(null);
  const [confirmPasswordError, setConfirmPasswordError] = useState<string | null>(null); 
  const navigate = useNavigate();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });

    if (e.target.name === "confirmPassword") {
      if (form.password !== e.target.value) {
        setConfirmPasswordError("As senhas não são iguais.");
      } else {
        setConfirmPasswordError(null);
      }
    }
    if (e.target.name === "password" && form.confirmPassword !== "") {
      if (form.password !== form.confirmPassword) {
        setConfirmPasswordError("As senhas não são iguais.");
      } else {
        setConfirmPasswordError(null);
      }
    }
  };

  const handlePasswordBlur = () => {
    if (form.password === "") {
      setPasswordError(null);
    } else if (form.password.length < 8) {
      setPasswordError("A senha deve ter pelo menos 8 caracteres.");
    } else {
      setPasswordError(null);
    }
  };

  const handleConfirmPasswordBlur = () => {
    if (form.confirmPassword === "") {
      setConfirmPasswordError(null);
    } else if (form.password !== form.confirmPassword) {
      setConfirmPasswordError("As senhas não são iguais.");
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (passwordError || confirmPasswordError) {
      setError("Corrija os erros antes de enviar");
      return;
    }

    setError(null);
    setSuccessMessage(null); 

    try {
      await axios.post("http://127.0.0.1:8000/api/register/", form);
      setSuccessMessage("Conta criada com sucesso!");
      setForm({ username: "", email: "", password: "", confirmPassword: "" });
      setTimeout(() => {
        navigate("/login");
      }, 2000);
    } catch (error: unknown) {
      if (axios.isAxiosError(error)) {
        setError(error.response?.data?.detail || "Erro na requisição.");
      } else {
        setError("Erro desconhecido.");
      }
    }
  };

  const handleLoginRedirect = () => {
    navigate("/login");
  };

  return (
    <div className="register-page">
      <div className="register-logo">
        <img src="/autolink2.png" alt="Logo" />
      </div>

      <div className="register-form-container">
        <h2>Crie sua conta!</h2>
        <form onSubmit={handleSubmit}>
          <div className="register-input-container">
            <input
              type="text"
              name="username"
              id="username"
              placeholder="Nome"
              value={form.username}
              onChange={handleChange}
              required
            />
            <label htmlFor="username">Nome</label>
          </div>

          <div className="register-input-container">
            <input
              type="email"
              name="email"
              id="email"
              placeholder="E-mail"
              value={form.email}
              onChange={handleChange}
              required
            />
            <label htmlFor="email">E-mail</label>
          </div>

          <div className="register-password-container">
            <div className="register-input-container">
              <input
                type={passwordVisible ? "text" : "password"}
                name="password"
                id="password"
                placeholder="Senha"
                value={form.password}
                onChange={handleChange}
                onBlur={handlePasswordBlur}
                required
              />
              <label htmlFor="password">Senha</label>
              <span
                className="register-eye-icon"
                onClick={() => setPasswordVisible(!passwordVisible)}
              >
                {passwordVisible ? <FiEyeOff /> : <FiEye />}
              </span>
            </div>
            {passwordError && <div className="register-error">{passwordError}</div>}
          </div>

          <div className="register-password-container">
            <div className="register-input-container">
              <input
                type={confirmPasswordVisible ? "text" : "password"}
                name="confirmPassword"
                id="confirmPassword"
                placeholder="Repetir Senha"
                value={form.confirmPassword}
                onChange={handleChange}
                onBlur={handleConfirmPasswordBlur}
                required
              />
              <label htmlFor="confirmPassword">Repetir Senha</label>
              <span
                className="register-eye-icon"
                onClick={() => setConfirmPasswordVisible(!confirmPasswordVisible)}
              >
                {confirmPasswordVisible ? <FiEyeOff /> : <FiEye />}
              </span>
            </div>
            {confirmPasswordError && <div className="register-error">{confirmPasswordError}</div>}
          </div>

          {error && <div className="register-error">{error}</div>}

          <button type="submit" className="register-submit-button">Criar conta</button>
        </form>

        <button className="register-login-btn" onClick={handleLoginRedirect}>
          Já tenho conta
        </button>

        {successMessage && <div className="register-success-message">{successMessage}</div>}
      </div>
    </div>
  );
};

export default Register;
