import mysql.connector

# Connect to the SQLCO database
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Iamgoogle292!',
)
# Create a cursor object
cursorObject = dataBase.cursor()

# Create a new database if it doesn't exist
cursorObject.execute("CREATE DATABASE sqlco")

print("All done")