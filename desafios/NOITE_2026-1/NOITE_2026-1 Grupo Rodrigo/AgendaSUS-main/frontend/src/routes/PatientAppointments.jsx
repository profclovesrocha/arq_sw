// HOOKS
import { useEffect, useContext } from "react";
import { useBD } from "../hooks/useBD";
// CONTEXT
import { SessionContext } from "../context/SessionContext";
import Appointments from "../components/Appointments";
// STYLES
import "./PatientAppointments.css";

const PatientAppointments = () => {
  const { patientSchedules, patientSchedulesLoaded, getPatientSchedules } =
    useBD();

  const { sessionData } = useContext(SessionContext);

  useEffect(() => {
    getPatientSchedules(sessionData.id);
  }, []);

  return (
    <div id="schedule-panel">
      <h2 className="appointments-title">Seus agendamentos</h2>
      {patientSchedulesLoaded ? (
        <Appointments patientSchedules={patientSchedules} />
      ) : (
        <p>Carregando...</p>
      )}
    </div>
  );
};

export default PatientAppointments;
