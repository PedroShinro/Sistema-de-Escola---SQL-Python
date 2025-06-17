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
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos` (
  `id_aluno` int NOT NULL AUTO_INCREMENT,
  `nome_aluno` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefone` varchar(100) DEFAULT NULL,
  `cpf` varchar(25) DEFAULT NULL,
  `sexo` enum('M','F') DEFAULT NULL,
  `data_nascimento` date DEFAULT NULL,
  `turma` varchar(20) DEFAULT NULL,
  `cursoaluno` int DEFAULT NULL,
  `turmaaluno` int DEFAULT NULL,
  PRIMARY KEY (`id_aluno`),
  KEY `fk_alunos_turma` (`turmaaluno`),
  KEY `cursoaluno` (`cursoaluno`),
  CONSTRAINT `alunos_ibfk_1` FOREIGN KEY (`cursoaluno`) REFERENCES `cursos` (`id_curso`),
  CONSTRAINT `fk_alunos_curso` FOREIGN KEY (`cursoaluno`) REFERENCES `cursos` (`id_curso`),
  CONSTRAINT `fk_alunos_turma` FOREIGN KEY (`turmaaluno`) REFERENCES `turmas` (`id_turma`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (1,'Ana Paula','ana.paula@gmail.com','(11) 9 8123-4001','11122233344','F','2001-01-15','Turma A',1,1),(2,'Bruno Oliveira','bruno.oliveira@gmail.com','(11) 9 8123-4002','22233344455','M','2000-02-20','Turma A',1,1),(3,'Camila Gonçalves','camila.goncalves@yahoo.com','(11) 9 8123-4003','33344455566','F','2002-03-18','Turma B',1,2),(4,'Daniel Souza','daniel.souza@outlook.com','(11) 9 8123-4004','44455566677','M','1999-04-30','Turma B',1,2),(5,'Eduardo Lima','eduardo.lima@gmail.com','(11) 9 8123-4005','55566677788','M','2003-05-25','Turma A',3,3),(6,'Fernanda Reis','fernanda.reis@yahoo.com','(11) 9 8123-4006','66677788899','F','2001-06-12','Turma A',3,3),(7,'Gabriel Martins','gabriel.martins@gmail.com','(11) 9 8123-4007','77788899900','M','2002-07-15','Turma A',4,4),(8,'Helena Barros','helena.barros@outlook.com','(11) 9 8123-4008','88899900011','F','2000-08-08','Turma Noturna',5,5),(9,'Igor Carvalho','igor.carvalho@gmail.com','(11) 9 8123-4009','99900011122','M','1998-09-19','Turma Sábado',6,6),(10,'Julia Pereira','julia.pereira@yahoo.com','(11) 9 8123-4010','00011122233','F','2003-10-27','Turma Sábado',6,6),(11,'Kleber Araújo','kleber.araujo@gmail.com','(11) 9 8123-4011','11133355577','M','2002-11-11','Turma A',7,7),(12,'Larissa Teixeira','larissa.tx@gmail.com','(11) 9 8123-4012','22244466688','F','2001-12-05','Turma B',7,8),(13,'Marcelo Almeida','marcelo.almeida@live.com','(11) 9 8123-4013','33355577799','M','1999-01-03','Turma A',8,9),(14,'Natália Santos','natalia.s@gmail.com','(11) 9 8123-4014','44466688800','F','2000-02-14','Turma A',8,9),(15,'Otávio Ribeiro','otavio.ribeiro@gmail.com','(11) 9 8123-4015','55577799911','M','2002-03-16','Turma A',10,11),(16,'Paula Nascimento','paula.nascimento@yahoo.com','(11) 9 8123-4016','66688800022','F','2001-04-21','Turma Noite',10,12),(17,'Rafael Freitas','rafael.freitas@outlook.com','(11) 9 8123-4017','77799911133','M','2000-05-12','Turma A',12,14),(18,'Simone Costa','simone.costa@gmail.com','(11) 9 8123-4018','88800022244','F','2003-06-06','Turma C',12,15),(19,'Tiago Monteiro','tiago.monteiro@gmail.com','(11) 9 8123-4019','99911133355','M','1998-07-07','Turma A',18,18),(20,'Vera Lins','vera.lins@outlook.com','(11) 9 8123-4020','00022244466','F','2001-08-18','Turma A',18,18);
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
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
