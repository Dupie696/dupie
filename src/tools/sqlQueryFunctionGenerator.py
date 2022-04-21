insert_template = """INSERT INTO DUPIE.USERSESSIONS
(USERSESSIONS_INDEX, UID, FRIENDLYNAME, SESSIONID, LANG_QUESTION, LANG_ANSWER, QUESTION_INDEX, QUESTIONS, ANSWERS, SHUFFLES, STATEMACHINE)
VALUES(0, 0, '', 0, '', '', 0, 0, 0, 0, '');"""



x_list = insert_template.split("(")[1].split(")")[0].split(", ")
x = ["%%(%s)s" % (y) for y in x_list]
print (x)
x = tuple (x)

y =  insert_template.split("(")[2].split(")")[0]
y = y.replace("0","%s").replace("''","'%s'") % x
print (y)
print ()
print ()
print ()

result = "\n".join(insert_template.split("\n")[0:2]) + "\nVALUES(%s)" % y

print (result)

print ()
print ()
print ()

xdto = ""
for a in x_list:
    xdto = xdto +  '\t\t\t"%s":  %s,\n' % (a,a)

xdto_result = """
    def template(self, %s):

        xdto = {
%s
            }
            query = \"\"\"%s\"\"\" %% dto[x]

            self.update(query)            
            """ % (",".join(x_list),xdto,result)


print (xdto_result)