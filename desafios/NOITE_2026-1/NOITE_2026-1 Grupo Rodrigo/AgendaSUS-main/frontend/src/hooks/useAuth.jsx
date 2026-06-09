// HOOKS
import { useEffect, useState, useContext } from "react";
import { useBD } from "./useBD";
import { useNavigate } from "react-router";
// CONTEXT
import { SessionContext } from "../context/SessionContext";
import { IpContext } from "../context/IpContext";

export function useAuth() {
  const navigate = useNavigate();

  const { user, getUser } = useBD();
  const [isAuth, setIsAuth] = useState(null);
  const [credentials, setCredentials] = useState(null);
  const { sessionData, setSessionData, logout } = useContext(SessionContext);

  const { ip } = useContext(IpContext);

  const authenticate = (email, password) => {
    const url = `http://${ip}:8080/api/users/search?email=${email}`;
    setCredentials({ email, password, url });
  };

  useEffect(() => {
    if (credentials) getUser(credentials.url);
  }, [credentials]);

  useEffect(() => {
    if (user && credentials) {
      if (
        credentials.email === user.email &&
        credentials.password === user.password
      ) {
        setSessionData(user);
        setIsAuth(true);
        navigate("agendar");
      } else {
        setIsAuth(false);
        console.log("Dados inválidos");
      }
    }
  }, [user]);

  return {
    isAuth,
    authenticate,
    logout,
    sessionData,
  };
}
