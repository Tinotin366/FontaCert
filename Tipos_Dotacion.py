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



cleaner()
Cabecera()

# Cree un cursor llamando al método cursor () en la conexión:

# Instanciar Cursor (Cursor de instancia)
# Obtener Cursor
# Titulares = [0, "Titular", "CIFNIF"]
cur = ConnectDB.cursor()
# Ejecucion de la consulta
cur.execute("SELECT Id_Instalacion, CIFNIF, Titular FROM Titulares;",)

# Print Result-set (Conjunto Resultante)

# Id_Instalacion, Id_Dotacion, CaudalMaximo, ØAcometida, ØContador, OrigenSuministro, TipoInstalacion, UsoDestino

print(f"\tId: \t CIFNIF:      \t   Nombre Titular: "   )
for (Id_Instalacion, Id_Dotacion, CaudalMaximo, ØAcometida, ØContador, OrigenSuministro, TipoInstalacion, UsoDestino) in cur:
    print(f"\t {IdTitular} \t       {CIFNIF} \t   {Titular}"   )

pause()
cleaner()
