#!/usr/bin/env python


import mariadb
# Python 3.8.6
# Conectar a la plataforma MariaDB utilizando la función connect () con los atributos relevantes.
import sys
import os
from conf import db

# Instanciar Connection

try:
   ConnectDB = mariadb.connect (
        host=db[0], port=db[1], user=db[2], password=db[3], database=db[4]
        )
except mariadb.Error as e:
    print(f"Error conectando a la Plataforma MariaDB: {e}")
    sys.exit(1)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

# Cree un cursor llamando al método cursor () en la conexión:

# Instanciar Cursor (Cursor de instancia)
# Obtener Cursor
# Titulares = [0, "Titular", "CIFNIF"]
cur = ConnectDB.cursor()
# Ejecucion de la consulta
cur.execute("SELECT Id_Titular, CIFNIF, Titular FROM Titulares;",)

# Print Result-set (Conjunto Resultante)
print(f"\tIdTitular: \t CIFNIF:      \t   Nombre Titular: "   )
for (IdTitular, CIFNIF, Titular) in cur:
    print(f"\t {IdTitular} \t       {CIFNIF} \t   {Titular}"   )
