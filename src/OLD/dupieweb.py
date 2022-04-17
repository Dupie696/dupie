import dupiegame

#global sessionsClass

class dupieweb(dupiegame.dupiegame):
   def passpass():
      pass
   # def __init__(self,language1,language2,numofquestions,numofanswers):
   #    self.quiz = dupiequiz.dupiequiz(language1,language2,numofquestions,numofanswers)
   #    self.language1 = language1
   #    self.language2 = language2
   #    self.numofanswers = numofanswers
   #    self.numofquestions = numofquestions

   # def nextQuestion(self):
   #    return self.quiz.nextQuestion()

   # def getQuestion(self):
   #    _question = self.quiz.getQuestion()[self.language1]
   #    _prompt = self.quiz.getPrompt(self.language2)[0]
   #    _template = "%s '%s' %s" % (_prompt['pre'],_question,_prompt['post'])

   #    return _template

   # def getDTO(self):
   #    prompts = self.quiz.getPrompt(self.language2)[0]
   #    answerfound = False
   #    while(not answerfound):
   #       answerlist,answerfound = self.quiz.getAnswerList()

   #    self.answerlist = answerlist

   #    questionaudio_template = "%s-" + longtoshort[self.language1] + ".mp3"
   #    choiceaudio_template = "%s-" + longtoshort[self.language2] + ".mp3"

   #    sessions = {
   #       "question": self.quiz.getQuestion()[self.language1],
   #       "prompt1": prompts['pre'],
   #       "prompt2": prompts['post'],
   #       "choices": [dtoindex[self.language2] for dtoindex in answerlist],
   #       "choicesAudio":[choiceaudio_template % dtoindex["vocabulary_index"] for dtoindex in answerlist],
   #       "questionAudio": ["%s-%s-1.mp3" % (longtoshort[self.language2],longtoshort[self.language2]),
   #                questionaudio_template % self.quiz.getQuestion()['vocabulary_index']
   #                ,"%s-%s-2.mp3"% (longtoshort[self.language2],longtoshort[self.language2])]
   #    }
   #    self.sessions = sessions
   #    return sessions

   # def checkAnswer(self,SelectedAnswer):
   #    #print (self.answerlist[int(SelectedAnswer)])
   #    return self.quiz.checkAnswer(SelectedAnswer)





# @bottle.route('/<sessionID>/resource/<folder>/<filename>')
# def server_static(folder, filename,sessionID):
#    # if developing comment out below line
#    bottle.response.set_header('Cache-Control', 'must-revalidate')

# # TODO: this probably isn't necessary, but will put regex here
# #   if filename in ["aquabutton.jpg","nh1.mp3","questionbox.jpg"]:
#    return bottle.static_file(filename, root='/var/www/wsgi/dupie/resource/%s' % (folder))
# #   else:
# #      return bottle.abort(404, "File not found.")




# @bottle.route('/<sessionID>/')
# def StartSession(sessionID):
#    bottle.response.set_header('Cache-Control', 'must-revalidate')

#    file_loader = jinja2.FileSystemLoader("/var/www/wsgi/dupie/template/quiz/")
#    env = jinja2.Environment(loader=file_loader)
#    template = env.get_template('quiz.html')
   
#    DTO = sessionsClass.getDTO()
#    output = template.render(DTO=DTO)

#    return (output)

# @bottle.route('/<sessionID>/getQuestion')
# def getQuestion(sessionID):
#    bottle.response.set_header('Cache-Control', 'must-revalidate')
#    return sessionsClass.getQuestion()

# @bottle.route('/<sessionID>/newQuestion')
# def newQuestion(sessionID):
#    bottle.response.set_header('Cache-Control', 'must-revalidate')
#    if sessionsClass.nextQuestion():
#       print ("TRUE")
#       return "True"
#    else:
#       print ("False")
#       return "False"
#    # print (_return)
#    # return _return


# @bottle.route('/<sessionID>/checkAnswer/<SelectedAnswer>')
# def checkAnswer(sessionID,SelectedAnswer):
#    bottle.response.set_header('Cache-Control', 'must-revalidate')
#    if sessionsClass.checkAnswer(sessionsClass.sessions["choices"][int(SelectedAnswer)]):
#       return "True"
#    else:
#       return "False"



#sessionsClass = dupieweb(numofanswers=True,loadfromDBIndex=1001)
#sessionsClass = dupieweb("english","espanol",9,9)
#sessionsClass = dupieweb("nihon","hangugeo",9,9)
#sessionsClass = dupieweb("zhongwen","hangugeo",3,3)


if __name__ == "__main__":
    def quickload():
        testClass = dupieweb(quickload=True)
        print (testClass.loadQuestion(101,1001))

    quickload()