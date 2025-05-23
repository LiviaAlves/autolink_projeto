import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import PrivateRoute from "./components/PrivateRoute";
import ForgotPassword from "./pages/ForgotPassword";
import RegisterCompany from "./pages/RegisterCompany";
import Company from "./pages/Company";
import TelaInicial from "./pages/TelaInicial";
import TelaPublica from "./pages/TelaPublica";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/register-company" element={ <PrivateRoute> <RegisterCompany /> </PrivateRoute> } />
        <Route path="/dashboard" element={ <PrivateRoute> <Dashboard /> </PrivateRoute> } />
        <Route path="/company" element={ <PrivateRoute> <Company /> </PrivateRoute>}/>
        <Route path="/inicio" element={<TelaInicial />} />
        <Route path="/" element={<TelaPublica />} />
        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
