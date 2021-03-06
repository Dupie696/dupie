# dumps all tables into a temp file
mysqldump --user=dupie --password="$(cat ../secret/dupiepassword.txt)" --lock-tables DUPIE ANSWERS > ANSWERS.sqlx
mysqldump --user=dupie --password="$(cat ../secret/dupiepassword.txt)" --lock-tables DUPIE QUESTIONS > QUESTIONS.sqlx
mysqldump --user=dupie --password="$(cat ../secret/dupiepassword.txt)" --lock-tables DUPIE USERSESSIONS > USERSESSIONS.sqlx
mysqldump --user=dupie --password="$(cat ../secret/dupiepassword.txt)" --lock-tables DUPIE PROMPT > PROMPT.sqlx
mysqldump --user=dupie --password="$(cat ../secret/dupiepassword.txt)" --lock-tables DUPIE VOCABULARY > VOCABULARY.sqlx

# deletes the comments in temp file (making a non-temp file)
grep -v "^--" ANSWERS.sqlx | grep -v "^/\*" > ANSWERS.sql
grep -v "^--" QUESTIONS.sqlx | grep -v "^/\*" > QUESTIONS.sql
grep -v "^--" USERSESSIONS.sqlx | grep -v "^/\*" > USERSESSIONS.sql
grep -v "^--" PROMPT.sqlx | grep -v "^/\*" > PROMPT.sql
grep -v "^--" VOCABULARY.sqlx | grep -v "^/\*" > VOCABULARY.sql

# removes temp files
rm -f ANSWERS.sqlx
rm -f QUESTIONS.sqlx
rm -f USERSESSIONS.sqlx
rm -f PROMPT.sqlx
rm -f VOCABULARY.sqlx
