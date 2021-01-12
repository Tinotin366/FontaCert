#!/usr/bin/env python


import mariadb
# Python 3.8.6
# Conectar a la plataforma MariaDB utilizando la función connect () con los atributos relevantes.
import sys
import os
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

cleaner()
Cabecera()
# Cree un cursor llamando al método cursor () en la conexión:

# Instanciar Cursor (Cursor de instancia)
# Obtener Cursor
# Titulares = [0, "Titular", "CIFNIF"]
cur = ConnectDB.cursor()
# Ejecucion de la consulta
cur.execute("SELECT Certificado, Certificados.Id_Titular, CIFNIF, Titular  FROM Certificados LEFT JOIN Titulares ON  Certificados.Id_Titular =  Titulares.Id_Titular;",)

# Print Result-set (Conjunto Resultante)
print("Certificado:  \t   ID Titular \t CIFNIF:\t  Titular:       \t\n")
for (Certificado, Id_Titular, CIFNIF, Titular) in cur:
    print(f"\t{Certificado} \t  {Id_Titular}\t   {CIFNIF}       {Titular} \t")
pause()
cleaner()
