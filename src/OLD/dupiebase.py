import mysql.connector
import class_templates.databases

class dupiebase(class_templates.databases.std_database):
    def getSessionInfo(self,ID):
        dto = self.query("""SELECT USERSESSIONS_INDEX, UID, FRIENDLYNAME, SESSIONID, LANG_QUESTION, LANG_ANSWER, QUESTION_INDEX, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE
                            FROM DUPIE.USERSESSIONS WHERE SESSIONID = %s;""" % ID)
        return dto[0]


class OLDSTUFF():
    def getLexiconETL(self,questionlanguage, answerlanguage):
        xdto = {
            "QUESTIONLANGUAGE": questionlanguage,
            "ANSWERLANGUAGE": answerlanguage
            }
        dto = (
            self.query("SELECT VOCABULARY_INDEX, %(QUESTIONLANGUAGE)s ""QUESTION"", %(ANSWERLANGUAGE)s ""ANSWER"" FROM DUPIE.VOCABULARY WHERE VOCABULARY_INDEX = SYNONYM AND %(QUESTIONLANGUAGE)s<>'' AND %(ANSWERLANGUAGE)s<>'';" % xdto )
        )

        for x in range(0, len(dto)):
            xdto["INDEX"] = dto[x]["VOCABULARY_INDEX"]
            dto[x]["ANSWER_AUDIO"] = "%(INDEX)s-%(ANSWERLANGUAGE)s.mp3" % xdto
            dto[x]["QUESTION_AUDIO"] = "%(INDEX)s-%(QUESTIONLANGUAGE)s.mp3" % xdto

        return dto

    def getQuestionFormat(self,ANSWERLANGUAGE):
        dto = {"ANSWERLANGUAGE": ANSWERLANGUAGE}

        dto.update(
            self.query("SELECT PRE, POST FROM DUPIE.PROMPT WHERE LANGUAGE = '%(ANSWERLANGUAGE)s';" % dto)[0]
        )

        dto.update(
            {
                "PRE_AUDIO": "%(ANSWERLANGUAGE)s-%(ANSWERLANGUAGE)s-1.mp3" % dto,
                "POST_AUDIO": "%(ANSWERLANGUAGE)s-%(ANSWERLANGUAGE)s-2.mp3" % dto
            }
        )
        return dto

    def update(self,query):
      sql_cursor = self.conn.cursor()
      sql_cursor.execute(query)
      self.conn.commit()


    def SaveQuestions(self, sessionID, UID,dto):
        xdto = {
            "SESSIONID": sessionID,
            "UID": UID,
            }

        for x in range(0, len(dto)):
            dto[x].update(xdto)
            dto[x].update({"QUIZQUESTION_INDEX":x})
            dto[x] =  {k.upper(): v for k, v in dto[x].items()}


            query = """INSERT INTO DUPIE.QUESTIONS
                    (SESSIONID, UID, QUESTION, QUESTION_AUDIO, ANSWER, ANSWER_AUDIO, VOCABULARY_INDEX,QUIZQUESTION_INDEX)
                VALUES 
                (%(SESSIONID)s, %(UID)s, '%(QUESTION)s', '%(QUESTION_AUDIO)s', '%(ANSWER)s', '%(ANSWER_AUDIO)s', '%(VOCABULARY_INDEX)s',%(QUIZQUESTION_INDEX)s);""" % dto[x]
            self.update(query)


    def SaveAnswers(self, sessionID, shuffle, quizquestion_index, dto,mixes):
        xdto = {
            "SESSIONID": sessionID,
            "SHUFFLE": shuffle,
            "QUIZQUESTION_INDEX":quizquestion_index,
            "QUIZANSWERANIMATION_INDEX":mixes
            }
        for x in range(0, len(dto)):
            dto[x].update(xdto)
            dto[x].update({"QUIZANSWER_INDEX":x})
            dto[x] =  {k.upper(): v for k, v in dto[x].items()}

            query = """INSERT INTO DUPIE.ANSWERS
                        (SESSIONID, VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO,QUIZQUESTION_INDEX,QUIZANSWER_INDEX,QUIZANSWERANIMATION_INDEX)
                        VALUES(%(SESSIONID)s, %(VOCABULARY_INDEX)s, %(SHUFFLE)s, '%(ANSWER)s', '%(ANSWER_AUDIO)s',%(QUIZQUESTION_INDEX)s,%(QUIZANSWER_INDEX)s,%(QUIZANSWERANIMATION_INDEX)s);""" % dto[x]

            self.update(query)

    def getSessionInfo(self,ID):
        dto = self.query("""SELECT USERSESSIONS_INDEX, UID, FRIENDLYNAME, SESSIONID, LANG_QUESTION, LANG_ANSWER, QUESTION_INDEX, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE
                            FROM DUPIE.USERSESSIONS WHERE SESSIONID = %s;""" % ID)
        return dto[0]


    def getQuestionList(self,ID):
        dto = self.query(""" SELECT QUESTION, QUESTION_AUDIO, ANSWER, ANSWER_AUDIO, VOCABULARY_INDEX, QUIZQUESTION_INDEX
                            FROM DUPIE.QUESTIONS WHERE SESSIONID = %s;""" % ID)
        return dto

    def getAnswerList(self,ID):
        numberofquestions = self.getSessionInfo(ID)["QUESTIONS"]

        _dto = self.query("""SELECT VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO, QUIZQUESTION_INDEX, QUIZANSWER_INDEX
                            FROM DUPIE.ANSWERS WHERE SHUFFLE = 0 AND SESSIONID = %s;""" % ID)

        dto = [[] for i in range(numberofquestions)]

        for x in _dto:
           dto[x["QUIZQUESTION_INDEX"]].append(x)


        return dto

    def getAnswerListAnimation(self,ID):
        numberofquestions = self.getSessionInfo(ID)["QUESTIONS"]
        numberofshuffles = self.getSessionInfo(ID)["SHUFFLES"]

        _dto = self.query("""SELECT SESSIONID, VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO, QUIZQUESTION_INDEX, QUIZANSWER_INDEX,QUIZANSWERANIMATION_INDEX
                            FROM DUPIE.ANSWERS where SHUFFLE = 1 and SESSIONID = %s;""" % ID)

        dto = [[[] for i in range(numberofshuffles)]  for i in range(numberofquestions)]

        for x in _dto:
           dto[x["QUIZQUESTION_INDEX"]][x["QUIZANSWERANIMATION_INDEX"]].append(x)

        return dto
####################################################
####################################################
####################################################
    def getUserSession(self, uid, sessionid):
        xdto = {
            "SESSIONID": sessionid,
            "UID": uid,
            }

        query = """SELECT 
                        USERSESSIONS_INDEX, UID, FRIENDLYNAME, SESSIONID, LANG_QUESTION, LANG_ANSWER, 
                        QUESTION_INDEX, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE
                    FROM DUPIE.USERSESSIONS
                    WHERE
                        SESSIONID = %(SESSIONID)s 
                        and UID = %(UID)s
                    ;""" % xdto   

        dto = self.query(query)

        if len(dto) == 1:
            return dto
        elif len(dto) == 0:
            raise BaseException("Failed to find session to load")
        else:
            raise BaseException("session table is corrupt! (probably not! hahah)")

####################################################
####################################################
####################################################
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
#    print(pprint.pformat(a.getAnswerListAnimation(1001)))

   
   print(pprint.pformat(a.getSessionInfo(1001)))
