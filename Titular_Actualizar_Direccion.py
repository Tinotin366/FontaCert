#!/usr/bin/env python


import mariadb
# Python 3.8.6
# Conectar a la plataforma MariaDB utilizando la función connect () con los atributos relevantes.
import sys
from conf import db

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

print ("Nuevo Titular")

# Creacion de la Variable de entrada para poder insertarla en la base de datos de TitularesForm


# Tabla Titulares

IdTitular = int(input("ID del Titular: "))
# CIFNIF = str(input("CIF/NIF: "))
# Titular= str(input("Nombre del Titular: "))

# Tabla Direccion Titulares

# Direccion
# Id_Direccion = int(input("
Id_Via = str(input("Tipo Via: "))               # Direccion[0]
NombreVia = str(input("Nombre de la Via: "))    # Direccion[1]
Numero = int(input("Numero: "))                 # Direccion[2]
Escalera = str(input("Escalera: "))             # Direccion[3]
Piso = str(input("Piso: "))                     # Direccion[4]
Puerta = str(input("Puerta: "))                 # Direccion[5]
Id_Municipio = int(input("Codigo Municipio: ")) # Direccion[6]



Titular = [IdTitular]
Direccion = [Id_Via, NombreVia, Numero, Escalera, Piso, Puerta, Id_Municipio]
print(Titular[0])
print (f"Los datos introducidos son: \n Titular: {Titular[0]}")

# SentenciaInsertSQL = "INSERT INTO Titulares (Id_Titular, CIFNIF, Titular) VALUES (%s,%s,%s)"
# DatosInsertSQL =(Titular[0],Titular[1],Titular[2])
# print(DatosInsertSQL)
# print(str(SentenciaInsertSQL))
# (Titular[0],Titular[1],Titular[2])
# cur.execute(SentenciaInsertSQL,DatosInsertSQL)

SentenciaInsertSQL = "INSERT INTO TitularesDireccion (Id_Titular, Id_Direccion,  Id_Via,         NombreVia,      Numero,         Escalera,       Piso,           Puerta,         Id_Municipio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
DatosInsertSQL =(Titular[0], Titular[0],    Direccion[0],   Direccion[1],   Direccion[2],   Direccion[3],   Direccion[4],   Direccion[5],   Direccion[6])

cur.execute(SentenciaInsertSQL,DatosInsertSQL)

ConnectDB.commit()
cur.close()
ConnectDB.close()
print (f"\n Actualizada Direccion del Titular nº: {Titular[0]}")
# Poner para solicitar si nuevo registro o Salir
