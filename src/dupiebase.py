import mysql.connector

class dupiebase:
    def __init__(self):
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
        print ("\n\n %s \n\n\n" % query)
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

    def getLexiconETL(self,language1, language2):
        return self.query("SELECT vocabulary_index, %s, %s FROM dupie.vocabulary where vocabulary_index = synonym and %s<>'' and %s<>'';" % (language1, language2, language1, language2))

    def getQuestionFormat(self,language2):
        return self.query("SELECT pre, post FROM dupie.prompt where `language` = '%s';" % (language2))
        



if __name__ == "__main__":
   a = dupiebase()
   import pprint
   print(pprint.pformat(a.getVocabDump()))
   counter = 1000
   for a in a.getVocabDump().values():
       counter= counter+1
#       print ('"%s",' % a['espanol']),
#       print ('"%s-es.mp3",' % counter),
       #print ('say %s -  %s ' % (counter,a['svenska'])),

   a = dupiebase()
   import pprint
   counter = 1000
   for a in a.getVocabDump().values():
       counter= counter+1
       print (' %s -  %s ' % (counter,a['english'])),
