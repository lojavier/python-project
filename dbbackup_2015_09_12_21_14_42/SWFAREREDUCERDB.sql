-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: SWFAREREDUCERDB
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AIRPORTS`
--

DROP TABLE IF EXISTS `AIRPORTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AIRPORTS` (
  `AIRPORT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `AIRPORT_CODE` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `AIRPORT_NAME` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`AIRPORT_ID`),
  UNIQUE KEY `AIRPORT_CODE` (`AIRPORT_CODE`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='AIRPORTS';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AIRPORTS`
--

LOCK TABLES `AIRPORTS` WRITE;
/*!40000 ALTER TABLE `AIRPORTS` DISABLE KEYS */;
INSERT INTO `AIRPORTS` VALUES (1,'ALB','Albany, NY - ALB'),(2,'ABQ','Albuquerque, NM - ABQ'),(3,'AMA','Amarillo, TX - AMA'),(4,'AUA','Aruba, Aruba - AUA'),(5,'ATL','Atlanta, GA - ATL'),(6,'AUS','Austin, TX - AUS'),(7,'BZE','Belize City, Belize - BZE'),(8,'BHM','Birmingham, AL - BHM'),(9,'BOI','Boise, ID - BOI'),(10,'BOT','[Boston Area:]'),(11,'BOS','Boston Logan, MA - BOS'),(12,'BUF','Buffalo/Niagara, NY - BUF'),(13,'SJD','Cabo San Lucas/Los Cabos, MX - SJD'),(14,'CUN','Cancun, Mexico - CUN'),(15,'CHS','Charleston, SC - CHS'),(16,'CLT','Charlotte, NC - CLT'),(17,'MDW','Chicago (Midway), IL - MDW'),(18,'CNN','[Cincinnati Area:]'),(19,'CVL','[Cleveland Area:]'),(20,'CAK','Akron-Canton, OH - CAK'),(21,'CLE','Cleveland, OH - CLE'),(22,'CMH','Columbus, OH - CMH'),(23,'CRP','Corpus Christi, TX - CRP'),(24,'DAL','Dallas (Love Field), TX - DAL'),(25,'DAY','Dayton, OH - DAY'),(26,'DEN','Denver, CO - DEN'),(27,'DSM','Des Moines, IA - DSM'),(28,'DTW','Detroit, MI - DTW'),(29,'ELP','El Paso, TX - ELP'),(30,'FNT','Flint, MI - FNT'),(31,'RSW','Ft. Myers, FL - RSW'),(32,'GRR','Grand Rapids, MI - GRR'),(33,'GSP','Greenville/Spartanburg, SC - GSP'),(34,'HRL','Harlingen, TX - HRL'),(35,'BDL','Hartford, CT - BDL'),(36,'HOU','Houston (Hobby), TX - HOU'),(37,'IND','Indianapolis, IN - IND'),(38,'JAX','Jacksonville, FL - JAX'),(39,'MCI','Kansas City, MO - MCI'),(40,'LAS','Las Vegas, NV - LAS'),(41,'LIR','Liberia, Costa Rica - LIR'),(42,'LIT','Little Rock, AR - LIT'),(43,'LOS','[Los Angeles Area:]'),(44,'BUR','Burbank, CA - BUR'),(45,'LAX','Los Angeles, CA - LAX'),(46,'SDF','Louisville, KY - SDF'),(47,'LBB','Lubbock, TX - LBB'),(48,'MHT','Manchester, NH - MHT'),(49,'MEM','Memphis, TN - MEM'),(50,'MEX','Mexico City, Mexico - MEX'),(51,'MMA','[Miami Area:]'),(52,'FLL','Ft. Lauderdale, FL - FLL'),(53,'MAF','Midland/Odessa, TX - MAF'),(54,'MKE','Milwaukee, WI - MKE'),(55,'MSP','Minneapolis/St. Paul (Terminal 2), MN - MSP'),(56,'MBJ','Montego Bay, Jamaica - MBJ'),(57,'BNA','Nashville, TN - BNA'),(58,'NAS','Nassau, Bahamas - NAS'),(59,'MSY','New Orleans, LA - MSY'),(60,'NWY','[New York Area:]'),(61,'ISP','Long Island/Islip, NY - ISP'),(62,'LGA','New York (LaGuardia), NY - LGA'),(63,'EWR','New York/Newark, NJ - EWR'),(64,'ORF','Norfolk, VA - ORF'),(65,'NFB','[Northwest Florida Beaches Area:]'),(66,'OKC','Oklahoma City, OK - OKC'),(67,'OMA','Omaha, NE - OMA'),(68,'ONT','Ontario/LA, CA - ONT'),(69,'SNA','Orange County/Santa Ana, CA - SNA'),(70,'MCO','Orlando, FL - MCO'),(71,'ECP','Panama City Beach, FL - ECP'),(72,'PNS','Pensacola, FL - PNS'),(73,'PHL','Philadelphia, PA - PHL'),(74,'PHX','Phoenix, AZ - PHX'),(75,'PIT','Pittsburgh, PA - PIT'),(76,'PDX','Portland, OR - PDX'),(77,'PWM','Portland, ME - PWM'),(78,'PVD','Providence, RI - PVD'),(79,'PVR','Puerto Vallarta, MX - PVR'),(80,'PUJ','Punta Cana, DR - PUJ'),(81,'RDU','Raleigh/Durham, NC - RDU'),(82,'RNO','Reno/Tahoe, NV - RNO'),(83,'RIC','Richmond, VA - RIC'),(84,'ROC','Rochester, NY - ROC'),(85,'SMF','Sacramento, CA - SMF'),(86,'SLC','Salt Lake City, UT - SLC'),(87,'SAT','San Antonio, TX - SAT'),(88,'SAN','San Diego, CA - SAN'),(89,'SFC','[San Francisco Area:]'),(90,'OAK','Oakland, CA - OAK'),(91,'SFO','San Francisco, CA - SFO'),(92,'SJC','San Jose, CA - SJC'),(93,'SJO','San Jose, Costa Rica - SJO'),(94,'SJU','San Juan, PR - SJU'),(95,'SEA','Seattle/Tacoma, WA - SEA'),(96,'GEG','Spokane, WA - GEG'),(97,'STL','St. Louis, MO - STL'),(98,'TPA','Tampa, FL - TPA'),(99,'TUS','Tucson, AZ - TUS'),(100,'TUL','Tulsa, OK - TUL'),(101,'WDC','[Washington, D.C. Area:]'),(102,'BWI','Baltimore/Washington, MD - BWI'),(103,'IAD','Washington (Dulles), DC - IAD'),(104,'DCA','Washington (Reagan National), DC - DCA'),(105,'PBI','West Palm Beach, FL - PBI'),(106,'ICT','Wichita, KS - ICT');
/*!40000 ALTER TABLE `AIRPORTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UPCOMING_FLIGHTS`
--

DROP TABLE IF EXISTS `UPCOMING_FLIGHTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UPCOMING_FLIGHTS` (
  `UPCOMING_FLIGHT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `CONFIRMATION_NUM` varchar(6) COLLATE utf8_unicode_ci NOT NULL,
  `FIRST_NAME` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `LAST_NAME` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `EMAIL` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `DEPART_AIRPORT_CODE` varchar(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ARRIVE_AIRPORT_CODE` varchar(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `DEPART_DATE` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `DEPART_TIME` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ARRIVE_TIME` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
  `FLIGHT_NUM` varchar(9) COLLATE utf8_unicode_ci DEFAULT NULL,
  `FARE_LABEL` varchar(7) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'DOLLARS',
  `FARE_PRICE` int(10) NOT NULL DEFAULT '0',
  `FARE_TYPE` varchar(15) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'Wanna Get Away',
  `LAST_ALERT` timestamp NULL DEFAULT NULL,
  `SUBMISSION_DATE` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`UPCOMING_FLIGHT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=100010 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='UPCOMING FLIGHTS';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UPCOMING_FLIGHTS`
--

LOCK TABLES `UPCOMING_FLIGHTS` WRITE;
/*!40000 ALTER TABLE `UPCOMING_FLIGHTS` DISABLE KEYS */;
INSERT INTO `UPCOMING_FLIGHTS` VALUES (100000,'8ABYGC','Lorenzo','Javier','9252007284@vtext.com','SJC','PHX','10/02/2015','8:05 PM','9:50 PM','179','POINTS',4291,'Wanna Get Away',NULL,'2015-09-13 03:35:24'),(100001,'8ABYGC','Lorenzo','Javier','9252007284@vtext.com','PHX','SJC','10/06/2015','5:40 AM','7:35 AM','2787','POINTS',2989,'Wanna Get Away',NULL,'2015-09-13 03:35:24'),(100002,'HHGRHL','Lorenzo','Javier','9252007284@vtext.com','SJC','ONT','10/30/2015','8:20 PM','9:30 PM','2953','POINTS',6798,'Wanna Get Away',NULL,'2015-09-13 03:35:24'),(100003,'HN9RRZ','Lorenzo','Javier','9252007284@vtext.com','LAX','SJC','11/02/2015','8:45 AM','9:55 AM','1147','POINTS',2924,'Wanna Get Away',NULL,'2015-09-13 03:35:24'),(100004,'832STR','Lorenzo','Javier','9252007284@vtext.com','SJC','PHX','11/04/2015','6:35 AM','9:20 AM','539','POINTS',2989,'Wanna Get Away',NULL,'2015-09-13 03:35:24'),(100005,'832STR','Lorenzo','Javier','9252007284@vtext.com','PHX','SJC','11/08/2015','8:40 PM','9:35 PM','1117','POINTS',8459,'Wanna Get Away',NULL,'2015-09-13 03:35:24'),(100006,'8J9T7V','Danielle','Gonzalez','9095698490@txt.att.net','ONT','SJC','09/03/2015','6:10 AM','7:20 AM','2964','DOLLARS',56,'Wanna Get Away',NULL,'2015-09-13 03:35:24'),(100007,'8J9T7V','Danielle','Gonzalez','9095698490@txt.att.net','SJC','ONT','09/09/2015','8:20 PM','9:30 PM','2953','DOLLARS',58,'Wanna Get Away',NULL,'2015-09-13 03:35:24'),(100008,'H9CRR8','Giovanni','Javier','9257856233@vtext.com','OAK','ONT','10/30/2015','8:40 AM','9:55 AM','2751','POINTS',3542,'Wanna Get Away',NULL,'2015-09-13 03:35:24'),(100009,'H38RR6','Giovanni','Javier','9257856233@vtext.com','LAX','OAK','11/02/2015','9:15 AM','10:30 AM','2906','POINTS',2924,'Wanna Get Away',NULL,'2015-09-13 03:35:24');
/*!40000 ALTER TABLE `UPCOMING_FLIGHTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WIRELESS_CARRIERS`
--

DROP TABLE IF EXISTS `WIRELESS_CARRIERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WIRELESS_CARRIERS` (
  `WIRELESS_CARRIER_ID` int(11) NOT NULL AUTO_INCREMENT,
  `CARRIER_NAME` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `CARRIER_TEXT_EMAIL` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`WIRELESS_CARRIER_ID`),
  UNIQUE KEY `CARRIER_NAME` (`CARRIER_NAME`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='WIRELESS CARRIERS';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WIRELESS_CARRIERS`
--

LOCK TABLES `WIRELESS_CARRIERS` WRITE;
/*!40000 ALTER TABLE `WIRELESS_CARRIERS` DISABLE KEYS */;
INSERT INTO `WIRELESS_CARRIERS` VALUES (1,'Alltel','@message.alltel.com'),(2,'AT&T','@txt.att.net'),(3,'Boost Mobile','@myboostmobile.com'),(4,'Cricket Wireless','@sms.mycricket.com'),(5,'MetroPCS','@MyMetroPcs.com'),(6,'Nextel','@messaging.nextel.com'),(7,'Sprint','@messaging.sprintpcs.com'),(8,'T-Mobile','@tmomail.net'),(9,'Ting','@message.ting.com'),(10,'U.S. Cellular','@email.uscc.net'),(11,'Verizon Wireless','@vtext.com'),(12,'Virgin Mobile','@vmobl.com');
/*!40000 ALTER TABLE `WIRELESS_CARRIERS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-12 21:14:42
