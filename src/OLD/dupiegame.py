import dupiequiz

sessions = {}

import pprint

class dupiegame():
    quiz = None
    questionlanguage = ""
    answerlanguage = ""
    numofanswers = 0
    numofquestions = 0
    answerlist = []
    answerlistanimation = []

    def __init__(self,questionlanguage=None,answerlanguage=None,numofquestions=None,numofanswers=None,loadfromDBIndex=0,quickload=False):

        if not quickload:
            loadfromDBIndex = True
            if (loadfromDBIndex):
                self.quiz = dupiequiz.dupiequiz(numofanswers=True,loadfromDBIndex=1001)
                quiz_ = self.quiz

                
                self.questionlanguage = quiz_.questionlanguage
                self.answerlanguage = quiz_.answerlanguage
                self.numofanswers = quiz_.numofanswers
                self.questions = quiz_.questions
                self.answerlist = quiz_.answerlist
                self.answerlistanimation = quiz_.answerlistanimation
            else:
                questionlanguage=shorttolong[questionlanguage]
                answerlanguage=shorttolong[answerlanguage]
                self.quiz = dupiequiz.dupiequiz(questionlanguage,answerlanguage,numofquestions,numofanswers)
                self.questionlanguage = questionlanguage
                self.answerlanguage = answerlanguage
                self.numofanswers = numofanswers

            self._langDTO = {
                "languageshort1": self.questionlanguage,
                "languageshort2": self.answerlanguage,
                "languagelong1": self.questionlanguage,
                "languagelong2": self.answerlanguage,
                }


            if (not loadfromDBIndex):
                self.setAnswerList()
                self.setAnswerListAnimation()
        else:
            pass

    def nextQuestion(self):
        self.quiz.nextQuestion()
#        self.setAnswerList()
#        self.setAnswerListAnimation()


    def getQuestion(self):
        dto = {}
        dto.update(self.quiz.getQuestion())
        dto.update(self.quiz.getPrompt(self.answerlanguage))
        dto.update(self._langDTO)

        #print (dto)

        snd = {
            "%(languagelong1)s_audio" % dto: "%(VOCABULARY_INDEX)s-%(languageshort1)s.mp3" % (dto),
            "%(languagelong2)s_audio" % dto: "%(VOCABULARY_INDEX)s-%(languageshort2)s.mp3" % (dto),
            "pre_audio": "%(languageshort2)s-%(languageshort2)s-1" % dto,
            "post_audio": "%(languageshort2)s-%(languageshort2)s-2" % dto
            }
        dto.update(snd)

        questionanswer = {
            "answer":dto["ANSWER"],
            "question":dto["QUESTION"],
            "answer_audio":dto["ANSWER" + "_AUDIO"],
            "question_audio":dto["QUESTION" + "_AUDIO"]
        }
        dto.update(questionanswer)
        
        return (dto)

    def  getAnswerList(self):
        return self.answerlist[self.quiz.questionIndex]
  

    def getAnswerListAnimation(self):
        return self.answerlistanimation[self.quiz.questionIndex]




if __name__ == "__main__":
    test = dupiegame("en","zh",9,3)
    test.getQuestion()
    test.getAnswerList()
    import pprint
    print (pprint.pformat(test.getAnswerListAnimation()))
