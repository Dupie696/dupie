class QuizGeneration():

    def generateQuiz_Session(self, UID, LANG_QUESTION, LANG_ANSWER, QUESTIONS, ANSWERS):
        xdto = {
                "UID":  UID,
                "FRIENDLYNAME":  "Dupie",
                "LANG_QUESTION":  LANG_QUESTION,
                "LANG_ANSWER":  LANG_ANSWER,
                "QUESTION_INDEX":  -1,
                "QUESTIONS":  QUESTIONS,
                "ANSWERS":  ANSWERS,
                "SHUFFLES":  10,
                "STATEMACHINE":  "GENERATING"
            }
        query = """INSERT INTO DUPIE.USERSESSIONS
                    (UID, FRIENDLYNAME, LANG_QUESTION, LANG_ANSWER, QUESTION_INDEX, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE)
                    VALUES(%(UID)s, '%(FRIENDLYNAME)s', '%(LANG_QUESTION)s', '%(LANG_ANSWER)s', %(QUESTION_INDEX)s, %(QUESTIONS)s, %(ANSWERS)s, %(SHUFFLES)s, '%(STATEMACHINE)s')""" % xdto

        return self.connector.update(query)     

    def generateQuiz_Questions(self, USERSESSIONS_INDEX,UID,QUESTION,QUESTION_AUDIO,ANSWER,ANSWER_AUDIO,VOCABULARY_INDEX,QUIZQUESTION_INDEX):

        xdto = {
                "USERSESSIONS_INDEX":  USERSESSIONS_INDEX,
                "UID":  UID,
                "QUESTION":  QUESTION,
                "QUESTION_AUDIO":  QUESTION_AUDIO,
                "ANSWER":  ANSWER,
                "ANSWER_AUDIO":  ANSWER_AUDIO,
                "VOCABULARY_INDEX":  VOCABULARY_INDEX,
            }
        query = """INSERT INTO DUPIE.QUESTIONS
                    (USERSESSIONS_INDEX, UID, QUESTION, QUESTION_AUDIO, ANSWER, ANSWER_AUDIO, VOCABULARY_INDEX)
                    VALUES(%(USERSESSIONS_INDEX)s, %(UID)s, '%(QUESTION)s', '%(QUESTION_AUDIO)s', '%(ANSWER)s', '%(ANSWER_AUDIO)s', %(VOCABULARY_INDEX)s)""" % dto[x]

        return self.connector.update(query)            


    def generateQuiz_Answers(self, USERSESSIONS_INDEX,VOCABULARY_INDEX,SHUFFLE,ANSWER,ANSWER_AUDIO,QUIZQUESTION_INDEX,QUIZANSWER_INDEX):

        xdto = {
                "USERSESSIONS_INDEX":  USERSESSIONS_INDEX,
                "VOCABULARY_INDEX":  VOCABULARY_INDEX,
                "SHUFFLE":  SHUFFLE,
                "ANSWER":  ANSWER,
                "ANSWER_AUDIO":  ANSWER_AUDIO,
                "QUIZQUESTION_INDEX":  QUIZQUESTION_INDEX,
                "QUIZANSWER_INDEX":  QUIZANSWER_INDEX,
            }
        query = """INSERT INTO DUPIE.ANSWERS
                    (USERSESSIONS_INDEX, VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO, QUIZQUESTION_INDEX, QUIZANSWER_INDEX)
                    VALUES(%(USERSESSIONS_INDEX)s, %(VOCABULARY_INDEX)s, %(SHUFFLE)s, '%(ANSWER)s', '%(ANSWER_AUDIO)s', %(QUIZQUESTION_INDEX)s, %(QUIZANSWER_INDEX)s)""" % dto[x]

        return self.connector.update(query)

    def getLexiconETL(self,questionlanguage, answerlanguage):
        xdto = {
            "QUESTIONLANGUAGE": questionlanguage,
            "ANSWERLANGUAGE": answerlanguage
            }
        dto = (
            self.connector.query("SELECT VOCABULARY_INDEX, %(QUESTIONLANGUAGE)s ""QUESTION"", %(ANSWERLANGUAGE)s ""ANSWER"" FROM DUPIE.VOCABULARY WHERE VOCABULARY_INDEX = SYNONYM AND %(QUESTIONLANGUAGE)s<>'' AND %(ANSWERLANGUAGE)s<>'';" % xdto )
        )

        for x in range(0, len(dto)):
            xdto["INDEX"] = dto[x]["VOCABULARY_INDEX"]
            dto[x]["ANSWER_AUDIO"] = "%(INDEX)s-%(ANSWERLANGUAGE)s.mp3" % xdto
            dto[x]["QUESTION_AUDIO"] = "%(INDEX)s-%(QUESTIONLANGUAGE)s.mp3" % xdto

        return dto



        
    def setQuestion(self,numofquestions):

        _questions = copy.deepcopy(self.lexicon)
        del _questions[numofquestions:]
        return _questions
        


    def getLexicon(self,questionlanguage,answerlanguage):
        import random
        _lexicon = self.getLexiconETL(questionlanguage,answerlanguage)
        random.shuffle(_lexicon)
        return (_lexicon)


    def getAnswerList(self):
        _answerlist = copy.deepcopy(self.lexicon)
        random.shuffle(_answerlist)
        del _answerlist[self.numofanswers:]
        _answerFound = self.checkAnswerListForCorrectAnswer(self.questionIndex, _answerlist)
        return _answerlist, _answerFound


    def makeMeAQuiz():
        pass