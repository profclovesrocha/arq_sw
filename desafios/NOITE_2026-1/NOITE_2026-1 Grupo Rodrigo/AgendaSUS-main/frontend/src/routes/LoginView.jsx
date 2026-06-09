// HOOKS
import { useEffect, useState } from "react";
import { useAuth } from "../hooks/useAuth";
import { useNavigate } from "react-router";
// ASSETS
import google_icon from "../assets/google-icon.svg";
// STYLES
import "./LoginView.css";
// COMPONENTS
import Presentation from "../components/Presentation";

const LoginView = () => {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { isAuth, authenticate, logout } = useAuth();

  useEffect(() => {
    logout();
    setEmail("");
    setPassword("");
  }, []);

  return (
    <div className="login-view">
      <Presentation />
      <section className="login-container">
        <form
          className="login"
          onSubmit={(e) => {
            e.preventDefault();
            authenticate(email.trim(), password.trim());
          }}
        >
          <h3>Identifique-se com:</h3>
          <p
            className="invalid-credentials"
            style={{ opacity: isAuth === false ? 1 : 0 }}
          >
            Credenciais inválidas! Tente novamente ou cadastre-se.
          </p>
          <label htmlFor="email">
            <span>E-mail:</span>
            <input
              type="email"
              required
              placeholder="Digite seu e-mail..."
              name="email"
              id="email"
              value={email}
              onChange={(e) => {
                setEmail(e.target.value);
              }}
            />
          </label>
          <label htmlFor="password">
            <span>Senha:</span>
            <input
              type="password"
              name="password"
              id="password"
              required
              placeholder="Digite sua senha..."
              value={password}
              onChange={(e) => {
                setPassword(e.target.value);
              }}
            />
          </label>
          <button type="submit">Entrar</button>
          <span className="forget-password">Esqueceu a senha?</span>
          <div className="login-methods">
            <span className="enter-with">Ou entrar com:</span>
            <div className="login-with-google">
              <img src={google_icon} alt="Google logo" />
              <span>Google</span>
            </div>
          </div>
          <span
            className="forget-password register-span"
            onClick={() => navigate("cadastrar")}
          >
            Registre-se aqui!
          </span>
        </form>
      </section>
    </div>
  );
};

export default LoginView;
