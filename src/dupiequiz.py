
# sessions[101] = {
#    "question": "sorry",
#    "prompt1": "¿Cómo se dice",
#    "prompt2": "en español?",

#    "answer": "Lo siento",
#    "choices": ["Hola","Adiós","Por favor","Gracias","Lo siento","Salud","Sí","No","Quién","Qué","Por qué","Dónde"],
#    "choicesAudio":["1001-es.mp3","1002-es.mp3","1003-es.mp3","1004-es.mp3","1005-es.mp3","1006-es.mp3","1007-es.mp3","1008-es.mp3","1009-es.mp3","1010-es.mp3","1011-es.mp3","1012-es.mp3"],
#    "questiuonAudio": ["es-es-1.mp3","1005-en.mp3","es-es-2.mp3"]

# }
import dupiebase
import random
import copy

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


class dupiequiz:
    questions = []
    lexicon = []
    prompt = {}
    numofanswers = 0

    def __init__(self,language1=None,language2=None,numofquestions=None,numofanswers=None,loadfromDBIndex=0):
        # master list of words
        #loadfromDBIndex = True
        if (loadfromDBIndex):
            db = dupiebase.dupiebase()
            _dto = db.getSessionInfo(1001)


            self.numofanswers = int(_dto["ANSWERS"])
            self.questionIndex = int(_dto["QUESTION_INDEX"])
            self.language1 = _dto["LANG_QUESTION"]
            self.language2 = _dto["LANG_ANSWER"]

            self.questions = db.getQuestionList(1001)
            self.answerlist = db.getAnswerList(1001)
            self.answerlistanimation = db.getAnswerListAnimation(1001)
            
            #import pprint
            #print( pprint.pformat(self.questions))




        else:
            self.numofanswers = numofanswers
            self.questionIndex = 0
            self.language1 = language1
            self.language2 = language2

            self.lexicon = self.getLexicon(language1,language2)
            self.questions = self.setQuestion(numofquestions)

        self.prompt = self.getPrompt(self.language2)

        self._langDTO = {
            "languageshort1": longtoshort[self.language1],
            "languageshort2": longtoshort[self.language2],
            "languagelong1": shorttolong[self.language1],
            "languagelong2": shorttolong[self.language2],
            }


    def nextQuestion(self):
        self.questionIndex+=1
        return (self.questionIndex < self.numofanswers)
        
        
    def setQuestion(self,numofquestions):

        _questions = copy.deepcopy(self.lexicon)
        del _questions[numofquestions:]
        return _questions
        


    def getLexicon(self,language1,language2):


        db = dupiebase.dupiebase()
        _lexicon = db.getLexiconETL(language1,language2)
        random.shuffle(_lexicon)

        return (_lexicon)
    
    def getPrompt(self,language2):
        db = dupiebase.dupiebase()
        return (db.getQuestionFormat(longtoshort[language2]))

    def getAnswerList(self):
        _answerlist = copy.deepcopy(self.lexicon)
        random.shuffle(_answerlist)
        del _answerlist[self.numofanswers:]
        _answerFound = self.checkAnswerListForCorrectAnswer(self.questionIndex, _answerlist)
        return _answerlist, _answerFound

    def checkAnswerListForCorrectAnswer(self, questionIndex, answerlist):
        _ansnwerFound = False
        #print (self.questions[questionIndex])

        _answer = self.questions[questionIndex]["answer"]
        for x in answerlist:
            if _answer == x["answer"]:
                _ansnwerFound = True
        return _ansnwerFound

    def checkAnswer(self, userAnswer):
        return (userAnswer == self.questions[self.questionIndex]["ANSWER"])


    def getQuestion(self):
        return self.questions[self.questionIndex]
   



    # TODO: move to quiz
    def setAnswerList2(self):
        _answerFound = False
        while not _answerFound:
            _dto_list, _answerFound = self.getAnswerList()

        dto = []

        for answer in _dto_list:
            _dto = {}
            _dto = {
                "answer":answer["answer"],
                "answer_audio":"%s-%s.mp3" % (
                    answer["vocabulary_index"],
                    self._langDTO["languageshort2"]
                    ),
                "vocabulary_index":answer["vocabulary_index"]
            }
            dto.append(_dto)

        self.answerlist = dto
        return dto

    # TODO: move to quiz
    def setAnswerListAnimation2(self):
        mixes = 10

        DTO_LIST = []
        for x in range(0, mixes):
            __dto = []
#            print ("reset")
            _answerFound = True
            _answerList = []
            while _answerFound:
                _answerList, _answerFound = self.getAnswerList()
#                print(_answerList)

            for answer in _answerList:
                _dto = {}
                _dto = {
                    "answer":answer["answer"],
                    "answer_audio":"",
                    "vocabulary_index":"0"

                }
                __dto.append(_dto)

            DTO_LIST.append(__dto)

        self.answerlistanimation = DTO_LIST
        return DTO_LIST
    

if __name__ == "__main__":
    import pprint
    # print(pprint.pformat(testClass.lexicon))
    # print("-"*11)
    # print(pprint.pformat(testClass.questions))
    # print("="*11)
    # print(pprint.pformat(testClass.prompt))
    # print("-"*11)
    #print(pprint.pformat(testClass.getQuestion()))
    # #print (testClass.questions)

    #print(pprint.pformat(testClass.questions))



   
    def test_save():
        testClass = dupiequiz("english","zhongwen",3,6)
        db = dupiebase.dupiebase()

        _questions = copy.deepcopy(testClass.questions)
        db.SaveQuestions(1001,101,_questions)

        for x in range(0, 3): 
            _answers = copy.deepcopy(testClass.setAnswerList2())
            shuffle = 0
            db.SaveAnswers(1001,shuffle,x,_answers,0)

            mixes = 10
            _answers2 = copy.deepcopy(testClass.setAnswerListAnimation2())

            for y in range(0, mixes): 
                shuffle = 1
                db.SaveAnswers(1001,shuffle,x,_answers2[y],y)
            testClass.nextQuestion()        


    def test_load():
        testClass = dupiequiz(loadfromDBIndex=1001)
        #db = dupiebase.dupiebase()
        #print(pprint.pformat(db.getSessionInfo(1001)))


    test_save()
    pass
