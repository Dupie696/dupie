class AuxWebpagesClass():
    def watchVideo(self):
        return self.getTemplate('video_menu_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[{"Video Menu":"/WatchVideo"}]
                )



 #   @bottle.route('/quiz/101')
    def doQuiz(self):
        #loadQuestion(101,1001)
        return self.getTemplate('quiz_list_get.html').render(
                DTO={ },
                BreadCrumbs=[{"Quizzes":"/quiz"}]
                )

 #   @bottle.route('/quiz/101/1001')
 #   @checkAuth
    def doQuiz(self):
        return self.getTemplate('quiz_main_get.html').render(
                DTO={ },
                BreadCrumbs=[{"Quizzes":"/quiz"},{"Pollito Tito":"/WatchVideo/PollitoTito"}]
                )
#    @bottle.route('/WatchVideo/PollitoTito')

    def watchPollitoTito(self):
        return self.getTemplate('video_watch_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[{"Video Menu":"/WatchVideo"},{"Pollito Tito":"/WatchVideo/PollitoTito"}]
                )