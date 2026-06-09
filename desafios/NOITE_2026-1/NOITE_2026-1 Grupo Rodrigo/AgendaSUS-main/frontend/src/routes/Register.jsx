import { useState } from "react";
import { useNavigate } from "react-router";
import { PatternFormat } from "react-number-format";
// COMPONENTS
import Presentation from "../components/Presentation";
import RegisterFeedback from "../components/RegisterFeedback";
// ASSETS
import backIcon from "../assets/back-icon.svg";
// STYLES
import "./Register.css";
// HOOKS
import { useBD } from "../hooks/useBD";

const Register = () => {
  const navigate = useNavigate();
  const { addUser, loading, isRegistered, setFinished, finished } = useBD();
  const [cpf, setCpf] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [birthdate, setBirthdate] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  return (
    <div className="login-view">
      <Presentation />
      {!finished ? (
        <section className="login-container" id="register-container">
          <form
            className="register-form"
            onSubmit={(e) => {
              e.preventDefault();
              const credentials = {
                users: {
                  email: email.trim(),
                  password: password.trim(),
                  role: "PATIENT",
                },
                patient: {
                  name: username.trim(),
                  cpf: cpf,
                  birthdate: birthdate,
                  phoneNumber: phoneNumber,
                },
              };
              addUser(credentials);
            }}
          >
            <div className="title-container">
              <img
                src={backIcon}
                alt="Voltar"
                className="back-icon"
                onClick={() => navigate("/")}
              />
              <h3>Cadastre-se</h3>
            </div>
            <label htmlFor="cpf">
              <span>
                CPF: <span className="required">*</span>
              </span>
              <PatternFormat
                format="###.###.###-##"
                mask="_"
                placeholder="000.000.000-00"
                required
                id="cpf"
                name="cpf"
                value={cpf || ""}
                onValueChange={(value) => {
                  setCpf(value.value);
                }}
              />
            </label>
            <label htmlFor="phone-number">
              <span>
                Número de telefone: <span className="required">*</span>
              </span>
              <PatternFormat
                format="(##)#####-####"
                mask=""
                placeholder="(81)99999-9999"
                required
                id="phone-number"
                name="phone-number"
                value={phoneNumber || ""}
                onValueChange={(value) => {
                  setPhoneNumber(value.value);
                }}
              />
            </label>
            <label htmlFor="birth-date">
              <span>
                Data de nascimento: <span className="required">*</span>
              </span>
              <input
                type="date"
                name="birth-date"
                id="birth-date"
                required
                value={birthdate}
                onChange={(e) => {
                  setBirthdate(e.target.value);
                }}
              />
            </label>
            <label htmlFor="username">
              <span>
                Nome de usuário: <span className="required">*</span>
              </span>
              <input
                type="text"
                name="username"
                id="username"
                required
                placeholder="Digite um nome de usuário..."
                value={username}
                onChange={(e) => {
                  setUsername(e.target.value);
                }}
              />
            </label>
            <label htmlFor="email">
              <span>
                E-mail: <span className="required">*</span>
              </span>
              <input
                type="email"
                name="email"
                id="email"
                required
                placeholder="Digite seu e-mail..."
                value={email}
                onChange={(e) => {
                  setEmail(e.target.value);
                }}
              />
            </label>
            <label htmlFor="password">
              <span>
                Senha: <span className="required">*</span>
              </span>
              <input
                type="password"
                name="password"
                id="password"
                required
                placeholder="Crie sua senha..."
                value={password}
                onChange={(e) => {
                  setPassword(e.target.value);
                }}
              />
            </label>
            <button type="submit" id="finish-register" disabled={loading}>
              {loading ? "..." : "Concluído"}
            </button>
          </form>
        </section>
      ) : (
        <RegisterFeedback
          isRegistered={isRegistered}
          setFinished={setFinished}
        />
      )}
    </div>
  );
};

export default Register;
