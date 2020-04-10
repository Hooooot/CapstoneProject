-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: hrp
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `browsing_history`
--

DROP TABLE IF EXISTS `browsing_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `browsing_history` (
  `browsing_history_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned DEFAULT NULL,
  `position_id` int(10) unsigned DEFAULT NULL,
  `browsing_history_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `browsing_history_state` tinyint(2) unsigned DEFAULT NULL,
  PRIMARY KEY (`browsing_history_id`),
  KEY `browsing_user_fore_idx` (`user_id`),
  KEY `browsing_position_fore_idx` (`position_id`),
  CONSTRAINT `browsing_position_fore` FOREIGN KEY (`position_id`) REFERENCES `position` (`position_id`),
  CONSTRAINT `browsing_user_fore` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户浏览岗位的历史，只有点进详细页面才记录';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `browsing_history`
--

LOCK TABLES `browsing_history` WRITE;
/*!40000 ALTER TABLE `browsing_history` DISABLE KEYS */;
INSERT INTO `browsing_history` VALUES (1,2,1,'2020-04-09 16:51:27',1),(2,2,2,'2020-04-08 13:56:30',1),(3,NULL,1,'2020-04-08 12:25:14',1),(4,NULL,2,'2020-04-07 17:43:56',1),(5,NULL,4,'2020-04-08 11:01:49',1),(6,2,5,'2020-04-08 13:56:19',1),(7,2,3,'2020-04-08 13:56:26',1);
/*!40000 ALTER TABLE `browsing_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-09 19:28:34
