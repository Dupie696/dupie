import mysql.connector

longtoshort = {
 "english":"en",
 "espanol":"es",
 "nihon":"ja",
 "zhongwen":"zh",
 "hangugeo":"ko"}

class dupiebase:
    def __init__(self):
        # setups database connection
        try:
            self.conn = mysql.connector.connect(
                user="dupie",
                password=open('/var/www/wsgi/dupie/secret/dupiepassword.txt', 'r').read(),
                host="localhost",
                port=3306,
                database="dupie"
            )
        except mysql.connector.errors.Error as err: 
            raise BaseException("DupieBase Constructor Failed!: \n {}".format(err))
      
        self.conn.autocommit = False

    def __del__(self):
        if hasattr("self", "conn"):
            self.conn.connector.close()

    def query(self,query):
        sql_cursor = self.conn.cursor()
        sql_cursor.execute(query)
        sql_field_names = [i[0] for i in sql_cursor.description]

        dto = []

        # reads all the rows and makes it into a dto
        for sql_row_data in sql_cursor:
            # grabs the field names and field data
            field_names = list(sql_field_names)
            field_datas = list(sql_row_data)

            # assigns field names to field data
            zipped_data = zip(field_names,field_datas)

            # packs up for dto as a dict
            _dto = dict(zipped_data)
            dto.append(_dto)
        return dto

    # def getVocabDump(self):
    #     etl = self.query("SELECT * FROM dupie.vocabulary where vocabulary_index = synonym ;")

    #     dto = {}
    #     for row in etl:
    #         dto[row["vocabulary_index"]+1001-3] = {
    #                 'deutsch': row['deutsch'],
    #                 'english': row['english'],
    #                 'espanol': row['espanol'],
    #                 'francais': row['francais'],
    #                 'svenska': row['svenska'],
    #                 'zhongwen': row['zhongwen']
    #             }
    #     return dto

    def getLexiconETL(self,questionlanguage, answerlanguage):
        xdto = {
            "questionlanguage": questionlanguage,
            "answerlanguage": answerlanguage,
            "shortquestionlanguage": longtoshort[questionlanguage],
            "shortanswerlanguage": longtoshort[answerlanguage]
            }
        dto = (
            self.query("SELECT vocabulary_index, %(questionlanguage)s ""question"", %(answerlanguage)s ""answer"" FROM dupie.vocabulary where vocabulary_index = synonym and %(questionlanguage)s<>'' and %(answerlanguage)s<>'';" % xdto )
        )

        for x in range(0, len(dto)):
            xdto["index"] = dto[x]["vocabulary_index"]

            dto[x]["answer_audio"] = "%(index)s-%(shortanswerlanguage)s.mp3" % xdto
            dto[x]["question_audio"] = "%(index)s-%(shortquestionlanguage)s.mp3" % xdto

        return dto

    def getQuestionFormat(self,answerlanguage):
        dto = {"answerlanguage": answerlanguage}

        dto.update(
            self.query("SELECT pre, post FROM dupie.PROMPT where LANGUAGE = '%(answerlanguage)s';" % dto)[0]
        )

        dto.update(
            {
                "pre_audio": "%(answerlanguage)s-%(answerlanguage)s-1.mp3" % dto,
                "post_audio": "%(answerlanguage)s-%(answerlanguage)s-2.mp3" % dto
            }
        )
        return dto

    def update(self,query):
      sql_cursor = self.conn.cursor()
      sql_cursor.execute(query)
      self.conn.commit()


    def SaveQuestions(self, sessionID, UID,dto):
        xdto = {
            "sessionID": sessionID,
            "UID": UID,
            }

        for x in range(0, len(dto)):
            dto[x].update(xdto)
            dto[x].update({"QUIZQUESTION_INDEX":x})
            dto[x] =  {k.upper(): v for k, v in dto[x].items()}


            query = """INSERT INTO dupie.QUESTIONS
                    (SESSIONID, UID, QUESTION, QUESTION_AUDIO, ANSWER, ANSWER_AUDIO, VOCABULARY_INDEX,QUIZQUESTION_INDEX)
                VALUES 
                (%(SESSIONID)s, %(UID)s, '%(QUESTION)s', '%(QUESTION_AUDIO)s', '%(ANSWER)s', '%(ANSWER_AUDIO)s', '%(VOCABULARY_INDEX)s',%(QUIZQUESTION_INDEX)s);""" % dto[x]
            self.update(query)


    def SaveAnswers(self, sessionID, shuffle, quizquestion_index, dto,mixes):
        xdto = {
            "sessionID": sessionID,
            "SHUFFLE": shuffle,
            "QUIZQUESTION_INDEX":quizquestion_index,
            "QUIZANSWERANIMATION_INDEX":mixes
            }
        for x in range(0, len(dto)):
            dto[x].update(xdto)
            dto[x].update({"QUIZANSWER_INDEX":x})
            dto[x] =  {k.upper(): v for k, v in dto[x].items()}

            query = """INSERT INTO dupie.ANSWERS
    (SESSIONID, VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO,QUIZQUESTION_INDEX,QUIZANSWER_INDEX,QUIZANSWERANIMATION_INDEX)
    VALUES(%(SESSIONID)s, %(VOCABULARY_INDEX)s, %(SHUFFLE)s, '%(ANSWER)s', '%(ANSWER_AUDIO)s',%(QUIZQUESTION_INDEX)s,%(QUIZANSWER_INDEX)s,%(QUIZANSWERANIMATION_INDEX)s);""" % dto[x]
