-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: libreria
-- ------------------------------------------------------
-- Server version	9.0.1

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
-- Table structure for table `libro`
--

DROP TABLE IF EXISTS `libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libro` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `total_paginas` int DEFAULT NULL,
  `puntuacion` decimal(10,2) unsigned NOT NULL,
  `isbn` varchar(13) DEFAULT NULL,
  `fecha_publicacion` date DEFAULT NULL,
  `id_editor` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_producto_marca_idx` (`id_editor`),
  CONSTRAINT `fk_producto_marca` FOREIGN KEY (`id_editor`) REFERENCES `editor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libro`
--

LOCK TABLES `libro` WRITE;
/*!40000 ALTER TABLE `libro` DISABLE KEYS */;
INSERT INTO `libro` VALUES (1,'La octava dimensión',182,1.73,'de3764836d','2023-05-25',3),(2,'Draroc el bueno',194,2.59,'ea4b81d719','1986-01-13',1),(3,'León del dolor',173,2.76,'ff890ca9a1','2026-01-30',2),(4,'Humano sin defectos',235,1.04,'2e3c3a6ccf','1998-02-26',3),(5,'Piratas de la felicidad',205,3.92,'193c4d6156','2010-07-31',3),(6,'Mujeres y piratas',169,3.50,'355295e102','2020-05-19',4),(7,'Raíz de plata',181,4.72,'7dc6b5ba51','2032-02-11',3),(8,'Visión de madera',246,4.10,'85189d7028','1993-04-28',4),(9,'Bailando en el universo',239,1.34,'6404c1b0d4','2036-05-19',1),(10,'Batalla de mis amigos',205,1.41,'43ddfe6db7','2027-10-14',2),(11,'Caballero de los desterrados',160,2.03,'a9cbb7022f','1991-09-22',4),(12,'Duque de los desamparados',234,4.91,'e2a0226d9a','1973-04-25',2),(13,'Brujas de la noche',238,1.44,'4a5744e589','1989-06-15',4),(14,'Enemigos con vigor',241,3.50,'e2a9f028ba','1989-04-13',2),(15,'BN170',238,4.17,'f3c9a0ba69','2008-01-17',4),(16,'Gatos y dioses',220,1.37,'dba2a3f3dc','2034-04-27',1),(17,'Creadores y herederos',236,1.31,'f490a3640e','1973-04-25',2),(18,'Aguja del próximo año',169,1.45,'5f7c864ead','1997-10-09',3),(19,'Unidad de grandeza',188,2.33,'a628161273','2030-11-10',4),(20,'Gritos en mi pasado',181,2.29,'2d83098a87','1986-10-30',3),(21,'Limpiando una tormenta',191,3.47,'7eb243528a','2007-09-02',3),(22,'Estafador con orgullo',163,1.47,'b7e65017a9','1971-10-07',1),(23,'Gigante de la esperanza',190,3.95,'54c2e8eebf','2001-11-28',3),(24,'Soldados del infinito',214,2.33,'8888d2036f','1988-02-27',4),(25,'Creadores de la paz',150,2.81,'13a975f3c1','2033-02-05',1),(26,'Ascendencia de los sueños',159,2.05,'4d38dbd8d3','2026-11-18',1),(27,'Canciones de mi familia',192,4.84,'b9f7dc0714','1997-01-19',4),(28,'La jungla',236,1.02,'d04dbca97a','2002-08-30',2),(29,'Agente de plata',153,1.61,'a122df6a0f','1984-02-10',3),(30,'Amigo de la luz',208,3.98,'44b7dbe2a3','2010-08-13',3),(31,'Perros de esperanza',231,2.08,'f7d06aad5b','1994-08-23',1),(32,'Héroes del ayer',179,1.45,'47b3d0f660','1971-05-14',2),(33,'Amigos y búhos',154,3.99,'45e8cbbac9','1970-12-12',1),(34,'Trono con esperanza',183,2.64,'0e4f42b0c5','1970-08-22',1),(35,'Señales en el norte',202,4.20,'4f7a913420','1970-05-09',1),(36,'Comer en los barcos',210,4.07,'cf58e3cef3','2037-11-23',4),(37,'Amigo de los perdidos',195,2.75,'4c98a0a070','2036-03-21',3),(38,'Oficiales de gloria',197,4.57,'b05bb2d3a1','2029-05-10',2),(39,'Gatos y creadores',249,1.58,'47c3050ee5','2000-01-30',4),(40,'Defensores y hombres',202,1.18,'9735d1ee67','2010-05-17',4),(41,'Honor del océano',216,4.17,'0ae9776499','2013-08-02',4),(42,'Causa de la libertad',223,4.31,'ab151c9f93','1998-10-02',2),(43,'La vida en el rey',218,4.02,'48bc6cc176','1983-01-01',3),(44,'Ayudando al sol',168,2.20,'66d1f39eb5','2016-10-19',1),(45,'Médicos y agentes',239,1.92,'aa1d3ef593','2028-11-24',2),(46,'Paz a la nación',238,2.00,'7fe5dc58f3','1987-12-28',1),(47,'Alterando a los ángeles',226,3.25,'f8d50541f4','2019-05-09',2),(48,'Adoptando el universo',166,1.24,'1aa9410046','2026-09-11',3),(49,'Oponente de la utopía',202,3.45,'b0cd1cfab3','2037-05-14',4),(50,'Diosa sin honor',162,4.55,'c941b29f65','2000-08-24',2),(51,'Sonidos en el vacío',154,3.37,'34cbc239dc','1989-03-07',1);
/*!40000 ALTER TABLE `libro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-29 18:09:26
