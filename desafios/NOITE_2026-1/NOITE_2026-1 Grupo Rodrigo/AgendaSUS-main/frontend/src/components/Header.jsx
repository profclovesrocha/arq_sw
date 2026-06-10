import { useContext, useEffect } from "react";
import { useNavigate, useLocation } from "react-router";
// ASSETS
import agendasus from "../assets/agendasus.svg";
import logout_icon from "../assets/logout.svg";
//CONTEXT
import { SessionContext } from "../context/SessionContext";
// STYLES
import "./Header.css";

const Header = () => {
  const { sessionData, logout } = useContext(SessionContext);
  const navigate = useNavigate();
  const location = useLocation();

  const isClinics = location.pathname === "/clinicas";
  const isAppointments = location.pathname === "/agendamentos";

  useEffect(() => {
    if (!sessionData) navigate("/");
  }, [sessionData]);

  return (
    <header>
      <div className="logo-container">
        <img
          src={agendasus}
          alt="Logo AgendaSUS"
          onClick={() => {
            if (sessionData) {
              navigate("/agendar");
            } else {
              navigate("/");
            }
          }}
          className="header-logo"
          title="Home"
        />
        <h2>
          <span className="green">Agenda</span>
          <span className="blue">SUS</span>
        </h2>
      </div>
      {sessionData ? (
        <div className="session-container">
          <div className="greetings-container">
            <span className="greetings" title="Alterar dados pessoais">
              Olá, {sessionData.name}
            </span>
          </div>
          <div className="links-container">
            <span
              className="header-links"
              onClick={() => navigate("/clinicas")}
              style={
                isClinics ? { backgroundColor: "#2883b5", color: "#fff" } : {}
              }
            >
              Nossas unidades
            </span>
            <span
              className="header-links"
              onClick={() => navigate("/agendamentos")}
              style={
                isAppointments
                  ? { backgroundColor: "#2883b5", color: "#fff" }
                  : {}
              }
            >
              Seus agendamentos
            </span>
            <img
              src={logout_icon}
              alt="Encerrar sessão"
              title="Encerrar sessão"
              onClick={() => logout()}
            />
          </div>
        </div>
      ) : (
        <div></div>
      )}
    </header>
  );
};

export default Header;