#            print (query)
            self.update(query)

    def getSessionInfo(self,ID):
        dto = self.query("""SELECT USERSESSIONS_INDEX, UID, FRIENDLYNAME, SESSIONID, LANG_QUESTION, LANG_ANSWER, QUESTION_INDEX, QUESTIONS, ANSWERS, SHUFFLES
FROM dupie.USERSESSIONS where SESSIONID = %s; 
""" % ID)
        return dto[0]


    def getQuestionList(self,ID):
        dto = self.query(""" SELECT SESSIONID, UID, QUESTION, QUESTION_AUDIO, ANSWER, ANSWER_AUDIO, VOCABULARY_INDEX, QUIZQUESTION_INDEX
FROM dupie.QUESTIONS
        where SESSIONID = %s; 
""" % ID)
        return dto

    def getAnswerList(self,ID):
#        numberofanswers = self.getSessionInfo(ID)["ANSWERS"]
        numberofquestions = self.getSessionInfo(ID)["QUESTIONS"]

        _dto = self.query("""
        SELECT SESSIONID, VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO, QUIZQUESTION_INDEX, QUIZANSWER_INDEX
FROM dupie.ANSWERS
        where SHUFFLE = 0 and SESSIONID = %s; 
""" % ID)

        dto = [[] for i in range(numberofquestions)]

        for x in _dto:
           dto[x["QUIZQUESTION_INDEX"]].append(x)


        return dto

    def getAnswerListAnimation(self,ID):
        numberofquestions = self.getSessionInfo(ID)["QUESTIONS"]
        numberofshuffles = self.getSessionInfo(ID)["SHUFFLES"]

        _dto = self.query("""
        SELECT SESSIONID, VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO, QUIZQUESTION_INDEX, QUIZANSWER_INDEX,QUIZANSWERANIMATION_INDEX
FROM dupie.ANSWERS
        where SHUFFLE = 1 and SESSIONID = %s; 
        """ % ID)

        dto = [[] for i in range(numberofquestions)]
        dto = [        [[] for i in range(numberofshuffles)]  for i in range(numberofquestions)]

        for x in _dto:
           dto[x["QUIZQUESTION_INDEX"]][x["QUIZANSWERANIMATION_INDEX"]].append(x)
        #    print (x["QUIZQUESTION_INDEX"])

        return dto

if __name__ == "__main__":
   a = dupiebase()
   import pprint
   #print (pprint.pformat(a.getQuestionFormat("zh")))   
   #print (pprint.pformat(a.getLexiconETL("english","zhongwen")))   

#    print(pprint.pformat(a.getVocabDump()))
#    counter = 1000
#    for a in a.getVocabDump().values():
#        counter= counter+1
# #       print ('"%s",' % a['espanol']),
# #       print ('"%s-es.mp3",' % counter),
#        #print ('say %s -  %s ' % (counter,a['svenska'])),
#    a = dupiebase()
#    import pprint
#    counter = 1000
#    for a in a.getVocabDump().values():
#        counter= counter+1
#        print (' %s -  %s ' % (counter,a['english'])),
   print(pprint.pformat(a.getAnswerListAnimation(1001)))
