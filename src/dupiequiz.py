# SessionInfo
# {
#  'LANG_ANSWER': 'ZH',
#  'LANG_QUESTION': 'EN',
#
#  'QUESTIONS': 3,
#  'ANSWERS': 6,
#  'SHUFFLES': 10,
#
#  'QUESTION_INDEX': 0,
#  'SESSIONID': 1001,
#
#  'FRIENDLYNAME': 'Kelly',
#  'UID': 101,

# Questions
# [{'ANSWER': '什么',
#   'ANSWER_AUDIO': '1010-zh.mp3',
#   'QUESTION': 'What',
#   'QUESTION_AUDIO': '1010-en.mp3',
#   'QUIZQUESTION_INDEX': 0,
#   'VOCABULARY_INDEX': 1010},
#  ...
#  {'ANSWER': '不',
#   'ANSWER_AUDIO': '1008-zh.mp3',
#   'QUESTION': 'No',
#   'QUESTION_AUDIO': '1008-en.mp3',
#   'QUIZQUESTION_INDEX': 2,
#   'VOCABULARY_INDEX': 1008}]




import dupiebase
import random
import copy
import pprint

db = dupiebase.dupiebase()

class dupiequiz:
    questions = []
    lexicon = []
    prompt = {}
    numofanswers = 0

    def __init__(self,questionlanguage=None,answerlanguage=None,numofquestions=None,numofanswers=None,loadfromDBIndex=0,quickload=False):
        # master list of words
        if not quickload:
            if (loadfromDBIndex):
            
                LoadedSessionDTO = db.getSessionInfo(1001)


                self.numofanswers = int(LoadedSessionDTO["ANSWERS"])
                self.questionIndex = int(LoadedSessionDTO["QUESTION_INDEX"])
                self.questionlanguage = LoadedSessionDTO["LANG_QUESTION"]
                self.answerlanguage = LoadedSessionDTO["LANG_ANSWER"]

                self.questions = db.getQuestionList(1001)

                self.answerlist = db.getAnswerList(1001)
                self.answerlistanimation = db.getAnswerListAnimation(1001)
                print (pprint.pformat(self.answerlist))

            else:
                self.numofanswers = numofanswers
                self.questionIndex = 0
                self.questionlanguage = questionlanguage
                self.answerlanguage = answerlanguage

                self.lexicon = self.getLexicon(questionlanguage,answerlanguage)
                self.questions = self.setQuestion(numofquestions)

            self.prompt = self.getPrompt(self.answerlanguage)
        else:
            pass

    def nextQuestion(self):
        self.questionIndex+=1
        return (self.questionIndex < self.numofanswers)
        
        
    def setQuestion(self,numofquestions):

        _questions = copy.deepcopy(self.lexicon)
        del _questions[numofquestions:]
        return _questions
        


    def getLexicon(self,questionlanguage,answerlanguage):


        db = dupiebase.dupiebase()
        _lexicon = db.getLexiconETL(questionlanguage,answerlanguage)
        random.shuffle(_lexicon)

        return (_lexicon)
    
    def getPrompt(self,answerlanguage):
        db = dupiebase.dupiebase()
        return (db.getQuestionFormat(answerlanguage))

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

    def loadQuestion(self, uid, sessionid):
        return db.getUserSession(uid, sessionid)
        pass
    

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


    #test_load()
    pass
    def quickload():
        testClass = dupiequiz(quickload=True)
        print (testClass.loadQuestion(101,1001))

    quickload()
