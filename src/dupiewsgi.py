import website.videos
import website.tools
import website.quiz
import quiz.database

class DupieWSGI(
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
    x = a.CheckAnswer(101,1001,1)
    print (x)