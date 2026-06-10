CREATE DATABASE agendasus_v1;
USE agendasus_v1;

CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    role ENUM('PATIENT', 'DOCTOR', 'ADMIN') NOT NULL DEFAULT 'PATIENT'
);

CREATE TABLE IF NOT EXISTS specialties (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS clinics (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS patients (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    birth_date DATE NOT NULL,
    phone_number VARCHAR(13),
    user_id INT NOT NULL UNIQUE,
    
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS doctors (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    crm VARCHAR(15) UNIQUE,
    user_id INT NOT NULL UNIQUE,
    specialtie_id INT NOT NULL,
    
    CONSTRAINT fk_user_doctor_id FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_specialtie_id FOREIGN KEY (specialtie_id) REFERENCES specialties(id)
);

CREATE TABLE IF NOT EXISTS free_schedules (
	id INT PRIMARY KEY AUTO_INCREMENT,
    start_time DATETIME NOT NULL,
    status BOOL DEFAULT TRUE,
    doctor_id INT NOT NULL,
    clinic_id INT NOT NULL,
    
    CONSTRAINT fk_doctor_schedule_id FOREIGN KEY (doctor_id) REFERENCES doctors(id),
    CONSTRAINT fk_clinic_schedule_id FOREIGN KEY (clinic_id) REFERENCES clinics(id)
);

CREATE TABLE IF NOT EXISTS appointments (
	id INT PRIMARY KEY AUTO_INCREMENT,
    status ENUM('SCHEDULED', 'CONCLUDED', 'CANCELED') NOT NULL,
    patient_id INT NOT NULL,
    free_schedule_id INT NOT NULL UNIQUE,
    
    CONSTRAINT fk_patient_appointment_id FOREIGN KEY (patient_id) REFERENCES patients(id),
    CONSTRAINT fk_schedule_appointment_id FOREIGN KEY (free_schedule_id) REFERENCES free_schedules(id)
);

CREATE TABLE IF NOT EXISTS overview (
	id INT PRIMARY KEY AUTO_INCREMENT,
    diagnosis TEXT,
    appointment_id INT NOT NULL UNIQUE,
    
    CONSTRAINT fk_appointment_overview_id FOREIGN KEY (appointment_id) REFERENCES appointments(id)
);

CREATE TABLE IF NOT EXISTS history (
	id INT PRIMARY KEY AUTO_INCREMENT,
    overview_id INT NOT NULL UNIQUE,
    
    CONSTRAINT fk_overview_history_id FOREIGN KEY (overview_id) REFERENCES overview(id)
);

CREATE TABLE IF NOT EXISTS notifications (
	id INT PRIMARY KEY AUTO_INCREMENT,
    type ENUM('SMS', 'EMAIL', 'WHATSAPP') NOT NULL,
    sent_at DATETIME NOT NULL,
    delivery_status ENUM('SENT', 'FAILED', 'PENDING') NOT NULL,
    appointment_id INT NOT NULL,
    
    CONSTRAINT fk_appointment_notification_id FOREIGN KEY (appointment_id) REFERENCES appointments(id)
);