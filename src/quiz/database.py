import apis.databases

class dupiebase():
    def __init__(self):
        self.connector = apis.databases.mysql_database_connector()

        super().__init__()



    def getAllSessionInfo(self,UID):
        dto = self.connector.query("""SELECT USERSESSIONS_INDEX, UID, FRIENDLYNAME, SESSIONID, LANG_QUESTION, LANG_ANSWER, QUESTION_INDEX, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE
                            FROM DUPIE.USERSESSIONS WHERE UID = %s;""" % UID)
        return dto


    def getSessionInfo(self,SessionID):
        dto = self.connector.query("""SELECT USERSESSIONS_INDEX, UID, FRIENDLYNAME, SESSIONID, LANG_QUESTION, LANG_ANSWER, QUESTION_INDEX, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE
                            FROM DUPIE.USERSESSIONS WHERE SESSIONID = %s;""" % SessionID)
        return dto[0]

    def getStaticAnswers(self,SessionID,QuestionIndex):
        dto = self.connector.query("""SELECT 
                                        ANSWERS_INDEX, SESSIONID, VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO, QUIZQUESTION_INDEX, QUIZANSWER_INDEX, QUIZANSWERANIMATION_INDEX 
                                      FROM 
                                        DUPIE.ANSWERS 
                                    where 
                                            SHUFFLE=0
                                        and SESSIONID = %s 
                                        and QUIZQUESTION_INDEX = %s;""" % (SessionID,QuestionIndex))
        return dto
        

    def getStaticQuestion(self,SessionID,QuestionIndex):
        dto = self.connector.query("""SELECT 
                                            QUESTIONS_INDEX, SESSIONID, UID, QUESTION, QUESTION_AUDIO, ANSWER, ANSWER_AUDIO, VOCABULARY_INDEX, QUIZQUESTION_INDEX
                                    FROM 
                                        DUPIE.QUESTIONS
                                    where 
                                            SESSIONID = 1001
                                        and QUIZQUESTION_INDEX = %s;""" % QuestionIndex)
        return dto[0]

    def getAnswerLanguage(self,SessionID):
        dto = self.connector.query("""SELECT 
                                            LANG_ANSWER
                                        FROM 
                                            DUPIE.USERSESSIONS 
                                        WHERE 
                                            SESSIONID = %s;""" % SessionID)
        return dto[0]["LANG_ANSWER"]

    def getPrompt(self,questionLanguage):
        dto = self.connector.query("""SELECT 
                                            PROMPT_INDEX, `LANGUAGE`, PRE, POST, PRE2, POST2
                                        FROM 
                                            DUPIE.PROMPT
                                        WHERE
                                            `LANGUAGE` = '%s';""" % questionLanguage)
        return dto[0]

    def getCheckAnswer(self,UID,sessionID,questionIndex):
        dto = self.connector.query("""SELECT 
                                            ANSWERS.QUIZQUESTION_INDEX, ANSWERS.ANSWER, QUESTIONS.ANSWER, ANSWERS.QUIZANSWER_INDEX
                                        FROM 
                                            QUESTIONS
                                        LEFT JOIN ANSWERS ON 
                                                ANSWERS.ANSWER=QUESTIONS.ANSWER 
                                            and ANSWERS.SESSIONID=QUESTIONS.SESSIONID 
                                            and QUESTIONS.QUIZQUESTION_INDEX=ANSWERS.QUIZQUESTION_INDEX 
                                        where 
                                                ANSWERS.SHUFFLE=0 
                                            and QUESTIONS.UID=%s 
                                            and QUESTIONS.SESSIONID=%s 
                                            and QUESTIONS.QUIZQUESTION_INDEX=%s;""" % (UID,sessionID,questionIndex))

        return dto[0]["QUIZANSWER_INDEX"]  