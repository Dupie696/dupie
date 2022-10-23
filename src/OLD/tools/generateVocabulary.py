import sys
sys.path.insert(0, "/var/www/wsgi/dupie/src")
import apis.databases

txtfile="""
1	yo	I
2	tu	you
3	y	and
4	pero 	but
5	es	is
6	esto	this
7	como	what/how
8	no sé	do not know
9	no es	is not
10	explicarlo	explain
11	asustado	afraid
12	culpa	fault"""[1:]



db = apis.databases.mysql_database_connector()

query = """INSERT INTO DUPIE.VOCABULARY
(EN, ES, DE, SV, ZH, FR, AR, AR2, ZH2, SYNONYM, JP, JP2, KO, KO2, RU, RU2)
VALUES('%s', '%s', '', '', '', '', '', '', '', NULL, '', '', '', '', '', '');
"""



import pprint
x = txtfile.split("\n")
z = [y.split("\t") for y in x]
print(pprint.pformat(z))

import os

os.system("touch test.mp4")

for i in z:
    sound_sound_file = ("Sound\\ %s.mp3" % (i[0]))
#    print ("the source sound file is: %s" % sound_sound_file)

    newsoundfileindex = db.update(query % (i[2],i[1]))

    print ("mv %s %s-ES.mp3" % (sound_sound_file,newsoundfileindex))
    os.system("mv %s %s-ES.mp3" % (sound_sound_file,newsoundfileindex))



