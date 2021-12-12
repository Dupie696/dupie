# Dupie
Universal Multiple Choice Language Learner


## Requirements
 - Linux OS (CentOS/Fedora/RHEL)
 - Python 3.x
 - WSGI
 - Apache 2.x
 - mysql/mariaDB
 - mod_ssl


## Installation
 * add below to /etc/httpd/conf/httpd.conf
 * WSGIScriptAlias / "/var/www/wsgi/dupie/dupie.wsgi"


DupieBase - pulls data from database, and renames fields, etc.
DupieQuiz - ADT holds all the data (could be an array of ADTs)
DupieGame - class that gets inherited, core functionality goes here

DupieCLI - user interface for DupieGame - CLI module
or
DupieWeb - user interface for DupieGame - Web module