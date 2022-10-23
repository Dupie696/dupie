import jinja2
secret="dupiedupiedupie!Ana!Duppy!DyppyDyppyDuppy!"
import os.path



class WSGIToolsClass():
    def __init__(self):
        self.bottle.post ("/newuser")                       (self.createAccount)
        self.bottle.route("/resource/<folder>/<filename>")  (self.getStaticFiles)
        self.bottle.route("/favicon.ico")  (self.getStaticICO)

        self.bottle.route("/")          (self.checkAuth(self.loadMainPage))
        self.bottle.route("/deleteuser")(self.checkAuth(self.deletemyaccount))
        super().__init__()

    def getStaticICO(self):
        return self.bottle.static_file("favicon.ico", root='/var/www/wsgi/dupie/resource/img/')


    def createAccount(self):
        username = self.bottle.request.forms.get("username")
        self.bottle.response.set_cookie("username",username,secret=secret )
        self.bottle.response.set_cookie("uid",101, secret=secret)
        self.bottle.response.set_cookie("sessionid",1001, secret=secret)
        return self.getTemplate('user_new_post.html').render(
                DTO={ "username":username },
                BreadCrumbs=[]
                )

    def getStaticFiles(self,folder, filename):
        # if developing comment out below line
        if (filename[-3:] != "mp3" and filename[-3:] != "css" and filename[-3:] != ".js"):
            self.bottle.response.set_header('Cache-Control', 'must-revalidate')
        else:
#            self.bottle.response.set_header("Cache-Control", "public, max-age=604800")
            print (filename)

        # TODO: this probably isn't necessary, but will put regex here
        #   if filename in ["aquabutton.jpg","nh1.mp3","questionbox.jpg"]:
        if (folder=="vocab") or (folder=="prompt"):
            if (os.path.isfile("/var/www/wsgi/dupie/resource/%sx/%s" % (folder,filename))):
                return self.bottle.static_file(filename, root='/var/www/wsgi/dupie/resource/%sx' % (folder))

            
        return self.bottle.static_file(filename, root='/var/www/wsgi/dupie/resource/%s' % (folder))
        #   else:
        #      return bottle.abort(404, "File not found.")

    def loadMainPage(self):
        return self.getTemplate('main_main_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[]
                )

    def deletemyaccount(self):
        self.bottle.response.delete_cookie("username") 
        self.bottle.response.delete_cookie("uid") 
        self.bottle.response.delete_cookie("sessionid") 
        return self.getTemplate('user_delete_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[]
                )

    def cookie(self,name):
        return self.bottle.request.get_cookie(name, secret=secret)

    def getTemplate(self, document):
        file_loader = jinja2.FileSystemLoader(
            [
                "/var/www/wsgi/dupie/template/quiz",
                "/var/www/wsgi/dupie/template/tools",
                "/var/www/wsgi/dupie/template/templates",
                "/var/www/wsgi/dupie/template/videos",
                "/var/www/wsgi/dupie/template/ttsbatchload",
                "/var/www/wsgi/dupie/template/review"
            ]
            
            )
        env = jinja2.Environment(loader=file_loader)
        template = env.get_template(document)
        return template






class CheckAuthClass():
    def __init__(self):
        super().__init__()

    def butWhoAreYou(self):
        return self.getTemplate('user_new_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[]
                )

    def userUnknown(self):
        self.bottle.response.set_header('Cache-Control', 'must-revalidate')
        return (str(self.bottle.request.get_cookie("username",secret=secret)) == "None")

    def checkAuth(self, bottle_function):
        def wrapper(*args, **kwargs):
            if self.userUnknown(): 
                return self.butWhoAreYou()
            else:
                return bottle_function(*args, **kwargs)
        return wrapper