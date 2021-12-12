


DROP TABLE IF EXISTS `PROMPT`;
CREATE TABLE `PROMPT` (
  `PROMPT_INDEX` int(11) NOT NULL,
  `LANGUAGE` varchar(5) NOT NULL,
  `PRE` varchar(100) NOT NULL,
  `POST` varchar(100) NOT NULL,
  `PRE2` varchar(100) NOT NULL,
  `POST2` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


LOCK TABLES `PROMPT` WRITE;
INSERT INTO `PROMPT` VALUES (1000,'en','How to say','in English','',''),(1001,'es','¿Cómo se dice','en español?','',''),(1002,'ar','كيف تقول','','kayf taqul',''),(1003,'zh','','用中文怎么说','',''),(1004,'ko','','를 한국어로 말하는 법','','leul hangug-eolo malhaneun beob');
UNLOCK TABLES;


