-- MySQL dump 10.13  Distrib 9.0.1, for Win64 (x86_64)
--
-- Host: localhost    Database: tienda
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `idCategoria` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Bebidas','Bebidas gaseosas y naturales'),(2,'Lácteos','Leches y quesos'),(3,'Frutas','Frutas naturales'),(4,'Carnes','Carnes blancas y carnes rojas');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `idCliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `ciudad` varchar(45) DEFAULT NULL,
  `pais` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Jordi','Peña','(216)390596','jordip@test.com','Brasilia','Brasil'),(2,'Álvaro','Gutierrez','(884)639106','alvarog@test.com','Dublín','Irlanda'),(3,'Lara','Gomez','(121)907333','lgomez@test.net','Bogotá','Colombia'),(4,'Adriana','Garrido','(120)217209','adrianag@test.com','Tegucigalpa','Honduras'),(5,'Isabel','Mora','(167)281764','luismora@test.es','Brucelas','Bélgica'),(6,'Óscar','Flores','(574)181598','oflores@test.net','Dallas','Estados Unidos'),(7,'Darío','Moya','(708)179745','morad@test.com','Quebec','Canadá'),(8,'Carlos','Carmona','(225)417374','ccarmona@test.net','Santigo','Chile'),(9,'Natalia','Gallego','(940)689766','natig@test.com','Budapest','Hungría'),(10,'Laura','Solis','(152)685846','lsolis@test.com','Madrid','España'),(11,'Alonso','Ortiz','(158)785844','alonsortiz@test.com','París','Francia');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamento`
--

