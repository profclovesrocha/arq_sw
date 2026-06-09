-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: agendasus_v1
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` enum('SCHEDULED','CONCLUDED','CANCELED') NOT NULL DEFAULT 'SCHEDULED',
  `patient_id` int(11) NOT NULL,
  `free_schedule_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `free_schedule_id` (`free_schedule_id`),
  KEY `fk_patient_appointment_id` (`patient_id`),
  CONSTRAINT `fk_patient_appointment_id` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`id`),
  CONSTRAINT `fk_schedule_appointment_id` FOREIGN KEY (`free_schedule_id`) REFERENCES `free_schedules` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (2,'SCHEDULED',4,6),(3,'CONCLUDED',5,7),(4,'SCHEDULED',6,8),(5,'CANCELED',7,9),(6,'CONCLUDED',8,10),(7,'SCHEDULED',9,11),(8,'SCHEDULED',10,12),(9,'CONCLUDED',11,13),(10,'SCHEDULED',12,14),(11,'CANCELED',13,15),(12,'SCHEDULED',14,16),(13,'CONCLUDED',15,17),(14,'SCHEDULED',16,18),(15,'SCHEDULED',17,19),(16,'CONCLUDED',18,20),(17,'SCHEDULED',19,21),(18,'CANCELED',20,22),(19,'SCHEDULED',21,23),(20,'CONCLUDED',22,24),(21,'SCHEDULED',23,25),(22,'SCHEDULED',24,26),(23,'CONCLUDED',25,27),(24,'SCHEDULED',26,28),(25,'CANCELED',27,29),(26,'SCHEDULED',28,30),(27,'CONCLUDED',29,31),(28,'SCHEDULED',30,32),(29,'SCHEDULED',31,33),(30,'CONCLUDED',32,34),(31,'SCHEDULED',33,35),(33,'SCHEDULED',7,47),(34,'SCHEDULED',4,43),(37,'SCHEDULED',4,36),(38,'SCHEDULED',4,40),(39,'SCHEDULED',4,38),(40,'SCHEDULED',4,41),(43,'SCHEDULED',4,37),(45,'SCHEDULED',4,44),(46,'SCHEDULED',4,53),(47,'SCHEDULED',4,39),(48,'SCHEDULED',4,49),(49,'SCHEDULED',4,42),(50,'SCHEDULED',4,51),(51,'SCHEDULED',98,63),(52,'SCHEDULED',98,135),(53,'SCHEDULED',4,97),(54,'SCHEDULED',99,158),(55,'SCHEDULED',4,110),(56,'SCHEDULED',93,99),(57,'SCHEDULED',93,175);
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER tg_schedule_appointment

AFTER INSERT ON appointments

FOR EACH ROW

BEGIN

	UPDATE free_schedules

    SET status = FALSE 

    WHERE id = NEW.free_schedule_id;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER tg_overview

AFTER INSERT ON appointments

FOR EACH ROW

BEGIN

	INSERT INTO overview (appointment_id) 

    VALUES (NEW.id);

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER tg_unschedule_appointment

AFTER DELETE ON appointments

FOR EACH ROW

BEGIN

	UPDATE free_schedules

    SET status = TRUE 

    WHERE id = OLD.free_schedule_id;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `clinics`
--

DROP TABLE IF EXISTS `clinics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clinics`
--

