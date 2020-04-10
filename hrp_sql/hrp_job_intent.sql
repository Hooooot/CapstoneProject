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
-- Table structure for table `job_intent`
--

DROP TABLE IF EXISTS `job_intent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `job_intent` (
  `job_intent_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned DEFAULT NULL,
  `job_intent_type` varchar(10) DEFAULT NULL,
  `job_intent_region` varchar(25) DEFAULT NULL,
  `job_intent_min_wages` int(10) unsigned DEFAULT NULL,
  `job_intent_max_wages` int(10) unsigned DEFAULT NULL,
  `job_intent_education` varchar(10) DEFAULT NULL,
  `job_intent_major` varchar(15) DEFAULT NULL,
  `job_intent_education_index` varchar(10) DEFAULT NULL,
  `job_intent_type_index` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`job_intent_id`),
  KEY `intent_user_fore_idx` (`user_id`),
  CONSTRAINT `intent_user_fore` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='工作意向';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_intent`
--

LOCK TABLES `job_intent` WRITE;
/*!40000 ALTER TABLE `job_intent` DISABLE KEYS */;
INSERT INTO `job_intent` VALUES (14,2,'后端开发','北京市,北京市,东城区',0,1,'博士','zhuanyemingc','7','0,0,0'),(15,2,'后端开发','北京市,北京市,东城区',3,4,'高中','','3','0,0,0');
/*!40000 ALTER TABLE `job_intent` ENABLE KEYS */;
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
