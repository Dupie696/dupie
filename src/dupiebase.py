import mysql.connector


longtoshort = {
 "english":"en",
 "espanol":"es",
 "nihon":"ja",
 "zhongwen":"zh",
 "hangugeo":"ko"}


class dupiebase:
    def __init__(self):
        # setups database connection
        try:
            self.conn = mysql.connector.connect(
                user="dupie",
                password=open('/var/www/wsgi/dupie/secret/dupiepassword.txt', 'r').read(),
                host="localhost",
                port=3306,
                database="dupie"
            )
        except mysql.connector.errors.Error as err: 
            raise BaseException("DupieBase Constructor Failed!: \n {}".format(err))
      
        self.conn.autocommit = False

    def __del__(self):
        if hasattr("self", "conn"):
            self.conn.connector.close()

    def query(self,query):
        sql_cursor = self.conn.cursor()
        sql_cursor.execute(query)
        sql_field_names = [i[0] for i in sql_cursor.description]

        dto = []

        # reads all the rows and makes it into a dto
        for sql_row_data in sql_cursor:
            # grabs the field names and field data
            field_names = list(sql_field_names)
            field_datas = list(sql_row_data)

            # assigns field names to field data
            zipped_data = zip(field_names,field_datas)

            # packs up for dto as a dict
            _dto = dict(zipped_data)
            dto.append(_dto)
        return dto

    def getVocabDump(self):
        etl = self.query("SELECT * FROM dupie.vocabulary where vocabulary_index = synonym ;")

        dto = {}
        for row in etl:
            dto[row["vocabulary_index"]+1001-3] = {
                    'deutsch': row['deutsch'],
                    'english': row['english'],
                    'espanol': row['espanol'],
                    'francais': row['francais'],
                    'svenska': row['svenska'],
                    'zhongwen': row['zhongwen']
                }
        return dto

    def getLexiconETL(self,questionlanguage, answerlanguage):
        xdto = {
            "questionlanguage": questionlanguage,
            "answerlanguage": answerlanguage,
            "shortquestionlanguage": longtoshort[questionlanguage],
            "shortanswerlanguage": longtoshort[answerlanguage]
            }
        dto = (
            self.query("SELECT vocabulary_index, %(questionlanguage)s ""question"", %(answerlanguage)s ""answer"" FROM dupie.vocabulary where vocabulary_index = synonym and %(questionlanguage)s<>'' and %(answerlanguage)s<>'';" % xdto )
        )

        for x in range(0, len(dto)):
            xdto["index"] = dto[x]["vocabulary_index"]

            dto[x]["answer_audio"] = "%(index)s-%(shortanswerlanguage)s.mp3" % xdto
            dto[x]["question_audio"] = "%(index)s-%(shortquestionlanguage)s.mp3" % xdto




        return dto

    def getQuestionFormat(self,answerlanguage):
        dto = {"answerlanguage": answerlanguage}

        dto.update(
            self.query("SELECT pre, post FROM dupie.prompt where `language` = '%(answerlanguage)s';" % dto)[0]
        )

        dto.update(
            {
                "pre_audio": "%(answerlanguage)s-%(answerlanguage)s-1.mp3" % dto,
                "post_audio": "%(answerlanguage)s-%(answerlanguage)s-2.mp3" % dto
            }
        )
        return dto
        



if __name__ == "__main__":
   a = dupiebase()
   import pprint
   print (pprint.pformat(a.getQuestionFormat("zh")))   
   print (pprint.pformat(a.getLexiconETL("english","zhongwen")))   

#    print(pprint.pformat(a.getVocabDump()))
#    counter = 1000
#    for a in a.getVocabDump().values():
#        counter= counter+1
# #       print ('"%s",' % a['espanol']),
# #       print ('"%s-es.mp3",' % counter),
#        #print ('say %s -  %s ' % (counter,a['svenska'])),
#    a = dupiebase()
#    import pprint
#    counter = 1000
#    for a in a.getVocabDump().values():
#        counter= counter+1
#        print (' %s -  %s ' % (counter,a['english'])),
    