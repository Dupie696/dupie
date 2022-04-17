import dupiegame
import time

class dupiecli(dupiegame.dupiegame):
    def printQuizQuestion(self):
        # makes an question shuffling animation

        for x in self.getAnswerListAnimation():
            self.printQuestion()
            self.printAnswerList(x)
            time.sleep(0.1)
        
        # prints final question box
        self.printQuestion()
        # prints final answer list
        _AnswerList = (self.getAnswerList())

        #print (_AnswerList); exit(0)
        self.printAnswerList(self.getAnswerList())

        # gets user input and corresponding answer
        userAnswer = _AnswerList[-1+int(self.printAnsweringBlock())]

        # provides user feedback if answer is correct or not
        print ()
        if self.quiz.checkAnswer(userAnswer["ANSWER"]):
            input ("You are correct!")
        else:
            input ("you are incorrect")
        print ()
    
    def printQuestion(self):
        # clears the screen
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

        # quests question and prints a banner
        _questionText = self.getQuestionMessage()
        print("".center(120, "="))

        # TODO: compare UTF-8 length to ANSI length and apply offsets
        #print("%s,s" %  ))
        offset = len(_questionText) - len(_questionText.encode("ascii", "ignore"))
        print((" %s " % _questionText).center(120 - offset, "="))
        print("".center(120, "="))

    def getQuestionMessage(self):
        # formats the question with selected languages
        dto = self.getQuestion()
        return "%(PRE)s %(QUESTION)s %(POST)s" % dto

    def printAnswerList(self,_AnswerList):
        # formats and populates the answer list
        _counter = 0
        #print (_AnswerList)
        for x in _AnswerList:
            _counter+=1
            offset = len(x["ANSWER"]) - len(x["ANSWER"].encode("ascii", "ignore"))
            print((" %s) %s " % (_counter, x["ANSWER"])).center(40-offset, " "), end='')
            if not _counter % 3:
                print()

    def printAnsweringBlock(self):
        # user input checking
        _answer = ""
        _answers = [str(i) for i in range(1,self.numofanswers+1)]
        #print(self.numofanswers)

        # loops until input is within the number of questions
        while (not _answer in _answers):
            _answer = input("Select Answer: ")

        return _answer


if __name__ == "__main__":
    quiz = dupiecli(loadfromDBIndex=1001)
#    quiz = dupiecli("english","english",3,3)
#    quiz = dupiecli("espanol","espanol",3,3)
    #quiz = dupiecli("english","hangugeo",3,3)
    # quiz = dupiecli("nihon","english",3,3)
    

    

    quiz.printQuizQuestion()
    quiz.nextQuestion()
    quiz.printQuizQuestion()
    quiz.nextQuestion()
    quiz.printQuizQuestion()
    quiz.nextQuestion()
    quiz.printQuizQuestion()
