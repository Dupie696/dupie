import sys
import bottle
import jinja2
import dupieweb

secret="dupiedupiedupie!Ana!Duppy!DyppyDyppyDuppy!"

@bottle.route('/resource/<folder>/<filename>')
def server_static(folder, filename):
   # if developing comment out below line
   bottle.response.set_header('Cache-Control', 'must-revalidate')

# TODO: this probably isn't necessary, but will put regex here
#   if filename in ["aquabutton.jpg","nh1.mp3","questionbox.jpg"]:
   return bottle.static_file(filename, root='/var/www/wsgi/dupie/resource/%s' % (folder))
#   else:
#      return bottle.abort(404, "File not found.")



# @bottle.route('/test/<test>')
# @checkAuth
# def testestPage(test):
#    return test



############################################################################################################################################
############################################################################################################################################

def butWhoAreYou():
   return getTemplate('user_new_get.html').render(
         DTO={ "username":cookie("username")},
         BreadCrumbs=[]
         )


def userUnknown():
   bottle.response.set_header('Cache-Control', 'must-revalidate')
   return (str(bottle.request.get_cookie("username",secret=secret)) == "None")

def getTemplate(document):
   # if "." in document.split("/")[0]:
   #    print ("/var/www/wsgi/dupie/template/")
   # elif document.split("/")[0] in ["account","quiz","video"]:
   #    print ("/var/www/wsgi/dupie/template/%s" % document.split("/")[0])
   # else:
   #    raise ValueError('A very specific bad thing happened, what is: %s' % document)


   file_loader = jinja2.FileSystemLoader("/var/www/wsgi/dupie/template/")
   env = jinja2.Environment(loader=file_loader)
   template = env.get_template(document)
   return template

def checkAuth(bottle_function):
   def wrapper(*args, **kwargs):
      if userUnknown(): 
         return butWhoAreYou()
      else:
         return bottle_function(*args, **kwargs)
   return wrapper

def cookie(name):
   return bottle.request.get_cookie(name, secret=secret)


@bottle.route('/')
@checkAuth
def loadMainPage():
   return getTemplate('main_main_get.html').render(
         DTO={ "username":cookie("username")},
         BreadCrumbs=[]
         )



@bottle.route('/WatchVideo')
@checkAuth
def watchVideo():
   return getTemplate('video_menu_get.html').render(
         DTO={ "username":cookie("username")},
         BreadCrumbs=[{"Video Menu":"/WatchVideo"}]
         )




@bottle.route('/deleteuser')
@checkAuth
def deletemyaccount():
   bottle.response.delete_cookie("username") 
   bottle.response.delete_cookie("uid") 
   bottle.response.delete_cookie("sessionid") 
   return getTemplate('user_delete_get.html').render(
         DTO={ "username":cookie("username")},
         BreadCrumbs=[]
         )



@bottle.post('/newuser')
def createaccount():
   username = bottle.request.forms.get("username")
   bottle.response.set_cookie("username",username,secret=secret )
   bottle.response.set_cookie("uid",101, secret=secret)
   bottle.response.set_cookie("sessionid",1001, secret=secret)
   return getTemplate('user_new_post.html').render(
         DTO={ "username":username },
         BreadCrumbs=[]
         )



@bottle.route('/quiz/101')
@checkAuth
def doQuiz():
   
   #loadQuestion(101,1001)
   return getTemplate('quiz_list_get.html').render(
         DTO={ },
         BreadCrumbs=[{"Quizzes":"/quiz"}]
         )

@bottle.route('/quiz/101/1001')
@checkAuth
def doQuiz():
   return getTemplate('quiz_main_get.html').render(
         DTO={ },
         BreadCrumbs=[{"Quizzes":"/quiz"},{"Pollito Tito":"/WatchVideo/PollitoTito"}]
         )

@bottle.route('/WatchVideo/PollitoTito')
@checkAuth
def watchPollitoTito():
   return getTemplate('video_watch_get.html').render(
         DTO={ "username":cookie("username")},
         BreadCrumbs=[{"Video Menu":"/WatchVideo"},{"Pollito Tito":"/WatchVideo/PollitoTito"}]
         )

if __name__ == "__main__":
   pass