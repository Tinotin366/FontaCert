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
cur = ConnectDB.cursor()
# Ejecucion de la consulta
cleaner()
Cabecera()
print ("\t\tNueva Instalacion\n")

# Creacion de la Variable de entrada para poder insertarla en la base de datos de InstalacionesForm


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
Id_Titular = int(input("\t\tID Titular : "))
Id_Instalacion = int(input("\t\tID de la Instalacion : "))
Id_Dotacion = Id_Dotacion
CaudalMaximo= float(input("\t\tCaudal Maximo (l/s): "))
ØAcometida= int(input("\t\tØ Acometida (mm): "))
ØContador= int(input("\t\tØ Contador (mm): "))
OrigenSuministro= str(input("\t\tOrigen del Suministro: "))
TipoInstalacion= str(input("\t\tTipo Instalacion: "))
UsoDestino = str(input("\t\tUso Destino: "))


Instalacion = [Id_Titular, Id_Instalacion, Id_Dotacion, CaudalMaximo, ØAcometida, ØContador, OrigenSuministro, TipoInstalacion, UsoDestino]
print(Instalacion[0])
print (f"\t\tLos datos introducidos son: Id Titular: {Instalacion[0]} \n Id Instalacion: {Instalacion[1]} \n Id Dotacion:      {Instalacion[2]} \n Caudal Maximo: {Instalacion[3]} \n ØAcometida : {Instalacion[4]} \n ØContador: {Instalacion[5]}\n Origen Suministro: {Instalacion[6]}\n Tipo Instalacion: {Instalacion[7]}\n Uso Destino {Instalacion[8]}")

SentenciaInsertSQL = "INSERT INTO Instalaciones (Id_Titular, Id_Instalacion, Id_Dotacion, CaudalMaximo, ØAcometida, ØContador, OrigenSuministro, TipoInstalacion, UsoDestino) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
DatosInsertSQL =(Instalacion[0],Instalacion[1],Instalacion[2],Instalacion[3],Instalacion[4],Instalacion[5],Instalacion[6],Instalacion[7], Instalacion[8])
print(DatosInsertSQL)
# print(str(SentenciaInsertSQL))
# (Titular[0],Titular[1],Titular[2])
cur.execute(SentenciaInsertSQL,DatosInsertSQL)
ConnectDB.commit()
cur.close()
ConnectDB.close()
print (f"\n\t\t Alta de la Instalacion nº: {Instalacion[0]}")
# Poner para solicitar si nuevo registro o Salir

pause()
