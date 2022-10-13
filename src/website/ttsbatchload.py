class ttsBatchLoad():
    def __init__(self):
        self.bottle.route("/ttsbatchload")      (self.checkAuth(self.GET_ttsBatchLoadPage))
        self.bottle.post("/ttsbatchload")       (self.checkAuth(self.POST_ttsBatchLoadPage))
        super().__init__()



    def GET_ttsBatchLoadPage(self):
        return self.getTemplate('tts_load_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[]
                )

    def POST_ttsBatchLoadPage(self):
        index = self.bottle.request.forms.get("INDEX")
        vocab1 = self.bottle.request.forms.get("VOCAB1")
        vocab2 = self.bottle.request.forms.get("VOCAB2")


        return self.getTemplate('tts_load_post.html').render(
                DTO={"data":[index,vocab1,vocab2] },
                BreadCrumbs=[]
                )


if __name__ == "__main__":
    pass

    testdata = {'data': ['1100\r\n1101\r\n1102\r\n1103\r\n1104\r\n1105\r\n1106\r\n1107\r\n1108\r\n1109\r\n1110\r\n1111\r\n1112\r\n1113\r\n1114\r\n1115\r\n1116\r\n1117\r\n1118\r\n1119\r\n1120\r\n1121\r\n1122\r\n1123\r\n1124\r\n1125\r\n1126\r\n1127\r\n1128\r\n1129\r\n1130\r\n1131\r\n1132\r\n1133\r\n1134\r\n1135\r\n1136\r\n1137\r\n1138\r\n1139\r\n1140\r\n1141\r\n1142\r\n1143\r\n1144', "Welcome Home\r\nWhere are you?\r\nWhat are you doing?\r\nHow are you?\r\nDid you eat?\r\nwere you sleeping?\r\nwhen will you sleep?\r\nWhat did you eat?\r\nsweet dreams\r\nI remember\r\nI forgot\r\nlet's go to sleep\r\nwhen will you get up tomorrow?\r\nI want to sleep now\r\ndid you sleep well?\r\ndon't stay up too late\r\nhow was your sleep?\r\ndid you have any dreams?\r\nwhat did you dream about?\r\nI'm in the bus\r\nare you home?\r\nI just got my coffee\r\nI am playing computer games\r\nI will go play computer games \r\nI want to play computer games \r\nI'm updating our lexicon\r\nI am waiting for you\r\nare you waiting for me?\r\nI have a headache\r\nI am tired \r\nI want that!\r\nI'm at a restaurant \r\nI want to embrace you\r\nI want your embrace\r\nI want to kiss you\r\nI want your kisses\r\nI want to eat fancy food\r\nCan I buy smirnoff?\r\nCan I order Chicken?\r\nCan update my lexicon?\r\nYou are so evil!\r\nDid you do your duolingo today?\r\nDid you study English today?\r\nDid you study Spanish today?\r\nDid you study Law today?", 'Bienvenido a casa\r\n¿Donde está?\r\n¿Que estas haciendo?\r\n¿Cómo estas\r\n¿ya comiste?\r\n¿estabas durmiendo?\r\n¿cuando vas a dormir?\r\n¿Que comistes?\r\nDulces sueños\r\nLo recuerdo\r\nLo olvidé \r\nvamos a dormir\r\n¿A que horas te despertaras mañana?\r\nQuiero dormir ahora \r\n¿Dormistes bien?\r\nNo te duermas demasiado tarde \r\n¿Cómo Dormistes?\r\n¿Tuviste algun sueño?\r\n¿Que soñaste?\r\nEstoy en el autobús \r\n¿Estas en casa?\r\nsolo tuve café \r\nEstoy jugando juegos de video\r\niré a jugar juegos de video\r\nQuiero jugar juegos de video\r\nEstoy actualizado nuestro léxico \r\n¡Te estoy esperando!\r\n¿Me estas esperando?\r\nTengo dolor de cabeza \r\n¡Estoy cansado!\r\n¡Quiero eso!\r\nEstoy en el restaurante \r\n¡Quiero abrazarte!\r\n¡Quiero tus abrazos!\r\n¡Quiero besarte!\r\n¡Quiero tus besos!\r\nQuiero comer comida elegante\r\n¿Puedo comprar smitnoff?\r\n¿Puedo ordenar pollo?\r\n¿puedes actualizar mi léxico?\r\n¡Eres tan malvado!\r\n¿Hiciste tu Duolingo hoy?\r\n¿Estudiaste inglés hoy?\r\n¿Estudiaste español hoy?\r\n¿Estudiaste derecho hoy?']}

    list0 = testdata['data'][0].split("\r\n")
    list1 = testdata['data'][1].split("\r\n")
    list2 = testdata['data'][2].split("\r\n")

    print (list0)
    print (list1)
    print (list2)

    mylist = []

    for i, (a,b,c) in enumerate(zip(list0,list1,list2)):
        print(i, a,b,c)
        mylist.append({
            "UID":101,
            "VOCABULARY_INDEX":a,
            "VOCAB1":b,
            "VOCAB2":c,
            "LANG1":"en",
            "LANG2":"es"
        })


    import pprint

    print (pprint.pformat(mylist))

    import sys
    sys.path.insert(0, "/var/www/wsgi/dupie/src")

    import apis.databases

    """INSERT INTO DUPIE.TTSBATCHLOAD
    (UID, VOCABULARY_INDEX, LANG1, LANG2, VOCAB1, VOCAB2)
    VALUES(, 0, '', '', '', '');"""
