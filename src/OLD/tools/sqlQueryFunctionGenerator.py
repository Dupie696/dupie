class GenerateSQLInsert():
    def __init__(self,raw_sql):
        self.raw_sql = raw_sql
        self.fieldsList = raw_sql.split("(")[1].split(")")[0].split(", ")
        parameterizedlist = ["%%(%s)s" % (x) for x in self.fieldsList]
        self.substitutionParameters = tuple (parameterizedlist)



        valuesList =  raw_sql.split("(")[2].split(")")[0]
        valuesList = valuesList.replace("0","%s").replace("''","'%s'") % self.substitutionParameters

        result = "\n\t\t\t".join(self.raw_sql.split("\n")[0:2]) + "\n\t\t\tVALUES(%s)" % valuesList

        dictTemplateList = ""
        for a in self.fieldsList:
            dictTemplateList = dictTemplateList +  '\t\t\t"%s":  %s,\n' % (a,a)

        xdto_result = """
    def template(self, %s):

        xdto = {
%s
            }
            query = \"\"\"%s\"\"\" %% dto[x]

            self.update(query)            
            """ % (",".join(self.fieldsList),dictTemplateList,result)
        
        self.templated_function = xdto_result


    def __str__(self):
        return (self.templated_function)




sql = """INSERT INTO DUPIE.QUESTIONS
(SESSIONID, UID, QUESTION, QUESTION_AUDIO, ANSWER, ANSWER_AUDIO, VOCABULARY_INDEX, QUIZQUESTION_INDEX)
VALUES(0, 0, '', '', '', '', 0, 0);
"""

sql = """INSERT INTO DUPIE.ANSWERS
(SESSIONID, VOCABULARY_INDEX, SHUFFLE, ANSWER, ANSWER_AUDIO, QUIZQUESTION_INDEX, QUIZANSWER_INDEX, QUIZANSWERANIMATION_INDEX)
VALUES(0, 0, 0, '', '', 0, 0, 0);
"""
print (GenerateSQLInsert(sql))