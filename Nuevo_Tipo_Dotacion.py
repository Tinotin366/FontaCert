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
print ("\t\tNuevo Tipo de Dotacion\n")

# Creacion de la Variable de entrada para poder insertarla en la base de datos de TitularesForm


Id_TipoDotacion = int(input("\t\tId Tipo Dotacion: "))
Tipo = str(input("\t\tNombre Dotacion: "))

Tipo = [Id_TipoDotacion, Tipo]
print(Tipo[0])
print (f"\t\tLos datos introducidos son: Id Tipo Dotacion {Id_TipoDotacion} \t Tipo Dotacion: {Tipo} \n ")

SentenciaInsertSQL = "INSERT INTO TipoDotacion (Id_TipoDotacion, Tipo) VALUES (%d, %s)"
DatosInsertSQL=(Tipo[0], Tipo[1])

# (Titular[0],Titular[1],Titular[2])
cur.execute(SentenciaInsertSQL, DatosInsertSQL)
ConnectDB.commit()
cur.close()
ConnectDB.close()
print (f"\n\t\t Alta de Nuevo Tipo de Dotacion : {Id_TipoDotacion}")
# Poner para solicitar si nuevo registro o Salir

pause()
