// HOOKS
import { createContext, useEffect, useState } from "react";

export const SessionContext = createContext();

export const SessionContextProvider = ({ children }) => {
  const [sessionData, setSessionData] = useState(null);

  const logout = () => {
    setSessionData(null);
  };

  return (
    <SessionContext.Provider value={{ sessionData, setSessionData, logout }}>
      {children}
    </SessionContext.Provider>
  );
};
