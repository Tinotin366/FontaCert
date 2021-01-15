#!/usr/bin/env python


import mariadb
# Python 3.8.6

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


# Id_Instalacion, Id_Dotacion, CaudalMaximo, ØAcometida, ØContador, OrigenSuministro, TipoInstalacion, UsoDestino
cur.execute("SELECT Id_Instalacion, Id_Dotacion, CaudalMaximo, ØAcometida, ØContador, OrigenSuministro, TipoInstalacion, UsoDestino FROM Instalaciones;",)

# Print Result-set (Conjunto Resultante)
print( "%-4s %-10s %-12s %-10s %-9s %-40s %-15s %-25s " % ('Id', 'Dotacion', 'CaudalMaximo', 'ØAcometida', 'ØContador', 'OrigenSuministro', 'TipoInstalacion', 'UsoDestino'))
for (Id_Instalacion, Id_Dotacion, CaudalMaximo, ØAcometida, ØContador, OrigenSuministro, TipoInstalacion, UsoDestino) in cur:
    print("%-4s %-10s %-12s %-10s %-9s %-40s %-15s %-25s " %  (Id_Instalacion, Id_Dotacion, CaudalMaximo, ØAcometida, ØContador, OrigenSuministro, TipoInstalacion, UsoDestino ))

pause()
cleaner()
