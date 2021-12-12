import dupiequiz

sessions = {}

shorttolong = {
 "EN":"english",
 "ES":"espanol",
 "JA":"nihon",
 "ZH":"zhongwen",
 "KO":"hangugeo",
 "en":"english",
 "es":"espanol",
 "ja":"nihon",
 "zh":"zhongwen",
 "ko":"hangugeo",
 "english":"english",
 "espanol":"espanol",
 "nihon":"nihon",
 "zhongwen":"zhongwen",
 "hangugeo":"hangugeo"}

longtoshort = {
 "english":"en",
 "espanol":"es",
 "nihon":"ja",
 "zhongwen":"zh",
 "hangugeo":"ko",
 "en":"en",
 "es":"es",
 "ja":"ja",
 "zh":"zh",
 "ko":"ko",
 "EN":"en",
 "ES":"es",
 "JA":"ja",
 "ZH":"zh",
 "KO":"ko"}

import pprint

class dupiegame():
    quiz = None
    language1 = ""
    language2 = ""
    numofanswers = 0
    numofquestions = 0
    answerlist = []
    answerlistanimation = []

    def __init__(self,language1=None,language2=None,numofquestions=None,numofanswers=None,loadfromDBIndex=0):


        loadfromDBIndex = True
        if (loadfromDBIndex):
            self.quiz = dupiequiz.dupiequiz(numofanswers=True,loadfromDBIndex=1001)

            language1=shorttolong[self.quiz.language1]
            language2=shorttolong[self.quiz.language2]
            self.language1 = language1
            self.language2 = language2
            self.numofanswers = self.quiz.numofanswers
            self.questions = self.quiz.questions
            self.answerlist = self.quiz.answerlist
            self.answerlistanimation = self.quiz.answerlistanimation
        else:
            language1=shorttolong[language1]
            language2=shorttolong[language2]
            self.quiz = dupiequiz.dupiequiz(language1,language2,numofquestions,numofanswers)
            self.language1 = language1
            self.language2 = language2
            self.numofanswers = numofanswers

        self._langDTO = {
            "languageshort1": longtoshort[self.language1],
            "languageshort2": longtoshort[self.language2],
            "languagelong1": shorttolong[self.language1],
            "languagelong2": shorttolong[self.language2],
            }


        if (not loadfromDBIndex):
            self.setAnswerList()
            self.setAnswerListAnimation()


    def nextQuestion(self):
        self.quiz.nextQuestion()
#        self.setAnswerList()
#        self.setAnswerListAnimation()


    def getQuestion(self):
        dto = {}
        dto.update(self.quiz.getQuestion())
        dto.update(self.quiz.getPrompt(self.language2))
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

    # # TODO: move to quiz
    # def setAnswerList(self):
    #     _answerFound = False
    #     while not _answerFound:
    #         _dto_list, _answerFound = self.quiz.getAnswerList()

    #     dto = []

    #     for answer in _dto_list:
    #         _dto = {}
    #         _dto = {
    #             "answer":answer["answer"],
    #             "answer_audio":"%s-%s.mp3" % (
    #                 answer["vocabulary_index"],
    #                 self._langDTO["languageshort2"]
    #                 )
    #         }
    #         dto.append(_dto)

    #     self.answerlist = dto

    def  getAnswerList(self):
        return self.answerlist[self.quiz.questionIndex]


    # # TODO: move to quiz
    # def setAnswerListAnimation(self):
    #     mixes = 10

    #     DTO_LIST = []
    #     for x in range(0, mixes):
    #         __dto = []
    #         print ("reset")
    #         _answerFound = True
    #         _answerList = []
    #         while _answerFound:
    #             _answerList, _answerFound = self.quiz.getAnswerList()
    #             print(_answerList)

    #         for answer in _answerList:
    #             _dto = {}
    #             _dto = {
    #                 "answer":answer["answer"]
    #             }
    #             __dto.append(_dto)

    #         DTO_LIST.append(__dto)

    #     self.answerlistanimation = DTO_LIST     

    def getAnswerListAnimation(self):
        return self.answerlistanimation[self.quiz.questionIndex]




if __name__ == "__main__":
    test = dupiegame("en","zh",9,3)
    test.getQuestion()
    test.getAnswerList()
    import pprint
    print (pprint.pformat(test.getAnswerListAnimation()))
