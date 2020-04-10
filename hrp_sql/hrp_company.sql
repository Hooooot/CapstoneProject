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
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company` (
  `company_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `company_owner_id` int(10) unsigned DEFAULT NULL COMMENT '注册人ID',
  `company_logo_id` int(10) unsigned DEFAULT NULL,
  `company_name` varchar(25) DEFAULT NULL,
  `company_organization_code` char(18) DEFAULT NULL COMMENT '组织机构代码 18 位',
  `company_financing_progress` varchar(10) DEFAULT NULL,
  `company_employees_num` varchar(10) DEFAULT NULL COMMENT '公司规模',
  `company_region` varchar(25) DEFAULT NULL,
  `company_detailed_location` varchar(35) DEFAULT NULL,
  `company_establishment_date` date DEFAULT NULL COMMENT '公司成立日期',
  `company_registered_capital` double DEFAULT NULL COMMENT '注册资金，单位万人民币，16位有效数字',
  `company_website` varchar(25) DEFAULT NULL COMMENT '公司官网',
  `company_detail` varchar(1024) DEFAULT NULL COMMENT '公司详细信息',
  `company_state` tinyint(2) unsigned DEFAULT NULL COMMENT '公司状态',
  PRIMARY KEY (`company_id`),
  KEY `onwer_company_fore_idx` (`company_owner_id`),
  KEY `comapny_logo_fore_idx` (`company_logo_id`),
  CONSTRAINT `comapny_logo_fore` FOREIGN KEY (`company_logo_id`) REFERENCES `file_blob` (`file_id`),
  CONSTRAINT `onwer_company_fore` FOREIGN KEY (`company_owner_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='公司表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (9,1,6,'123456789','123456789123456789','C轮','1000-9999人','[object Array]','公司的详细地址','2014-04-04',20000.123,'www.changtiaorap.cn','123456\n\n\ndasdas\n\n\n\n啊实打实\n      啊实打实阿萨     阿松大阿松大\n打算\n\n',1),(10,1,6,'123456789','123456789123456789','C轮','1000-9999人','[object Array]','公司的详细地址','2014-04-04',20000.123,'www.changtiaorap.cn','123456\n\n\ndasdas\n\n\n\n啊实打实\n      啊实打实阿萨     阿松大阿松大\n打算\n\n',1),(11,2,7,'123','123123123123123123','C轮','10000人以上','[object Array]','123deqeqwe详细地址','2015-04-04',12.0324545,'www.chadasdasdasdasd.cn','\n234\n啊打发撒旦\n\n\n\n\n啊手动阀撒旦\n\n\n\n\n啊手动阀阿松大      士大夫\n 是的',6),(12,2,14,'公司名称','123456789123456789','B轮','10000人以上','[object Array]','公司的详细地址','2014-04-07',20000.213,'www.china.cn','简介\n短简介',6),(13,2,15,'第三个公司名字','123456789123456789','C轮','1000-9999人','[object Array]','详细地址','2015-04-07',10000.0001,'www.china.cn','简介\n简介',1),(14,2,16,'新公司第一个','123456789123456789','已上市','1000-9999人','北京市,北京市,东城区','新公司第一个的详细地址','2015-04-08',123456789,'官网','简介\n\n简介',1);
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
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
