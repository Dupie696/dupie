class QuizWebpagesClass():
    def __init__(self):
        super().__init__()

    def doQuiz(self):
        return self.getTemplate('quiz_list_get.html').render(
                DTO={ },
                BreadCrumbs=[{"Quizzes":"/quiz"}]
                )

    def doQuiz(self):
        return self.getTemplate('quiz_main_get.html').render(
                DTO={ },
                BreadCrumbs=[{"Quizzes":"/quiz"},{"Pollito Tito":"/WatchVideo/PollitoTito"}]
                )
