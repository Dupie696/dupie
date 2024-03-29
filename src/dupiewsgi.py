import quiz.database

import website.videos
import website.tools
import website.quiz
import quiz.generation
import website.ttsbatchload
import website.review

class DupieWSGI(
    quiz.database.dupiebase,
    website.review.ReviewWebpageClass,
    quiz.generation.QuizGeneration,
    website.tools.CheckAuthClass,
    website.videos.VideoWebpagesClass,
    website.quiz.QuizWebpagesClass,
    website.tools.WSGIToolsClass,
    website.ttsbatchload.ttsBatchLoadWeb,
    ):

    def __init__(self,bottle):
        self.bottle = bottle
        super().__init__()

if __name__ == "__main__":
    import bottle

    a = DupieWSGI(bottle)
    # #print (a.getAllSessionInfo(101))
    # # USERSESSIONS_INDEX = a.generateQuiz_Session(101,"EN","ES",3,6)
    # # x = a.makeMeAQuiz_Questions(101,USERSESSIONS_INDEX,3,3, "EN","ES")
    # #x = a.makeMeAQuiz_Answers(1003, 1, 1003,3,"EN","ES")
    # print ("starting")
    # a.NewQuizPage()
    # #import pprint
    # # print (pprint.pformat(x))
    # # print ("USERSESSIONS_INDEX %s" % USERSESSIONS_INDEX)


    print( a.getListofLanguages())