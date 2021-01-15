#!/usr/bin/env python


import mariadb
# Python 3.8.6

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
cur.execute("SELECT Certificado, Certificados.Id_Titular, CIFNIF, Titular, Id_Instalacion, Id_Dotacion, Id_Objeto, Id_Instaladora, Fecha   FROM Certificados LEFT JOIN Titulares ON  Certificados.Id_Titular =  Titulares.Id_Titular;",)

# Print Result-set (Conjunto Resultante)
print("Certificado:  \t   ID Titular \t CIFNIF:\t  Titular:       \t Id_Instalacion: \t Id_Dotacion: \t Id_Objeto: \t Id_Instaladora: \t Fecha: ")
for (Certificado, Id_Titular, CIFNIF, Titular, Id_Instalacion, Id_Dotacion, Id_Objeto, Id_Instaladora, Fecha ) in cur:
    print(f"\t{Certificado} \t  {Id_Titular}\t   {CIFNIF}  \t    {Titular} \t  {Id_Instalacion} \t {Id_Dotacion} \t {Id_Objeto} \t {Id_Instaladora} \t{Fecha} ")
pause()
cleaner()
