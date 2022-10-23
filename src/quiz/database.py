import apis.databases

class dupiebase():
    def __init__(self):
        self.connector = apis.databases.mysql_database_connector()

        super().__init__()

    def dtocleaner(self, xdto):
        for idx, mylist in enumerate(xdto):
            for k, v in mylist.items():
                if isinstance(v, str):
                    if v.find('"')!=-1:
                        xdto[idx][k] = v.replace('"',r'\"')
                    if v.find("'")!=-1:
                        xdto[idx][k] = v.replace("'",r"\'")
        return xdto



    def getAllSessionInfo(self,UID):
        dto = self.connector.query("""SELECT USERSESSIONS_INDEX, UID, FRIENDLYNAME, LANG_QUESTION, LANG_ANSWER, QUIZQUESTION_NUMBER, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE
                            FROM DUPIE.USERSESSIONS WHERE UID = %s;""" % UID)
        return dto


    def getSessionInfo(self,USERSESSIONS_INDEX):
        dto = self.connector.query("""SELECT USERSESSIONS_INDEX, UID, FRIENDLYNAME, LANG_QUESTION, LANG_ANSWER, QUIZQUESTION_NUMBER, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE
                            FROM DUPIE.USERSESSIONS WHERE USERSESSIONS_INDEX = %s;""" % USERSESSIONS_INDEX)
        return dto[0]

    def getStaticAnswers(self,USERSESSIONS_INDEX,QuestionIndex):
        dto = self.connector.query("""SELECT 
                                        ANSWERS_INDEX, USERSESSIONS_INDEX, VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO, QUIZQUESTION_NUMBER, QUIZANSWER_NUMBER, QUIZANSWERANIMATION_INDEX 
                                      FROM 
                                        DUPIE.ANSWERS 
                                    where 
                                            SHUFFLE=0
                                        and USERSESSIONS_INDEX = %s 
                                        and QUIZQUESTION_NUMBER = %s;""" % (USERSESSIONS_INDEX,QuestionIndex))
        return dto
        

    def getStaticQuestion(self,USERSESSIONS_INDEX,QuestionIndex):
        dto = self.connector.query("""SELECT 
                                            QUESTIONS_INDEX, USERSESSIONS_INDEX, UID, QUESTION, QUESTION_AUDIO, ANSWER, ANSWER_AUDIO, VOCABULARY_INDEX, QUIZQUESTION_NUMBER
                                    FROM 
                                        DUPIE.QUESTIONS
                                    where 
                                            USERSESSIONS_INDEX = %s
                                        and QUIZQUESTION_NUMBER = %s;""" % (USERSESSIONS_INDEX, QuestionIndex))
        return dto[0]



    def getReviewQuestion(self,USERSESSIONS_INDEX):
        dto = self.connector.query("""SELECT 
                                            QUESTIONS_INDEX, USERSESSIONS_INDEX, UID, QUESTION, QUESTION_AUDIO, ANSWER, ANSWER_AUDIO, VOCABULARY_INDEX, QUIZQUESTION_NUMBER
                                    FROM 
                                        DUPIE.QUESTIONS
                                    where 
                                            USERSESSIONS_INDEX = %s;""" % (USERSESSIONS_INDEX))
        return dto


    def getAnswerLanguage(self,USERSESSIONS_INDEX):
        dto = self.connector.query("""SELECT 
                                            LANG_ANSWER
                                        FROM 
                                            DUPIE.USERSESSIONS 
                                        WHERE 
                                            USERSESSIONS_INDEX = %s;""" % USERSESSIONS_INDEX)
        return dto[0]["LANG_ANSWER"]

    def getPrompt(self,questionLanguage):
        dto = self.connector.query("""SELECT 
                                            PROMPT_INDEX, `LANGUAGE`, PRE, POST, PRE2, POST2, PRE_AUDIO, POST_AUDIO
                                        FROM 
                                            DUPIE.PROMPT
                                        WHERE
                                            `LANGUAGE` = '%s';""" % questionLanguage)
        return dto[0]

    def getCheckAnswer(self,UID,USERSESSIONS_INDEX,questionIndex):
        dto = self.connector.query("""SELECT 
                                            ANSWERS.QUIZQUESTION_NUMBER, ANSWERS.ANSWER, QUESTIONS.ANSWER, ANSWERS.QUIZANSWER_NUMBER
                                        FROM 
                                            QUESTIONS
                                        LEFT JOIN ANSWERS ON 
                                                ANSWERS.ANSWER=QUESTIONS.ANSWER 
                                            and ANSWERS.USERSESSIONS_INDEX=QUESTIONS.USERSESSIONS_INDEX 
                                            and QUESTIONS.QUIZQUESTION_NUMBER=ANSWERS.QUIZQUESTION_NUMBER 
                                        where 
                                                ANSWERS.SHUFFLE=0 
                                            and QUESTIONS.UID=%s 
                                            and QUESTIONS.USERSESSIONS_INDEX=%s 
                                            and QUESTIONS.QUIZQUESTION_NUMBER=%s;""" % (UID,USERSESSIONS_INDEX,questionIndex))

        return dto[0]["QUIZANSWER_NUMBER"]  