USE agendasus_v1;

/*CONSULTAS COM JOIN*/
/*DRAFT*/
SELECT * FROM specialties ORDER BY id;
SELECT * FROM clinics ORDER BY id;
SELECT * FROM users;
SELECT * FROM doctors;
SELECT * FROM patients;
SELECT * FROM free_schedules;
SELECT * FROM appointments;
SELECT * FROM notifications;
SELECT * FROM overview;
SELECT * FROM history;
/*VIEWS*/
SELECT * FROM view_patients; 
SELECT * FROM view_doctors;
SELECT * FROM view_all_schedules;
SELECT * FROM view_free_schedules;
SELECT * FROM view_appointments;
SELECT * FROM view_notifications;
SELECT * FROM view_history;

/*USERS
 - Usado para autenticar: adicionar um where para encontrar o email e validar a senha*/
SELECT * FROM users WHERE role = "PATIENT";

/*PACIENTES: view_patients
 - Usado para a sessão ativa, encontrar o paciente através de user_id*/
CREATE VIEW view_patients AS
SELECT 
	users.email, users.password, patients.*
FROM 
	patients 
INNER JOIN 
	users ON users.id = patients.user_id;

/*MÉDICOS: view_doctors*/
CREATE VIEW view_doctors AS
SELECT
	doctors.id, doctors.name, doctors.crm, users.email, users.password, specialties.name AS specialtie
FROM
	doctors
INNER JOIN
	users ON users.id = doctors.user_id
INNER JOIN
	specialties ON doctors.specialtie_id = specialties.id;
    
/*TODAS AS AGENDAS: view_all_schedules*/
CREATE VIEW view_all_schedules AS
SELECT
	free_schedules.id, free_schedules.start_time, free_schedules.status, doctors.name AS doctor, specialties.name AS specialtie, clinics.name AS clinic
FROM
	free_schedules
INNER JOIN
	doctors ON free_schedules.doctor_id = doctors.id
INNER JOIN
	specialties ON doctors.specialtie_id = specialties.id
INNER JOIN
	clinics ON free_schedules.clinic_id = clinics.id;
    
/*AGENDAS DISPONÍVEIS: view_free_schedules*/
CREATE VIEW view_free_schedules AS
SELECT
	free_schedules.id, free_schedules.start_time, doctors.name AS doctor, specialties.name AS specialtie, clinics.name AS clinic
FROM
	free_schedules
INNER JOIN
	doctors ON free_schedules.doctor_id = doctors.id
INNER JOIN
	specialties ON doctors.specialtie_id = specialties.id
INNER JOIN
	clinics ON free_schedules.clinic_id = clinics.id
WHERE free_schedules.status = 1;

/*CONSULTAS MARCADAS: view_appointments*/
CREATE VIEW view_appointments AS
SELECT
	appointments.id, appointments.status,patients.id AS patient_id, patients.name AS patient_name, free_schedules.start_time, doctors.name AS doctor, specialties.name AS specialtie, clinics.name AS location
FROM
	appointments
INNER JOIN
	patients ON patient_id = patients.id
INNER JOIN
	free_schedules ON free_schedule_id = free_schedules.id
INNER JOIN
	doctors ON doctor_id = doctors.id
INNER JOIN
	clinics ON clinic_id = clinics.id
INNER JOIN
	specialties ON specialtie_id = specialties.id;

/*NOTIFICAÇÕES: view_notifications*/
CREATE VIEW view_notifications AS
SELECT
	notifications.id AS notification_id, notifications.type, notifications.sent_at, notifications.delivery_status, view_appointments.*
FROM
	notifications
INNER JOIN
	view_appointments ON appointment_id = view_appointments.id;
    
/*HISTÓRICO: view_history*/
CREATE VIEW view_history AS
SELECT
	history.id AS history_id, overview.diagnosis, view_appointments.*
FROM
	history
INNER JOIN
	overview ON overview_id = overview.id
INNER JOIN
	view_appointments ON appointment_id = view_appointments.id;