// HOOKS
import { useEffect } from "react";
import { useBD } from "../hooks/useBD";
// STYLES
import "./Clinics.css"

const Clinics = () => {
  const { getClinics, clinics } = useBD();

  useEffect(() => {
    getClinics();
  }, []);
  return (
    <div id="clinics-container">
      <h2 className="clinics-title">Nossas Unindades</h2>
      <ul className="clinics-list">
        {clinics ? (
          clinics.map((clinic) => (
            <li key={clinic.id}>
              <p>{clinic.name}</p>
            </li>
          ))
        ) : (
          <p className="loading">Carregando...</p>
        )}
      </ul>
    </div>
  );
};

export default Clinics;
