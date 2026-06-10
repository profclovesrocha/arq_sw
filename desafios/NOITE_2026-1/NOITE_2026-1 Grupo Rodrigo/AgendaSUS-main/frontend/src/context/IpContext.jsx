import { createContext } from "react";

export const IpContext = createContext();

export const IpContextProvider = ({ children }) => {
  const ip = window.location.hostname; //ALTERAR IP AQUI

  return <IpContext.Provider value={{ ip }}>{children}</IpContext.Provider>;
};
