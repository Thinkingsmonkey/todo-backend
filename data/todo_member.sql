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
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password_hash` varchar(500) NOT NULL,
  `salt` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (2,'asfasdf','asdfsafd','a6ed175e4e23e0bdbd864c1a9154b576','test@gmail.com'),(4,'asdfasf','pbkdf2:sha256:600000$UOZJMOkWHjVu8Q4Y$2f29162ef276f9bdf0c184ebe6de472ce8044e9457a3dc09b1c9e6af61f5d98e','30b217b98e1f361d3631c0c7a6c7c8cd','test1@gmail.com'),(6,'sdfs','pbkdf2:sha256:600000$nToV6qf2btGb6Vui$627b4d766f6f3d09d8cd3548d959a2e7860bd49edd84f9f24babab293f9cdfc2','78242411862fc75a6f1affd95928e202','294b99e8-2ce9-43f4-aee8-21b51674eca9'),(7,'aaaaa','pbkdf2:sha256:600000$idFfUrU3FaNnE0W3$8d3d60e34d28436f94be21c914496411f0fa24da16fb31825a1cf03d8bdda308','a293cd0e76e57d464465bd4248596b99','dddd'),(10,'aaaaaddddddd','pbkdf2:sha256:600000$Gsdae1ESVTTGmSvi$791369eb683c937110adfde765c6ae8df6c54266a3cb4460d565cc63ccc7a8c5','dc927f654c2aec1e315c1dc81e1fa0cd','ddddssssssss'),(11,'qwerqwer','pbkdf2:sha256:600000$sYI3oLQC4yQjcViD$e8ec5e132fbdbf454f0ea052ea00f36472e75437d71e23ae9fef0a458796227a','9c82fd4e001f1297979365bb003a8fae','qwerqwer'),(14,'test','pbkdf2:sha256:600000$vGbNAB3q9Eh59L2h$ad62c32240a4fa5c3cfd4861e04d29ccbba1577cfd17fd040f661c6d64a8c341','029e54a96906f4cf8163367ac255c4af','test'),(15,'test1','pbkdf2:sha256:600000$rMA07DijEdb4IjtP$bf1fc81f4a9b9fbf6628d99098f874b401b32d261445972c893147d6c488c683','969c60b897cb613fd9970972c436c86e','test@'),(16,'qqq','pbkdf2:sha256:600000$QZuRxvKZIIWqIA0I$164d9c0d1c179d3de6269b79342d235ba7b03b5b45bf330c4d8b1ca7a697e99f','cae1c42a072be9fabf9a5f4e7d95af96','qqq'),(17,'www','pbkdf2:sha256:600000$kmFIFVUgcdrdB91s$fb87100de889c8435c840f0e838f75b33163a4183e2029f12cce24b679fb191f','585695f2e278c4a0a9aef442968d0053','www');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
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