LOCK TABLES `clinics` WRITE;
/*!40000 ALTER TABLE `clinics` DISABLE KEYS */;
INSERT INTO `clinics` VALUES (10,'Centro de Diagnóstico Alpha'),(20,'Centro de Reabilitação'),(29,'Centro de Terapias'),(25,'Centro de Trauma'),(4,'Centro Médico Vida'),(17,'Centro Pediátrico'),(7,'Clínica Bem Estar'),(16,'Clínica da Mulher'),(19,'Clínica Dermatológica Lótus'),(13,'Clínica Dr. Silva'),(24,'Clínica MultiMed'),(9,'Clínica Ortopédica Sul'),(31,'Clínica Sanitas'),(22,'Clínica São José'),(3,'Clínica Saúde Total'),(28,'Clínica Viver Mais'),(23,'Consultório Reaviva'),(15,'Espaço Saúde'),(27,'Hospital da Criança'),(21,'Hospital das Nações'),(12,'Hospital do Coração'),(32,'Hospital Geral'),(5,'Hospital Santa Helena'),(8,'Instituto da Visão'),(18,'Instituto de Neurologia'),(26,'Instituto Endócrino'),(11,'Medicina Integrada'),(33,'Posto da guabiraba'),(6,'Pronto Socorro Central'),(34,'UBS Tabajara'),(30,'Unidade Avançada Oeste'),(14,'Unidade Básica Norte');
/*!40000 ALTER TABLE `clinics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `crm` varchar(15) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `specialtie_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `crm` (`crm`),
  KEY `fk_specialtie_id` (`specialtie_id`),
  CONSTRAINT `fk_specialtie_id` FOREIGN KEY (`specialtie_id`) REFERENCES `specialties` (`id`),
  CONSTRAINT `fk_user_doctor_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (6,'Dr. Arthur Silva','CRM/SP 10001',8,4),(7,'Dra. Beatriz Santos','CRM/SP 10002',9,5),(8,'Dr. Caio Oliveira','CRM/SP 10003',10,6),(9,'Dra. Daniela Lima','CRM/SP 10004',11,7),(10,'Dr. Eduardo Costa','CRM/SP 10005',12,8),(11,'Dra. Fernanda Rocha','CRM/SP 10006',13,9),(12,'Dr. Gabriel Almeida','CRM/SP 10007',14,10),(13,'Dra. Helena Souza','CRM/SP 10008',15,11),(14,'Dr. Igor Carvalho','CRM/SP 10009',16,12),(15,'Dra. Julia Pereira','CRM/SP 10010',17,13),(16,'Dr. Kevin Mendes','CRM/SP 10011',18,4),(17,'Dra. Larissa Ramos','CRM/SP 10012',19,5),(18,'Dr. Mauricio Nunes','CRM/SP 10013',20,6),(19,'Dra. Nicole Farias','CRM/SP 10014',21,7),(20,'Dr. Otavio Castro','CRM/SP 10015',22,8),(21,'Dra. Patricia Melo','CRM/SP 10016',23,9),(22,'Dr. Quiterio Jorge','CRM/SP 10017',24,10),(23,'Dra. Roberta Viana','CRM/SP 10018',25,11),(24,'Dr. Samuel Antunes','CRM/SP 10019',26,12),(25,'Dra. Tatiana Gomes','CRM/SP 10020',27,13),(26,'Dr. Uriel Duarte','CRM/SP 10021',28,4),(27,'Dra. Vanessa Lins','CRM/SP 10022',29,5),(28,'Dr. Wagner Moura','CRM/SP 10023',30,6),(29,'Dra. Ximena Ortiz','CRM/SP 10024',31,7),(30,'Dr. Yuri Boyka','CRM/SP 10025',32,8),(31,'Dra. Zilda Arns','CRM/SP 10026',33,9),(32,'Dr. Angelo Neto','CRM/SP 10027',34,10),(33,'Dra. Bruna Marquez','CRM/SP 10028',35,11),(34,'Dr. Claudio Raiol','CRM/SP 10029',36,12),(35,'Dra. Debora Seco','CRM/SP 10030',37,13);
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `free_schedules`
--

DROP TABLE IF EXISTS `free_schedules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `free_schedules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_time` datetime NOT NULL,
  `status` tinyint(1) DEFAULT 1,
  `doctor_id` int(11) NOT NULL,
  `clinic_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_doctor_schedule_id` (`doctor_id`),
  KEY `fk_clinic_schedule_id` (`clinic_id`),
  CONSTRAINT `fk_clinic_schedule_id` FOREIGN KEY (`clinic_id`) REFERENCES `clinics` (`id`),
  CONSTRAINT `fk_doctor_schedule_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=176 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `free_schedules`
--

LOCK TABLES `free_schedules` WRITE;
/*!40000 ALTER TABLE `free_schedules` DISABLE KEYS */;
INSERT INTO `free_schedules` VALUES (6,'2026-06-01 08:00:00',0,6,3),(7,'2026-06-01 09:00:00',0,7,4),(8,'2026-06-01 10:00:00',0,8,5),(9,'2026-06-01 11:00:00',0,9,6),(10,'2026-06-01 13:00:00',0,10,7),(11,'2026-06-01 14:00:00',0,11,8),(12,'2026-06-01 15:00:00',0,12,9),(13,'2026-06-01 16:00:00',0,13,10),(14,'2026-06-01 17:00:00',0,14,11),(15,'2026-06-02 08:00:00',0,15,12),(16,'2026-06-02 09:00:00',0,16,13),(17,'2026-06-02 10:00:00',0,17,14),(18,'2026-06-02 11:00:00',0,18,15),(19,'2026-06-02 13:00:00',0,19,16),(20,'2026-06-02 14:00:00',0,20,17),(21,'2026-06-02 15:00:00',0,21,18),(22,'2026-06-02 16:00:00',0,22,19),(23,'2026-06-02 17:00:00',0,23,20),(24,'2026-06-03 08:00:00',0,24,21),(25,'2026-06-03 09:00:00',0,25,22),(26,'2026-06-03 10:00:00',0,26,23),(27,'2026-06-03 11:00:00',0,27,24),(28,'2026-06-03 13:00:00',0,28,25),(29,'2026-06-03 14:00:00',0,29,26),(30,'2026-06-03 15:00:00',0,30,27),(31,'2026-06-03 16:00:00',0,31,28),(32,'2026-06-03 17:00:00',0,32,29),(33,'2026-06-04 08:00:00',0,33,30),(34,'2026-06-04 09:00:00',0,34,31),(35,'2026-06-04 10:00:00',0,35,32),(36,'2026-06-04 11:00:00',0,6,3),(37,'2026-06-04 13:00:00',0,7,4),(38,'2026-06-04 14:00:00',0,8,5),(39,'2026-06-04 15:00:00',0,9,6),(40,'2026-06-04 16:00:00',0,10,7),(41,'2026-06-04 17:00:00',0,11,8),(42,'2026-06-05 08:00:00',0,12,9),(43,'2026-06-05 09:00:00',0,13,10),(44,'2026-06-05 10:00:00',0,14,11),(45,'2026-06-05 11:00:00',1,15,12),(46,'2026-06-05 13:00:00',1,16,13),(47,'2026-06-05 14:00:00',0,17,14),(48,'2026-06-05 15:00:00',1,18,15),(49,'2026-06-05 16:00:00',0,19,16),(50,'2026-06-05 17:00:00',1,20,17),(51,'2026-06-06 08:00:00',0,21,18),(52,'2026-06-06 09:00:00',1,22,19),(53,'2026-06-06 10:00:00',0,23,20),(54,'2026-06-06 11:00:00',1,24,21),(55,'2026-06-06 13:00:00',1,25,22),(56,'2026-06-01 08:30:00',1,6,8),(57,'2026-06-02 09:00:00',1,26,14),(58,'2026-05-30 08:00:00',1,6,8),(59,'2026-05-29 16:00:00',1,26,21),(60,'2026-06-11 11:30:00',1,26,9),(61,'2026-05-29 10:30:00',1,16,9),(62,'2026-06-02 11:30:00',1,6,3),(63,'2026-06-10 09:30:00',0,16,20),(64,'2026-06-06 08:30:00',1,26,4),(65,'2026-06-10 09:30:00',1,26,20),(66,'2026-06-09 17:00:00',1,27,3),(67,'2026-05-30 11:30:00',1,7,28),(68,'2026-06-05 09:30:00',1,17,15),(69,'2026-06-09 10:30:00',1,17,7),(70,'2026-06-06 09:00:00',1,27,24),(71,'2026-06-05 10:30:00',1,17,9),(72,'2026-06-05 13:00:00',1,7,27),(73,'2026-05-30 13:30:00',1,17,3),(74,'2026-06-04 17:30:00',1,7,21),(75,'2026-06-13 14:30:00',1,7,9),(76,'2026-06-02 11:30:00',1,34,19),(77,'2026-06-11 17:30:00',1,24,8),(78,'2026-06-02 16:30:00',1,14,25),(79,'2026-05-30 09:00:00',1,34,6),(80,'2026-06-11 17:00:00',1,24,13),(81,'2026-06-12 16:30:00',1,34,28),(82,'2026-05-29 09:30:00',1,34,11),(83,'2026-06-01 12:30:00',1,14,15),(84,'2026-05-29 12:00:00',1,34,30),(85,'2026-06-01 12:00:00',1,14,12),(86,'2026-06-03 16:00:00',1,30,11),(87,'2026-06-13 08:00:00',1,20,29),(88,'2026-06-07 11:00:00',1,10,29),(89,'2026-05-31 09:30:00',1,10,25),(90,'2026-06-02 10:30:00',1,30,6),(91,'2026-06-06 16:30:00',1,10,30),(92,'2026-06-04 12:30:00',1,30,21),(93,'2026-06-09 15:30:00',1,10,8),(94,'2026-06-05 09:30:00',1,10,19),(95,'2026-06-05 17:00:00',1,10,3),(96,'2026-05-30 11:00:00',1,13,28),(97,'2026-06-08 09:00:00',0,23,22),(98,'2026-06-13 11:00:00',1,33,30),(99,'2026-06-13 11:30:00',0,23,7),(100,'2026-06-01 09:30:00',1,23,14),(101,'2026-06-11 15:00:00',1,33,21),(102,'2026-06-01 08:30:00',1,33,11),(103,'2026-06-01 11:00:00',1,13,18),(104,'2026-06-12 10:30:00',1,13,9),(105,'2026-06-12 11:00:00',1,23,26),(106,'2026-06-01 08:00:00',1,12,30),(107,'2026-06-05 10:30:00',1,22,16),(108,'2026-06-04 14:00:00',1,12,13),(109,'2026-05-29 14:30:00',1,22,10),(110,'2026-06-11 16:30:00',0,12,7),(111,'2026-06-07 11:00:00',1,32,24),(112,'2026-05-30 13:00:00',1,12,19),(113,'2026-06-13 16:00:00',1,12,17),(114,'2026-05-31 10:00:00',1,32,3),(115,'2026-06-05 14:00:00',1,32,8),(126,'2026-06-02 12:30:00',1,28,7),(127,'2026-06-08 11:30:00',1,28,16),(128,'2026-06-06 08:00:00',1,28,14),(129,'2026-06-06 08:00:00',1,18,25),(130,'2026-06-02 12:00:00',1,28,15),(131,'2026-06-11 16:00:00',1,8,3),(132,'2026-06-02 16:00:00',1,18,19),(133,'2026-06-02 14:00:00',1,8,10),(134,'2026-06-09 08:30:00',1,8,22),(135,'2026-06-05 09:30:00',0,28,29),(136,'2026-06-11 17:00:00',1,11,28),(137,'2026-06-03 10:30:00',1,11,6),(138,'2026-06-08 14:00:00',1,21,6),(139,'2026-06-01 14:00:00',1,21,8),(140,'2026-06-04 15:30:00',1,21,27),(141,'2026-06-05 11:00:00',1,31,7),(142,'2026-06-10 13:30:00',1,11,25),(143,'2026-06-06 13:30:00',1,31,27),(144,'2026-06-08 08:00:00',1,21,6),(145,'2026-06-06 08:00:00',1,31,14),(156,'2026-06-09 12:00:00',1,29,6),(157,'2026-06-07 08:30:00',1,29,13),(158,'2026-06-13 17:00:00',0,9,3),(159,'2026-06-06 09:30:00',1,29,29),(160,'2026-05-29 11:00:00',1,9,12),(161,'2026-06-12 11:00:00',1,19,12),(162,'2026-06-07 14:30:00',1,29,24),(163,'2026-06-11 08:30:00',1,19,10),(164,'2026-06-05 12:00:00',1,9,3),(165,'2026-06-01 17:00:00',1,19,21),(166,'2026-06-03 16:30:00',1,25,23),(167,'2026-05-29 09:30:00',1,15,25),(168,'2026-06-11 12:30:00',1,15,21),(169,'2026-06-07 12:00:00',1,15,17),(170,'2026-06-06 17:00:00',1,35,12),(171,'2026-06-06 14:00:00',1,35,24),(172,'2026-06-04 14:30:00',1,15,18),(173,'2026-06-04 12:00:00',1,35,28),(174,'2026-06-03 16:30:00',1,25,24),(175,'2026-06-11 17:00:00',0,25,18);
/*!40000 ALTER TABLE `free_schedules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `overview_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `overview_id` (`overview_id`),
  CONSTRAINT `fk_overview_history_id` FOREIGN KEY (`overview_id`) REFERENCES `overview` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),(21,21),(22,22),(23,23),(24,24),(25,25),(26,26),(27,27),(28,28),(29,29),(30,30),(31,31),(32,32),(33,33),(34,34),(35,35),(36,36),(37,37),(38,38),(39,39),(40,40),(41,41),(42,42),(43,43),(44,44),(45,45);
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notifications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` enum('SMS','EMAIL','WHATSAPP') NOT NULL,
  `sent_at` datetime NOT NULL,
  `delivery_status` enum('SENT','FAILED','PENDING') NOT NULL,
  `appointment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_appointment_notification_id` (`appointment_id`),
  CONSTRAINT `fk_appointment_notification_id` FOREIGN KEY (`appointment_id`) REFERENCES `appointments` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES (1,'EMAIL','2026-05-01 08:00:00','SENT',2),(2,'SMS','2026-05-01 08:05:00','SENT',3),(3,'WHATSAPP','2026-05-01 09:00:00','SENT',4),(4,'EMAIL','2026-05-01 10:30:00','FAILED',5),(5,'WHATSAPP','2026-05-02 08:00:00','SENT',6),(6,'SMS','2026-05-02 08:15:00','PENDING',7),(7,'EMAIL','2026-05-02 09:00:00','SENT',8),(8,'WHATSAPP','2026-05-02 11:00:00','SENT',9),(9,'SMS','2026-05-03 14:00:00','SENT',10),(10,'EMAIL','2026-05-03 15:00:00','SENT',11),(11,'WHATSAPP','2026-05-03 16:30:00','FAILED',12),(12,'SMS','2026-05-04 08:00:00','SENT',13),(13,'EMAIL','2026-05-04 09:20:00','SENT',14),(14,'WHATSAPP','2026-05-04 10:00:00','SENT',15),(15,'SMS','2026-05-04 11:45:00','SENT',16),(16,'EMAIL','2026-05-05 08:00:00','SENT',17),(17,'WHATSAPP','2026-05-05 08:30:00','PENDING',18),(18,'SMS','2026-05-05 09:15:00','SENT',19),(19,'EMAIL','2026-05-05 10:00:00','SENT',20),(20,'WHATSAPP','2026-05-05 13:00:00','SENT',21),(21,'SMS','2026-05-05 14:00:00','SENT',22),(22,'EMAIL','2026-05-05 15:30:00','FAILED',23),(23,'WHATSAPP','2026-05-05 16:00:00','SENT',24),(24,'SMS','2026-05-05 17:00:00','SENT',25),(25,'EMAIL','2026-05-05 18:00:00','SENT',26),(26,'WHATSAPP','2026-05-06 08:00:00','SENT',27),(27,'SMS','2026-05-06 09:00:00','SENT',28),(28,'EMAIL','2026-05-06 10:00:00','PENDING',29),(29,'WHATSAPP','2026-05-06 11:00:00','SENT',30),(30,'SMS','2026-05-06 12:00:00','SENT',31);
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `overview`
--

DROP TABLE IF EXISTS `overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `overview` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `diagnosis` text DEFAULT NULL,
  `appointment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `appointment_id` (`appointment_id`),
  CONSTRAINT `fk_appointment_overview_id` FOREIGN KEY (`appointment_id`) REFERENCES `appointments` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `overview`
--

LOCK TABLES `overview` WRITE;
/*!40000 ALTER TABLE `overview` DISABLE KEYS */;
INSERT INTO `overview` VALUES (1,'Paciente apresenta quadro de fadiga crônica e deficiência de vitamina D.',2),(2,'Resultados de exames cardíacos normais. Recomendado retorno em 6 meses.',3),(3,'Crise alérgica sazonal. Prescrito anti-histamínico e repouso.',4),(4,'Lesão muscular leve no joelho esquerdo devido a esforço repetitivo.',5),(5,'Suspeita de gastrite nervosa. Encaminhado para endoscopia.',6),(6,'Acompanhamento pré-natal: desenvolvimento fetal dentro da normalidade.',7),(7,'Quadro depressivo moderado. Iniciado acompanhamento psicoterapêutico.',8),(8,'Conjuntivite bacteriana confirmada. Prescrito colírio antibiótico.',9),(9,'Enxaqueca tensional recorrente. Sugerido ajuste na rotina de sono.',10),(10,'Diabetes Tipo 2 sob controle. Mantida a dosagem atual de medicação.',11),(11,'Hipertensão arterial estágio 1. Recomendada dieta hipossódica.',12),(12,'Dermatite de contato por exposição a produtos de limpeza.',13),(13,'Infecção urinária recorrente. Iniciado ciclo de antibióticos.',14),(14,'Avaliação física para atividades esportivas: apto sem restrições.',15),(15,'Rinite alérgica aguda. Recomendado uso de purificador de ar.',16),(16,'Check-up anual: níveis de colesterol ligeiramente elevados.',17),(17,'Escoliose leve detectada. Encaminhado para sessões de RPG.',18),(18,'Anemia ferropriva detectada. Iniciada suplementação de ferro.',19),(19,'Ansiedade generalizada. Discutidas opções de tratamento natural.',20),(20,'Sintomas de gripe comum (Influenza). Recomendado isolamento e hidratação.',21),(21,'Recuperação pós-cirúrgica excelente. Retirada de pontos realizada.',22),(22,'Dores lombares crônicas. Prescrito relaxante muscular e fisioterapia.',23),(23,'Sinusite aguda. Prescrito corticóide nasal e lavagem salina.',24),(24,'Hipotiroidismo estável com o uso de Levotiroxina.',25),(25,'Exame de fundo de olho sem alterações. Mantido grau atual de miopia.',26),(26,NULL,33),(27,NULL,34),(28,NULL,37),(29,NULL,38),(30,NULL,39),(31,NULL,40),(32,NULL,43),(33,NULL,45),(34,NULL,46),(35,NULL,47),(36,NULL,48),(37,NULL,49),(38,NULL,50),(39,NULL,51),(40,NULL,52),(41,NULL,53),(42,NULL,54),(43,NULL,55),(44,NULL,56),(45,NULL,57);
/*!40000 ALTER TABLE `overview` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER tg_history

AFTER INSERT ON overview

FOR EACH ROW

BEGIN

	INSERT INTO history (overview_id) 

    VALUES (NEW.id);

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `birth_date` date NOT NULL,
  `user_id` int(11) NOT NULL,
  `phone_number` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (4,'João Silva','10000000001','1990-01-10',38,'11987654321'),(5,'Maria Oliveira','10000000002','1985-05-22',39,'11976543210'),(6,'Carlos Souza','10000000003','1978-11-30',40,'21965432109'),(7,'Ana Costa','10000000004','1992-03-15',41,'21954321098'),(8,'Lucas Santos','10000000005','2000-07-08',42,'31943210987'),(9,'Bruna Lima','10000000006','1988-12-12',43,'31932109876'),(10,'Ricardo Alves','10000000007','1995-02-25',44,'41921098765'),(11,'Julia Ribeiro','10000000008','1982-09-14',45,'41910987654'),(12,'Marcos Rocha','10000000009','1975-06-20',46,'51909876543'),(13,'Fernanda Gomes','10000000010','1991-08-05',47,'51998877665'),(14,'Paulo Vieira','10000000011','1980-04-18',48,NULL),(15,'Camila Martins','10000000012','1993-10-27',49,NULL),(16,'Gabriel Barbosa','10000000013','1987-01-02',50,NULL),(17,'Larissa Freitas','10000000014','1998-11-11',51,NULL),(18,'Rafael Carvalho','10000000015','1984-03-09',52,NULL),(19,'Amanda Silva','10000000016','1979-05-30',53,NULL),(20,'Igor Pereira','10000000017','1996-07-21',54,NULL),(21,'Leticia Castro','10000000018','1989-02-14',55,NULL),(22,'Gustavo Nunes','10000000019','1994-09-03',56,NULL),(23,'Beatriz Lopes','10000000020','1981-12-25',57,NULL),(24,'André Cardoso','10000000021','1977-06-15',58,NULL),(25,'Tatiana Neves','10000000022','1990-11-20',59,NULL),(26,'Fabio Azevedo','10000000023','1983-04-10',60,NULL),(27,'Priscila Ramos','10000000024','1992-01-05',61,NULL),(28,'Thiago Barros','10000000025','1986-08-17',62,NULL),(29,'Vanessa Teixeira','10000000026','1997-03-29',63,NULL),(30,'Leonardo Mendes','10000000027','1988-10-12',64,NULL),(31,'Daniela Borges','10000000028','1976-02-28',65,NULL),(32,'Sandro Correa','10000000029','1982-05-14',66,NULL),(33,'Monica Farias','10000000030','1995-12-01',67,NULL),(34,'Renato Guimarães','10000000031','1984-07-19',68,NULL),(35,'Elaine Machado','10000000032','1991-09-30',69,NULL),(36,'Vitor Moreira','10000000033','1979-01-22',70,NULL),(37,'Simone Duarte','10000000034','1987-11-08',71,NULL),(38,'Marcelo Pires','10000000035','1993-06-04',72,NULL),(39,'Cristiane Fonseca','10000000036','1980-03-12',73,NULL),(40,'Eduardo Aguiar','10000000037','1996-10-15',74,NULL),(41,'Flavia Campos','10000000038','1985-02-27',75,NULL),(42,'Alexandre Viana','10000000039','1978-08-09',76,NULL),(43,'Patrícia Leal','10000000040','1994-04-21',77,NULL),(44,'Hugo Antunes','10000000041','1989-12-05',78,NULL),(45,'Milena Matos','10000000042','1998-07-11',79,NULL),(46,'Rogério Prado','10000000043','1981-09-18',80,NULL),(47,'Cíntia Moraes','10000000044','1983-01-30',81,NULL),(48,'Douglas Batista','10000000045','1990-05-14',82,NULL),(49,'Sabrina Caldas','10000000046','1977-10-25',83,NULL),(50,'Murilo Peixoto','10000000047','1992-06-08',84,NULL),(51,'Kelly Assis','10000000048','1986-03-22',85,NULL),(52,'Caio Figueiredo','10000000049','1999-11-19',86,NULL),(53,'Roseane Monteiro','10000000050','1984-08-31',87,NULL),(54,'Jonas Gaspar','10000000051','1975-02-14',88,NULL),(55,'Gisele Arantes','10000000052','1991-04-03',89,NULL),(56,'Samuel Galvão','10000000053','1982-12-07',90,NULL),(57,'Erica Tavarez','10000000054','1995-09-16',91,NULL),(58,'Roberto Lacerda','10000000055','1980-01-25',92,NULL),(59,'Talita Bezerra','10000000056','1993-07-14',93,NULL),(60,'Otávio Brandão','10000000057','1987-05-19',94,NULL),(61,'Debora Santana','10000000058','1979-11-02',95,NULL),(62,'Wesley Malta','10000000059','1996-03-08',96,NULL),(63,'Regina Paiva','10000000060','1988-06-24',97,NULL),(64,'Helder Quintas','10000000061','1983-10-10',98,NULL),(65,'Viviane Dornelas','10000000062','1994-08-28',99,NULL),(66,'Artur Braganca','10000000063','1981-04-01',100,NULL),(67,'Lorena Vasconcelos','10000000064','1997-12-15',101,NULL),(68,'Cristiano Nobre','10000000065','1985-09-09',102,NULL),(69,'Sonia Abrantes','10000000066','1976-11-20',103,NULL),(70,'Valter Maia','10000000067','1990-02-22',104,NULL),(71,'Silvia Junqueira','10000000068','1982-07-06',105,NULL),(72,'Breno Eustaquio','10000000069','1992-05-18',106,NULL),(73,'Zilda Ferreira','10000000070','1988-01-01',107,NULL),(74,'Rodrigo Teste','98989898989','0043-03-04',108,'98798798798'),(76,'Tomas de aquino','91827310928','0012-03-12',110,'81997979129'),(78,'alksdjf','12983109823','0002-03-12',112,'81981723981'),(79,'brenoca','91238470129','2011-01-21',113,'91287310928'),(80,'Teste','12312312312','1234-03-12',115,'12312312312'),(81,'Rodrigo Nunes','70863782400','2004-03-16',116,'81997976188'),(82,';\'dsfglkdafs\';lk@alksfjdl;s','01293810298','2002-03-14',117,'01927830129'),(93,'Teste da Silva','12312412131','2003-12-12',128,'13233423423'),(94,'marcinho','23498572908','2022-11-14',129,'19283719827'),(95,'Italo teste','89721347912','0003-02-03',130,'10293810293'),(96,'Indonesia Silva','13330202020','2998-12-12',131,'81999719719'),(98,'Brenoca','32112323164','2211-12-12',133,'12312331221'),(99,'Rosangela Pereira','97402311449','1976-08-03',134,'81988922324');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specialties`
--

DROP TABLE IF EXISTS `specialties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `specialties` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialties`
--

LOCK TABLES `specialties` WRITE;
/*!40000 ALTER TABLE `specialties` DISABLE KEYS */;
INSERT INTO `specialties` VALUES (4,'Cardiologia'),(5,'Dermatologia'),(12,'Endocrinologia'),(8,'Ginecologia'),(11,'Neurologia'),(10,'Oftalmologia'),(7,'Ortopedia'),(6,'Pediatria'),(14,'Proctologista'),(9,'Psiquiatria'),(13,'Urologia');
/*!40000 ALTER TABLE `specialties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` enum('PATIENT','DOCTOR','ADMIN') NOT NULL DEFAULT 'PATIENT',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (8,'medico1@teste.com','pass123','DOCTOR'),(9,'medico2@teste.com','pass123','DOCTOR'),(10,'medico3@teste.com','pass123','DOCTOR'),(11,'medico4@teste.com','pass123','DOCTOR'),(12,'medico5@teste.com','pass123','DOCTOR'),(13,'medico6@teste.com','pass123','DOCTOR'),(14,'medico7@teste.com','pass123','DOCTOR'),(15,'medico8@teste.com','pass123','DOCTOR'),(16,'medico9@teste.com','pass123','DOCTOR'),(17,'medico10@teste.com','pass123','DOCTOR'),(18,'medico11@teste.com','pass123','DOCTOR'),(19,'medico12@teste.com','pass123','DOCTOR'),(20,'medico13@teste.com','pass123','DOCTOR'),(21,'medico14@teste.com','pass123','DOCTOR'),(22,'medico15@teste.com','pass123','DOCTOR'),(23,'medico16@teste.com','pass123','DOCTOR'),(24,'medico17@teste.com','pass123','DOCTOR'),(25,'medico18@teste.com','pass123','DOCTOR'),(26,'medico19@teste.com','pass123','DOCTOR'),(27,'medico20@teste.com','pass123','DOCTOR'),(28,'medico21@teste.com','pass123','DOCTOR'),(29,'medico22@teste.com','pass123','DOCTOR'),(30,'medico23@teste.com','pass123','DOCTOR'),(31,'medico24@teste.com','pass123','DOCTOR'),(32,'medico25@teste.com','pass123','DOCTOR'),(33,'medico26@teste.com','pass123','DOCTOR'),(34,'medico27@teste.com','pass123','DOCTOR'),(35,'medico28@teste.com','pass123','DOCTOR'),(36,'medico29@teste.com','pass123','DOCTOR'),(37,'medico30@teste.com','pass123','DOCTOR'),(38,'paciente1@teste.com','paz456','PATIENT'),(39,'paciente2@teste.com','paz456','PATIENT'),(40,'paciente3@teste.com','paz456','PATIENT'),(41,'paciente4@teste.com','paz456','PATIENT'),(42,'paciente5@teste.com','paz456','PATIENT'),(43,'paciente6@teste.com','paz456','PATIENT'),(44,'paciente7@teste.com','paz456','PATIENT'),(45,'paciente8@teste.com','paz456','PATIENT'),(46,'paciente9@teste.com','paz456','PATIENT'),(47,'paciente10@teste.com','paz456','PATIENT'),(48,'paciente11@teste.com','paz456','PATIENT'),(49,'paciente12@teste.com','paz456','PATIENT'),(50,'paciente13@teste.com','paz456','PATIENT'),(51,'paciente14@teste.com','paz456','PATIENT'),(52,'paciente15@teste.com','paz456','PATIENT'),(53,'paciente16@teste.com','paz456','PATIENT'),(54,'paciente17@teste.com','paz456','PATIENT'),(55,'paciente18@teste.com','paz456','PATIENT'),(56,'paciente19@teste.com','paz456','PATIENT'),(57,'paciente20@teste.com','paz456','PATIENT'),(58,'paciente21@teste.com','paz456','PATIENT'),(59,'paciente22@teste.com','paz456','PATIENT'),(60,'paciente23@teste.com','paz456','PATIENT'),(61,'paciente24@teste.com','paz456','PATIENT'),(62,'paciente25@teste.com','paz456','PATIENT'),(63,'paciente26@teste.com','paz456','PATIENT'),(64,'paciente27@teste.com','paz456','PATIENT'),(65,'paciente28@teste.com','paz456','PATIENT'),(66,'paciente29@teste.com','paz456','PATIENT'),(67,'paciente30@teste.com','paz456','PATIENT'),(68,'paciente31@teste.com','paz456','PATIENT'),(69,'paciente32@teste.com','paz456','PATIENT'),(70,'paciente33@teste.com','paz456','PATIENT'),(71,'paciente34@teste.com','paz456','PATIENT'),(72,'paciente35@teste.com','paz456','PATIENT'),(73,'paciente36@teste.com','paz456','PATIENT'),(74,'paciente37@teste.com','paz456','PATIENT'),(75,'paciente38@teste.com','paz456','PATIENT'),(76,'paciente39@teste.com','paz456','PATIENT'),(77,'paciente40@teste.com','paz456','PATIENT'),(78,'paciente41@teste.com','paz456','PATIENT'),(79,'paciente42@teste.com','paz456','PATIENT'),(80,'paciente43@teste.com','paz456','PATIENT'),(81,'paciente44@teste.com','paz456','PATIENT'),(82,'paciente45@teste.com','paz456','PATIENT'),(83,'paciente46@teste.com','paz456','PATIENT'),(84,'paciente47@teste.com','paz456','PATIENT'),(85,'paciente48@teste.com','paz456','PATIENT'),(86,'paciente49@teste.com','paz456','PATIENT'),(87,'paciente50@teste.com','paz456','PATIENT'),(88,'paciente51@teste.com','paz456','PATIENT'),(89,'paciente52@teste.com','paz456','PATIENT'),(90,'paciente53@teste.com','paz456','PATIENT'),(91,'paciente54@teste.com','paz456','PATIENT'),(92,'paciente55@teste.com','paz456','PATIENT'),(93,'paciente56@teste.com','paz456','PATIENT'),(94,'paciente57@teste.com','paz456','PATIENT'),(95,'paciente58@teste.com','paz456','PATIENT'),(96,'paciente59@teste.com','paz456','PATIENT'),(97,'paciente60@teste.com','paz456','PATIENT'),(98,'paciente61@teste.com','paz456','PATIENT'),(99,'paciente62@teste.com','paz456','PATIENT'),(100,'paciente63@teste.com','paz456','PATIENT'),(101,'paciente64@teste.com','paz456','PATIENT'),(102,'paciente65@teste.com','paz456','PATIENT'),(103,'paciente66@teste.com','paz456','PATIENT'),(104,'paciente67@teste.com','paz456','PATIENT'),(105,'paciente68@teste.com','paz456','PATIENT'),(106,'paciente69@teste.com','paz456','PATIENT'),(107,'paciente70@teste.com','paz456','PATIENT'),(108,'teste1@gmail.com','12345','PATIENT'),(110,'tomas@gmail.com','12345','PATIENT'),(112,'asldkjf@sldkj','12345','PATIENT'),(113,'brenoloiro@gmail.com','bren123','PATIENT'),(115,'123@123','123','PATIENT'),(116,'rodrigonpp1@gmail.com','12345','PATIENT'),(117,'ASLKJD@ALSDKJF','aslkdjf','PATIENT'),(128,'teste@teste','12345','PATIENT'),(129,'marcio@marcio','12345','PATIENT'),(130,'italo@teste','12345','PATIENT'),(131,'indo@gmail.com','12345','PATIENT'),(133,'breno@ca','12345','PATIENT'),(134,'rosa@gmail.com','12345','PATIENT');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `view_all_schedules`
--

DROP TABLE IF EXISTS `view_all_schedules`;
/*!50001 DROP VIEW IF EXISTS `view_all_schedules`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `view_all_schedules` AS SELECT
 1 AS `id`,
  1 AS `start_time`,
  1 AS `status`,
  1 AS `doctor`,
  1 AS `specialtie`,
  1 AS `clinic` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_appointments`
--

DROP TABLE IF EXISTS `view_appointments`;
/*!50001 DROP VIEW IF EXISTS `view_appointments`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `view_appointments` AS SELECT
 1 AS `id`,
  1 AS `status`,
  1 AS `patient_id`,
  1 AS `patient_name`,
  1 AS `start_time`,
  1 AS `doctor`,
  1 AS `specialtie`,
  1 AS `location` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_doctors`
--

DROP TABLE IF EXISTS `view_doctors`;
/*!50001 DROP VIEW IF EXISTS `view_doctors`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `view_doctors` AS SELECT
 1 AS `id`,
  1 AS `name`,
  1 AS `crm`,
  1 AS `email`,
  1 AS `password`,
  1 AS `specialtie` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_free_schedules`
--

DROP TABLE IF EXISTS `view_free_schedules`;
/*!50001 DROP VIEW IF EXISTS `view_free_schedules`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `view_free_schedules` AS SELECT
 1 AS `id`,
  1 AS `start_time`,
  1 AS `doctor`,
  1 AS `specialtie`,
  1 AS `clinic` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_history`
--

DROP TABLE IF EXISTS `view_history`;
/*!50001 DROP VIEW IF EXISTS `view_history`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `view_history` AS SELECT
 1 AS `history_id`,
  1 AS `diagnosis`,
  1 AS `id`,
  1 AS `status`,
  1 AS `patient_id`,
  1 AS `patient_name`,
  1 AS `start_time`,
  1 AS `doctor`,
  1 AS `specialtie`,
  1 AS `location` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_notifications`
--

DROP TABLE IF EXISTS `view_notifications`;
/*!50001 DROP VIEW IF EXISTS `view_notifications`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `view_notifications` AS SELECT
 1 AS `notification_id`,
  1 AS `type`,
  1 AS `sent_at`,
  1 AS `delivery_status`,
  1 AS `id`,
  1 AS `status`,
  1 AS `patient_id`,
  1 AS `patient_name`,
  1 AS `start_time`,
  1 AS `doctor`,
  1 AS `specialtie`,
  1 AS `location` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_patients`
--

DROP TABLE IF EXISTS `view_patients`;
/*!50001 DROP VIEW IF EXISTS `view_patients`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `view_patients` AS SELECT
 1 AS `email`,
  1 AS `password`,
  1 AS `id`,
  1 AS `name`,
  1 AS `cpf`,
  1 AS `birth_date`,
  1 AS `user_id`,
  1 AS `phone_number` */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `view_all_schedules`
