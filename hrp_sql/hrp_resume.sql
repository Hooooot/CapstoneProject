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
-- Table structure for table `resume`
--

DROP TABLE IF EXISTS `resume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `resume` (
  `resume_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `resume_name` varchar(45) DEFAULT NULL COMMENT '简历文件名',
  `resume_file_id` int(10) unsigned DEFAULT NULL,
  `resume_type` varchar(10) DEFAULT NULL COMMENT '简历类型 .doc .docx .pdf',
  `resume_submit_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '简历上传时间',
  `resume_size` int(10) unsigned DEFAULT NULL COMMENT '简历的大小，单位Byte',
  `resume_state` tinyint(2) unsigned DEFAULT NULL COMMENT '简历是否被用户删除',
  PRIMARY KEY (`resume_id`),
  KEY `resume_user_fore_idx` (`user_id`),
  KEY `file_resume_idx` (`resume_file_id`),
  CONSTRAINT `file_resume` FOREIGN KEY (`resume_file_id`) REFERENCES `file_blob` (`file_id`),
  CONSTRAINT `user_resume` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='简历表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resume`
--

LOCK TABLES `resume` WRITE;
/*!40000 ALTER TABLE `resume` DISABLE KEYS */;
INSERT INTO `resume` VALUES (4,2,'校招入职须知2020.docx',10,'docx','2020-04-05 17:12:58',85659,6),(5,2,'app.txt',11,'txt','2020-04-05 17:15:06',201,6),(6,2,'安卓题库.docx',12,'docx','2020-04-05 17:29:02',398750,6),(7,2,'03-1504011019-王浩禹-毕业设计(论文)开题报告.doc',13,'doc','2020-04-07 15:01:32',59904,6),(8,2,'}CD4O94{J4$G9A~C8S3TM$6.png',7,'png','2020-04-07 17:05:13',29898,6),(9,2,'03-1504011019-王浩禹-毕业设计(论文)开题报告.doc',13,'doc','2020-04-07 17:38:08',59904,1);
/*!40000 ALTER TABLE `resume` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-09 19:28:32
