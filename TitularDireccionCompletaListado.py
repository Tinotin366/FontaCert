#!/usr/bin/env python


import mariadb
# Python 3.8.6
# Conectar a la plataforma MariaDB utilizando la función connect () con los atributos relevantes.
import sys
from conf import db

# Instanciar Connection

try:
   ConnectDB = mariadb.connect (
        host=db[0], port=db[1], user=db[2], password=db[3], database=db[4]
        )
except mariadb.Error as e:
    print(f"Error conectando a la Plataforma MariaDB: {e}")
    sys.exit(1)



# Cree un cursor llamando al método cursor () en la conexión:

# Instanciar Cursor (Cursor de instancia)
# Obtener Cursor
# Titulares = [0, "Titular", "CIFNIF"]
cur = ConnectDB.cursor()
# Ejecucion de la consulta
cur.execute("SELECT Titulares.Id_Titular, Titulares.CIFNIF, Titulares.Titular,  TitularesDireccion.Id_Via, TitularesDireccion.NombreVia, TitularesDireccion.Numero, TitularesDireccion.Escalera, TitularesDireccion.Piso, TitularesDireccion.Puerta, Municipios.Poblacion, Municipios.Municipio, Municipios.CP  FROM  Titulares, TitularesDireccion LEFT JOIN Municipios ON  TitularesDireccion.Id_Poblacion =  Municipios.Id_Poblacion WHERE Titulares.Id_Titular = TitularesDireccion.Id_Direccion;",)

# Print Result-set (Conjunto Resultante)
# Header
print(f"Id:   CIFNIF: \t   Nombre Titular: \t  Id_Via  \t NombreVia:  \t Numero:  \t Id Titular:  \t Escalera:  \t Piso:  \t Puerta:  \t Poblacion:  \t Municipio:  \t CP: \t"   )
for (Id_Titular, CIFNIF, Titular, Id_Via, NombreVia, Numero, Escalera, Piso, Puerta, Poblacion, Municipio, CP) in cur:
    print(f"{Id_Titular}        {CIFNIF} \t  {Titular}  \t \t {Id_Via} \t  {NombreVia} \t  {Numero} \t  {Id_Titular} \t  {Escalera} \t  {Piso} \t  {Puerta} \t  {Poblacion} \t  {Municipio} \t {CP} \t"   )
