import mysql.connector

mysql_ = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Oal.1989_omaro"
) 

my_cursor = mysql_.cursor()
#sql = "CREATE DATABASE universidad"
#my_cursor.execute(sql)

sql = "SHOW DATABASES"
my_cursor.execute(sql)

for items in my_cursor:
    print(items)