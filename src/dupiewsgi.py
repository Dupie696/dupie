import class_templates.wsgi
import website.videos
import website.tools
import website.quiz

class DupieWSGI(website.tools.CheckAuthClass,
                website.videos.VideoWebpagesClass,
                website.quiz.QuizWebpagesClass,
                website.tools.WSGIToolsClass):

    def __init__(self,bottle):
        self.bottle = bottle
        super().__init__()

if __name__ == "__main__":
    import bottle

    DupieWSGI(bottle)