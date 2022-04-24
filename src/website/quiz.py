class QuizWebpagesClass():
    def __init__(self):
        self.bottle.route("/quiz")          (self.checkAuth(self.QuizSelectionPage))
        self.bottle.route("/quiz/newquiz")   (self.checkAuth(self.NewQuizPage))
        self.bottle.route("/quiz/<UID>/<USERSESSIONS_INDEX>/<QuestionIndex>/")   (self.checkAuth(self.QuizPage))

        self.bottle.route("/quiz/<UID>/<USERSESSIONS_INDEX>/<QuestionIndex>/checkAnswer/<AnswerID>")   (self.checkAuth(self.CheckAnswer))

        super().__init__()

    def QuizSelectionPage(self):
        return self.getTemplate('quiz_list_get.html').render(
                DTO={"AllSessionInfo":self.getAllSessionInfo(101)},
                BreadCrumbs=[{"Quizzes":"/quiz"}]
                )

    def QuizPage(self,UID,USERSESSIONS_INDEX,QuestionIndex):
        answerLanguage = self.getAnswerLanguage(USERSESSIONS_INDEX)

        if int(self.getSessionInfo(USERSESSIONS_INDEX)["QUESTIONS"])==int(QuestionIndex)+1:
            gamecomplete = "True"
        else:
            gamecomplete = "False"

        return self.getTemplate('quiz_main_get.html').render(
                DTO={
                    "question":self.getStaticQuestion(USERSESSIONS_INDEX,QuestionIndex),
                    "answers":self.getStaticAnswers(USERSESSIONS_INDEX,QuestionIndex),
                    "prompt":self.getPrompt(answerLanguage),
                    "gamecomplete":gamecomplete,
                    "nexttarget":"/quiz/%s/%s/%s/" % (UID,USERSESSIONS_INDEX,int(QuestionIndex)+1)

                    },
                BreadCrumbs=[{"Quizzes":"/quiz"}]
                )

    def CheckAnswer(self,UID,USERSESSIONS_INDEX,QuestionIndex,AnswerID):
        if (int(AnswerID) == int(self.getCheckAnswer(UID,USERSESSIONS_INDEX,QuestionIndex))):
            return "True"
        else:
            return "False"

    def NewQuizPage(self):
        USERSESSIONS_INDEX = self.generateQuiz_Session(101,"EN","ES",10,9)
        self.makeMeAQuiz_Questions(101,USERSESSIONS_INDEX,10,9, "EN","ES")

        # USERSESSIONS_INDEX = self.generateQuiz_Session(101,"EN","AR",10,9)
        # self.makeMeAQuiz_Questions(101,USERSESSIONS_INDEX,10,9, "EN","AR")

        # USERSESSIONS_INDEX = self.generateQuiz_Session(101,"EN","KO",10,9)
        # self.makeMeAQuiz_Questions(101,USERSESSIONS_INDEX,10,9, "EN","KO")

        # USERSESSIONS_INDEX = self.generateQuiz_Session(101,"EN","RU",10,9)
        # self.makeMeAQuiz_Questions(101,USERSESSIONS_INDEX,10,9, "EN","RU")

        return """<meta http-equiv="refresh" content="1;url=/quiz/101/%s/0/" />""" % str(USERSESSIONS_INDEX) + str(USERSESSIONS_INDEX)
