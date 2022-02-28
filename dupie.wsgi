import sys
sys.path.insert(0, "/var/www/wsgi/dupie/src")
import bottle
import dupiewsgi
application = bottle.default_app()
