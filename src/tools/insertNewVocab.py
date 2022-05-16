textfile = """
3001	Pollito	Little Chicken
3002	Tito	<male pet name>
3003	Deja que te cuente	Let me tell you
3004	Deja	Let me
3005	que	what?/that
3006	te	you
3007	Cuente	Tell you
3008	un/una	a
3009	historia	history/story
3010	sobre	about
3011	pollito	chicken 
3012	su	your/their
3013	nombre	name
3014	es	is
3015	Tito	Tito
3016	Él	He
3017	vive	lives
3018	en	in
3019	gallinero	hen house
3020	pequeño	small
3021	y	and
3022	normal	normal
3023	en	in
3024	vecindario	neighborhood
3025	pequeño	small
3026	normal	normal
3027	pollito	chicken
3028	no	no
3034	alto	tall
3035	ni	neither
3036	bajo	short
"""[1:-1]

import sys
sys.path.insert(0, "/var/www/wsgi/dupie/src")
import pprint
import apis.databases
import os

x = textfile.split("\n")
z = [y.split("\t") for y in x]
print(pprint.pformat(z))


db = apis.databases.mysql_database_connector()

query = """INSERT INTO DUPIE.VOCABULARY
(EN, ES, DE, SV, ZH, FR, AR, AR2, ZH2, SYNONYM, JP, JP2, KO, KO2, RU, RU2)
VALUES('%s', '%s', '', '', '', '', '', '', '', '%s', '', '', '', '', '', '');
"""


for i in z:
    sound_sound_file = ("/var/www/wsgi/dupie/resource/vocabx/%s.wav" % (i[0]))
    newsoundfileindex = db.update(query % (i[2],i[1],i[0]))
    os.system("ffmpeg -i %s /var/www/wsgi/dupie/resource/vocabx/%s-ES.mp3" % (sound_sound_file,newsoundfileindex))
