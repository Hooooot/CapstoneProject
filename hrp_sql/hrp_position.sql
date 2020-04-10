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
-- Table structure for table `position`
--

DROP TABLE IF EXISTS `position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `position` (
  `position_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `company_id` int(10) unsigned NOT NULL,
  `position_name` varchar(20) DEFAULT NULL,
  `position_type` varchar(10) DEFAULT NULL COMMENT '岗位类型',
  `position_min_wages` int(10) DEFAULT NULL,
  `position_max_wages` int(10) DEFAULT NULL,
  `position_education` varchar(10) DEFAULT NULL,
  `position_experience` varchar(10) DEFAULT NULL,
  `position_region` varchar(25) DEFAULT NULL,
  `position_detailed_location` varchar(35) DEFAULT NULL,
  `position_tags` varchar(45) DEFAULT NULL,
  `position_send_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `position_sender_position` varchar(15) DEFAULT NULL,
  `position_detail` varchar(1024) DEFAULT NULL,
  `position_state` tinyint(2) unsigned DEFAULT NULL,
  PRIMARY KEY (`position_id`),
  KEY `company_position_fore_idx` (`company_id`),
  CONSTRAINT `company_position_fore` FOREIGN KEY (`company_id`) REFERENCES `company` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='职位表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `position`
--

LOCK TABLES `position` WRITE;
/*!40000 ALTER TABLE `position` DISABLE KEYS */;
INSERT INTO `position` VALUES (1,11,'岗位名称','测试工程师',4,5,'高中','1-3年','北京市,北京市,东城区','详细地址','高中,1-3年,C++,C#,Java','2020-04-06 17:54:04','HR','简介\n\n\n\n\n\n简介       \n 简介\n\n\n\n\n   \n    简介',1),(2,11,'岗位名称','测试工程师',4,5,'高中','1-3年','北京市,北京市,东城区','详细地址','高中,1-3年,C++,C#,Java','2020-04-06 17:54:04','HR','简介\n\n\n\n\n\n简介       \n 简介\n\n\n\n\n   \n    简介',1),(3,12,'第二个公司的岗位','C#',4,5,'大专','3-5年','北京市,北京市,东城区','岗位的详细地址','大专,3-5年,X86,I2C,SPI,单片机开发','2020-04-07 18:16:42','人事经理','岗位简介\n\n简介',1),(4,11,'第一个公司的岗位名称','数据采集',11,12,'本科','1-3年','北京市,北京市,东城区','第一个公司的职位的详细地址','本科,1-3年,Java,C#,C++,Node.js','2020-04-07 21:03:49','人事','岗位简介',1),(5,13,'老公司第一个岗位','Golang',4,5,'学历不限','1-3年','北京市,北京市,东城区','详细工作地址','学历不限,1-3年,原画,动画动漫','2020-04-08 11:10:27','人事','岗位简介',1);
/*!40000 ALTER TABLE `position` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-09 19:28:36
