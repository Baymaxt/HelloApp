-- MySQL dump 10.13  Distrib 5.7.18, for Win64 (x86_64)
--
-- Host: localhost    Database: helloapp
-- ------------------------------------------------------
-- Server version	5.7.18-log

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
-- Table structure for table `authentications`
--

DROP TABLE IF EXISTS `authentications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authentications` (
  `uid` varchar(20) NOT NULL,
  `authentication_name` varchar(20) DEFAULT NULL,
  KEY `uid` (`uid`),
  CONSTRAINT `authentications_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentications`
--

LOCK TABLES `authentications` WRITE;
/*!40000 ALTER TABLE `authentications` DISABLE KEYS */;
/*!40000 ALTER TABLE `authentications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blacklists`
--

DROP TABLE IF EXISTS `blacklists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blacklists` (
  `uid` varchar(20) NOT NULL,
  `black_uid` varchar(20) NOT NULL,
  `mutual_black` tinyint(1) DEFAULT NULL,
  KEY `uid` (`uid`),
  CONSTRAINT `blacklists_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blacklists`
--

LOCK TABLES `blacklists` WRITE;
/*!40000 ALTER TABLE `blacklists` DISABLE KEYS */;
/*!40000 ALTER TABLE `blacklists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coin_orders`
--

DROP TABLE IF EXISTS `coin_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coin_orders` (
  `oid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(20) NOT NULL,
  `from_uid` varchar(20) NOT NULL,
  `coin_figure` int(11) NOT NULL,
  `order_time` datetime DEFAULT NULL,
  PRIMARY KEY (`oid`),
  KEY `uid` (`uid`),
  CONSTRAINT `coin_orders_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coin_orders`
--

LOCK TABLES `coin_orders` WRITE;
/*!40000 ALTER TABLE `coin_orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `coin_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collections`
--

DROP TABLE IF EXISTS `collections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `collections` (
  `pid` int(11) NOT NULL,
  `uid` varchar(20) NOT NULL,
  `collect_time` datetime DEFAULT NULL,
  KEY `pid` (`pid`),
  KEY `uid` (`uid`),
  CONSTRAINT `collections_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `posts` (`pid`),
  CONSTRAINT `collections_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collections`
--

LOCK TABLES `collections` WRITE;
/*!40000 ALTER TABLE `collections` DISABLE KEYS */;
/*!40000 ALTER TABLE `collections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `cid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `uid` varchar(20) DEFAULT NULL,
  `comment_time` datetime DEFAULT NULL,
  `comment_content` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cid`),
  KEY `pid` (`pid`),
  KEY `uid` (`uid`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `posts` (`pid`),
  CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coupons`
--

DROP TABLE IF EXISTS `coupons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coupons` (
  `uid` varchar(20) NOT NULL,
  `reach` int(11) NOT NULL,
  `subtract` int(11) NOT NULL,
  `indate` datetime DEFAULT NULL,
  KEY `uid` (`uid`),
  CONSTRAINT `coupons_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupons`
--

LOCK TABLES `coupons` WRITE;
/*!40000 ALTER TABLE `coupons` DISABLE KEYS */;
/*!40000 ALTER TABLE `coupons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(20) NOT NULL,
  `post_category` int(11) NOT NULL,
  `comment_amount` int(11) DEFAULT '0',
  `post_time` datetime DEFAULT NULL,
  `forward_amount` int(11) DEFAULT NULL,
  `origin` int(11) DEFAULT NULL,
  PRIMARY KEY (`pid`),
  UNIQUE KEY `pid` (`pid`),
  KEY `uid` (`uid`),
  CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts_content`
--

DROP TABLE IF EXISTS `posts_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts_content` (
  `pid` int(11) NOT NULL,
  `content` varchar(255) DEFAULT NULL,
  KEY `pid` (`pid`),
  CONSTRAINT `posts_content_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `posts` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts_content`
--

LOCK TABLES `posts_content` WRITE;
/*!40000 ALTER TABLE `posts_content` DISABLE KEYS */;
/*!40000 ALTER TABLE `posts_content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presents`
--

DROP TABLE IF EXISTS `presents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `presents` (
  `uid` varchar(20) NOT NULL,
  `from_uid` varchar(20) NOT NULL,
  `present_category` varchar(20) DEFAULT NULL,
  `receive_time` datetime DEFAULT NULL,
  `is_exchange` tinyint(1) DEFAULT NULL,
  KEY `uid` (`uid`),
  CONSTRAINT `presents_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presents`
--

LOCK TABLES `presents` WRITE;
/*!40000 ALTER TABLE `presents` DISABLE KEYS */;
/*!40000 ALTER TABLE `presents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presents_categories`
--

DROP TABLE IF EXISTS `presents_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `presents_categories` (
  `present_category` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presents_categories`
--

LOCK TABLES `presents_categories` WRITE;
/*!40000 ALTER TABLE `presents_categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `presents_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sounds_content`
--

DROP TABLE IF EXISTS `sounds_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sounds_content` (
  `pid` int(11) NOT NULL,
  `sound` varchar(255) DEFAULT NULL,
  KEY `pid` (`pid`),
  CONSTRAINT `sounds_content_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `posts` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sounds_content`
--

LOCK TABLES `sounds_content` WRITE;
/*!40000 ALTER TABLE `sounds_content` DISABLE KEYS */;
/*!40000 ALTER TABLE `sounds_content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscriptions`
--

DROP TABLE IF EXISTS `subscriptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscriptions` (
  `uid` varchar(20) NOT NULL,
  `following_uid` varchar(20) NOT NULL,
  `mutual_following` tinyint(1) DEFAULT NULL,
  KEY `uid` (`uid`),
  CONSTRAINT `subscriptions_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscriptions`
--

LOCK TABLES `subscriptions` WRITE;
/*!40000 ALTER TABLE `subscriptions` DISABLE KEYS */;
/*!40000 ALTER TABLE `subscriptions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tags` (
  `uid` varchar(20) DEFAULT NULL,
  `tag_name` varchar(20) DEFAULT NULL,
  KEY `uid` (`uid`),
  CONSTRAINT `tags_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction_details`
--

DROP TABLE IF EXISTS `transaction_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction_details` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(20) NOT NULL,
  `is_withdraw` tinyint(1) NOT NULL,
  `transaction_figure` int(11) NOT NULL,
  `transaction_time` datetime DEFAULT NULL,
  PRIMARY KEY (`tid`),
  KEY `uid` (`uid`),
  CONSTRAINT `transaction_details_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_details`
--

LOCK TABLES `transaction_details` WRITE;
/*!40000 ALTER TABLE `transaction_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaction_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `uid` varchar(20) NOT NULL,
  `username` varchar(50) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` tinyint(1) DEFAULT '1',
  `portrait` varchar(255) DEFAULT NULL,
  `real_name` varchar(50) DEFAULT NULL,
  `ID_number` varchar(50) DEFAULT NULL,
  `following_amount` int(11) DEFAULT NULL,
  `follower_amount` int(11) DEFAULT NULL,
  `mutual_follow_amount` int(11) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `uid` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('123123','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'pbkdf2_sha256$150000$FFGCXbxt2gep$rLwgtIeOOF+1Ts6El7fQQGuD5z+kEjtXolI9jOvENgs=');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `votes`
--

DROP TABLE IF EXISTS `votes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `votes` (
  `pid` int(11) NOT NULL,
  `topic` varchar(255) DEFAULT NULL,
  `option1` varchar(100) DEFAULT NULL,
  `option1_amount` int(11) DEFAULT '0',
  `option2` varchar(100) DEFAULT NULL,
  `option2_amount` int(11) DEFAULT '0',
  `option3` varchar(100) DEFAULT NULL,
  `option3_amount` int(11) DEFAULT '0',
  `option4` varchar(100) DEFAULT NULL,
  `option4_amount` int(11) DEFAULT '0',
  `option5` varchar(100) DEFAULT NULL,
  `option5_amount` int(11) DEFAULT '0',
  `option6` varchar(100) DEFAULT NULL,
  `option6_amount` int(11) DEFAULT '0',
  KEY `pid` (`pid`),
  CONSTRAINT `votes_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `posts` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `votes`
--

LOCK TABLES `votes` WRITE;
/*!40000 ALTER TABLE `votes` DISABLE KEYS */;
/*!40000 ALTER TABLE `votes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wallets`
--

DROP TABLE IF EXISTS `wallets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wallets` (
  `wid` int(11) NOT NULL,
  `uid` varchar(20) NOT NULL,
  `balance` int(11) DEFAULT '0',
  `coin_amount` int(11) DEFAULT '0',
  `can_withdraw` int(11) DEFAULT '0',
  `coupon_amount` int(11) DEFAULT '0',
  PRIMARY KEY (`wid`),
  KEY `uid` (`uid`),
  CONSTRAINT `wallets_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wallets`
--

LOCK TABLES `wallets` WRITE;
/*!40000 ALTER TABLE `wallets` DISABLE KEYS */;
/*!40000 ALTER TABLE `wallets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-08 14:56:37
