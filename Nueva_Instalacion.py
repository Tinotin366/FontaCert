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



Id_Instalacion = int(input("\t\tID de la Instalacion: "))
Id_Dotacion = str(input("\t\tId Dotacion: "))
CaudalMaximo= str(input("\t\tCaudal Maximo (l/s): "))
ØAcometida= str(input("\t\tØ Acometida (mm): "))
ØContador= str(input("\t\tØ Contador (mm): "))
OrigenSuministro= str(input("\t\tOrigen del Suministro: "))
TipoInstalacion= str(input("\t\tTipo Instalacion: "))
UsoDestino = str(input("\t\tUso Destino: "))


Instalacion = [Id_Instalacion, Id_Dotacion, CaudalMaximo, ØAcometida, ØContador, OrigenSuministro, TipoInstalacion, UsoDestino]
print(Instalacion[0])
print (f"\t\tLos datos introducidos son: \n Id Instalacion: {Instalacion[0]} \n Id Dotacion:      {Instalacion[1]} \n Caudal Maximo: {Instalacion[2]} \n ØAcometida : {Instalacion[3]} \n ØContador: {Instalacion[4]}\n Origen Suministro: {Instalacion[5]}\n Tipo Instalacion: {Instalacion[6]}\n Uso Destino {Instalacion[7]}")

SentenciaInsertSQL = "INSERT INTO Instalaciones (Id_Instalacion, Id_Dotacion, CaudalMaximo, ØAcometida, ØContador, OrigenSuministro, TipoInstalacion, UsoDestino) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
DatosInsertSQL =(Instalacion[0],Instalacion[1],Instalacion[2],Instalacion[3],Instalacion[4],Instalacion[5],Instalacion[6],Instalacion[7])
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
