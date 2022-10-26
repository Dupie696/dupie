import jinja2


class ttsBatchLoad():
    def dtocleaner(self, xdto):
        for idx, mylist in enumerate(xdto):
            for k, v in mylist.items():
                if isinstance(v, str):
                    if v.find('"')!=-1:
                        xdto[idx][k] = v.replace('"',r'\"')
                    if v.find("'")!=-1:
                        xdto[idx][k] = v.replace("'",r"\'")
        return xdto

    def __init__(self, isTest=False):
        if isTest:
            import sys
            sys.path.insert(0, "/var/www/wsgi/dupie/src")

            import apis.databases

            self.connector = apis.databases.mysql_database_connector()
            
    def inserttsbatchload(self, xdto):
        query =     """INSERT INTO DUPIE.TTSBATCHLOAD
                        (UID, VOCABULARY_INDEX, LANG1, LANG2, VOCAB1, VOCAB2)
                        VALUES(%(UID)s, %(VOCABULARY_INDEX)s, '%(LANG1)s', '%(LANG2)s', '%(VOCAB1)s', '%(VOCAB2)s');""" % xdto
        return self.connector.update(query)   



    def processTTSTextBoxes(self,pre_dto):
        list0 = pre_dto['data'][0].split("\r\n")
        list1 = pre_dto['data'][1].split("\r\n")
        list2 = pre_dto['data'][2].split("\r\n")

        mylist = []

        for i, (a,b,c) in enumerate(zip(list0,list1,list2)):
            mylist.append({
                "UID":101,
                "VOCABULARY_INDEX":a,
                "VOCAB1":b,
                "VOCAB2":c,
                "LANG1":"en",
                "LANG2":"es"
            })

        return self.dtocleaner(mylist)



    def jinjaRender(self,doc,dto):
        return self.getTTSTemplate(doc).render(dto=dto)


    def getTTSTemplate(self, document):
        file_loader = jinja2.FileSystemLoader(
            [
                "/var/www/wsgi/dupie/template/ttsbatchload"
            ]
            
            )
        env = jinja2.Environment(loader=file_loader)
        template = env.get_template(document)
        return template

    def returnVBSTTSfile(self,pre_dto):
        list0 = pre_dto['data'][0].split("\r\n")
        list1 = pre_dto['data'][1].split("\r\n")
        list2 = pre_dto['data'][2].split("\r\n")
        dto = {
                "lang0index":list0,
                "lang1words":list1,
                "lang2words":list2,

                "lang1speaker":0,
                "lang2speaker":2,
                "lang1code":"EN",
                "lang2code":"ES",
                "lang1rate":0.5,
                "lang2rate":0.5,
                }
        return (ttsBatchLoad().jinjaRender("ttsgenerator.vbs.jinj2",dto))        



    def getbatchload(self):
        query =     """SELECT TTSBATCHLOAD_INDEX, UID, VOCABULARY_INDEX, LANG1, LANG2, VOCAB1, VOCAB2 FROM DUPIE.TTSBATCHLOAD;"""
        return self.connector.query(query)   


    def insertDTOintoVocab(self,dto):

        for rdto in dto:
            query = """
    INSERT INTO DUPIE.VOCABULARY
    (VOCABULARY_INDEX, EN, ES, DE, SV, ZH, FR, AR, AR2, ZH2, SYNONYM, JP, JP2, KO, KO2, RU, RU2)
    VALUES(%(VOCABULARY_INDEX)s,'%(VOCAB1)s', '%(VOCAB2)s', '', '', '', '', '', '', '', NULL, '', '', '', '', '', '');
            """ % rdto
            self.connector.update(query)

    def trucatebatchload(self):
        self.connector.update("TRUNCATE DUPIE.TTSBATCHLOAD")


class ttsBatchLoadWeb(ttsBatchLoad):
    def __init__(self):
        self.bottle.route("/ttsbatchload")      (self.checkAuth(self.GET_ttsBatchLoadPage))
        self.bottle.post("/ttsgenerator.vbs")       (self.checkAuth(self.POST_ttsBatchLoadPage))
        self.bottle.route("/ttssoundtest.vbs")       (self.checkAuth(self.FILE_ttsSoundTest))
        super().__init__()



    def GET_ttsBatchLoadPage(self):
        return self.getTemplate('tts_load_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[]
                )

    def FILE_ttsSoundTest(self):
        self.bottle.response.set_header('Content-Type', 'application/vbs')
        self.bottle.response.set_header('Accept-Ranges', 'bytes')
        return self.getTemplate('ttsSoundTest.vbs').render().encode('utf-16le')

    def POST_ttsBatchLoadPage(self):
        index = self.bottle.request.forms.get("INDEX")
        vocab1 = self.bottle.request.forms.get("VOCAB1")
        vocab2 = self.bottle.request.forms.get("VOCAB2")

