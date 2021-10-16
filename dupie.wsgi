import sys
sys.path.insert(0, "/var/www/wsgi/learner/src")
import bottle
import learner
application = bottle.default_app()
