import sys
import bottle
import jinja2
import dupiebase

global sessions
sessions = {}
sessions[101] = {
   "question": "sorry",
   "prompt1": "¿Cómo se dice",
   "prompt2": "en español?",

   "answer": "Lo siento",
   "choices": ["Hola","Adiós","Por favor","Gracias","Lo siento","Salud","Sí","No","Quién","Qué","Por qué","Dónde"],
   "choicesAudio":["1001-es.mp3","1002-es.mp3","1003-es.mp3","1004-es.mp3","1005-es.mp3","1006-es.mp3","1007-es.mp3","1008-es.mp3","1009-es.mp3","1010-es.mp3","1011-es.mp3","1012-es.mp3"],
   "questiuonAudio": ["es-es-1.mp3","1005-en.mp3","es-es-2.mp3"]

}


dto = dupiebase.dupiebase().getVocabDump()


# dto = {
# #   "1000":["Spanish", "English", "Swedish", "German", "Chinese", "French"],
#    "1001":["Hola","Hello", "Hallo","Hej","你好","Bonjour"],
#    "1002":["Adiós","Goodbye","Auf Wiedersehen","Hej då","再见","Au revoir"],
#    "1003":["Por favor","Please","Bitte","Snälla","请","S'il vous plaît"],
#    "1004":["Gracias","Thank you","Danke","Tack","谢谢","Merci"],
#    "1005":["Lo siento","Sorry","Entschuldigung","Ursäkta/Ledsen","不好意思","Pardon"],
#    "1006":["Salud","Bless you","Gesundheit","Prosit",None,None],
#    "1007":["Sí","Yes","Ja","Ja","是的","Oui"],
#    "1008":["No","No","Nein","nej","不","Non"],
#    "1009":["Quién","Who","Wer","Vem","谁","Qui"],
#    "1010":["Qué","What","Was","Vad","什么","Que"],
#    "1011":["Por qué","Why","Wieso","Varför","为什么","Pourquoi"],
#    "1012":["Dónde","Where","Wo","Var","在哪里","Où"]
# }

@bottle.route('/<sessionID>/resource/<folder>/<filename>')
def server_static(folder, filename,sessionID):
# TODO: this probably isn't necessary, but will put regex here
#   if filename in ["aquabutton.jpg","nh1.mp3","questionbox.jpg"]:
   return bottle.static_file(filename, root='/var/www/wsgi/dupie/resource/%s' % (folder))
#   else:
#      return bottle.abort(404, "File not found.")

@bottle.route('/ajax/test')
def test():
   return "this was a test"

@bottle.route('/')
def hello():
   # quiz =  [dto[dtoindex]['espanol'] for dtoindex in dto]
   # file_loader = jinja2.FileSystemLoader("/var/www/wsgi/dupie/template")
   # env = jinja2.Environment(loader=file_loader)
   # template = env.get_template('main.jinja2')
   # DTO = {"questions":quiz}
   # output = template.render(DTO=DTO)
   # return output
   return '<a href="/101/">clickme</a>'

@bottle.route('/<sessionID>/')
def StartSession(sessionID):

   # quiz =  [dto[dtoindex]['espanol'] for dtoindex in dto]
   file_loader = jinja2.FileSystemLoader("/var/www/wsgi/dupie/template/quiz/")
   env = jinja2.Environment(loader=file_loader)
   template = env.get_template('quiz.html')
   DTO = sessions[101]
   output = template.render(DTO=DTO)
   # return output

   return (output)



@bottle.route('/<sessionID>/getTime')
def getTime(sessionID):
   import time
   seconds = time.time()
   return ("Seconds since epoch = %s" % seconds)	

@bottle.route('/<sessionID>/getQuestion')
def getQuestion(sessionID):
   return "%(prompt1)s '%(question)s' %(prompt2)s" % sessions[int(sessionID)]

@bottle.route('/<sessionID>/getAnswers')
def getAnswers(sessionID):
   return ("getAnswers")

@bottle.route('/<sessionID>/newQuestion')
def newQuestion(sessionID):
   sessions[101] = {
      "question": "yes",
      "prompt1": "¿Cómo se dice",
      "prompt2": "en español?",

      "answer": "Sí",
      "choices": ["Hola","Adiós","Por favor","Gracias","Lo siento","Salud","Sí","No","Quién","Qué","Por qué","Dónde"],
      "choicesAudio":["1001-es.mp3","1002-es.mp3","1003-es.mp3","1004-es.mp3","1005-es.mp3","1006-es.mp3","1007-es.mp3","1008-es.mp3","1009-es.mp3","1010-es.mp3","1011-es.mp3","1012-es.mp3"],
      "questiuonAudio": ["es-es-1.mp3","1007-en.mp3","es-es-2.mp3"]

   }
   return


@bottle.route('/<sessionID>/checkAnswer/<SelectedAnswer>')
def checkAnswer(sessionID,SelectedAnswer):
   #if  == 4:
   if sessions[int(sessionID)]["answer"] == sessions[int(sessionID)]["choices"][int(SelectedAnswer)]:
      return "True"
   else:
      return "False"
