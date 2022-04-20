class QuizWebpagesClass():
    def __init__(self):
        self.bottle.route("/quiz")          (self.checkAuth(self.QuizSelectionPage))
        self.bottle.route("/quiz/<UID>/<SessionID>/<QuestionIndex>/")   (self.checkAuth(self.QuizPage))

        self.bottle.route("/quiz/<UID>/<SessionID>/<QuestionIndex>/checkAnswer/<AnswerID>")   (self.checkAuth(self.CheckAnswer))

        super().__init__()

    def QuizSelectionPage(self):
        return self.getTemplate('quiz_list_get.html').render(
                DTO={"AllSessionInfo":self.getAllSessionInfo(101)},
                BreadCrumbs=[{"Quizzes":"/quiz"}]
                )

    def QuizPage(self,UID,SessionID,QuestionIndex):
        answerLanguage = self.getAnswerLanguage(SessionID)
        return self.getTemplate('quiz_main_get.html').render(
                DTO={
                    "question":self.getStaticQuestion(SessionID,QuestionIndex),
                    "answers":self.getStaticAnswers(SessionID,QuestionIndex),
                    "prompt":self.getPrompt(answerLanguage)
                    },
                BreadCrumbs=[{"Quizzes":"/quiz"}]
                )

    def CheckAnswer(self,UID,SessionID,QuestionIndex,AnswerID):
        if (int(AnswerID) == int(self.getCheckAnswer(UID,SessionID,QuestionIndex))):
            return "True"
        else:
            return "False"
