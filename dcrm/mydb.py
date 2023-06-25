import mysql.connector

dataBase= mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd= 'Iamgoogle292!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE sqlco")

print("All Done")