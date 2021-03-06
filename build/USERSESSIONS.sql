


DROP TABLE IF EXISTS `USERSESSIONS`;
CREATE TABLE `USERSESSIONS` (
  `USERSESSIONS_INDEX` int(11) NOT NULL AUTO_INCREMENT,
  `UID` int(11) NOT NULL,
  `FRIENDLYNAME` varchar(100) NOT NULL,
  `LANG_QUESTION` varchar(2) NOT NULL,
  `LANG_ANSWER` varchar(2) NOT NULL,
  `QUIZQUESTION_NUMBER` int(11) NOT NULL,
  `QUESTIONS` int(11) NOT NULL,
  `ANSWERS` int(11) NOT NULL,
  `SHUFFLES` int(11) NOT NULL,
  `STATEMACHINE` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`USERSESSIONS_INDEX`),
  UNIQUE KEY `USERSESSIONS_INDEX` (`USERSESSIONS_INDEX`)
) ENGINE=InnoDB AUTO_INCREMENT=1105 DEFAULT CHARSET=utf8;


LOCK TABLES `USERSESSIONS` WRITE;
INSERT INTO `USERSESSIONS` VALUES (1001,101,'Kelly','EN','ZH',0,3,6,10,'NEWGAME'),(1101,101,'Dupie','EN','ES',-1,10,9,10,'GENERATING'),(1102,101,'Dupie','EN','AR',-1,10,9,10,'GENERATING'),(1103,101,'Dupie','EN','KO',-1,10,9,10,'GENERATING'),(1104,101,'Dupie','EN','RU',-1,10,9,10,'GENERATING');
UNLOCK TABLES;


