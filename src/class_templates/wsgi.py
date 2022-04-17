import jinja2
secret="dupiedupiedupie!Ana!Duppy!DyppyDyppyDuppy!"


class std_wsgi():
    def cookie(self,name):
        return self.bottle.request.get_cookie(name, secret=secret)


#    @bottle.route('/resource/<folder>/<filename>')
    def server_static(self,folder, filename):
        # if developing comment out below line
        self.bottle.response.set_header('Cache-Control', 'must-revalidate')

        # TODO: this probably isn't necessary, but will put regex here
        #   if filename in ["aquabutton.jpg","nh1.mp3","questionbox.jpg"]:
        return self.bottle.static_file(filename, root='/var/www/wsgi/dupie/resource/%s' % (folder))
        #   else:
        #      return bottle.abort(404, "File not found.")


    def getTemplate(self, document):
        file_loader = jinja2.FileSystemLoader("/var/www/wsgi/dupie/template/")
        env = jinja2.Environment(loader=file_loader)
        template = env.get_template(document)
        return template


    def userUnknown(self):
        self.bottle.response.set_header('Cache-Control', 'must-revalidate')
        return (str(self.bottle.request.get_cookie("username",secret=secret)) == "None")    


class CheckAuthClass(std_wsgi):

    def __init__(self,bottle):
        self.bottle = bottle

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