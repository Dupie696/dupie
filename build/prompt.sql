--
-- Table structure for table `prompt`
--

DROP TABLE IF EXISTS `prompt`;

CREATE TABLE `prompt` (
  `prompt_index` int(11) NOT NULL,
  `language` varchar(5) NOT NULL,
  `pre` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pre2` varchar(100) NOT NULL,
  `post2` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `prompt`
--

LOCK TABLES `prompt` WRITE;

INSERT INTO `prompt` VALUES (1000,'en','How to say','in English','',''),(1001,'es','¿Cómo se dice','en español?','',''),(1002,'ar','كيف تقول','','kayf taqul','');

UNLOCK TABLES;