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
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `telefono` char(20) NOT NULL,
  `email` varchar(45) NOT NULL,
  `registro` date DEFAULT '2023-09-12',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Juanita','Lind','(123) 8592-2238','juanitalind@test.com','2023-09-12'),(2,'George','Weissnat','(123) 6599-8313','georgeweissnat@test.com','2023-09-12'),(3,'Leilani','Langworth','(123) 3376-7786','leilanilangworth@test.com','2023-09-12'),(4,'Reggie','Schmitt','(123) 1886-6216','reggieschmitt@test.com','2023-09-12'),(5,'Delores','Rippin','(123) 9976-1342','deloresrippin@test.com','2023-09-12'),(6,'Guido','Rogahn','(123) 4357-9648','guidorogahn@test.com','2023-09-12'),(7,'Delfina','Schmeler','(123) 3819-7691','delfinaschmeler@test.com','2023-09-12'),(8,'Lon','Conroy','(123) 9585-9496','lonconroy@test.com','2023-09-12'),(9,'Arden','Schumm','(123) 1197-5529','ardenschumm@test.com','2023-09-12'),(10,'Elliott','Kulas','(123) 1748-9216','elliottkulas@test.com','2023-09-12'),(11,'Cristobal','Wiza','(123) 5681-8953','cristobalwiza@test.com','2023-09-12'),(12,'Marcia','Davis','(123) 9293-6426','marciadavis@test.com','2023-09-12'),(13,'Aliya','Marks','(123) 1893-4467','aliyamarks@test.com','2023-09-12'),(14,'Milo','Schneider','(123) 3997-7463','miloschneider@test.com','2023-09-12'),(15,'Shad','Bechtelar','(123) 5257-4753','shadbechtelar@test.com','2023-09-12'),(16,'Frank','Will','(123) 2384-5446','frankwill@test.com','2023-09-12'),(17,'Onie','Rutherford','(123) 7943-2934','onierutherford@test.com','2023-09-12'),(18,'Candice','Hane','(123) 6413-1663','candicehane@test.com','2023-09-12'),(19,'Duncan','Leffler','(123) 2176-6559','duncanleffler@test.com','2023-09-12'),(20,'Christop','Olson','(123) 8922-2453','christopolson@test.com','2023-09-12'),(21,'Johnson','Spencer','(123) 1197-9238','johnsonspencer@test.com','2023-09-12'),(22,'Tabitha','Okuneva','(123) 7469-9997','tabithaokuneva@test.com','2023-09-12'),(23,'Ewald','VonRueden','(123) 1963-5516','ewaldvonrueden@test.com','2023-09-12'),(24,'Cory','Kemmer','(123) 3359-1678','corykemmer@test.com','2023-09-12'),(25,'Kacey','Moen','(123) 1634-3999','kaceymoen@test.com','2023-09-12'),(26,'Karlee','Johns','(123) 6166-5523','karleejohns@test.com','2023-09-12'),(27,'Avis','Beatty','(123) 4957-2676','avisbeatty@test.com','2023-09-12'),(28,'Jermaine','Brekke','(123) 3564-1328','jermainebrekke@test.com','2023-09-12'),(29,'Madge','Emmerich','(123) 7316-7961','madgeemmerich@test.com','2023-09-12'),(30,'Ewell','Hackett','(123) 7766-6929','ewellhackett@test.com','2023-09-12'),(31,'Sharon','Weber','(123) 1748-1683','sharonweber@test.com','2023-09-12'),(32,'Angie','Kautzer','(123) 2147-8734','angiekautzer@test.com','2023-09-12'),(33,'Cordia','Lind','(123) 8242-1543','cordialind@test.com','2023-09-12'),(34,'Rodolfo','Deckow','(123) 2488-9844','rodolfodeckow@test.com','2023-09-12'),(35,'Cassandre','Walter','(123) 8243-5334','cassandrewalter@test.com','2023-09-12'),(36,'Amos','Glover','(123) 4686-5593','amosglover@test.com','2023-09-12'),(37,'Garret','Robel','(123) 1477-4732','garretrobel@test.com','2023-09-12'),(38,'Zaria','Schowalter','(123) 3548-7273','zariaschowalter@test.com','2023-09-12'),(39,'Christa','Marvin','(123) 2536-5518','christamarvin@test.com','2023-09-12'),(40,'Krystel','Block','(123) 5156-3621','krystelblock@test.com','2023-09-12'),(41,'Francisca','Parisian','(123) 4488-1418','franciscaparisian@test.com','2023-09-12'),(42,'Omari','Russel','(123) 4488-1411','omarirussel@test.com','2023-09-12'),(43,'Emmanuel','Vandervort','(123) 1886-5871','emmanuelvandervort@test.com','2023-09-12'),(44,'Murl','Kuhic','(123) 4818-9154','murlkuhic@test.com','2023-09-12'),(45,'Jaiden','Balistreri','(123) 6912-8469','jaidenbalistreri@test.com','2023-09-12'),(46,'Forest','Jakubowski','(123) 4943-2899','forestjakubowski@test.com','2023-09-12'),(47,'Karlee','Heller','(123) 4961-3548','karleeheller@test.com','2023-09-12'),(48,'Sydney','Buckridge','(123) 5252-2245','sydneybuckridge@test.com','2023-09-12'),(49,'Mabelle','Terry','(123) 4666-9215','mabelleterry@test.com','2023-09-12'),(50,'Raymond','Ortiz','(123) 8321-4263','raymondortiz@test.com','2023-09-12'),(51,'Isadore','Bernhard','(123) 8681-8238','isadorebernhard@test.com','2023-09-12'),(52,'Turner','Sporer','(123) 3591-4125','turnersporer@test.com','2023-09-12'),(53,'Madison','Schoen','(123) 1216-8515','madisonschoen@test.com','2023-09-12'),(54,'Brittany','Bernhard','(123) 4615-3781','brittanybernhard@test.com','2023-09-12'),(55,'Theron','Watsica','(123) 2899-9979','theronwatsica@test.com','2023-09-12'),(56,'Bernhard','Schroeder','(123) 6286-6413','bernhardschroeder@test.com','2023-09-12'),(57,'Cristobal','Runte','(123) 2987-1818','cristobalrunte@test.com','2023-09-12'),(58,'Elsa','Thompson','(123) 7145-5914','elsathompson@test.com','2023-09-12'),(59,'Tyra','Hickle','(123) 4476-7125','tyrahickle@test.com','2023-09-12'),(60,'Jarrod','Dach','(123) 3579-8449','jarroddach@test.com','2023-09-12'),(61,'Juan','Riquelme','112356789','Gaby.cabj@gmail.com','2024-09-27');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
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
