#!/usr/bin/env python
# Python 3.8.6

import mariadb
import sys
from conf import db
from Funciones import *
from Colors import bcolors

# Instanciar Connection

try:
   ConnectDB = mariadb.connect (
        host=db[0], port=db[1], user=db[2], password=db[3], database=db[4]
        )
except mariadb.Error as e:
    print(f"Error conectando a la Plataforma MariaDB: {e}")
    sys.exit(1)



# Cree un cursor llamando al método cursor () en la conexión:
cleaner()
Cabecera()
print ("\t\tClonar Direccion de la Instalacion por la del Titular [Titular vive en la Instalacion]\n")

Busqueda = str(input("\t\t\t\tTitular (Min 3 chr): "))

Busqueda = "'%" + Busqueda + "%'"
Sql = "SELECT Id_Titular, CIFNIF, Titular FROM Titulares WHERE Titular  LIKE " + Busqueda + " OR CIFNIF LIKE " + Busqueda +";"

cur = ConnectDB.cursor()
# Ejecucion de la consulta

cur.execute(Sql)
#
# # Print Result-set (Conjunto Resultante)
print(f"\n\n\t\tIdTitular: \t CIFNIF:      \t   Nombre Titular: "   )
for (IdTitular, CIFNIF, Titular) in cur:
     print(f"\t\t {IdTitular} \t       {CIFNIF} \t   {Titular}"   )

Clonar = str(input("\t\t\t\tQue Id quiere clonar a la Tabla de Instalaciones?: "))

print("Valor Pulsado: %s" % (Clonar))

sql = "SELECT Id_Titular, Id_Poblacion, Id_Via, NombreVia, Numero, Escalera, Piso, Puerta FROM TitularesDireccion WHERE Id_Titular = " + Clonar + ";"

print (sql)
pause()

cur.execute(sql, Clonar)
for (Id_Titular, Id_Poblacion, Id_Via, NombreVia, Numero, Escalera, Piso, Puerta ) in cur:
# Direccion =    (Id_Titular, Id_Poblacion, Id_Via, NombreVia, Numero, Escalera, Piso, Puerta)
    print("%-4s %-10s  %-7s %-25s %-5s %-7s %-7s  %5s" % (Id_Titular, Id_Poblacion, Id_Via, NombreVia, Numero, Escalera, Piso, Puerta))


# print (Direccion)
pause()


# sql ="INSERT INTO Instalaciones (Id_Instalacion, Id_Dotacion, Id_Poblacion, Id_Via, NombreVia, Numero, Escalera, Piso, Puerta )
#  VALUES
# ({Clon}, {Clon}, , 'Cl', 'Camino de Coin, edf. Azucena ', 39, '-', 7, 'A1', 1, 63, 15, ' Instalación común, divisionaria', 'A', 'Doméstico');"
# cur.execute("SELECT Titulares.Id_Titular, Titulares.CIFNIF, Titulares.Titular,  TitularesDireccion.Id_Via, TitularesDireccion.NombreVia, TitularesDireccion.Numero, TitularesDireccion.Escalera, TitularesDireccion.Piso, TitularesDireccion.Puerta, Municipios.Poblacion, Municipios.Municipio, Municipios.CP  FROM  Titulares, TitularesDireccion LEFT JOIN Municipios ON  TitularesDireccion.Id_Poblacion =  Municipios.Id_Poblacion WHERE Titulares.Id_Titular = TitularesDireccion.Id_Direccion;",)

# Print Result-set (Conjunto Resultante)
# Header
# print("%-4s %-10s %-30s %-10s %-40s %-7s %-10s %-5s %-7s %25s %-20s %-5s " % ('Id:', 'CIFNIF:', 'Titular:', 'Id_Via', 'NombreVia:', 'Numero:', 'Escalera:', 'Piso:', 'Puerta:', 'Poblacion:', 'Municipio:', 'CP:' ))
# for (Id_Titular, CIFNIF, Titular, Id_Via, NombreVia, Numero, Escalera, Piso, Puerta, Poblacion, Municipio, CP) in cur:
#     print("%-4s %-10s %-30s %-10s %-40s %-7s %-10s %-5s %-7s %-25s %-20s %5s" % (Id_Titular, CIFNIF ,Titular ,Id_Via ,NombreVia , Numero, Escalera, Piso, Puerta, Poblacion, Municipio, CP))

pause()
cleaner()
