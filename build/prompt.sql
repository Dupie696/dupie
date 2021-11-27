


DROP TABLE IF EXISTS `prompt`;
CREATE TABLE `prompt` (
  `prompt_index` int(11) NOT NULL,
  `language` varchar(5) NOT NULL,
  `pre` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pre2` varchar(100) NOT NULL,
  `post2` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


LOCK TABLES `prompt` WRITE;
INSERT INTO `prompt` VALUES (1000,'en','How to say','in English','',''),(1001,'es','¿Cómo se dice','en español?','',''),(1002,'ar','كيف تقول','','kayf taqul',''),(1003,'zh','','用中文怎么说','',''),(1004,'ko','','를 한국어로 말하는 법','','leul hangug-eolo malhaneun beob');
UNLOCK TABLES;


