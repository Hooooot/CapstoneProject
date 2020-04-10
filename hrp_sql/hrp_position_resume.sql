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
-- Table structure for table `position_resume`
--

DROP TABLE IF EXISTS `position_resume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `position_resume` (
  `position_resume_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned DEFAULT NULL,
  `position_id` int(10) unsigned DEFAULT NULL,
  `resume_id` int(10) unsigned DEFAULT NULL,
  `position_resume_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '投递时间',
  `position_resume_state` tinyint(2) unsigned DEFAULT NULL COMMENT '投递简历的状态：已下载、已查看等',
  `position_resume_checked` tinyint(2) unsigned DEFAULT NULL,
  PRIMARY KEY (`position_resume_id`),
  KEY `resume_position_user_idx` (`user_id`),
  KEY `position_resume_position_fore_idx` (`position_id`),
  KEY `resume_position_fore_idx` (`resume_id`),
  CONSTRAINT `position_resume_position_fore` FOREIGN KEY (`position_id`) REFERENCES `position` (`position_id`),
  CONSTRAINT `resume_position_fore` FOREIGN KEY (`resume_id`) REFERENCES `resume` (`resume_id`),
  CONSTRAINT `resume_position_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户投递的简历表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `position_resume`
--

LOCK TABLES `position_resume` WRITE;
/*!40000 ALTER TABLE `position_resume` DISABLE KEYS */;
INSERT INTO `position_resume` VALUES (8,2,1,7,'2020-04-07 16:30:57',1,10),(9,2,1,9,'2020-04-07 17:43:42',1,10);
/*!40000 ALTER TABLE `position_resume` ENABLE KEYS */;
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
