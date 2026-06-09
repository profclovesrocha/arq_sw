import React from "react";
// STYLES
import "./Appointments.css";

const Appointments = ({ patientSchedules }) => {
  return (
    <div className="schedules-container">
      <ul className="schedules-list">
        {!patientSchedules || patientSchedules.length < 1 ? (
          <p>Sem consultas agendadas.</p>
        ) : (
          patientSchedules.map((agenda) => {
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

            let borderStyle;

            switch (agenda.status) {
              case "CANCELED":
                borderStyle = { border: "3px solid #DC143C" };
                break;
              case "SCHEDULED":
                borderStyle = { border: "3px solid #2581B2" };
                break;
              case "CONCLUDED":
                borderStyle = { border: "3px solid #36A26F" };
                break;
            }

            return (
              <li key={agenda.id} className="schedule" style={borderStyle}>
                <div>
                  <h2 className="doctor">{agenda.doctor}</h2>
                  <span className="specialtie">{agenda.specialtie}</span>
                </div>
                <div>
                  <span className="local">Local:</span>
                  <span className="clinic">{agenda.location}</span>
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
      <div className="status-info">
        <div className="info">
          <div className="color info-blue"></div>
          <span>Agendado</span>
        </div>
        <div className="info">
          <div className="color info-green"></div>
          <span>Concluído</span>
        </div>
        <div className="info">
          <div className="color info-red"></div>
          <span>Cancelado</span>
        </div>
      </div>
    </div>
  );
};

export default Appointments;
