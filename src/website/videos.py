class VideoWebpagesClass():
    def __init__(self):
        self.bottle.route("/WatchVideo")            (self.checkAuth(self.watchVideo))
        self.bottle.route("/WatchVideo/PollitoTito")(self.checkAuth(self.watchPollitoTito))
        super().__init__()

    def watchVideo(self):
        return self.getTemplate('video_menu_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[{"Video Menu":"/WatchVideo"}]
                )

    def watchPollitoTito(self):
        return self.getTemplate('video_watch_get.html').render(
                DTO={ "username":self.cookie("username")},
                BreadCrumbs=[{"Video Menu":"/WatchVideo"},{"Pollito Tito":"/WatchVideo/PollitoTito"}]
                )