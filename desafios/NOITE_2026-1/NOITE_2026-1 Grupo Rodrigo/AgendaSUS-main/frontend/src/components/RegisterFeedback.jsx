import React from "react";
// ASSETS
import error from "../assets/error.svg";
import success from "../assets/success.svg";
// STYLES
import "./RegisterFeedback.css";
// HOOKS
import { useNavigate } from "react-router";

const RegisterFeedback = ({ isRegistered, setFinished }) => {
  const navigate = useNavigate();
  return (
    <section
      className="login-container register-situation"
      id="register-container"
    >
      <div className="situation">
        <img
          src={isRegistered ? success : error}
          alt="Ícone situação do registro"
        />
        <p className="text-situation">
          {isRegistered
            ? "Usuário cadastrado com sucesso!"
            : "Falha ao cadastrar usuário. Tente novamente!"}
        </p>
        <button
          id="finish-register"
          onClick={() => {
            isRegistered ? navigate("../") : setFinished(false); //faltando uma forma de voltar para o formulário de cadastro;
          }}
        >
          {isRegistered ? "Fazer login" : "Cadastrar"}
        </button>
      </div>
    </section>
  );
};

export default RegisterFeedback;
