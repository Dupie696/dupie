
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

longtoshort = {
 "english":"en",
 "espanol":"es",
 "zhongwen":"zh"}


shorttolong = {
 "en":"english",
 "es":"espanol",
 "zh":"zhongwen"}


class dupiequiz:
    def __init__(self,language1,language2,numofquestions,numofanswers):
        self.lexicon = self.getLexicon(language1,language2)
        self.questions = self.setQuestion(numofquestions)
        self.prompt = self.getPrompt(language2)
        self.numofanswers = numofanswers
        self.language1 = language1
        self.language2 = language2

        self.questionIndex = 0
        
        
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
        #print ("answerlist: %s " % _answerlist)
        _answerFound = self.checkAnswerListForCorrectAnswer(self.questionIndex, _answerlist,self.language2)
        return _answerlist, _answerFound

    def checkAnswerListForCorrectAnswer(self, questionIndex, answerlist, language2):
        _ansnwerFound = False
        _answer = self.questions[questionIndex][language2]
        for x in answerlist:
            if _answer == x[language2]:
                _ansnwerFound = True
        return _ansnwerFound

    def checkAnswer(self, userAnswer):
        return (userAnswer == self.questions[self.questionIndex][self.language2])


    def getQuestion(self):
        return self.questions[self.questionIndex]


if __name__ == "__main__":
    testClass = dupiequiz("english","espanol",2,2)
    print(testClass.lexicon)
    print(testClass.questions)
    print("="*11)
    print(testClass.prompt)
    print(testClass.getQuestion())

    pass