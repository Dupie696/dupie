


DROP TABLE IF EXISTS `vocabulary`;
CREATE TABLE `vocabulary` (
  `vocabulary_index` int(11) NOT NULL AUTO_INCREMENT,
  `english` varchar(100) NOT NULL,
  `espanol` varchar(100) NOT NULL,
  `deutsch` varchar(100) NOT NULL,
  `svenska` varchar(100) NOT NULL,
  `zhongwen` varchar(100) NOT NULL,
  `francais` varchar(100) NOT NULL,
  `earab` varchar(100) NOT NULL,
  `earab2` varchar(100) NOT NULL,
  `zhongwen2` varchar(100) NOT NULL,
  `synonym` int(11) DEFAULT NULL,
  `nihon` varchar(100) NOT NULL,
  `nihon2` varchar(100) NOT NULL,
  `hangugeo` varchar(100) NOT NULL,
  `hangugeo2` varchar(100) NOT NULL,
  KEY `vocabulary_vocabulary_index_IDX` (`vocabulary_index`,`synonym`,`english`,`deutsch`,`earab`,`earab2`,`espanol`,`francais`,`svenska`,`zhongwen`,`zhongwen2`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10012 DEFAULT CHARSET=utf8;


LOCK TABLES `vocabulary` WRITE;
INSERT INTO `vocabulary` VALUES (1001,'Hello','Hola','Hallo','Hej','你好','Bonjour','مرحبًا ','mrhban','ni3hao3',1001,'こんにちは','Kon\'nichiwa','안녕','annyeong'),(1002,'Goodbye','Adiós','Auf Wiedersehen','Hej då','再见','Au revoir','إلي إلقاء ','\'iilay \'iilqa\'','zai4jian4',1002,'こんばんは','Konbanwa','안녕','annyeong'),(1003,'Please','Por favor','Bitte','Snälla','请','S\'il vous plaît','من فضلك ','min fadlik','qing3',1003,'ねがいいします','Negai ishimasu','제발','jebal'),(1004,'Thank you','Gracias','Danke','Tack','谢谢','Merci','شكرا لك ','shukran lak','xie4xie4',1004,'ありがとう','Arigatō','감사합니다','gamsahabnida'),(1005,'Sorry','Lo siento','Entschuldigung','Ursäkta/Ledsen','不好意思','Pardon','آسف ','asf','bu4hao3yi4si0',1005,'ごめんなさい','Gomen\'nasai','미안합니다','mianhabnida'),(1006,'Bless you','Salud','Gesundheit','Prosit','','None',' بارك الله لك','barak allah lak','',1006,'','','',''),(1007,'Yes','Sí','Ja','Ja','是的','Oui',' نعم ','naeam','shi4de0',1007,'はい','Hai','네','ne'),(1008,'No','No','Nein','nej','不','Non','لا ','la','bu4',1008,'いいえ','Īe','아니요','aniyo'),(1009,'Who','Quién','Wer','Vem','谁','Qui','من ','man','shui2',1009,'だれ','Dare','누가','nuga'),(1010,'What','Qué','Was','Vad','什么','Que','ما','ma','shen2me0',1010,'なに','Nani','무엇이','mueos-i'),(1011,'Why','Por qué','Wieso','Varför','为什么','Pourquoi','لماذا ','limadha','wei4shen2me0',1011,'なぜ','Naze','왜','wae'),(1012,'Where','Dónde','Wo','Var','哪里 ','Où','اين  ','ayn','na3li3',1012,'だれ','Dare','어디에','eodie'),(10010,'What','','','','','','ماذا','madha','',1010,'','','',''),(10005,'Sorry',' ',' ',' ',' ',' ',' ',' ',' ',1005,'ごめん','Gomen','',''),(10007,'Yes',' ',' ',' ',' ',' ',' ',' ',' ',1007,'うん','Un','','');
UNLOCK TABLES;


