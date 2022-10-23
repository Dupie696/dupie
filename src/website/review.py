class ReviewWebpageClass():
    def __init__(self):
        print ("HELLO!")
        self.bottle.route("/quiz/review/<UID>/<USERSESSIONS_INDEX>/")   (self.checkAuth(self.ReviewPage))
        super().__init__()


    def ReviewPage(self,UID,USERSESSIONS_INDEX):

        return self.getTemplate('review_main_get.html').render(
                DTO={
                    "dto":self.getReviewQuestion(USERSESSIONS_INDEX)
                    },
                BreadCrumbs=[{"Quizzes":"/quiz"}]
                )
