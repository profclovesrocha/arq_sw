// HOOKS
import { useState } from "react";
import { Outlet } from "react-router";
// COMPONENTS
import Header from "./components/Header.jsx";
// STYLES
import "./App.css";

function App() {
  return (
    <div className="main-view">
      <Header />
      <Outlet />
    </div>
  );
}

export default App;
