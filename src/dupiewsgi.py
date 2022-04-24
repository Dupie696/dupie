import website.videos
import website.tools
import website.quiz
import quiz.database
import quiz.generation

class DupieWSGI(
    quiz.generation.QuizGeneration,
    quiz.database.dupiebase,
    website.tools.CheckAuthClass,
    website.videos.VideoWebpagesClass,
    website.quiz.QuizWebpagesClass,
    website.tools.WSGIToolsClass):

    def __init__(self,bottle):
        self.bottle = bottle
        super().__init__()

if __name__ == "__main__":
    import bottle

    a = DupieWSGI(bottle)
    #print (a.getAllSessionInfo(101))
    USERSESSIONS_INDEX = a.generateQuiz_Session(101,"EN","ES",3,6)
    x = a.makeMeAQuiz_Questions(101,USERSESSIONS_INDEX,3,3, "EN","ES")
    #x = a.makeMeAQuiz_Answers(1003, 1, 1003,3,"EN","ES")
    import pprint
    print (pprint.pformat(x))
    print ("USERSESSIONS_INDEX %s" % USERSESSIONS_INDEX)