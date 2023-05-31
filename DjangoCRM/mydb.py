import mysql.connector


dataBase= mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd= 'Iamgoogle292!',
    

)
print(dataBase)

cursorobject = dataBase.cursor()


cursorobject.execute("CREATE DATABASE DjangoCRM")

print("All done")