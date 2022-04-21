class QuizGeneration():
    def getNextTableIndex(self,TableName):
        """
            stub
        """
        return (1)

    def getNextSessionID(self):
        """
            stub
        """
        return (1002)

    def generateQuiz(self, UID, LANG_QUESTION, LANG_ANSWER, QUESTIONS, ANSWERS):
        xdto = {
                "USERSESSIONS_INDEX":  self.getNextTableIndex("USERSESSIONS"),
                "UID":  UID,
                "FRIENDLYNAME":  "Kelly",
                "SESSIONID":  self.getNextSessionID(),
                "LANG_QUESTION":  LANG_QUESTION,
                "LANG_ANSWER":  LANG_ANSWER,
                "QUESTION_INDEX":  -1,
                "QUESTIONS":  QUESTIONS,
                "ANSWERS":  ANSWERS,
                "SHUFFLES":  10,
                "STATEMACHINE":  "GENERATING"
            }
        query = """INSERT INTO DUPIE.USERSESSIONS
                    (USERSESSIONS_INDEX, UID, FRIENDLYNAME, SESSIONID, LANG_QUESTION, LANG_ANSWER, QUESTION_INDEX, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE)
                    VALUES(%(USERSESSIONS_INDEX)s, %(UID)s, '%(FRIENDLYNAME)s', %(SESSIONID)s, '%(LANG_QUESTION)s', '%(LANG_ANSWER)s', %(QUESTION_INDEX)s, %(QUESTIONS)s, %(ANSWERS)s, %(SHUFFLES)s, '%(STATEMACHINE)s')""" % xdto

        self.connector.update(query)     

