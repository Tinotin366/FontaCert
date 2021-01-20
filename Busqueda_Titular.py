#!/usr/bin/env python


import mariadb
# Python 3.8.6

import sys
import os
from Colors import bcolors
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

# Cree un cursor llamando al método cursor () en la conexión:

# Instanciar Cursor (Cursor de instancia)
# Obtener Cursor
# Titulares = [0, "Titular", "CIFNIF"]

print('\n\t')
print (f'\n\t\t\t{bcolors.OkCyan}{bcolors.Bold}FontaCert:{bcolors.EndC} Programa de Gestion de Certificados de Fontaneria')
print ('\t\t___________________________________________________________________________')
print ('                                                                          ')
Busqueda = str(input("\t\t\t\tTitular (Min 3 chr): "))

Busqueda = "'%" + Busqueda + "%'"
# SetBusqueda = "SET  @Busqueda = " + "'%" + Busqueda + "%'"

Sql = "SELECT Id_Titular, CIFNIF, Titular FROM Titulares WHERE Titular  LIKE " + Busqueda + " OR CIFNIF LIKE " + Busqueda +";"

# cursor.execute(sql, params)
cur = ConnectDB.cursor()
# Ejecucion de la consulta

cur.execute(Sql)
#
# # Print Result-set (Conjunto Resultante)
print(f"\n\n\t\tIdTitular: \t CIFNIF:      \t   Nombre Titular: "   )
for (IdTitular, CIFNIF, Titular) in cur:
     print(f"\t\t {IdTitular} \t       {CIFNIF} \t   {Titular}"   )


pause()