#        self.bottle.response.set_header('Content-Type', 'binary')
        self.bottle.response.set_header('Content-Type', 'application/vbs')
        self.bottle.response.set_header('Accept-Ranges', 'bytes')

#Accept-Ranges: bytes

        pre_dto = {"data":[index,vocab1,vocab2] }
        vbs_file = ttsBatchLoad().returnVBSTTSfile(pre_dto).encode('utf-16le')

        return(vbs_file)


        # for xdto in (self.processTTSTextBoxes({"data":[index,vocab1,vocab2] })):
        #     self.inserttsbatchload(xdto)

        # return self.getTemplate('tts_load_post.html').render(
        #         DTO={"data":[index,vocab1,vocab2] },
        #         BreadCrumbs=[]
        #         )




  


if __name__ == "__main__":
    import jinja2

    ttsBL = ttsBatchLoad(isTest=True)
    #pre_dto = {'data': ['1100\r\n1101\r\n1102\r\n1103\r\n1104\r\n1105\r\n1106\r\n1107\r\n1108\r\n1109\r\n1110\r\n1111\r\n1112\r\n1113\r\n1114\r\n1115\r\n1116\r\n1117\r\n1118\r\n1119\r\n1120\r\n1121\r\n1122\r\n1123\r\n1124\r\n1125\r\n1126\r\n1127\r\n1128\r\n1129\r\n1130\r\n1131\r\n1132\r\n1133\r\n1134\r\n1135\r\n1136\r\n1137\r\n1138\r\n1139\r\n1140\r\n1141\r\n1142\r\n1143\r\n1144', "Welcome Home\r\nWhere are you?\r\nWhat are you doing?\r\nHow are you?\r\nDid you eat?\r\nwere you sleeping?\r\nwhen will you sleep?\r\nWhat did you eat?\r\nsweet dreams\r\nI remember\r\nI forgot\r\nlets go to sleep\r\nwhen will you get up tomorrow?\r\nI want to sleep now\r\ndid you sleep well?\r\ndon't stay up too late\r\nhow was your sleep?\r\ndid you have any dreams?\r\nwhat did you dream about?\r\nI'm in the bus\r\nare you home?\r\nI just got my coffee\r\nI am playing computer games\r\nI will go play computer games \r\nI want to play computer games \r\nI'm updating our lexicon\r\nI am waiting for you\r\nare you waiting for me?\r\nI have a headache\r\nI am tired \r\nI want that!\r\nI'm at a restaurant \r\nI want to embrace you\r\nI want your embrace\r\nI want to kiss you\r\nI want your kisses\r\nI want to eat fancy food\r\nCan I buy smirnoff?\r\nCan I order Chicken?\r\nCan update my lexicon?\r\nYou are so evil!\r\nDid you do your duolingo today?\r\nDid you study English today?\r\nDid you study Spanish today?\r\nDid you study Law today?", 'Bienvenido a casa\r\n¿Donde está?\r\n¿Que estas haciendo?\r\n¿Cómo estas\r\n¿ya comiste?\r\n¿estabas durmiendo?\r\n¿cuando vas a dormir?\r\n¿Que comistes?\r\nDulces sueños\r\nLo recuerdo\r\nLo olvidé \r\nvamos a dormir\r\n¿A que horas te despertaras mañana?\r\nQuiero dormir ahora \r\n¿Dormistes bien?\r\nNo te duermas demasiado tarde \r\n¿Cómo Dormistes?\r\n¿Tuviste algun sueño?\r\n¿Que soñaste?\r\nEstoy en el autobús \r\n¿Estas en casa?\r\nsolo tuve café \r\nEstoy jugando juegos de video\r\niré a jugar juegos de video\r\nQuiero jugar juegos de video\r\nEstoy actualizado nuestro léxico \r\n¡Te estoy esperando!\r\n¿Me estas esperando?\r\nTengo dolor de cabeza \r\n¡Estoy cansado!\r\n¡Quiero eso!\r\nEstoy en el restaurante \r\n¡Quiero abrazarte!\r\n¡Quiero tus abrazos!\r\n¡Quiero besarte!\r\n¡Quiero tus besos!\r\nQuiero comer comida elegante\r\n¿Puedo comprar smitnoff?\r\n¿Puedo ordenar pollo?\r\n¿puedes actualizar mi léxico?\r\n¡Eres tan malvado!\r\n¿Hiciste tu Duolingo hoy?\r\n¿Estudiaste inglés hoy?\r\n¿Estudiaste español hoy?\r\n¿Estudiaste derecho hoy?']}

    # uploads data to database preloading table
    # for xdto in (ttsBL.processTTSTextBoxes(pre_dto)):
    #     ttsBL.inserttsbatchload(xdto)


    #print (ttsBL.returnVBSTTSfile(pre_dto))

    # sends all the files from bulkload to vocabulary, this needs so much more work!!
    x = ttsBL.dtocleaner(ttsBL.getbatchload())
    ttsBL.insertDTOintoVocab(x)
    ttsBL.trucatebatchload()
    
