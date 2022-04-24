


DROP TABLE IF EXISTS `QUESTIONS`;
CREATE TABLE `QUESTIONS` (
  `QUESTIONS_INDEX` int(11) NOT NULL AUTO_INCREMENT,
  `USERSESSIONS_INDEX` int(11) NOT NULL,
  `UID` int(11) NOT NULL,
  `QUESTION` varchar(100) NOT NULL,
  `QUESTION_AUDIO` varchar(100) NOT NULL,
  `ANSWER` varchar(100) NOT NULL,
  `ANSWER_AUDIO` varchar(100) NOT NULL,
  `VOCABULARY_INDEX` int(11) NOT NULL,
  `QUIZQUESTION_NUMBER` int(11) NOT NULL,
  PRIMARY KEY (`QUESTIONS_INDEX`)
) ENGINE=InnoDB AUTO_INCREMENT=537 DEFAULT CHARSET=utf8;


LOCK TABLES `QUESTIONS` WRITE;
INSERT INTO `QUESTIONS` VALUES (112,1001,101,'What','1010-en.mp3','什么','1010-zh.mp3',1010,0),(113,1001,101,'Thank you','1004-en.mp3','谢谢','1004-zh.mp3',1004,1),(114,1001,101,'No','1008-en.mp3','不','1008-zh.mp3',1008,2),(497,1101,101,'Who','1009-EN.mp3','Quién','1009-ES.mp3',1009,0),(498,1101,101,'Sorry','1005-EN.mp3','Lo siento','1005-ES.mp3',1005,1),(499,1101,101,'Bless you','1006-EN.mp3','Salud','1006-ES.mp3',1006,2),(500,1101,101,'Please','1003-EN.mp3','Por favor','1003-ES.mp3',1003,3),(501,1101,101,'What','1010-EN.mp3','Qué','1010-ES.mp3',1010,4),(502,1101,101,'Hello','1001-EN.mp3','Hola','1001-ES.mp3',1001,5),(503,1101,101,'Yes','1007-EN.mp3','Sí','1007-ES.mp3',1007,6),(504,1101,101,'No','1008-EN.mp3','No','1008-ES.mp3',1008,7),(505,1101,101,'Thank you','1004-EN.mp3','Gracias','1004-ES.mp3',1004,8),(506,1101,101,'Goodbye','1002-EN.mp3','Adiós','1002-ES.mp3',1002,9),(507,1102,101,'Hello','1001-EN.mp3','مرحبًا ','1001-AR.mp3',1001,0),(508,1102,101,'Thank you','1004-EN.mp3','شكرا لك ','1004-AR.mp3',1004,1),(509,1102,101,'Yes','1007-EN.mp3',' نعم ','1007-AR.mp3',1007,2),(510,1102,101,'Why','1011-EN.mp3','لماذا ','1011-AR.mp3',1011,3),(511,1102,101,'Sorry','1005-EN.mp3','آسف ','1005-AR.mp3',1005,4),(512,1102,101,'Where','1012-EN.mp3','اين  ','1012-AR.mp3',1012,5),(513,1102,101,'Goodbye','1002-EN.mp3','إلي إلقاء ','1002-AR.mp3',1002,6),(514,1102,101,'What','1010-EN.mp3','ما','1010-AR.mp3',1010,7),(515,1102,101,'Please','1003-EN.mp3','من فضلك ','1003-AR.mp3',1003,8),(516,1102,101,'No','1008-EN.mp3','لا ','1008-AR.mp3',1008,9),(517,1103,101,'Please','1003-EN.mp3','제발','1003-KO.mp3',1003,0),(518,1103,101,'Why','1011-EN.mp3','왜','1011-KO.mp3',1011,1),(519,1103,101,'No','1008-EN.mp3','아니요','1008-KO.mp3',1008,2),(520,1103,101,'Hello','1001-EN.mp3','안녕','1001-KO.mp3',1001,3),(521,1103,101,'Yes','1007-EN.mp3','네','1007-KO.mp3',1007,4),(522,1103,101,'Thank you','1004-EN.mp3','감사합니다','1004-KO.mp3',1004,5),(523,1103,101,'Sorry','1005-EN.mp3','미안합니다','1005-KO.mp3',1005,6),(524,1103,101,'Where','1012-EN.mp3','어디에','1012-KO.mp3',1012,7),(525,1103,101,'What','1010-EN.mp3','무엇이','1010-KO.mp3',1010,8),(526,1103,101,'Who','1009-EN.mp3','누가','1009-KO.mp3',1009,9),(527,1104,101,'What','1010-EN.mp3','Что','1010-RU.mp3',1010,0),(528,1104,101,'Bless you','1006-EN.mp3','Будь здоров','1006-RU.mp3',1006,1),(529,1104,101,'Goodbye','1002-EN.mp3','Пока','1002-RU.mp3',1002,2),(530,1104,101,'Hello','1001-EN.mp3','Привет','1001-RU.mp3',1001,3),(531,1104,101,'Why','1011-EN.mp3','Почему','1011-RU.mp3',1011,4),(532,1104,101,'Who','1009-EN.mp3','Кто','1009-RU.mp3',1009,5),(533,1104,101,'Where','1012-EN.mp3','Где','1012-RU.mp3',1012,6),(534,1104,101,'Please','1003-EN.mp3','Пожалуйста','1003-RU.mp3',1003,7),(535,1104,101,'Thank you','1004-EN.mp3','Спасибо','1004-RU.mp3',1004,8),(536,1104,101,'Yes','1007-EN.mp3','Да','1007-RU.mp3',1007,9);
UNLOCK TABLES;


