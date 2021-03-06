


DROP TABLE IF EXISTS `VOCABULARY`;
CREATE TABLE `VOCABULARY` (
  `VOCABULARY_INDEX` int(11) NOT NULL AUTO_INCREMENT,
  `EN` varchar(100) NOT NULL,
  `ES` varchar(100) NOT NULL,
  `DE` varchar(100) NOT NULL,
  `SV` varchar(100) NOT NULL,
  `ZH` varchar(100) NOT NULL,
  `FR` varchar(100) NOT NULL,
  `AR` varchar(100) NOT NULL,
  `AR2` varchar(100) NOT NULL,
  `ZH2` varchar(100) NOT NULL,
  `SYNONYM` int(11) DEFAULT NULL,
  `JP` varchar(100) NOT NULL,
  `JP2` varchar(100) NOT NULL,
  `KO` varchar(100) NOT NULL,
  `KO2` varchar(100) NOT NULL,
  `RU` varchar(100) NOT NULL,
  `RU2` varchar(100) NOT NULL,
  KEY `vocabulary_vocabulary_index_IDX` (`VOCABULARY_INDEX`,`SYNONYM`,`EN`,`DE`,`AR`,`AR2`,`ES`,`FR`,`SV`,`ZH`,`ZH2`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10012 DEFAULT CHARSET=utf8;


LOCK TABLES `VOCABULARY` WRITE;
INSERT INTO `VOCABULARY` VALUES (1001,'Hello','Hola','Hallo','Hej','你好','Bonjour','مرحبًا ','mrhban','ni3hao3',1001,'こんにちは','Kon\'nichiwa','안녕','annyeong','Привет','Privet'),(1002,'Goodbye','Adiós','Auf Wiedersehen','Hej då','再见','Au revoir','إلي إلقاء ','\'iilay \'iilqa\'','zai4jian4',1002,'こんばんは','Konbanwa','안녕','annyeong','Пока','Poka'),(1003,'Please','Por favor','Bitte','Snälla','请','S\'il vous plaît','من فضلك ','min fadlik','qing3',1003,'ねがいいします','Negai ishimasu','제발','jebal','Пожалуйста','Pozhaluysta'),(1004,'Thank you','Gracias','Danke','Tack','谢谢','Merci','شكرا لك ','shukran lak','xie4xie4',1004,'ありがとう','Arigatō','감사합니다','gamsahabnida','Спасибо','Spasibo'),(1005,'Sorry','Lo siento','Entschuldigung','Ursäkta/Ledsen','不好意思','Pardon','آسف ','asf','bu4hao3yi4si0',1005,'ごめんなさい','Gomen\'nasai','미안합니다','mianhabnida','Прости','Prosti'),(1006,'Bless you','Salud','Gesundheit','Prosit','','None',' بارك الله لك','barak allah lak','',1006,'','','','','Будь здоров','Budʹ zdorov'),(1007,'Yes','Sí','Ja','Ja','是的','Oui',' نعم ','naeam','shi4de0',1007,'はい','Hai','네','ne','Да','Da'),(1008,'No','No','Nein','nej','不','Non','لا ','la','bu4',1008,'いいえ','Īe','아니요','aniyo','Нет','Net'),(1009,'Who','Quién','Wer','Vem','谁','Qui','من ','man','shui2',1009,'だれ','Dare','누가','nuga','Кто','Kto'),(1010,'What','Qué','Was','Vad','什么','Que','ما','ma','shen2me0',1010,'なに','Nani','무엇이','mueos-i','Что','Chto'),(1011,'Why','Por qué','Wieso','Varför','为什么','Pourquoi','لماذا ','limadha','wei4shen2me0',1011,'なぜ','Naze','왜','wae','Почему','Pochemu'),(1012,'Where','Dónde','Wo','Var','哪里 ','Où','اين  ','ayn','na3li3',1012,'だれ','Dare','어디에','eodie','Где','Gde');
UNLOCK TABLES;


