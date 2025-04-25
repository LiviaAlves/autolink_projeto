import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import '../styles/forgotpassword.css';

const ForgotPassword = () => {
  const [email, setEmail] = useState("");
  const [code, setCode] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState(""); 
  const [step, setStep] = useState(1); 
  const [error, setError] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);
  const [passwordError, setPasswordError] = useState<string | null>(null);
  const [confirmPasswordError, setConfirmPasswordError] = useState<string | null>(null); 
  const navigate = useNavigate();

 
  const handleEmailSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccessMessage(null);

    try {
      await axios.post("http://127.0.0.1:8000/api/forgot-password/", { email });
      setSuccessMessage("Código enviado para seu email!");
      setStep(2);
    } catch (error: unknown) {
      if (axios.isAxiosError(error)) {
        const responseError = error.response?.data?.detail || "Erro ao enviar o código. Tente novamente.";
        setError(responseError);
      } else if (error instanceof Error) {
        setError(error.message || "Erro desconhecido.");
      } else {
        setError("Erro desconhecido.");
      }
    }
  };

 
  const handleCodeSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccessMessage(null);

   
    if (newPassword.length < 8) {
      setPasswordError("A nova senha deve ter pelo menos 8 caracteres.");
      return;
    } else {
      setPasswordError(null);
    }

    
    if (newPassword !== confirmPassword) {
      setConfirmPasswordError("As senhas não são iguais. Tente novamente!");
      return;
    } else {
      setConfirmPasswordError(null); 
    }

    try {
      await axios.post("http://127.0.0.1:8000/api/reset-password/", {
        email,
        reset_code: code,
        new_password: newPassword,
      });

      setSuccessMessage("Senha alterada com sucesso!");
      setTimeout(() => navigate("/login"), 2000);
    } catch (error: unknown) {
      if (axios.isAxiosError(error)) {
        const responseError = error.response?.data;
        console.log("Erro na resposta do backend:", responseError);

        if (responseError?.non_field_errors) {
       
          setError(responseError.non_field_errors[0]);
        } else {
       
          setError(responseError?.detail || "Erro desconhecido.");
        }
      } else if (error instanceof Error) {
        setError(error.message || "Erro desconhecido.");
      } else {
        setError("Erro desconhecido.");
      }
    }
  };


  const handleNewPasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setNewPassword(value);

    
    if (value.length >= 8) {
      setPasswordError(null);
    }
  };

  
  const handleConfirmPasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setConfirmPassword(value);

    
    if (value === newPassword) {
      setConfirmPasswordError(null); 
    }
  };

  return (
    <div className="forgot-password-page">
    <div className="forgot-password-logo">
      <img src="/autolink2.png" alt="Logo" />
    </div>

    <div className="forgot-password-form-container">
      {step === 1 ? (
        <>
          <h2>Recuperação de Senha</h2>
          <form onSubmit={handleEmailSubmit} className="forgot-password-form">
            <div className="forgot-password-input-container">
              <input
                type="email"
                name="email"
                placeholder=" "
                onChange={(e) => setEmail(e.target.value)}
                required
                value={email}
              />
              <label htmlFor="email">Digite seu email</label>
            </div>
            {error && <div className="forgot-password-error">{error}</div>}
            <button type="submit" className="forgot-password-submit-button">Enviar código</button>
          </form>
        </>
      ) : (
        <>
          <h2>Verificação do Código</h2>
          <form onSubmit={handleCodeSubmit} className="forgot-password-form">
            <div className="forgot-password-input-container">
              <input
                type="text"
                name="code"
                placeholder=" "
                onChange={(e) => setCode(e.target.value)}
                required
                value={code}
              />
              <label htmlFor="code">Código recebido</label>
            </div>

            <div className="forgot-password-input-container">
              <input
                type="password"
                name="newPassword"
                placeholder=" "
                onChange={handleNewPasswordChange}
                required
                value={newPassword}
              />
              <label htmlFor="newPassword">Nova Senha</label>
              {passwordError && <div className="forgot-password-error">{passwordError}</div>}
            </div>

            <div className="forgot-password-input-container">
              <input
                type="password"
                name="confirmPassword"
                placeholder=" "
                onChange={handleConfirmPasswordChange}
                required
                value={confirmPassword}
              />
              <label htmlFor="confirmPassword">Confirmar Nova Senha</label>
              {confirmPasswordError && <div className="forgot-password-error">{confirmPasswordError}</div>}
            </div>

            {error && <div className="forgot-password-error">{error}</div>}
            <button type="submit" className="forgot-password-submit-button">Redefinir Senha</button>
          </form>
        </>
      )}

      {successMessage && <div className="forgot-password-success-message">{successMessage}</div>}
    </div>
  </div>
  );
};

export default ForgotPassword;
