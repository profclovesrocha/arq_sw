// HOOKS
import { useState, useContext } from "react";
import { useBD } from "../hooks/useBD";
// CONTEXTS
import { SessionContext } from "../context/SessionContext";

const FreeSchedules = ({ freeSchedules, filter, addAppointmentStatus, addAppointment }) => {
  console.log(filter);
  const { sessionData } = useContext(SessionContext);

  const appointmentResponse = (status) => {
    switch (status) {
      case "OK":
        return "Consulta marcada com sucesso!";
        break;
      case "NOT OK":
        return "Erro na marcação, tente novamente!";
        break;
      case "NETWORK ERROR":
        return "Erro de conexão. Verifique sua internet!";
        break;
      default:
        return "";
        break;
    }
  };

  return (
    <div className="schedules-container">
      <ul className="schedules-list">
        {addAppointmentStatus && (
          <p
            className="appointment-response"
            style={
              addAppointmentStatus === "OK"
                ? { color: "#36a26f" }
                : { color: "#dc143c" }
            }
          >
            {appointmentResponse(addAppointmentStatus)}
          </p>
        )}
        {!freeSchedules ? (
          <p>Filtre para encontrar uma consulta.</p>
        ) : (
          freeSchedules.map((agenda) => {
            const date = new Date(agenda.start_time);
            const formatedDate = new Intl.DateTimeFormat("pt-BR", {
              day: "2-digit",
              month: "2-digit",
              year: "numeric",
            }).format(date);

            const start_time = new Intl.DateTimeFormat("pt-BR", {
              hour: "2-digit",
              minute: "2-digit",
            }).format(date);

            const weekDay = new Intl.DateTimeFormat("pt-BR", {
              weekday: "short",
            }).format(date);

            return (
              <li
                key={agenda.id}
                className="schedule"
                onDoubleClick={() => {
                  addAppointment(sessionData.id, agenda.id, filter);
                }}
              >
                <div>
                  <h2 className="doctor">{agenda.doctor}</h2>
                  <span className="specialtie">{agenda.specialtie}</span>
                </div>
                <div>
                  <span className="local">Local:</span>
                  <span className="clinic">{agenda.clinic}</span>
                </div>
                <div className="date-and-time-info">
                  <span className="start-time">{start_time}</span>
                  <span className="weekday">{weekDay}</span>
                  <span className="date">{formatedDate}</span>
                </div>
              </li>
            );
          })
        )}
      </ul>
    </div>
  );
};

export default FreeSchedules;
