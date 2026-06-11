import { useState } from "react";

export default function Login() {
  const [usuario, setUsuario] = useState("");
  const [senha, setSenha] = useState("");

  const fazerLogin = (e) => {
    e.preventDefault();

    if (usuario === "admin" && senha === "123456") {
      alert("Login realizado com sucesso!");
    } else {
      alert("Usuário ou senha incorretos!");
    }
  };

  return (
    <div className="container">
      <form className="login-box" onSubmit={fazerLogin}>
        <h2>Login</h2>

        <input
          type="text"
          placeholder="Usuário"
          value={usuario}
          onChange={(e) => setUsuario(e.target.value)}
        />

        <input
          type="password"
          placeholder="Senha"
          value={senha}
          onChange={(e) => setSenha(e.target.value)}
        />

        <button type="submit">Entrar</button>
      </form>
    </div>
  );
}node