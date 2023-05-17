import mysql.connector

def connectionBD():
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="",
        database = "tiendaog"
        )
    if mydb:
        print ("Conexion exitosa")
    else:
        print ("Error en la conexion a BD")
    return mydb
