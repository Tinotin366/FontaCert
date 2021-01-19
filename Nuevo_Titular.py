#!/usr/bin/env python


import mariadb
# Python 3.8.6

import sys
from conf import db
from Funciones import *
# Instanciar Connection

try:
   ConnectDB = mariadb.connect (
        host=db[0], port=db[1], user=db[2], password=db[3], database=db[4]
        )
except mariadb.Error as e:
    print(f"Error conectando a la Plataforma MariaDB: {e}")
    sys.exit(1)


ConnectDB.autocommit = False
# Cree un cursor llamando al método cursor () en la conexión:

# Instanciar Cursor (Cursor de instancia)
# Obtener Cursor
# Titulares = [0, "Titular", "CIFNIF"]
cur = ConnectDB.cursor()
# Ejecucion de la consulta
cleaner()
Cabecera()
print ("\t\tNuevo Titular\n")

# Creacion de la Variable de entrada para poder insertarla en la base de datos de TitularesForm



IdTitular = int(input("\t\tID del Titular: "))
CIFNIF = str(input("\t\tCIF/NIF: "))
Titular= str(input("\t\tNombre del Titular: "))

Titular = [IdTitular, CIFNIF, Titular]
print(Titular[0])
print (f"\t\tLos datos introducidos son: \n Titular: {Titular[0]} \n CIFNIF:      {Titular[1]} \n   Nombre Titular: {Titular[2]}")

SentenciaInsertSQL = "INSERT INTO Titulares (Id_Titular, CIFNIF, Titular) VALUES (%s,%s,%s)"
DatosInsertSQL =(Titular[0],Titular[1],Titular[2])
print(DatosInsertSQL)
# print(str(SentenciaInsertSQL))
# (Titular[0],Titular[1],Titular[2])
cur.execute(SentenciaInsertSQL,DatosInsertSQL)
ConnectDB.commit()
cur.close()
ConnectDB.close()
print (f"\n\t\t Alta de el Titular nº: {Titular[0]}")
# Poner para solicitar si nuevo registro o Salir

pause()
