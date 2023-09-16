-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: todo
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task` (
  `id` int NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `priority` enum('High','Medium','Low') DEFAULT 'Medium',
  `state` enum('Todo','Doing','Done') DEFAULT 'Todo',
  `start` datetime DEFAULT CURRENT_TIMESTAMP,
  `deadline` datetime DEFAULT ((now() + interval 1 day)),
  `description` text,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `task_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (51,14,'asdfasdfasfd','Medium','Todo','2023-09-10 00:00:00','2023-09-11 00:00:00','dddd'),(52,14,'111111111111111111','Low','Doing','2023-09-10 00:00:00','2023-09-11 00:00:00',''),(53,14,'dddddddddddddd','Medium','Todo','2023-09-10 00:00:00','2023-09-11 00:00:00',''),(54,4,'e1e1e','Medium','Todo','2023-09-13 00:00:00','2023-09-14 00:00:00',''),(55,7,'11111','Medium','Done','2023-09-12 00:00:00','2023-09-14 00:00:00',''),(56,7,'qwdqdfq','High','Doing','2023-09-13 00:00:00','2023-09-06 00:00:00','dddd'),(57,14,'111','Medium','Todo','2023-09-13 16:51:04','2023-09-14 16:42:36',''),(58,14,'1111','Medium','Todo','2023-09-13 16:51:18','2023-09-14 16:42:36',''),(59,14,'111','Medium','Todo','2023-09-13 17:05:17','2023-09-14 16:42:36',''),(60,14,'4444444444444444','Medium','Todo','2023-09-13 17:05:30','2023-09-14 16:42:36',''),(61,15,'111','Medium','Todo','2023-09-13 17:06:35','2023-09-14 16:42:36',''),(62,14,'tttttttttttttttt','Medium','Todo','2023-09-13 17:10:33','2023-09-14 17:09:26',''),(63,14,'tttttttttttwwwwwwwwwwwww','Medium','Todo','2023-09-13 17:10:40','2023-09-14 17:09:26',''),(64,14,'asdvasdv','Medium','Todo','2023-09-13 17:10:51','2023-09-14 17:09:26','asdvasvsavsavsadvsav'),(65,14,'ddd','Medium','Todo','2023-09-14 16:39:15','2023-09-15 15:56:18',''),(66,14,'1111','Medium','Todo','2023-09-14 18:28:41','2023-09-15 18:27:59',''),(67,14,'dddd','Medium','Todo','2023-09-14 18:36:02','2023-09-15 18:36:00',''),(68,14,'111','Medium','Todo','2023-09-14 18:39:24','2023-09-15 18:38:54',''),(69,14,'11114444','Medium','Todo','2023-09-14 18:54:48','2023-09-15 18:54:48',''),(70,14,'eddd','Medium','Todo','2023-09-14 19:12:23','2023-09-15 19:06:47',''),(71,14,'111','Medium','Todo','2023-09-14 19:16:26','2023-09-15 19:15:07',''),(72,14,'1','Medium','Todo','2023-09-14 19:17:14','2023-09-15 19:15:07',''),(73,14,'111','Medium','Todo','2023-09-14 19:18:07','2023-09-15 19:15:07',''),(74,14,'11111','Medium','Todo','2023-09-14 19:18:27','2023-09-15 19:15:07',''),(75,14,'111','Medium','Todo','2023-09-14 20:27:33','2023-09-15 20:25:51',''),(76,14,'2222222222222222222222222222222222222','Medium','Todo','2023-09-14 20:27:59','2023-09-15 20:25:51',''),(77,14,'2222','Medium','Todo','2023-09-14 22:04:05','2023-09-15 22:02:50',''),(78,14,'asfvasvasvsavasvsadvsadvasdbvabsdfbsd','Medium','Todo','2023-09-14 22:04:14','2023-09-15 22:02:50',''),(81,14,'string','Medium','Todo','2023-09-16 01:37:21','2023-09-16 01:37:21','string'),(82,14,'111','Medium','Todo','2023-09-16 13:02:19','2023-09-17 13:02:16',''),(83,14,'111','Medium','Todo','2023-09-16 13:17:52','2023-09-17 13:14:06',''),(84,14,'111','Medium','Todo','2023-09-16 13:18:00','2023-09-17 13:14:06',''),(85,14,'1111','Medium','Todo','2023-09-16 13:21:52','2023-09-17 13:14:06',''),(86,14,'111','Medium','Todo','2023-09-16 13:27:33','2023-09-17 13:23:59',''),(87,14,'222','Medium','Todo','2023-09-16 13:27:36','2023-09-17 13:23:59',''),(88,16,'dddasdfasdf','High','Done','2023-09-13 00:00:00','2023-09-21 00:00:00',''),(89,16,'33333','Medium','Todo','2023-09-16 13:30:56','2023-09-17 13:29:42',''),(90,14,'1111','Medium','Todo','2023-09-16 13:37:16','2023-09-17 13:29:42','');
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-16 14:45:08
