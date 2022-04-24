


DROP TABLE IF EXISTS `PROMPT`;
CREATE TABLE `PROMPT` (
  `PROMPT_INDEX` int(11) NOT NULL,
  `LANGUAGE` varchar(5) NOT NULL,
  `PRE` varchar(100) NOT NULL,
  `POST` varchar(100) NOT NULL,
  `PRE2` varchar(100) NOT NULL,
  `POST2` varchar(100) NOT NULL,
  `PRE_AUDIO` varchar(100) NOT NULL,
  `POST_AUDIO` varchar(100) NOT NULL,
  PRIMARY KEY (`PROMPT_INDEX`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


LOCK TABLES `PROMPT` WRITE;
INSERT INTO `PROMPT` VALUES (1000,'EN','How to say','in English','','','en-en-1.mp3','en-en-2.mp3'),(1001,'ES','¿Cómo se dice','en español?','','','es-es-1.mp3','es-es-2.mp3'),(1002,'AR','كيف تقول','','kayf taqul','','ar-ar-1.mp3','ar-ar-2.mp3'),(1003,'ZH','','用中文怎么说','','yong4 zhong1 wen2 zen3 me5 shuo1','zh-zh-1.mp3','zh-zh-2.mp3'),(1004,'KO','','를 한국어로 말하는 법','','leul hangug-eolo malhaneun beob','ko-ko-1.mp3','ko-ko-2.mp3'),(1005,'RU','Как сказать','на русском','Kak skazat\'','na russkom','ru-ru-1.mp3','ru-ru-2.mp3');
UNLOCK TABLES;


