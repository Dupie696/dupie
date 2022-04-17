import sys
import bottle

import class_templates.wsgi
import website.auxwebpages

CheckAuth = class_templates.wsgi.CheckAuthClass(bottle)
secret="dupiedupiedupie!Ana!Duppy!DyppyDyppyDuppy!"

class DupieWSGI(class_templates.wsgi.std_wsgi,
                website.auxwebpages.AuxWebpagesClass):
    def __init__(self,bottle):
        self.bottle = bottle
        self.bottle.route("/resource/<folder>/<filename>")                      (self.server_static)

        self.bottle.route("/")                              (CheckAuth.checkAuth(self.loadMainPage))
        self.bottle.route("/WatchVideo")                    (CheckAuth.checkAuth(self.watchVideo))
        self.bottle.route("/WatchVideo/PollitoTito")        (CheckAuth.checkAuth(self.watchPollitoTito))
        self.bottle.route("/deleteuser")                    (CheckAuth.checkAuth(self.deletemyaccount))
        self.bottle.post ("/newuser")                                           (self.createaccount)

    def loadMainPage(self):
        return self.getTemplate('main_main_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[]
                )

    def deletemyaccount(self):
        bottle.response.delete_cookie("username") 
        bottle.response.delete_cookie("uid") 
        bottle.response.delete_cookie("sessionid") 
        return self.getTemplate('user_delete_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[]
                )

    def createaccount(self):
        username = bottle.request.forms.get("username")
        bottle.response.set_cookie("username",username,secret=secret )
        bottle.response.set_cookie("uid",101, secret=secret)
        bottle.response.set_cookie("sessionid",1001, secret=secret)
        return self.getTemplate('user_new_post.html').render(
                DTO={ "username":username },
                BreadCrumbs=[]
                )


if __name__ == "__main__":
    pass