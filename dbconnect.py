import mysql
from mysql.connector import *
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", db = "pythondb")
mycursor = mydb.cursor()
mycursor.execute("select * from student")
for i in mycursor:
    print(i)