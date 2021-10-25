--
-- Table structure for table `vocabulary`
--

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
  PRIMARY KEY (`vocabulary_index`)
) ENGINE=InnoDB AUTO_INCREMENT=10011 DEFAULT CHARSET=utf8;

LOCK TABLES `vocabulary` WRITE;

INSERT INTO `vocabulary` VALUES (1001,'Hello','Hola','Hallo','Hej','你好','Bonjour','مرحبًا ','mrhban','ni3hao3',1001),(1002,'Goodbye','Adiós','Auf Wiedersehen','Hej då','再见','Au revoir','إلي إلقاء ','\'iilay \'iilqa\'','zai4jian4',1002),(1003,'Please','Por favor','Bitte','Snälla','请','S\'il vous plaît','من فضلك ','min fadlik','qing3',1003),(1004,'Thank you','Gracias','Danke','Tack','谢谢','Merci','شكرا لك ','shukran lak','xie4xie4',1004),(1005,'Sorry','Lo siento','Entschuldigung','Ursäkta/Ledsen','不好意思','Pardon','آسف ','asf','bu4hao3yi4si0',1005),(1006,'Bless you','Salud','Gesundheit','Prosit','','None',' بارك الله لك','barak allah lak','',1006),(1007,'Yes','Sí','Ja','Ja','是的','Oui',' نعم ','naeam','shi4de0',1007),(1008,'No','No','Nein','nej','不','Non','لا ','la','bu4',1008),(1009,'Who','Quién','Wer','Vem','谁','Qui','من ','man','shui2',1009),(1010,'What','Qué','Was','Vad','什么','Que','ما','ma','shen2me0',1010),(1011,'Why','Por qué','Wieso','Varför','为什么','Pourquoi','لماذا ','limadha','wei4shen2me0',1011),(1012,'Where','Dónde','Wo','Var','哪里 ','Où','اين  ','ayn','na3li3',1012),(10010,'What','','','','','','ماذا','madha','',1010);

UNLOCK TABLES;
