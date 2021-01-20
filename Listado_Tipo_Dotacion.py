#!/usr/bin/env python
# Python 3.8.6
import mariadb
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

cleaner()
Cabecera()
print ("\t\tListado Titulares\n")
# Cree un cursor llamando al método cursor () en la conexión:

cur = ConnectDB.cursor()
# Ejecucion de la consulta

cur.execute("SELECT Id_TipoDotacion AS Id, Tipo FROM TipoDotacion;",)

# Print Result-set (Conjunto Resultante)
print( 30*' ' + "%-4s %-15s" % ('Id', 'Tipo'))
for (Id_TipoDotacion, Tipo) in cur:
    print(30*' '+ "%-4s %-15s  " %  (Id_TipoDotacion, Tipo ))

pause()
cleaner()