DROP TABLE IF EXISTS `departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamento` (
  `idDepartamento` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idDepartamento`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,'Frutas'),(2,'Carnes'),(3,'General');
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_factura`
--

DROP TABLE IF EXISTS `detalle_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_factura` (
  `idDetalle` int NOT NULL AUTO_INCREMENT,
  `idFactura` int DEFAULT NULL,
  `idProducto` int DEFAULT NULL,
  `precioUnitario` decimal(10,2) DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  PRIMARY KEY (`idDetalle`),
  KEY `FK_REL_FAC_DET_idx` (`idFactura`),
  KEY `FK_REL_PRO_DET_idx` (`idProducto`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_factura`
--

LOCK TABLES `detalle_factura` WRITE;
/*!40000 ALTER TABLE `detalle_factura` DISABLE KEYS */;
INSERT INTO `detalle_factura` VALUES (1,1,5,2.20,1),(2,1,2,6.00,1),(3,1,4,2.30,4),(4,1,9,1.18,2),(5,2,5,2.20,1),(6,2,3,0.50,1),(7,2,8,0.50,4),(8,3,10,3.50,1),(9,3,2,6.00,2),(10,3,6,1.50,3),(11,4,7,1.80,1),(12,5,5,2.20,1),(13,5,10,3.50,4),(14,5,9,1.18,4),(15,5,11,1.60,2),(16,5,1,2.00,1),(17,6,7,1.80,3),(18,6,5,2.20,4),(19,6,6,1.50,4),(20,6,8,0.50,4),(21,7,7,1.80,2),(22,7,8,0.50,1),(23,7,2,6.00,2),(24,7,4,2.30,2),(25,7,10,3.50,1),(26,8,7,1.80,2),(27,8,5,2.20,4),(28,8,6,1.50,4),(29,9,8,0.50,1),(30,9,5,2.20,2),(31,9,7,1.80,4),(32,10,10,3.50,3),(33,11,6,1.50,1),(34,11,10,3.50,1),(35,11,9,1.18,4),(36,12,3,0.50,1),(37,12,6,1.50,1),(38,12,4,2.30,4),(39,12,11,1.60,1),(40,13,10,3.50,4),(41,14,5,2.20,3),(42,14,8,0.50,4),(43,14,2,6.00,1),(44,15,7,1.80,4),(45,16,7,1.80,3),(46,16,5,2.20,1),(47,16,4,2.30,1),(48,16,9,1.18,4),(49,17,8,0.50,1),(50,18,1,2.00,1),(51,18,3,0.50,2),(52,18,10,3.50,4),(53,19,1,2.00,1),(54,19,10,3.50,2),(55,19,4,2.30,1),(56,19,8,0.50,4),(57,20,6,1.50,3),(58,20,7,1.80,1);
/*!40000 ALTER TABLE `detalle_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleado` (
  `idEmpleado` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `fechaIngreso` date DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `sexo` enum('hombre','mujer') DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `idDepartamento` int DEFAULT NULL,
  PRIMARY KEY (`idEmpleado`),
  KEY `FK_REL_DEP_EMP_idx` (`idDepartamento`),
  CONSTRAINT `FK_REL_DEP_EMP` FOREIGN KEY (`idDepartamento`) REFERENCES `departamento` (`idDepartamento`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES (1,'John','Turner','2018-01-20','1971-08-21','hombre','johnturner@ejemplo.com','410-944-0947',500.00,1),(2,'Hilda','Ulloa','2019-05-05','1950-07-03','mujer','hildaulloa@ejemplo.com','761 910 312',650.00,2),(3,'Alice','Costa','2018-04-26','1991-04-22','mujer','alicecostap@ejemplo.com','617 177 211',490.00,3),(4,'Anna','Cunha','2019-02-15','1980-01-27','mujer','annacunha@ejemplo.com','619 571 031',512.00,1),(5,'Thiago','Pereira','2018-11-03','1983-10-08','hombre','thiagopereira@ejemplo.com','757 579 534',360.00,2),(6,'Arturo','Garrido','2019-02-01','1982-09-23','hombre','arturogarrido@ejemplo.com',NULL,495.00,1);
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factura`
--

DROP TABLE IF EXISTS `factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `idFactura` int NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT NULL,
  `idCliente` int DEFAULT NULL,
  `idEmpleado` int DEFAULT NULL,
  PRIMARY KEY (`idFactura`),
  KEY `FK_REL_CLI_FAC_idx` (`idCliente`),
  KEY `FK_REL_EMP_FAC_idx` (`idEmpleado`),
  CONSTRAINT `FK_REL_CLI_FAC` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `FK_REL_EMP_FAC` FOREIGN KEY (`idEmpleado`) REFERENCES `empleado` (`idEmpleado`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES (1,'2016-10-16 00:00:00',6,2),(2,'2016-11-29 00:00:00',5,3),(3,'2017-01-22 00:00:00',10,3),(4,'2017-02-20 00:00:00',3,1),(5,'2017-03-07 00:00:00',7,3),(6,'2017-03-16 00:00:00',9,2),(7,'2017-09-06 00:00:00',11,4),(8,'2017-11-09 00:00:00',1,2),(9,'2017-11-09 00:00:00',7,3),(10,'2017-12-05 00:00:00',9,3),(11,'2018-07-18 00:00:00',3,5),(12,'2018-08-01 00:00:00',4,1),(13,'2018-08-03 00:00:00',4,4),(14,'2019-01-17 00:00:00',1,3),(15,'2019-01-22 00:00:00',7,3),(16,'2019-02-08 00:00:00',9,4),(17,'2019-03-29 00:00:00',3,4),(18,'2019-06-14 00:00:00',6,4),(19,'2019-07-14 00:00:00',1,5),(20,'2019-07-17 00:00:00',9,1);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `idProducto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `precioUnitario` int DEFAULT NULL,
  `idCategoria` int DEFAULT NULL,
  PRIMARY KEY (`idProducto`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (2,'Arroz',300,1),(3,'pollo',8000,2),(4,'fideos',800,3),(5,'Harina',800,4),(6,'Avena',2,2),(7,'Queso',6,4),(8,'Kiwi',1,5),(9,'Coco',2,2),(10,'Leche',2,4),(11,'Agua',2,3),(12,'Jugo de Naranja',2,3),(13,'Manzanas',1,5),(14,'Peras',1,5),(15,'Uvas',4,5),(16,'Jugo de Manzana',2,3),(17,'Arroz Yaman',4,2),(18,'Ciruela',2,6);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-22 16:43:29
