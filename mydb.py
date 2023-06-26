import mysql.connector


dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Rb21284729!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Database created!!")