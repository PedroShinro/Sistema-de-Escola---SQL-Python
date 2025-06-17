CREATE DATABASE  IF NOT EXISTS `cadastro` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cadastro`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cadastro
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `turmas`
--

DROP TABLE IF EXISTS `turmas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turmas` (
  `id_turma` int NOT NULL AUTO_INCREMENT,
  `nome_turma` varchar(30) DEFAULT NULL,
  `cursos` varchar(50) DEFAULT NULL,
  `data_inicio` date DEFAULT NULL,
  `turmacurso` int DEFAULT NULL,
  PRIMARY KEY (`id_turma`),
  KEY `fk_turmas_curso` (`turmacurso`),
  CONSTRAINT `fk_turmas_curso` FOREIGN KEY (`turmacurso`) REFERENCES `cursos` (`id_curso`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turmas`
--

LOCK TABLES `turmas` WRITE;
/*!40000 ALTER TABLE `turmas` DISABLE KEYS */;
INSERT INTO `turmas` VALUES (1,'Turma A','Python Básico','2025-02-03',1),(2,'Turma B','Python Básico','2025-03-10',1),(3,'Turma A','JavaScript Essencial','2025-02-17',3),(4,'Turma A','Java Fundamentos','2025-03-01',4),(5,'Turma Noturna','C# com .NET','2025-03-15',5),(6,'Turma Sábado','MySQL Iniciante','2025-04-06',6),(7,'Turma A','HTML e CSS','2025-04-08',7),(8,'Turma B','HTML e CSS','2025-04-29',7),(9,'Turma A','PHP Laravel','2025-05-05',8),(10,'Turma A','Redes','2025-05-19',9),(11,'Turma Manhã','Segurança Info','2025-06-02',10),(12,'Turma Noite','Segurança Info','2025-06-16',10),(13,'Turma A','Data Science','2025-06-23',11),(14,'Turma B','Excel Avançado','2025-07-07',12),(15,'Turma C','Excel Avançado','2025-07-14',12),(16,'Turma A','Power BI','2025-07-21',13),(17,'Turma A','Photoshop','2025-08-04',14),(18,'Turma A','React.js','2025-08-11',18),(19,'Turma A','Node.js API REST','2025-08-18',19),(20,'Turma A','Docker & DevOps','2025-08-25',20);
/*!40000 ALTER TABLE `turmas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-13 14:36:16
