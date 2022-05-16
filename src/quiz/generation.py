class QuizGeneration():

    def generateQuiz_Session(self, UID, LANG_QUESTION, LANG_ANSWER, QUESTIONS, ANSWERS):
        xdto = {
                "UID":  UID,
                "FRIENDLYNAME":  "Dupie",
                "LANG_QUESTION":  LANG_QUESTION,
                "LANG_ANSWER":  LANG_ANSWER,
                "QUIZQUESTION_NUMBER":  -1,
                "QUESTIONS":  QUESTIONS,
                "ANSWERS":  ANSWERS,
                "SHUFFLES":  10,
                "STATEMACHINE":  "GENERATING"
            }
        query = """INSERT INTO DUPIE.USERSESSIONS
                    (UID, FRIENDLYNAME, LANG_QUESTION, LANG_ANSWER, QUIZQUESTION_NUMBER, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE)
                    VALUES(%(UID)s, '%(FRIENDLYNAME)s', '%(LANG_QUESTION)s', '%(LANG_ANSWER)s', %(QUIZQUESTION_NUMBER)s, %(QUESTIONS)s, %(ANSWERS)s, %(SHUFFLES)s, '%(STATEMACHINE)s')""" % xdto

        return self.connector.update(query)     

    def generateQuiz_Questions(self, USERSESSIONS_INDEX,UID,QUESTION,QUESTION_AUDIO,ANSWER,ANSWER_AUDIO,VOCABULARY_INDEX,QUIZQUESTION_NUMBER):

        xdto = {
                "USERSESSIONS_INDEX":  USERSESSIONS_INDEX,
                "UID":  UID,
                "QUESTION":  QUESTION,
                "QUESTION_AUDIO":  QUESTION_AUDIO,
                "ANSWER":  ANSWER,
                "ANSWER_AUDIO":  ANSWER_AUDIO,
                "VOCABULARY_INDEX":  VOCABULARY_INDEX,
                "QUIZQUESTION_NUMBER": QUIZQUESTION_NUMBER
            }
        query = """INSERT INTO DUPIE.QUESTIONS
                    (USERSESSIONS_INDEX, UID, QUESTION, QUESTION_AUDIO, ANSWER, ANSWER_AUDIO, VOCABULARY_INDEX,QUIZQUESTION_NUMBER)
                    VALUES(%(USERSESSIONS_INDEX)s, %(UID)s, '%(QUESTION)s', '%(QUESTION_AUDIO)s', '%(ANSWER)s', '%(ANSWER_AUDIO)s', %(VOCABULARY_INDEX)s, %(QUIZQUESTION_NUMBER)s)""" % xdto

        return self.connector.update(query)            


    def generateQuiz_Answers(self, USERSESSIONS_INDEX,VOCABULARY_INDEX,SHUFFLE,ANSWER,ANSWER_AUDIO,QUIZQUESTION_NUMBER,QUIZANSWER_NUMBER,QUIZANSWERANIMATION_INDEX):

        xdto = {
                "USERSESSIONS_INDEX":  USERSESSIONS_INDEX,
                "VOCABULARY_INDEX":  VOCABULARY_INDEX,
                "SHUFFLE":  SHUFFLE,
                "ANSWER":  ANSWER,
                "ANSWER_AUDIO":  ANSWER_AUDIO,
                "QUIZQUESTION_NUMBER":  QUIZQUESTION_NUMBER,
                "QUIZANSWER_NUMBER":  QUIZANSWER_NUMBER,
                "QUIZANSWERANIMATION_INDEX": QUIZANSWERANIMATION_INDEX
            }
        query = """INSERT INTO DUPIE.ANSWERS
                    (USERSESSIONS_INDEX, VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO, QUIZQUESTION_NUMBER, QUIZANSWER_NUMBER, QUIZANSWERANIMATION_INDEX)
                    VALUES(%(USERSESSIONS_INDEX)s, %(VOCABULARY_INDEX)s, %(SHUFFLE)s, '%(ANSWER)s', '%(ANSWER_AUDIO)s', %(QUIZQUESTION_NUMBER)s, %(QUIZANSWER_NUMBER)s, %(QUIZANSWERANIMATION_INDEX)s)""" % xdto

        return self.connector.update(query)

    def getLexiconETL(self,questionlanguage, answerlanguage):
        xdto = {
            "QUESTIONLANGUAGE": questionlanguage,
            "ANSWERLANGUAGE": answerlanguage
            }
        dto = (
#            self.connector.query("SELECT VOCABULARY_INDEX, %(QUESTIONLANGUAGE)s ""QUESTION"", %(ANSWERLANGUAGE)s ""ANSWER"" FROM DUPIE.VOCABULARY WHERE %(QUESTIONLANGUAGE)s<>'' AND %(ANSWERLANGUAGE)s<>'';" % xdto )
            self.connector.query("SELECT VOCABULARY_INDEX, %(QUESTIONLANGUAGE)s ""QUESTION"", %(ANSWERLANGUAGE)s ""ANSWER"" FROM DUPIE.VOCABULARY WHERE %(QUESTIONLANGUAGE)s<>'' AND %(ANSWERLANGUAGE)s<>'';" % xdto )
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
        

    def getAnswerList(self):
        _answerlist = copy.deepcopy(self.lexicon)
        random.shuffle(_answerlist)
        del _answerlist[self.numofanswers:]
        _answerFound = self.checkAnswerListForCorrectAnswer(self.questionIndex, _answerlist)
        return _answerlist, _answerFound


    def makeMeAQuiz_Questions(self,UID,USERSESSIONS_INDEX,numberofQuestions,numberofAnswers,questionlanguage,answerlanguage):
        import random
        import copy
        _lexicon = copy.deepcopy(self.getLexiconETL(questionlanguage,answerlanguage))
        while numberofQuestions > len(_lexicon):
            print ("---")
            _lexicon = _lexicon + copy.deepcopy(self.getLexiconETL(questionlanguage,answerlanguage))
        random.shuffle(_lexicon)
        _lexicon = _lexicon[:numberofQuestions]

        for QUIZQUESTION_NUMBER, x in enumerate(_lexicon):
            y = self.generateQuiz_Questions(USERSESSIONS_INDEX,UID,x["QUESTION"],x["QUESTION_AUDIO"],x["ANSWER"],x["ANSWER_AUDIO"],x["VOCABULARY_INDEX"],QUIZQUESTION_NUMBER)

            self.makeMeAQuiz_Answers(USERSESSIONS_INDEX,QUIZQUESTION_NUMBER, x["VOCABULARY_INDEX"],numberofAnswers,questionlanguage,answerlanguage)


    def makeMeAQuiz_Answers(self,USERSESSIONS_INDEX,QUIZQUESTION_NUMBER, VOCABULARY_INDEX,numberofAnswers,questionlanguage,answerlanguage):
        import random
        x = []
        _lexicon = []
        while VOCABULARY_INDEX not in x:
            _lexicon = self.getLexiconETL(questionlanguage,answerlanguage)
            random.shuffle(_lexicon)
            _lexicon = _lexicon[:numberofAnswers]
            x = [y["VOCABULARY_INDEX"] for y in _lexicon]


        for QUIZANSWER_NUMBER, x in enumerate(_lexicon):
            self.generateQuiz_Answers(USERSESSIONS_INDEX,x["VOCABULARY_INDEX"],0,x["ANSWER"],x["ANSWER_AUDIO"],QUIZQUESTION_NUMBER,QUIZANSWER_NUMBER,0)

