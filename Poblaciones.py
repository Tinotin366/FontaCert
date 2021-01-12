#!/usr/bin/env python


import mariadb
# Python 3.8.6
# Conectar a la plataforma MariaDB utilizando la función connect () con los atributos relevantes.
import sys
import os
from conf import db
from Colors import bcolors
from Funciones import *


# Instanciar Connection

try:
   ConnectDB = mariadb.connect (
        host=db[0], port=db[1], user=db[2], password=db[3], database=db[4]
        )
except mariadb.Error as e:
    print(f"Error conectando a la Plataforma MariaDB: {e}")
    sys.exit(1)


# now, to cleaner the screen
cleaner()
Cabecera()

# Cree un cursor llamando al método cursor () en la conexión:

# Instanciar Cursor (Cursor de instancia)
# Obtener Cursor
# Titulares = [0, "Titular", "CIFNIF"]
cur = ConnectDB.cursor()
# Ejecucion de la consulta
cur.execute("SELECT Id_Poblacion, Poblacion, Municipio, Provincia,CP  FROM  Municipios",)

# Print Result-set (Conjunto Resultante)
print("\t %-8s %-30s %-30s %-15s %-10s " % ('Id Poblacion:','Poblacion:','Municipio:','Provincia:','CP:'))
for (Id_Poblacion, Poblacion, Municipio, Provincia, CP) in cur:
    # print(f"\t {Id_Poblacion}\t{Poblacion}\t\t  {Municipio}\t{CP}"   )
    print("\t %-8s %-30s %-30s %-15s %-10s " % (Id_Poblacion, Poblacion, Municipio, Provincia,CP))

pause()
cleaner()
