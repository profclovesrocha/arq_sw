/*TRIGGERS*/
DELIMITER //
CREATE TRIGGER tg_schedule_appointment
AFTER INSERT ON appointments
FOR EACH ROW
BEGIN
	UPDATE free_schedules
    SET status = FALSE 
    WHERE id = NEW.free_schedule_id;
END; // 
DELIMITER ;

DELIMITER //
CREATE TRIGGER tg_unschedule_appointment
AFTER DELETE ON appointments
FOR EACH ROW
BEGIN
	UPDATE free_schedules
    SET status = TRUE 
    WHERE id = OLD.free_schedule_id;
END; // 
DELIMITER ;

DELIMITER //
CREATE TRIGGER tg_overview
AFTER INSERT ON appointments
FOR EACH ROW
BEGIN
	INSERT INTO overview (appointment_id) 
    VALUES (NEW.id);
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER tg_history
AFTER INSERT ON overview
FOR EACH ROW
BEGIN
	INSERT INTO history (overview_id) 
    VALUES (NEW.id);
END; //
DELIMITER ;