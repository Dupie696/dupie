 mysqldump --user=root --password --lock-tables dupie prompt > prompt.sqlx
 mysqldump --user=root --password --lock-tables dupie vocabulary > vocabulary.sqlx

 grep -v "^--" prompt.sqlx | grep -v "^/\*" > prompt.sql
 grep -v "^--" vocabulary.sqlx | grep -v "^/\*" > vocabulary.sql

rm -f prompt.sqlx
rm -f vocabulary.sqlx