--

/*!50001 DROP VIEW IF EXISTS `view_all_schedules`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_all_schedules` AS select `free_schedules`.`id` AS `id`,`free_schedules`.`start_time` AS `start_time`,`free_schedules`.`status` AS `status`,`doctors`.`name` AS `doctor`,`specialties`.`name` AS `specialtie`,`clinics`.`name` AS `clinic` from (((`free_schedules` join `doctors` on(`free_schedules`.`doctor_id` = `doctors`.`id`)) join `specialties` on(`doctors`.`specialtie_id` = `specialties`.`id`)) join `clinics` on(`free_schedules`.`clinic_id` = `clinics`.`id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_appointments`
--

/*!50001 DROP VIEW IF EXISTS `view_appointments`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_appointments` AS select `appointments`.`id` AS `id`,`appointments`.`status` AS `status`,`patients`.`id` AS `patient_id`,`patients`.`name` AS `patient_name`,`free_schedules`.`start_time` AS `start_time`,`doctors`.`name` AS `doctor`,`specialties`.`name` AS `specialtie`,`clinics`.`name` AS `location` from (((((`appointments` join `patients` on(`appointments`.`patient_id` = `patients`.`id`)) join `free_schedules` on(`appointments`.`free_schedule_id` = `free_schedules`.`id`)) join `doctors` on(`free_schedules`.`doctor_id` = `doctors`.`id`)) join `clinics` on(`free_schedules`.`clinic_id` = `clinics`.`id`)) join `specialties` on(`doctors`.`specialtie_id` = `specialties`.`id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_doctors`
--

/*!50001 DROP VIEW IF EXISTS `view_doctors`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_doctors` AS select `doctors`.`id` AS `id`,`doctors`.`name` AS `name`,`doctors`.`crm` AS `crm`,`users`.`email` AS `email`,`users`.`password` AS `password`,`specialties`.`name` AS `specialtie` from ((`doctors` join `users` on(`users`.`id` = `doctors`.`user_id`)) join `specialties` on(`doctors`.`specialtie_id` = `specialties`.`id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_free_schedules`
--

/*!50001 DROP VIEW IF EXISTS `view_free_schedules`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_free_schedules` AS select `free_schedules`.`id` AS `id`,`free_schedules`.`start_time` AS `start_time`,`doctors`.`name` AS `doctor`,`specialties`.`name` AS `specialtie`,`clinics`.`name` AS `clinic` from (((`free_schedules` join `doctors` on(`free_schedules`.`doctor_id` = `doctors`.`id`)) join `specialties` on(`doctors`.`specialtie_id` = `specialties`.`id`)) join `clinics` on(`free_schedules`.`clinic_id` = `clinics`.`id`)) where `free_schedules`.`status` = 1 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_history`
--

/*!50001 DROP VIEW IF EXISTS `view_history`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_history` AS select `history`.`id` AS `history_id`,`overview`.`diagnosis` AS `diagnosis`,`view_appointments`.`id` AS `id`,`view_appointments`.`status` AS `status`,`view_appointments`.`patient_id` AS `patient_id`,`view_appointments`.`patient_name` AS `patient_name`,`view_appointments`.`start_time` AS `start_time`,`view_appointments`.`doctor` AS `doctor`,`view_appointments`.`specialtie` AS `specialtie`,`view_appointments`.`location` AS `location` from ((`history` join `overview` on(`history`.`overview_id` = `overview`.`id`)) join `view_appointments` on(`overview`.`appointment_id` = `view_appointments`.`id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_notifications`
--

/*!50001 DROP VIEW IF EXISTS `view_notifications`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_notifications` AS select `notifications`.`id` AS `notification_id`,`notifications`.`type` AS `type`,`notifications`.`sent_at` AS `sent_at`,`notifications`.`delivery_status` AS `delivery_status`,`view_appointments`.`id` AS `id`,`view_appointments`.`status` AS `status`,`view_appointments`.`patient_id` AS `patient_id`,`view_appointments`.`patient_name` AS `patient_name`,`view_appointments`.`start_time` AS `start_time`,`view_appointments`.`doctor` AS `doctor`,`view_appointments`.`specialtie` AS `specialtie`,`view_appointments`.`location` AS `location` from (`notifications` join `view_appointments` on(`notifications`.`appointment_id` = `view_appointments`.`id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_patients`
--

/*!50001 DROP VIEW IF EXISTS `view_patients`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_patients` AS select `users`.`email` AS `email`,`users`.`password` AS `password`,`patients`.`id` AS `id`,`patients`.`name` AS `name`,`patients`.`cpf` AS `cpf`,`patients`.`birth_date` AS `birth_date`,`patients`.`user_id` AS `user_id`,`patients`.`phone_number` AS `phone_number` from (`patients` join `users` on(`users`.`id` = `patients`.`user_id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-08 23:00:32
