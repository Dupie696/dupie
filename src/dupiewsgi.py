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
    #x = a.generateQuiz_Session(101,"EN","EN",3,6)
    x = a.getLexicon("EN","FR")
    import pprint
    print (pprint.pformat(x))