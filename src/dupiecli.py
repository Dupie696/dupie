
import dupiequiz
import time

class dupiecli:
    def __init__(self,language1,language2,numofquestions,numofanswers):
        self.testClass = dupiequiz.dupiequiz(language1,language2,numofquestions,numofanswers)
        self.prompt = self.setPrompt(language2)
        self.language1 = language1
        self.language2 = language2
        self.numofanswers = numofanswers


    def setPrompt(self,language2):
        _prompt = self.testClass.getPrompt(language2)[0]
        return(_prompt["pre"] + " '%s' " + _prompt["post"])

    def getQuestionMessage(self):       
        return self.prompt % self.testClass.getQuestion()[self.language1]
    
    def getAnswerList(self):
        dto = []
        _answerList, _answerFound = self.testClass.getAnswerList()
        for i in _answerList:
            dto.append(i[self.language2])

        return (dto,_answerFound)
    
    def printQuestion(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

        _questionText = self.getQuestionMessage()
        print("".center(120, "="))
        print((" %s " % _questionText).center(120, "="))
        print("".center(120, "="))

    def printAnswerList(self):
        _AnswerList, _answerFound = self.getAnswerList()
        print()
        _counter = 0

        for x in _AnswerList:
            _counter+=1
            print((" %s) %s " % (_counter, x)).center(40, " "), end='')
            if not _counter % 3:
                print()

        print()
        
        return _AnswerList, _answerFound

    def printAnsweringBlock(self):
        _answer = ""
        _answers = [str(i) for i in range(1,self.numofanswers+1)]

        while (not _answer in _answers):
            _answer = input("Select Answer: ")

        return _answer

    def printQuizQuestion(self):
        _answerFound = False
        while(not _answerFound):
            self.printQuestion()
            _AnswerList, _answerFound = self.printAnswerList()
            time.sleep(0.1)
        
        userAnswer = _AnswerList[-1+int(self.printAnsweringBlock())]

        self.testClass.checkAnswer(userAnswer)
    


if __name__ == "__main__":
#    testClass = dupiecli("english","zhongwen",3,3)
#    testClass = dupiecli("english","english",3,3)
    testClass = dupiecli("espanol","espanol",3,3)

    

    testClass.printQuizQuestion()
