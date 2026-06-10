import { useState, useContext } from "react";

import { IpContext } from "../context/IpContext";

export function useBD() {
  const [users, setUsers] = useState(null);
  const [user, setUser] = useState(null);
  const [freeSchedules, setFreeSchedules] = useState();
  const [clinics, setClinics] = useState(null);
  const [specialties, setSpecialties] = useState({});
  const [patientSchedules, setPatientSchedules] = useState(null);

  const [addAppointmentStatus, setAddAppointmentStatus] = useState(null);
  const [loading, setLoading] = useState(false);
  const [freeSchedulesLoaded, setFreeSchedulesLoaded] = useState(true);
  const [patientSchedulesLoaded, setPatientSchedulesLoaded] = useState(true);
  const [clinicLoaded, setClinicLoaded] = useState(false);
  const [specialtieLoaded, setSpecialtieLoaded] = useState(false);
  const [finished, setFinished] = useState(false);
  const [isRegistered, setIsRegistered] = useState();

  const { ip } = useContext(IpContext);

  const getUsers = async () => {
    try {
      const response = await fetch(`http://${ip}:8080/api/users`);
      const data = await response.json();
      setUsers(data);
    } catch (error) {
      console.log("Erro: ", error);
    }
  };

  const getUser = async (url) => {
    try {
      const response = await fetch(url);
      const data = await response.json();
      setUser(data);
    } catch (error) {
      console.log("Erro: ", error);
    }
  };

  const addUser = async (credentials) => {
    try {
      setFinished(false);
      setLoading(true);
      const response = await fetch(`http://${ip}:8080/api/addUser`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify(credentials),
      });

      const result = await response.json();

      if (response.ok) {
        console.log("Registrado com sucesso!");
        setIsRegistered(true);
      } else {
        console.log("Erro: ", result.error);
        setIsRegistered(false);
      }
    } catch (error) {
      console.log("Erro na requisição");
      setIsRegistered(false);
    } finally {
      setLoading(false);
      setFinished(true);
    }
  };

  const getClinics = async () => {
    try {
      setClinicLoaded(false);
      const response = await fetch(`http://${ip}:8080/api/clinics`);
      const data = await response.json();
      setClinics(data);
      console.log(data);
    } catch (error) {
      console.log("Erro: ", error);
    } finally {
      setClinicLoaded(true);
    }
  };

  const getSpecialties = async () => {
    try {
      setSpecialtieLoaded(false);
      const response = await fetch(`http://${ip}:8080/api/specialties`);
      const data = await response.json();
      setSpecialties(data);
    } catch (error) {
      console.log("Error: ", error);
    } finally {
      setSpecialtieLoaded(true);
    }
  };

  const getFreeSchedules = async (filter) => {
    try {
      setFreeSchedulesLoaded(false);
      const specialtie = encodeURIComponent(filter.specialtieState);
      const date = filter.date || "";
      let url = `http://${ip}:8080/api/filtered_schedules/search?specialtie=${specialtie}&start_time=${date}`;
      if (filter.clinicState && filter.clinicState !== "undefined") {
        url += `&clinic=${encodeURIComponent(filter.clinicState)}`;
      }

      const response = await fetch(url);
      const data = await response.json();

      console.log(data);
      setFreeSchedules(data);
    } catch (error) {
      console.log("Error: ", error);
    } finally {
      setFreeSchedulesLoaded(true);
    }
  };

  const getPatientSchedules = async (id) => {
    try {
      setPatientSchedules(false);
      const url = `http://${ip}:8080/api/schedule_by_patient/search?patient=${id}`;

      const response = await fetch(url);
      const data = await response.json();

      console.log(data);
      setPatientSchedules(data);
    } catch (error) {
      console.log("Erro: ", error);
    } finally {
      setPatientSchedulesLoaded(true);
    }
  };

  const addAppointment = async (patient_id, free_schedule_id, filter) => {
    setAddAppointmentStatus(null);
    const data = { patient_id, free_schedule_id };
    try {
      const response = await fetch(`http://${ip}:8080/api/add_appointment`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();

      if (response.ok) {
        console.log("Consulta marcada com sucesso");
        setAddAppointmentStatus("OK");
      } else {
        console.log("Erro: ", result.error);
        setAddAppointmentStatus("NOT OK");
      }
    } catch (error) {
      console.log("Erro na requisição");
      setAddAppointmentStatus("NETWORK ERROR");
    } finally {
      getFreeSchedules(filter);
      setTimeout(() => {
        setAddAppointmentStatus(null);
      }, 5000);
    }
  };

  return {
    users,
    user,
    loading,
    isRegistered,
    finished,
    freeSchedules,
    clinics,
    specialties,
    clinicLoaded,
    specialtieLoaded,
    freeSchedulesLoaded,
    patientSchedules,
    patientSchedulesLoaded,
    addAppointmentStatus,
    setIsRegistered,
    setFinished,
    getUsers,
    getUser,
    addUser,
    getClinics,
    getSpecialties,
    getFreeSchedules,
    getPatientSchedules,
    addAppointment,
  };
}
